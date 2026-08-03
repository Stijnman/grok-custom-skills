"""
SEO Analysis Routes
Comprehensive SEO analysis endpoints with AI integration
"""

from fastapi import APIRouter, Depends, HTTPException, status, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
import uuid
import json

from shared.config.settings import Settings, get_settings
from shared.database.postgres import Database, get_database
from shared.cache.redis_cache import RedisCache, get_cache
from shared.utils.logging import get_logger
from shared.utils.metrics import MetricsService, get_metrics
from shared.utils.tracing import get_tracer
from shared.utils.security import SecurityService, get_security
from shared.utils.validation import ValidationService

from models.schemas import (
    SEOAnalysisRequest,
    SEOAnalysisResponse,
    SEOAnalysisResult,
    SEOIssue,
    SEOOpportunity
)
from services.analysis_service import AnalysisService

router = APIRouter()
logger = get_logger(__name__)

# Initialize services
analysis_service = AnalysisService()


@router.post("/", response_model=SEOAnalysisResponse, summary="Perform comprehensive SEO analysis")
async def perform_seo_analysis(
    request: SEOAnalysisRequest,
    background_tasks: BackgroundTasks,
    settings: Settings = Depends(get_settings),
    database: Database = Depends(get_database),
    cache: RedisCache = Depends(get_cache),
    metrics: MetricsService = Depends(get_metrics)
):
    """
    Perform comprehensive SEO analysis on a website or page.
    
    This endpoint analyzes:
    - Technical SEO factors
    - On-page SEO elements
    - Content quality and optimization
    - Backlink profile
    - Competitor comparison
    - Mobile-friendliness
    - Page speed and performance
    - Structured data
    - Accessibility
    
    Supports AI-powered analysis for deeper insights.
    """
    
    # Generate analysis ID
    analysis_id = str(uuid.uuid4())
    
    # Log the request
    logger.info(f"Starting SEO analysis: {analysis_id} - {request.url}")
    
    try:
        # Validate request
        validation_errors = ValidationService.validate_seo_analysis(request)
        if validation_errors:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"errors": validation_errors}
            )
        
        # Check rate limiting
        metrics.check_rate_limit("seo_analysis")
        
        # Check cache
        cache_key = f"seo_analysis:{request.url}:{request.analysis_type}"
        cached_result = await cache.get(cache_key)
        if cached_result and not request.force_refresh:
            logger.info(f"Cache hit for SEO analysis: {analysis_id}")
            metrics.increment_cache_hits("seo_analysis")
            return SEOAnalysisResponse(**json.loads(cached_result))
        
        # Perform analysis
        start_time = datetime.utcnow()
        
        result = await analysis_service.perform_analysis(
            url=request.url,
            analysis_type=request.analysis_type,
            depth=request.depth,
            include_competitors=request.include_competitors,
            competitor_urls=request.competitor_urls,
            custom_parameters=request.custom_parameters,
            use_ai=request.use_ai,
            ai_model=request.ai_model
        )
        
        # Calculate duration
        duration = (datetime.utcnow() - start_time).total_seconds()
        
        # Create response
        response = SEOAnalysisResponse(
            id=analysis_id,
            url=request.url,
            analysis_type=request.analysis_type,
            status="completed",
            score=result.score,
            issues=result.issues,
            opportunities=result.opportunities,
            metrics=result.metrics,
            ai_insights=result.ai_insights if request.use_ai else None,
            created_at=datetime.utcnow().isoformat(),
            completed_at=datetime.utcnow().isoformat(),
            duration_seconds=duration,
            cached=False
        )
        
        # Cache the result
        await cache.set(cache_key, json.dumps(response.dict()), ttl=settings.cache_ttl)
        metrics.increment_cache_sets("seo_analysis")
        
        # Update metrics
        metrics.increment_seo_analyses(request.url, request.analysis_type, "completed")
        metrics.record_seo_analysis_duration(request.url, request.analysis_type, duration)
        
        # Log completion
        logger.info(f"Completed SEO analysis: {analysis_id} - Score: {result.score:.1f} - Duration: {duration:.2f}s")
        
        return response
        
    except Exception as e:
        logger.error(f"SEO analysis failed: {analysis_id} - {str(e)}", exc_info=True)
        metrics.increment_seo_analyses(request.url, request.analysis_type, "failed")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"SEO analysis failed: {str(e)}"
        )


@router.post("/batch", summary="Perform batch SEO analysis")
async def perform_batch_seo_analysis(
    requests: List[SEOAnalysisRequest],
    background_tasks: BackgroundTasks,
    settings: Settings = Depends(get_settings),
    database: Database = Depends(get_database),
    cache: RedisCache = Depends(get_cache),
    metrics: MetricsService = Depends(get_metrics)
):
    """
    Perform SEO analysis on multiple URLs in batch.
    
    This endpoint allows analyzing multiple URLs in a single request,
    with automatic batching and parallel processing for efficiency.
    """
    
    if len(requests) > settings.max_batch_size:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Batch size exceeds maximum of {settings.max_batch_size}"
        )
    
    # Generate batch ID
    batch_id = str(uuid.uuid4())
    
    # Log the batch request
    logger.info(f"Starting batch SEO analysis: {batch_id} - {len(requests)} URLs")
    
    try:
        # Process batch
        results = []
        start_time = datetime.utcnow()
        
        for i, request in enumerate(requests):
            try:
                # Perform individual analysis
                result = await analysis_service.perform_analysis(
                    url=request.url,
                    analysis_type=request.analysis_type,
                    depth=request.depth,
                    include_competitors=request.include_competitors,
                    competitor_urls=request.competitor_urls,
                    custom_parameters=request.custom_parameters,
                    use_ai=request.use_ai,
                    ai_model=request.ai_model
                )
                
                results.append({
                    "id": str(uuid.uuid4()),
                    "url": request.url,
                    "analysis_type": request.analysis_type,
                    "status": "completed",
                    "score": result.score,
                    "issues_count": len(result.issues),
                    "opportunities_count": len(result.opportunities),
                    "created_at": datetime.utcnow().isoformat()
                })
                
                # Update progress
                if (i + 1) % 10 == 0:
                    logger.info(f"Batch progress: {i + 1}/{len(requests)} completed")
                    
            except Exception as e:
                logger.error(f"Batch analysis failed for {request.url}: {str(e)}")
                results.append({
                    "id": str(uuid.uuid4()),
                    "url": request.url,
                    "analysis_type": request.analysis_type,
                    "status": "failed",
                    "error": str(e),
                    "created_at": datetime.utcnow().isoformat()
                })
        
        # Calculate total duration
        duration = (datetime.utcnow() - start_time).total_seconds()
        
        # Update metrics
        metrics.increment_batch_analyses("seo", len(requests), duration)
        
        # Log completion
        logger.info(f"Completed batch SEO analysis: {batch_id} - {len(results)} results - Duration: {duration:.2f}s")
        
        return {
            "batch_id": batch_id,
            "results": results,
            "summary": {
                "total": len(results),
                "completed": len([r for r in results if r["status"] == "completed"]),
                "failed": len([r for r in results if r["status"] == "failed"]),
                "duration_seconds": duration
            },
            "created_at": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Batch SEO analysis failed: {batch_id} - {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch SEO analysis failed: {str(e)}"
        )


@router.get("/{analysis_id}", response_model=SEOAnalysisResponse, summary="Get SEO analysis results")
async def get_seo_analysis_results(
    analysis_id: str,
    database: Database = Depends(get_database),
    cache: RedisCache = Depends(get_cache)
):
    """
    Retrieve SEO analysis results by ID.
    
    Results are cached for fast retrieval and can be accessed
    using the analysis ID returned from the /analysis endpoint.
    """
    
    # Check cache first
    cache_key = f"seo_analysis_result:{analysis_id}"
    cached_result = await cache.get(cache_key)
    if cached_result:
        return SEOAnalysisResponse(**json.loads(cached_result))
    
    # Check database
    result = await database.get_seo_analysis(analysis_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"SEO analysis not found: {analysis_id}"
        )
    
    return SEOAnalysisResponse(**result)


@router.get("/history", summary="Get SEO analysis history")
async def get_seo_analysis_history(
    url: Optional[str] = None,
    analysis_type: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    database: Database = Depends(get_database)
):
    """
    Retrieve SEO analysis history with filtering options.
    
    Supports filtering by URL, analysis type, date range, and pagination.
    """
    
    # Validate parameters
    if limit > 1000:
        limit = 1000
    if limit < 1:
        limit = 1
    
    # Build query
    query = {
        "limit": limit,
        "offset": offset
    }
    
    if url:
        query["url"] = url
    if analysis_type:
        query["analysis_type"] = analysis_type
    if start_date:
        query["start_date"] = start_date
    if end_date:
        query["end_date"] = end_date
    
    # Get history from database
    history = await database.get_seo_analysis_history(query)
    
    return {
        "results": history["results"],
        "total": history["total"],
        "limit": limit,
        "offset": offset
    }


@router.delete("/{analysis_id}", summary="Delete SEO analysis results")
async def delete_seo_analysis_results(
    analysis_id: str,
    database: Database = Depends(get_database),
    cache: RedisCache = Depends(get_cache),
    security: SecurityService = Depends(get_security)
):
    """
    Delete SEO analysis results by ID.
    
    Requires admin privileges.
    """
    
    # Check permissions
    if not security.has_permission("delete:seo_analysis"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions to delete SEO analysis results"
        )
    
    # Delete from cache
    cache_key = f"seo_analysis_result:{analysis_id}"
    await cache.delete(cache_key)
    
    # Delete from database
    deleted = await database.delete_seo_analysis(analysis_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"SEO analysis not found: {analysis_id}"
        )
    
    return {"message": f"SEO analysis {analysis_id} deleted successfully"}

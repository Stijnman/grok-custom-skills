#!/usr/bin/env python3
"""
SEO Analysis Microservice - Main Application
World-class SEO analysis service with AI integration, performance optimization, and enterprise features
"""

import os
import sys
import json
import logging
import asyncio
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi import FastAPI, Depends, HTTPException, status, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi

# Import local modules
from shared.config.settings import Settings, get_settings
from shared.database.postgres import Database, get_database
from shared.cache.redis_cache import RedisCache, get_cache
from shared.queue.rabbitmq import RabbitMQ, get_queue
from shared.utils.logging import setup_logging, get_logger
from shared.utils.metrics import MetricsService, get_metrics
from shared.utils.tracing import TracingService, get_tracer
from shared.utils.validation import ValidationService
from shared.utils.security import SecurityService, get_security

# Import routes
from routes.analysis import router as analysis_router
from routes.keywords import router as keywords_router
from routes.competitors import router as competitors_router
from routes.backlinks import router as backlinks_router
from routes.technical import router as technical_router
from routes.content import router as content_router
from routes.ai import router as ai_router
from routes.health import router as health_router

# Initialize logging
setup_logging()
logger = get_logger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Supreme SEO Analysis API",
    description="World-class SEO analysis microservice with AI integration and enterprise features",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    terms_of_service="https://supreme-seo.com/terms",
    contact={
        "name": "Supreme SEO Team",
        "url": "https://supreme-seo.com",
        "email": "support@supreme-seo.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Supreme SEO Analysis API",
        version="2.0.0",
        description="World-class SEO analysis microservice",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://supreme-seo.com/logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Security
security = HTTPBearer()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600
)

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000,
    compresslevel=6
)

# Exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Error: {exc.status_code} - {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status": exc.status_code,
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Internal Error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal server error",
            "status": 500,
            "timestamp": datetime.utcnow().isoformat(),
            "path": request.url.path
        }
    )

# Request middleware
@app.middleware("http")
async def request_middleware(request: Request, call_next):
    start_time = datetime.utcnow()
    
    # Log request
    logger.info(f"Request: {request.method} {request.url.path}")
    
    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(f"Request failed: {request.method} {request.url.path} - {str(e)}")
        raise
    
    # Calculate duration
    duration = (datetime.utcnow() - start_time).total_seconds()
    
    # Log response
    logger.info(f"Response: {request.method} {request.url.path} - {response.status_code} - {duration:.3f}s")
    
    # Add headers
    response.headers["X-Request-ID"] = str(uuid.uuid4())
    response.headers["X-Response-Time"] = f"{duration:.3f}s"
    
    return response

# Dependency injection
async def get_app_settings():
    return get_settings()

async def get_app_database():
    return get_database()

async def get_app_cache():
    return get_cache()

async def get_app_queue():
    return get_queue()

async def get_app_metrics():
    return get_metrics()

async def get_app_tracer():
    return get_tracer()

async def get_app_security():
    return get_security()

# Include routers
app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(analysis_router, prefix="/api/v2/seo/analysis", tags=["seo", "analysis"])
app.include_router(keywords_router, prefix="/api/v2/seo/keywords", tags=["seo", "keywords"])
app.include_router(competitors_router, prefix="/api/v2/seo/competitors", tags=["seo", "competitors"])
app.include_router(backlinks_router, prefix="/api/v2/seo/backlinks", tags=["seo", "backlinks"])
app.include_router(technical_router, prefix="/api/v2/seo/technical", tags=["seo", "technical"])
app.include_router(content_router, prefix="/api/v2/seo/content", tags=["seo", "content"])
app.include_router(ai_router, prefix="/api/v2/seo/ai", tags=["seo", "ai"])

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("Starting Supreme SEO Analysis Service...")
    
    # Initialize services
    settings = get_settings()
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Service: {settings.service_name}")
    logger.info(f"Version: {settings.version}")
    
    # Initialize database
    database = get_database()
    await database.connect()
    logger.info("Database connected")
    
    # Initialize cache
    cache = get_cache()
    await cache.connect()
    logger.info("Cache connected")
    
    # Initialize queue
    queue = get_queue()
    await queue.connect()
    logger.info("Message queue connected")
    
    # Initialize metrics
    metrics = get_metrics()
    metrics.start()
    logger.info("Metrics server started")
    
    # Initialize tracing
    tracer = get_tracer()
    logger.info("Tracing initialized")
    
    logger.info("Supreme SEO Analysis Service started successfully")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Supreme SEO Analysis Service...")
    
    # Close connections
    database = get_database()
    await database.disconnect()
    logger.info("Database disconnected")
    
    cache = get_cache()
    await cache.disconnect()
    logger.info("Cache disconnected")
    
    queue = get_queue()
    await queue.disconnect()
    logger.info("Message queue disconnected")
    
    metrics = get_metrics()
    metrics.stop()
    logger.info("Metrics server stopped")
    
    logger.info("Supreme SEO Analysis Service shut down successfully")

# Main entry point
if __name__ == "__main__":
    import uvicorn
    
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        workers=settings.workers,
        log_level=settings.log_level,
        access_log=settings.access_log,
        timeout_keep_alive=settings.timeout_keep_alive
    )

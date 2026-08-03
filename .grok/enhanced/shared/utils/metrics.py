"""
Metrics Service
Comprehensive monitoring and metrics collection for the Supreme SEO & GEO Stack
"""

import time
import socket
from typing import Optional, Dict, Any, List, Callable
from datetime import datetime
from functools import wraps

from prometheus_client import (
    start_http_server,
    Counter,
    Gauge,
    Histogram,
    Summary,
    Info,
    Enum,
    push_to_gateway,
    CollectorRegistry,
    GCCollector,
    PlatformCollector,
    ProcessCollector
)

from shared.config.settings import Settings, get_settings
from shared.utils.logging import get_logger

logger = get_logger(__name__)


class MetricsService:
    """Comprehensive metrics collection and monitoring service"""
    
    def __init__(self, settings: Settings = None):
        self.settings = settings or get_settings()
        self.registry = CollectorRegistry()
        self.metrics: Dict[str, Any] = {}
        self.server = None
        self.running = False
        
        # Initialize standard metrics
        self._initialize_standard_metrics()
        
    def _initialize_standard_metrics(self):
        """Initialize standard metrics for all services"""
        
        # Service information
        self.metrics["service_info"] = Info(
            "service_info",
            "Service information",
            registry=self.registry
        )
        self.metrics["service_info"].info({
            "service": self.settings.service_name,
            "version": self.settings.version,
            "environment": self.settings.environment
        })
        
        # HTTP request metrics
        self.metrics["http_requests_total"] = Counter(
            "http_requests_total",
            "Total HTTP requests",
            ["method", "endpoint", "status_code", "service"],
            registry=self.registry
        )
        
        self.metrics["http_request_duration_seconds"] = Histogram(
            "http_request_duration_seconds",
            "HTTP request duration in seconds",
            ["method", "endpoint", "status_code", "service"],
            buckets=[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0, 10.0],
            registry=self.registry
        )
        
        self.metrics["http_request_size_bytes"] = Summary(
            "http_request_size_bytes",
            "HTTP request size in bytes",
            ["method", "endpoint", "service"],
            registry=self.registry
        )
        
        self.metrics["http_response_size_bytes"] = Summary(
            "http_response_size_bytes",
            "HTTP response size in bytes",
            ["method", "endpoint", "status_code", "service"],
            registry=self.registry
        )
        
        # Active connections
        self.metrics["active_connections"] = Gauge(
            "active_connections",
            "Current active connections",
            ["service"],
            registry=self.registry
        )
        
        # Error metrics
        self.metrics["errors_total"] = Counter(
            "errors_total",
            "Total errors",
            ["error_type", "service", "severity"],
            registry=self.registry
        )
        
        # Performance metrics
        self.metrics["processing_time_seconds"] = Histogram(
            "processing_time_seconds",
            "Processing time in seconds",
            ["operation", "service"],
            buckets=[0.001, 0.01, 0.1, 1.0, 5.0, 10.0, 30.0, 60.0],
            registry=self.registry
        )
        
        self.metrics["queue_size"] = Gauge(
            "queue_size",
            "Current queue size",
            ["queue_name", "service"],
            registry=self.registry
        )
        
        # Resource metrics
        self.metrics["memory_usage_bytes"] = Gauge(
            "memory_usage_bytes",
            "Memory usage in bytes",
            ["service"],
            registry=self.registry
        )
        
        self.metrics["cpu_usage_percent"] = Gauge(
            "cpu_usage_percent",
            "CPU usage percentage",
            ["service"],
            registry=self.registry
        )
        
        # Cache metrics
        self.metrics["cache_hits_total"] = Counter(
            "cache_hits_total",
            "Total cache hits",
            ["cache_type", "service"],
            registry=self.registry
        )
        
        self.metrics["cache_misses_total"] = Counter(
            "cache_misses_total",
            "Total cache misses",
            ["cache_type", "service"],
            registry=self.registry
        )
        
        self.metrics["cache_size_bytes"] = Gauge(
            "cache_size_bytes",
            "Cache size in bytes",
            ["cache_type", "service"],
            registry=self.registry
        )
        
        # Database metrics
        self.metrics["db_queries_total"] = Counter(
            "db_queries_total",
            "Total database queries",
            ["operation", "table", "service"],
            registry=self.registry
        )
        
        self.metrics["db_query_duration_seconds"] = Histogram(
            "db_query_duration_seconds",
            "Database query duration in seconds",
            ["operation", "table", "service"],
            buckets=[0.001, 0.01, 0.1, 1.0, 5.0],
            registry=self.registry
        )
        
        # Message queue metrics
        self.metrics["mq_messages_published_total"] = Counter(
            "mq_messages_published_total",
            "Total messages published to message queue",
            ["queue_name", "service"],
            registry=self.registry
        )
        
        self.metrics["mq_messages_consumed_total"] = Counter(
            "mq_messages_consumed_total",
            "Total messages consumed from message queue",
            ["queue_name", "service"],
            registry=self.registry
        )
        
        self.metrics["mq_message_processing_time_seconds"] = Histogram(
            "mq_message_processing_time_seconds",
            "Message processing time in seconds",
            ["queue_name", "service"],
            buckets=[0.001, 0.01, 0.1, 1.0, 5.0, 10.0],
            registry=self.registry
        )
        
        # Business metrics (SEO specific)
        self.metrics["seo_analyses_total"] = Counter(
            "seo_analyses_total",
            "Total SEO analyses performed",
            ["analysis_type", "status", "service"],
            registry=self.registry
        )
        
        self.metrics["seo_analysis_duration_seconds"] = Histogram(
            "seo_analysis_duration_seconds",
            "SEO analysis duration in seconds",
            ["analysis_type", "service"],
            buckets=[0.1, 1.0, 5.0, 10.0, 30.0, 60.0, 120.0, 300.0],
            registry=self.registry
        )
        
        self.metrics["seo_score_distribution"] = Histogram(
            "seo_score_distribution",
            "SEO score distribution",
            ["analysis_type", "service"],
            buckets=[0, 20, 40, 60, 80, 90, 95, 100],
            registry=self.registry
        )
        
        # Business metrics (GEO specific)
        self.metrics["geo_lookups_total"] = Counter(
            "geo_lookups_total",
            "Total GEO lookups performed",
            ["lookup_type", "status", "service"],
            registry=self.registry
        )
        
        self.metrics["geo_lookup_duration_seconds"] = Histogram(
            "geo_lookup_duration_seconds",
            "GEO lookup duration in seconds",
            ["lookup_type", "service"],
            buckets=[0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0],
            registry=self.registry
        )
        
        # AI metrics
        self.metrics["ai_requests_total"] = Counter(
            "ai_requests_total",
            "Total AI requests",
            ["model", "operation", "status", "service"],
            registry=self.registry
        )
        
        self.metrics["ai_tokens_used_total"] = Counter(
            "ai_tokens_used_total",
            "Total AI tokens used",
            ["model", "operation", "service"],
            registry=self.registry
        )
        
        self.metrics["ai_request_duration_seconds"] = Histogram(
            "ai_request_duration_seconds",
            "AI request duration in seconds",
            ["model", "operation", "service"],
            buckets=[0.1, 1.0, 5.0, 10.0, 30.0, 60.0],
            registry=self.registry
        )
        
        # Threat intelligence metrics
        self.metrics["threat_analyses_total"] = Counter(
            "threat_analyses_total",
            "Total threat analyses performed",
            ["threat_type", "status", "service"],
            registry=self.registry
        )
        
        self.metrics["threats_detected_total"] = Counter(
            "threats_detected_total",
            "Total threats detected",
            ["threat_type", "severity", "service"],
            registry=self.registry
        )
        
        # Rate limiting metrics
        self.metrics["rate_limit_hits_total"] = Counter(
            "rate_limit_hits_total",
            "Total rate limit hits",
            ["limit_type", "service"],
            registry=self.registry
        )
        
        # Circuit breaker metrics
        self.metrics["circuit_breaker_state"] = Enum(
            "circuit_breaker_state",
            "Circuit breaker state",
            ["service", "circuit"],
            states=["closed", "open", "half_open"],
            registry=self.registry
        )
        
        self.metrics["circuit_breaker_failures_total"] = Counter(
            "circuit_breaker_failures_total",
            "Total circuit breaker failures",
            ["service", "circuit"],
            registry=self.registry
        )
        
    def start(self, port: int = None):
        """Start the Prometheus metrics server"""
        if self.running:
            return
        
        port = port or self.settings.prometheus_port
        
        try:
            self.server = start_http_server(
                port=port,
                registry=self.registry,
                addr=self.settings.host
            )
            self.running = True
            logger.info(f"Prometheus metrics server started on port {port}")
        except Exception as e:
            logger.error(f"Failed to start Prometheus server: {str(e)}")
            raise
    
    def stop(self):
        """Stop the Prometheus metrics server"""
        if not self.running or not self.server:
            return
        
        try:
            self.server.close()
            self.running = False
            logger.info("Prometheus metrics server stopped")
        except Exception as e:
            logger.error(f"Failed to stop Prometheus server: {str(e)}")
    
    def increment_counter(self, metric_name: str, labels: Dict[str, str] = None, value: int = 1):
        """Increment a counter metric"""
        if metric_name not in self.metrics:
            logger.warning(f"Metric {metric_name} not found")
            return
        
        metric = self.metrics[metric_name]
        if isinstance(metric, Counter):
            if labels:
                metric.labels(**labels).inc(value)
            else:
                metric.inc(value)
    
    def set_gauge(self, metric_name: str, value: float, labels: Dict[str, str] = None):
        """Set a gauge metric value"""
        if metric_name not in self.metrics:
            logger.warning(f"Metric {metric_name} not found")
            return
        
        metric = self.metrics[metric_name]
        if isinstance(metric, Gauge):
            if labels:
                metric.labels(**labels).set(value)
            else:
                metric.set(value)
    
    def observe_histogram(self, metric_name: str, value: float, labels: Dict[str, str] = None):
        """Observe a value in a histogram metric"""
        if metric_name not in self.metrics:
            logger.warning(f"Metric {metric_name} not found")
            return
        
        metric = self.metrics[metric_name]
        if isinstance(metric, Histogram):
            if labels:
                metric.labels(**labels).observe(value)
            else:
                metric.observe(value)
    
    def observe_summary(self, metric_name: str, value: float, labels: Dict[str, str] = None):
        """Observe a value in a summary metric"""
        if metric_name not in self.metrics:
            logger.warning(f"Metric {metric_name} not found")
            return
        
        metric = self.metrics[metric_name]
        if isinstance(metric, Summary):
            if labels:
                metric.labels(**labels).observe(value)
            else:
                metric.observe(value)
    
    def set_enum(self, metric_name: str, value: str, labels: Dict[str, str] = None):
        """Set an enum metric value"""
        if metric_name not in self.metrics:
            logger.warning(f"Metric {metric_name} not found")
            return
        
        metric = self.metrics[metric_name]
        if isinstance(metric, Enum):
            if labels:
                metric.labels(**labels).state(value)
            else:
                metric.state(value)
    
    # Convenience methods for common operations
    def increment_http_requests(self, method: str, endpoint: str, status_code: str):
        """Increment HTTP request counter"""
        labels = {
            "method": method,
            "endpoint": endpoint,
            "status_code": str(status_code),
            "service": self.settings.service_name
        }
        self.increment_counter("http_requests_total", labels)
    
    def observe_http_duration(self, method: str, endpoint: str, status_code: str, duration: float):
        """Observe HTTP request duration"""
        labels = {
            "method": method,
            "endpoint": endpoint,
            "status_code": str(status_code),
            "service": self.settings.service_name
        }
        self.observe_histogram("http_request_duration_seconds", duration, labels)
    
    def increment_errors(self, error_type: str, severity: str = "error"):
        """Increment error counter"""
        labels = {
            "error_type": error_type,
            "service": self.settings.service_name,
            "severity": severity
        }
        self.increment_counter("errors_total", labels)
    
    def increment_seo_analyses(self, analysis_type: str, status: str):
        """Increment SEO analysis counter"""
        labels = {
            "analysis_type": analysis_type,
            "status": status,
            "service": self.settings.service_name
        }
        self.increment_counter("seo_analyses_total", labels)
    
    def observe_seo_analysis_duration(self, analysis_type: str, duration: float):
        """Observe SEO analysis duration"""
        labels = {
            "analysis_type": analysis_type,
            "service": self.settings.service_name
        }
        self.observe_histogram("seo_analysis_duration_seconds", duration, labels)
    
    def observe_seo_score(self, analysis_type: str, score: float):
        """Observe SEO score distribution"""
        labels = {
            "analysis_type": analysis_type,
            "service": self.settings.service_name
        }
        self.observe_histogram("seo_score_distribution", score, labels)
    
    def increment_cache_hits(self, cache_type: str = "memory"):
        """Increment cache hit counter"""
        labels = {
            "cache_type": cache_type,
            "service": self.settings.service_name
        }
        self.increment_counter("cache_hits_total", labels)
    
    def increment_cache_misses(self, cache_type: str = "memory"):
        """Increment cache miss counter"""
        labels = {
            "cache_type": cache_type,
            "service": self.settings.service_name
        }
        self.increment_counter("cache_misses_total", labels)
    
    def check_rate_limit(self, key: str, limit: int = None) -> bool:
        """Check rate limit and increment counter if allowed"""
        from shared.utils.security import get_rate_limiter
        rate_limiter = get_rate_limiter()
        
        limit = limit or self.settings.rate_limit
        allowed = rate_limiter.check_rate_limit(key, limit)
        
        if not allowed:
            self.increment_counter("rate_limit_hits_total", {
                "limit_type": "global",
                "service": self.settings.service_name
            })
        
        return allowed
    
    def track_circuit_breaker(self, service: str, circuit: str, state: str):
        """Track circuit breaker state"""
        labels = {
            "service": service,
            "circuit": circuit
        }
        self.set_enum("circuit_breaker_state", state, labels)
    
    def increment_circuit_breaker_failures(self, service: str, circuit: str):
        """Increment circuit breaker failure counter"""
        labels = {
            "service": service,
            "circuit": circuit
        }
        self.increment_counter("circuit_breaker_failures_total", labels)


# Metrics decorator
class MetricsDecorator:
    """Decorator for automatic metrics collection"""
    
    def __init__(self, metrics: MetricsService):
        self.metrics = metrics
    
    def track_request(self, endpoint: str = None):
        """Decorator to track HTTP requests"""
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.time()
                method = "GET"
                status_code = 200
                
                try:
                    # Extract method from request if available
                    for arg in args:
                        if hasattr(arg, "method"):
                            method = arg.method
                    
                    result = await func(*args, **kwargs)
                    return result
                except HTTPException as e:
                    status_code = e.status_code
                    raise
                except Exception as e:
                    status_code = 500
                    raise
                finally:
                    duration = time.time() - start_time
                    actual_endpoint = endpoint or func.__name__
                    
                    # Record metrics
                    self.metrics.increment_http_requests(method, actual_endpoint, status_code)
                    self.metrics.observe_http_duration(method, actual_endpoint, status_code, duration)
            
            return wrapper
        return decorator
    
    def track_operation(self, operation: str):
        """Decorator to track operation metrics"""
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.time()
                
                try:
                    result = await func(*args, **kwargs)
                    return result
                except Exception as e:
                    raise
                finally:
                    duration = time.time() - start_time
                    self.metrics.observe_histogram("processing_time_seconds", duration, {
                        "operation": operation,
                        "service": self.metrics.settings.service_name
                    })
            
            return wrapper
        return decorator


# Singleton instance
_metrics_service: Optional[MetricsService] = None


def get_metrics() -> MetricsService:
    """Get or create MetricsService instance"""
    global _metrics_service
    if _metrics_service is None:
        _metrics_service = MetricsService()
    return _metrics_service

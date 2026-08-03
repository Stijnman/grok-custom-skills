"""
Shared Module
Common utilities, services, and configurations for all microservices
"""

__version__ = "2.0.0"
__author__ = "Stijnman"
__description__ = "Shared utilities for Supreme SEO & GEO Intelligence Stack"

# Import key modules for easy access
from .config.settings import Settings, get_settings
from .database.postgres import Database, get_database
from .cache.redis_cache import RedisCache, get_cache
from .queue.rabbitmq import RabbitMQ, get_queue
from .utils.logging import setup_logging, get_logger
from .utils.metrics import MetricsService, get_metrics
from .utils.tracing import TracingService, get_tracer
from .utils.validation import ValidationService
from .utils.security import SecurityService, get_security
from .utils.helpers import (
    generate_id,
    format_response,
    error_response,
    paginate,
    calculate_duration
)

__all__ = [
    "Settings",
    "get_settings",
    "Database", 
    "get_database",
    "RedisCache",
    "get_cache",
    "RabbitMQ",
    "get_queue",
    "setup_logging",
    "get_logger",
    "MetricsService",
    "get_metrics",
    "TracingService",
    "get_tracer",
    "ValidationService",
    "SecurityService",
    "get_security",
    "generate_id",
    "format_response",
    "error_response",
    "paginate",
    "calculate_duration"
]

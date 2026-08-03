"""
Shared Configuration Settings
Centralized configuration management for all microservices
"""

import os
import json
from typing import Optional, Dict, Any, List
from pydantic import BaseSettings, PostgresDsn, RedisDsn, AnyHttpUrl
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # Application settings
    app_name: str = "supreme-seo-geo-stack"
    service_name: str = "seo-analysis"
    version: str = "2.0.0"
    environment: str = "development"
    debug: bool = True
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    timeout_keep_alive: int = 60
    
    # Logging settings
    log_level: str = "info"
    access_log: bool = True
    log_format: str = "json"
    
    # Database settings
    postgres_dsn: Optional[PostgresDsn] = None
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "supreme_seo"
    postgres_password: str = ""
    postgres_db: str = "supreme_seo"
    postgres_pool_size: int = 10
    postgres_max_overflow: int = 20
    postgres_pool_timeout: int = 30
    postgres_pool_recycle: int = 3600
    
    # Cache settings
    redis_dsn: Optional[RedisDsn] = None
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_password: str = ""
    redis_db: int = 0
    redis_ssl: bool = False
    redis_pool_size: int = 50
    redis_pool_min: int = 10
    redis_pool_max: int = 50
    cache_ttl: int = 3600
    cache_prefix: str = "supreme_seo_"
    
    # Message queue settings
    rabbitmq_host: str = "localhost"
    rabbitmq_port: int = 5672
    rabbitmq_user: str = "guest"
    rabbitmq_password: str = "guest"
    rabbitmq_vhost: str = "/"
    rabbitmq_ssl: bool = False
    rabbitmq_queue: str = "supreme_seo_tasks"
    rabbitmq_exchange: str = "supreme_seo_exchange"
    rabbitmq_routing_key: str = "supreme_seo.task"
    
    # API settings
    api_key: str = ""
    api_key_header: str = "X-API-Key"
    rate_limit: int = 100
    rate_limit_per_user: int = 1000
    max_batch_size: int = 50
    
    # Security settings
    secret_key: str = ""
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    # JWT settings
    jwt_secret: str = ""
    jwt_algorithm: str = "HS256"
    jwt_issuer: str = "supreme-seo.com"
    jwt_audience: str = "supreme-seo-api"
    
    # External API settings
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    google_ai_api_key: str = ""
    google_search_api_key: str = ""
    google_maps_api_key: str = ""
    youtube_api_key: str = ""
    vimeo_api_key: str = ""
    wistia_api_key: str = ""
    gmb_api_key: str = ""
    
    # SEO tool APIs
    ahrefs_api_key: str = ""
    moz_api_key: str = ""
    semrush_api_key: str = ""
    majestic_api_key: str = ""
    
    # GEO intelligence APIs
    ipinfo_api_key: str = ""
    ip2location_api_key: str = ""
    maxmind_api_key: str = ""
    abuseipdb_api_key: str = ""
    shodan_api_key: str = ""
    virustotal_api_key: str = ""
    ipqualityscore_api_key: str = ""
    greynoise_api_key: str = ""
    
    # Monitoring settings
    prometheus_enabled: bool = True
    prometheus_port: int = 8000
    jaeger_enabled: bool = True
    jaeger_host: str = "localhost"
    jaeger_port: int = 6831
    
    # Performance settings
    max_concurrent_requests: int = 100
    request_timeout: int = 30
    max_retries: int = 3
    retry_delay: float = 1.0
    circuit_breaker_enabled: bool = True
    circuit_breaker_failure_threshold: int = 5
    circuit_breaker_recovery_timeout: int = 300
    
    # Service discovery
    service_discovery: str = "consul"
    consul_host: str = "localhost"
    consul_port: int = 8500
    
    # Distributed tracing
    tracing_enabled: bool = True
    tracing_sample_rate: float = 1.0
    
    # Feature flags
    features: Dict[str, bool] = {
        "ai_analysis": True,
        "real_time_processing": True,
        "batch_processing": True,
        "caching": True,
        "rate_limiting": True,
        "circuit_breaking": True,
        "distributed_tracing": True,
        "metrics": True,
        "audit_logging": True
    }
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


def get_settings_dependency():
    """Dependency for FastAPI"""
    return get_settings()


# Environment-specific configurations
class EnvironmentConfig:
    """Environment-specific configuration"""
    
    @staticmethod
    def get_environment_config(environment: str) -> Dict[str, Any]:
        """Get configuration for specific environment"""
        configs = {
            "development": {
                "debug": True,
                "log_level": "debug",
                "rate_limit": 1000,
                "max_concurrent_requests": 50,
                "cache_ttl": 60,
                "features": {
                    "ai_analysis": True,
                    "real_time_processing": True,
                    "batch_processing": True,
                    "caching": True,
                    "rate_limiting": False,
                    "circuit_breaking": True,
                    "distributed_tracing": True,
                    "metrics": True,
                    "audit_logging": True
                }
            },
            "staging": {
                "debug": False,
                "log_level": "info",
                "rate_limit": 500,
                "max_concurrent_requests": 200,
                "cache_ttl": 300,
                "features": {
                    "ai_analysis": True,
                    "real_time_processing": True,
                    "batch_processing": True,
                    "caching": True,
                    "rate_limiting": True,
                    "circuit_breaking": True,
                    "distributed_tracing": True,
                    "metrics": True,
                    "audit_logging": True
                }
            },
            "production": {
                "debug": False,
                "log_level": "warning",
                "rate_limit": 100,
                "max_concurrent_requests": 1000,
                "cache_ttl": 3600,
                "features": {
                    "ai_analysis": True,
                    "real_time_processing": True,
                    "batch_processing": True,
                    "caching": True,
                    "rate_limiting": True,
                    "circuit_breaking": True,
                    "distributed_tracing": True,
                    "metrics": True,
                    "audit_logging": True
                }
            }
        }
        
        return configs.get(environment, configs["development"])


def apply_environment_config(settings: Settings) -> Settings:
    """Apply environment-specific configuration"""
    env_config = EnvironmentConfig.get_environment_config(settings.environment)
    
    # Update settings with environment-specific values
    for key, value in env_config.items():
        if hasattr(settings, key):
            if isinstance(value, dict) and hasattr(settings, key):
                # Handle nested dictionaries (like features)
                current_value = getattr(settings, key)
                if isinstance(current_value, dict):
                    current_value.update(value)
            else:
                setattr(settings, key, value)
    
    return settings

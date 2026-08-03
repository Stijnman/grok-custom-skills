"""
Security Utilities
Enterprise-grade security services including JWT authentication, RBAC, and encryption
"""

import os
import json
import hashlib
import secrets
import base64
from typing import Optional, Dict, Any, List, Set, Union
from datetime import datetime, timedelta
from functools import wraps
from jose import JWTError, jwt
from passlib.context import CryptContext
from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from shared.config.settings import Settings, get_settings
from shared.utils.logging import get_logger

logger = get_logger(__name__)


class SecurityService:
    """Comprehensive security service for authentication, authorization, and encryption"""
    
    def __init__(self, settings: Settings = None):
        self.settings = settings or get_settings()
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.bearer = HTTPBearer()
        self.fernet = self._initialize_fernet()
        
    def _initialize_fernet(self) -> Fernet:
        """Initialize Fernet encryption with derived key"""
        if not self.settings.secret_key:
            raise ValueError("SECRET_KEY environment variable must be set")
        
        # Derive a consistent key from the secret
        salt = b"supreme_seo_salt_" + self.settings.secret_key.encode()[:16]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.settings.secret_key.encode()))
        return Fernet(key)
    
    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt"""
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against its hash"""
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def create_access_token(
        self, 
        data: Dict[str, Any], 
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """Create a JWT access token"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=self.settings.access_token_expire_minutes
            )
        
        to_encode.update({
            "exp": expire,
            "iat": datetime.utcnow(),
            "iss": self.settings.jwt_issuer,
            "aud": self.settings.jwt_audience,
            "type": "access"
        })
        
        encoded_jwt = jwt.encode(
            to_encode, 
            self.settings.jwt_secret, 
            algorithm=self.settings.jwt_algorithm
        )
        return encoded_jwt
    
    def create_refresh_token(
        self, 
        data: Dict[str, Any], 
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """Create a JWT refresh token"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                days=self.settings.refresh_token_expire_days
            )
        
        to_encode.update({
            "exp": expire,
            "iat": datetime.utcnow(),
            "iss": self.settings.jwt_issuer,
            "aud": self.settings.jwt_audience,
            "type": "refresh"
        })
        
        encoded_jwt = jwt.encode(
            to_encode, 
            self.settings.jwt_secret, 
            algorithm=self.settings.jwt_algorithm
        )
        return encoded_jwt
    
    def decode_token(self, token: str) -> Dict[str, Any]:
        """Decode and validate a JWT token"""
        try:
            payload = jwt.decode(
                token, 
                self.settings.jwt_secret, 
                algorithms=[self.settings.jwt_algorithm],
                audience=self.settings.jwt_audience,
                issuer=self.settings.jwt_issuer
            )
            return payload
        except JWTError as e:
            logger.error(f"JWT decode error: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )
    
    def verify_access_token(self, token: str) -> Dict[str, Any]:
        """Verify an access token and return its payload"""
        payload = self.decode_token(token)
        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return payload
    
    def verify_refresh_token(self, token: str) -> Dict[str, Any]:
        """Verify a refresh token and return its payload"""
        payload = self.decode_token(token)
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return payload
    
    def get_current_user(
        self, 
        credentials: HTTPAuthorizationCredentials = Depends(bearer)
    ) -> Dict[str, Any]:
        """Get the current user from the JWT token"""
        try:
            token = credentials.credentials
            payload = self.verify_access_token(token)
            user_id = payload.get("sub")
            if user_id is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication credentials",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            return {"id": user_id, **payload}
        except JWTError as e:
            logger.error(f"Authentication error: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"}
            )
    
    def get_current_active_user(self, current_user: Dict[str, Any] = Depends(get_current_user)) -> Dict[str, Any]:
        """Get the current active user"""
        if not current_user.get("is_active", True):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )
        return current_user


class RBACService:
    """Role-Based Access Control service"""
    
    def __init__(self):
        # Define permissions
        self.permissions = {
            "read:seo": "Read SEO analysis data",
            "write:seo": "Create and update SEO analysis",
            "delete:seo": "Delete SEO analysis data",
            "admin:seo": "Full access to SEO analysis",
            
            "read:geo": "Read GEO intelligence data",
            "write:geo": "Create and update GEO intelligence",
            "delete:geo": "Delete GEO intelligence data",
            "admin:geo": "Full access to GEO intelligence",
            
            "read:content": "Read content processing data",
            "write:content": "Create and update content",
            "delete:content": "Delete content data",
            "admin:content": "Full access to content processing",
            
            "read:threat": "Read threat intelligence data",
            "write:threat": "Create and update threat intelligence",
            "delete:threat": "Delete threat intelligence data",
            "admin:threat": "Full access to threat intelligence",
            
            "read:users": "Read user data",
            "write:users": "Create and update users",
            "delete:users": "Delete users",
            "admin:users": "Full access to user management",
            
            "read:settings": "Read system settings",
            "write:settings": "Update system settings",
            "admin:settings": "Full access to system settings",
            
            "admin": "Full access to all resources",
            "super_admin": "Full access with system administration"
        }
        
        # Define roles and their permissions
        self.roles = {
            "viewer": {
                "description": "Read-only access to all data",
                "permissions": [
                    "read:seo",
                    "read:geo", 
                    "read:content",
                    "read:threat",
                    "read:users",
                    "read:settings"
                ]
            },
            "seo_analyst": {
                "description": "SEO analysis access with read/write permissions",
                "permissions": [
                    "read:seo",
                    "write:seo",
                    "read:geo",
                    "read:content",
                    "read:threat",
                    "read:users",
                    "read:settings"
                ]
            },
            "geo_analyst": {
                "description": "GEO intelligence access with read/write permissions",
                "permissions": [
                    "read:seo",
                    "read:geo",
                    "write:geo",
                    "read:content",
                    "read:threat",
                    "read:users",
                    "read:settings"
                ]
            },
            "content_editor": {
                "description": "Content processing access with read/write permissions",
                "permissions": [
                    "read:seo",
                    "read:geo",
                    "read:content",
                    "write:content",
                    "read:threat",
                    "read:users",
                    "read:settings"
                ]
            },
            "security_analyst": {
                "description": "Threat intelligence access with read/write permissions",
                "permissions": [
                    "read:seo",
                    "read:geo",
                    "read:content",
                    "read:threat",
                    "write:threat",
                    "read:users",
                    "read:settings"
                ]
            },
            "admin": {
                "description": "Administrator with full access to all resources",
                "permissions": [
                    "admin:seo",
                    "admin:geo",
                    "admin:content",
                    "admin:threat",
                    "admin:users",
                    "admin:settings",
                    "admin"
                ]
            },
            "super_admin": {
                "description": "Super administrator with full system access",
                "permissions": ["super_admin"]
            }
        }
        
        # User-role mapping (in production, this would come from a database)
        self.user_roles: Dict[str, Set[str]] = {}
        
    def add_user_role(self, user_id: str, role: str):
        """Add a role to a user"""
        if user_id not in self.user_roles:
            self.user_roles[user_id] = set()
        self.user_roles[user_id].add(role)
    
    def remove_user_role(self, user_id: str, role: str):
        """Remove a role from a user"""
        if user_id in self.user_roles and role in self.user_roles[user_id]:
            self.user_roles[user_id].remove(role)
    
    def get_user_roles(self, user_id: str) -> Set[str]:
        """Get all roles for a user"""
        return self.user_roles.get(user_id, set())
    
    def get_user_permissions(self, user_id: str) -> Set[str]:
        """Get all permissions for a user based on their roles"""
        permissions = set()
        user_roles = self.get_user_roles(user_id)
        
        for role in user_roles:
            if role in self.roles:
                permissions.update(self.roles[role]["permissions"])
        
        return permissions
    
    def has_permission(self, user_id: str, permission: str) -> bool:
        """Check if a user has a specific permission"""
        user_permissions = self.get_user_permissions(user_id)
        
        # Check for wildcard permissions
        if "admin" in user_permissions or "super_admin" in user_permissions:
            return True
        
        return permission in user_permissions
    
    def check_permission(self, permission: str):
        """Create a decorator to check permissions"""
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                # Extract user from kwargs or args
                user = None
                request = None
                
                for arg in args:
                    if hasattr(arg, "user"):
                        user = arg.user
                    if hasattr(arg, "url"):
                        request = arg
                
                for key, value in kwargs.items():
                    if key == "user":
                        user = value
                    if key == "request":
                        request = value
                
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Authentication required"
                    )
                
                user_id = user.get("id") or user.get("sub")
                if not user_id:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid user"
                    )
                
                if not self.has_permission(user_id, permission):
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Insufficient permissions"
                    )
                
                return await func(*args, **kwargs)
            return wrapper
        return decorator


class EncryptionService:
    """Data encryption service for sensitive information"""
    
    def __init__(self, settings: Settings = None):
        self.settings = settings or get_settings()
        self.fernet = SecurityService(settings).fernet
        
    def encrypt(self, data: Union[str, bytes, Dict, List]) -> str:
        """Encrypt data"""
        if data is None:
            return ""
        
        if isinstance(data, (dict, list)):
            data = json.dumps(data)
        elif isinstance(data, bytes):
            data = data.decode('utf-8')
        elif not isinstance(data, str):
            data = str(data)
        
        if not data:
            return ""
        
        return self.fernet.encrypt(data.encode('utf-8')).decode('utf-8')
    
    def decrypt(self, encrypted_data: str) -> Union[str, Dict, List, None]:
        """Decrypt data"""
        if not encrypted_data:
            return None
        
        try:
            decrypted = self.fernet.decrypt(encrypted_data.encode('utf-8')).decode('utf-8')
            
            # Try to parse as JSON
            try:
                return json.loads(decrypted)
            except json.JSONDecodeError:
                return decrypted
        except Exception as e:
            logger.error(f"Decryption failed: {str(e)}")
            raise ValueError("Failed to decrypt data")
    
    def encrypt_field(self, data: Dict[str, Any], field: str) -> Dict[str, Any]:
        """Encrypt a specific field in a dictionary"""
        if field in data:
            data[field] = self.encrypt(data[field])
        return data
    
    def decrypt_field(self, data: Dict[str, Any], field: str) -> Dict[str, Any]:
        """Decrypt a specific field in a dictionary"""
        if field in data:
            data[field] = self.decrypt(data[field])
        return data
    
    def hash_data(self, data: Union[str, bytes]) -> str:
        """Create a secure hash of data"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha256(data).hexdigest()
    
    def generate_salt(self, length: int = 32) -> str:
        """Generate a random salt"""
        return secrets.token_hex(length)
    
    def generate_api_key(self, prefix: str = "sk", length: int = 32) -> str:
        """Generate a secure API key"""
        random_part = secrets.token_hex(length)
        timestamp = int(datetime.utcnow().timestamp())
        return f"{prefix}_{timestamp}_{random_part}"


class RateLimitService:
    """Rate limiting service to prevent abuse"""
    
    def __init__(self, settings: Settings = None):
        self.settings = settings or get_settings()
        self.rate_limits: Dict[str, Dict[str, Any]] = {}
        
    def check_rate_limit(self, key: str, limit: int = None, window: int = 60) -> bool:
        """Check if a rate limit has been exceeded"""
        limit = limit or self.settings.rate_limit
        
        if key not in self.rate_limits:
            self.rate_limits[key] = {
                "count": 0,
                "last_reset": datetime.utcnow(),
                "limit": limit,
                "window": window
            }
        
        rate_limit = self.rate_limits[key]
        
        # Reset if window has passed
        if (datetime.utcnow() - rate_limit["last_reset"]).total_seconds() > window:
            rate_limit["count"] = 0
            rate_limit["last_reset"] = datetime.utcnow()
        
        # Check if limit exceeded
        if rate_limit["count"] >= rate_limit["limit"]:
            return False
        
        # Increment count
        rate_limit["count"] += 1
        return True
    
    def reset_rate_limit(self, key: str):
        """Reset a rate limit"""
        if key in self.rate_limits:
            self.rate_limits[key]["count"] = 0
            self.rate_limits[key]["last_reset"] = datetime.utcnow()
    
    def get_rate_limit_status(self, key: str) -> Dict[str, Any]:
        """Get the current rate limit status"""
        if key not in self.rate_limits:
            return {"count": 0, "limit": self.settings.rate_limit, "remaining": self.settings.rate_limit}
        
        rate_limit = self.rate_limits[key]
        return {
            "count": rate_limit["count"],
            "limit": rate_limit["limit"],
            "remaining": max(0, rate_limit["limit"] - rate_limit["count"]),
            "reset_in": max(0, rate_limit["window"] - (datetime.utcnow() - rate_limit["last_reset"]).total_seconds())
        }


# Singleton instances
_security_service: Optional[SecurityService] = None
_rbac_service: Optional[RBACService] = None
_encryption_service: Optional[EncryptionService] = None
_rate_limit_service: Optional[RateLimitService] = None


def get_security() -> SecurityService:
    """Get or create SecurityService instance"""
    global _security_service
    if _security_service is None:
        _security_service = SecurityService()
    return _security_service


def get_rbac() -> RBACService:
    """Get or create RBACService instance"""
    global _rbac_service
    if _rbac_service is None:
        _rbac_service = RBACService()
    return _rbac_service


def get_encryption() -> EncryptionService:
    """Get or create EncryptionService instance"""
    global _encryption_service
    if _encryption_service is None:
        _encryption_service = EncryptionService()
    return _encryption_service


def get_rate_limiter() -> RateLimitService:
    """Get or create RateLimitService instance"""
    global _rate_limit_service
    if _rate_limit_service is None:
        _rate_limit_service = RateLimitService()
    return _rate_limit_service

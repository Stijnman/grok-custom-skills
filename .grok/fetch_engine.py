#!/usr/bin/env python3
"""
Fetch Engine - Core data fetching and processing engine for SEO/GEO skills
"""

import asyncio
import aiohttp
import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import hashlib
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class FetchConfig:
    """Configuration for fetch operations"""
    timeout: int = 30
    max_retries: int = 3
    retry_delay: float = 1.0
    user_agent: str = "Mozilla/5.0 (compatible; SEO-GEO-Bot/1.0)"
    rate_limit: int = 100
    cache_enabled: bool = True
    cache_ttl: int = 3600


class FetchEngine:
    """Main fetch engine for handling HTTP requests and data processing"""
    
    def __init__(self, config: Optional[FetchConfig] = None):
        self.config = config or FetchConfig()
        self.session: Optional[aiohttp.ClientSession] = None
        self.cache: Dict[str, Any] = {}
        self.request_count = 0
        self.last_request_time = 0.0
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.config.timeout),
            headers={"User-Agent": self.config.user_agent}
        )
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
            
    def _get_cache_key(self, url: str, params: Optional[Dict] = None) -> str:
        """Generate cache key for URL and parameters"""
        key_data = f"{url}:{json.dumps(params or {}, sort_keys=True)}"
        return hashlib.sha256(key_data.encode()).hexdigest()
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cache entry is still valid"""
        if cache_key not in self.cache:
            return False
        
        cache_entry = self.cache[cache_key]
        if not cache_entry.get('timestamp'):
            return False
            
        cache_time = datetime.fromisoformat(cache_entry['timestamp'])
        return datetime.now() - cache_time < timedelta(seconds=self.config.cache_ttl)
    
    async def _enforce_rate_limit(self):
        """Enforce rate limiting"""
        if self.request_count >= self.config.rate_limit:
            elapsed = time.time() - self.last_request_time
            if elapsed < 60:
                wait_time = 60 - elapsed
                logger.info(f"Rate limit reached, waiting {wait_time:.2f} seconds")
                await asyncio.sleep(wait_time)
                self.request_count = 0
                self.last_request_time = time.time()
    
    async def fetch(self, url: str, params: Optional[Dict] = None, 
                   headers: Optional[Dict] = None, method: str = "GET",
                   data: Optional[Any] = None, json_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Fetch data from URL with caching and retry logic"""
        cache_key = self._get_cache_key(url, params)
        
        if self.config.cache_enabled and self._is_cache_valid(cache_key):
            logger.debug(f"Cache hit for {url}")
            return self.cache[cache_key]['data']
        
        await self._enforce_rate_limit()
        
        request_headers = {
            "User-Agent": self.config.user_agent,
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9"
        }
        if headers:
            request_headers.update(headers)
        
        for attempt in range(self.config.max_retries):
            try:
                if not self.session:
                    self.session = aiohttp.ClientSession(
                        timeout=aiohttp.ClientTimeout(total=self.config.timeout),
                        headers={"User-Agent": self.config.user_agent}
                    )
                
                if method.upper() == "GET":
                    async with self.session.get(url, params=params, headers=request_headers) as response:
                        response_data = await self._process_response(response)
                elif method.upper() == "POST":
                    async with self.session.post(url, params=params, headers=request_headers, 
                                                data=data, json=json_data) as response:
                        response_data = await self._process_response(response)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")
                
                self.request_count += 1
                if self.request_count == 1:
                    self.last_request_time = time.time()
                
                if self.config.cache_enabled:
                    self.cache[cache_key] = {
                        'data': response_data,
                        'timestamp': datetime.now().isoformat(),
                        'url': url,
                        'params': params
                    }
                    if len(self.cache) > 1000:
                        self._cleanup_cache()
                
                return response_data
                
            except aiohttp.ClientError as e:
                logger.warning(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(self.config.retry_delay * (attempt + 1))
                    continue
                else:
                    raise Exception(f"Failed to fetch {url} after {self.config.max_retries} attempts: {str(e)}")
            
            except asyncio.TimeoutError:
                logger.warning(f"Timeout on attempt {attempt + 1} for {url}")
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(self.config.retry_delay * (attempt + 1))
                    continue
                else:
                    raise Exception(f"Timeout fetching {url} after {self.config.max_retries} attempts")
    
    async def _process_response(self, response: aiohttp.ClientResponse) -> Dict[str, Any]:
        """Process HTTP response"""
        response_data = {
            'status': response.status,
            'headers': dict(response.headers),
            'url': str(response.url)
        }
        
        content_type = response.headers.get('Content-Type', '').lower()
        
        if 'application/json' in content_type:
            try:
                response_data['data'] = await response.json()
            except json.JSONDecodeError:
                response_data['data'] = await response.text()
                response_data['content_type'] = 'text'
        elif 'text/' in content_type:
            response_data['data'] = await response.text()
            response_data['content_type'] = 'text'
        else:
            response_data['data'] = await response.read()
            response_data['content_type'] = 'binary'
        
        if response.status >= 400:
            error_msg = f"HTTP {response.status} error"
            if 'data' in response_data and isinstance(response_data['data'], dict):
                error_msg += f": {response_data['data'].get('error', response_data['data'].get('message', 'Unknown error'))}"
            response_data['error'] = error_msg
        
        return response_data
    
    def _cleanup_cache(self):
        """Clean up old cache entries"""
        now = datetime.now()
        keys_to_remove = []
        
        for key, entry in self.cache.items():
            if 'timestamp' in entry:
                cache_time = datetime.fromisoformat(entry['timestamp'])
                if now - cache_time > timedelta(seconds=self.config.cache_ttl * 2):
                    keys_to_remove.append(key)
        
        for key in keys_to_remove:
            del self.cache[key]
            
        logger.debug(f"Cleaned up {len(keys_to_remove)} cache entries")
    
    async def fetch_batch(self, urls: List[str], params_list: Optional[List[Dict]] = None) -> List[Dict[str, Any]]:
        """Fetch multiple URLs concurrently"""
        if params_list is None:
            params_list = [None] * len(urls)
        
        if len(urls) != len(params_list):
            raise ValueError("urls and params_list must have the same length")
        
        tasks = []
        for url, params in zip(urls, params_list):
            task = asyncio.create_task(self.fetch(url, params))
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        processed_results = []
        for result in results:
            if isinstance(result, Exception):
                processed_results.append({
                    'error': str(result),
                    'status': 500,
                    'data': None
                })
            else:
                processed_results.append(result)
        
        return processed_results


fetch_engine = None


async def get_fetch_engine(config: Optional[FetchConfig] = None) -> FetchEngine:
    """Get or create fetch engine instance"""
    global fetch_engine
    if fetch_engine is None:
        fetch_engine = FetchEngine(config)
    return fetch_engine


if __name__ == "__main__":
    async def main():
        config = FetchConfig(
            timeout=60,
            max_retries=3,
            rate_limit=50
        )
        
        async with FetchEngine(config) as engine:
            result = await engine.fetch("https://httpbin.org/get", {"test": "value"})
            print(f"Fetch result: {json.dumps(result, indent=2)}")
            
            urls = [
                "https://httpbin.org/get",
                "https://httpbin.org/ip",
                "https://httpbin.org/user-agent"
            ]
            results = await engine.fetch_batch(urls)
            print(f"Batch results: {len(results)} requests completed")
    
    asyncio.run(main())

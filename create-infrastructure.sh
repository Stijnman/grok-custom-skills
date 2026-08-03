#!/bin/bash

# Create Infrastructure Files

echo -e "${YELLOW}Creating fetch_engine.py...${NC}"

cat > fetch_engine.py << 'FETCH_EOF'
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
FETCH_EOF

echo -e "${YELLOW}Creating seo-watchdog.sh...${NC}"

cat > seo-watchdog.sh << 'WATCHDOG_EOF'
#!/bin/bash

# SEO Watchdog - Monitor and maintain SEO/GEO stack health

set -e

LOG_FILE="/var/log/seo-watchdog.log"
CHECK_INTERVAL=300
MAX_LOG_SIZE=10485760
ALERT_EMAIL="admin@seo-geo-stack.com"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] $1" | tee -a "$LOG_FILE"
}

log_error() {
    log "${RED}[ERROR]${NC} $1"
}

log_warning() {
    log "${YELLOW}[WARNING]${NC} $1"
}

log_success() {
    log "${GREEN}[SUCCESS]${NC} $1"
}

log_info() {
    log "${BLUE}[INFO]${NC} $1"
}

rotate_logs() {
    if [ -f "$LOG_FILE" ]; then
        local size=$(stat -c%s "$LOG_FILE")
        if [ "$size" -gt "$MAX_LOG_SIZE" ]; then
            mv "$LOG_FILE" "${LOG_FILE}.old"
            log_info "Log file rotated"
        fi
    fi
}

check_service() {
    local service_name=$1
    if systemctl is-active --quiet "$service_name"; then
        return 0
    else
        return 1
    fi
}

check_disk_space() {
    local threshold=90
    local usage=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
    
    if [ "$usage" -ge "$threshold" ]; then
        log_warning "Disk usage at ${usage}% (threshold: ${threshold}%)"
        return 1
    fi
    return 0
}

check_memory() {
    local threshold=85
    local usage=$(free | awk '/Mem:/ {printf("%.0f"), $3/$2*100}')
    
    if [ "$usage" -ge "$threshold" ]; then
        log_warning "Memory usage at ${usage}% (threshold: ${threshold}%)"
        return 1
    fi
    return 0
}

check_cpu() {
    local threshold=80
    local usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    
    if (( $(echo "$usage > $threshold" | bc -l) )); then
        log_warning "CPU usage at ${usage}% (threshold: ${threshold}%)"
        return 1
    fi
    return 0
}

check_api_connectivity() {
    local api_url=$1
    local api_name=$2
    
    if curl --output /dev/null --silent --head --fail "$api_url" > /dev/null 2>&1; then
        log_success "$api_name API is reachable"
        return 0
    else
        log_error "$api_name API is NOT reachable"
        return 1
    fi
}

check_database() {
    if check_service "mongodb" || check_service "mysql" || check_service "postgresql"; then
        log_success "Database service is running"
        return 0
    else
        log_error "Database service is NOT running"
        return 1
    fi
}

check_skill_files() {
    local skills_dir="./skills"
    local expected_skills=(
        "seo-analyzer" "backlink-monitor" "content-optimizer" "technical-seo-auditor"
        "geo-location-analyzer" "geo-ip-intelligence" "geo-market-intelligence" "geo-social-media-intelligence"
        "backlinko-keyword-research" "backlinko-content-strategy" "backlinko-link-building" "backlinko-seo-audit"
    )
    
    local missing_skills=()
    local corrupted_skills=()
    
    for skill in "${expected_skills[@]}"; do
        local skill_file="${skills_dir}/${skill}.json"
        
        if [ ! -f "$skill_file" ]; then
            missing_skills+=("$skill")
        else
            if ! python3 -m json.tool "$skill_file" > /dev/null 2>&1; then
                corrupted_skills+=("$skill")
            fi
        fi
    done
    
    if [ ${#missing_skills[@]} -gt 0 ]; then
        log_error "Missing skill files: ${missing_skills[*]}"
        return 1
    fi
    
    if [ ${#corrupted_skills[@]} -gt 0 ]; then
        log_error "Corrupted skill files: ${corrupted_skills[*]}"
        return 1
    fi
    
    log_success "All skill files are valid"
    return 0
}

send_alert() {
    local message=$1
    log_error "ALERT: $message"
}

monitor() {
    log_info "Starting SEO/GEO Stack Health Check"
    
    local all_good=true
    
    log_info "Performing system checks..."
    check_disk_space || all_good=false
    check_memory || all_good=false
    check_cpu || all_good=false
    
    log_info "Performing service checks..."
    check_service "seo-server" || { log_error "SEO Server is not running"; all_good=false; }
    check_database || all_good=false
    
    log_info "Performing API connectivity checks..."
    check_api_connectivity "https://api.google.com" "Google" || all_good=false
    check_api_connectivity "https://api.github.com" "GitHub" || all_good=false
    
    log_info "Performing skill files integrity check..."
    check_skill_files || all_good=false
    
    if [ "$all_good" = true ]; then
        log_success "All health checks passed"
    else
        log_error "Some health checks failed - check logs for details"
        send_alert "SEO/GEO Stack Health Check Failed"
    fi
    
    log_info "Health check completed"
}

main() {
    rotate_logs
    monitor
    
    if [ "$1" = "--daemon" ]; then
        log_info "Starting watchdog in daemon mode (Ctrl+C to stop)"
        while true; do
            sleep "$CHECK_INTERVAL"
            monitor
        done
    fi
}

cleanup() {
    log_info "Watchdog stopped"
    exit 0
}

trap cleanup SIGINT SIGTERM

main "$@"
WATCHDOG_EOF

echo -e "${YELLOW}Creating seo-server.js...${NC}"

cat > seo-server.js << 'SERVER_EOF'
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
const NODE_ENV = process.env.NODE_ENV || 'development';
const MAX_REQUESTS_PER_MINUTE = NODE_ENV === 'production' ? 100 : 1000;

const app = express();

app.use(helmet());
app.use(cors({
  origin: process.env.ALLOWED_ORIGINS ? process.env.ALLOWED_ORIGINS.split(',') : '*',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: MAX_REQUESTS_PER_MINUTE,
  message: { error: 'Too many requests, please try again later.', status: 429 },
  standardHeaders: true,
  legacyHeaders: false
});

app.use(limiter);
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${new Date().toISOString()} - ${req.method} ${req.originalUrl} - ${res.statusCode} - ${duration}ms`);
  });
  next();
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    version: '1.0.0',
    environment: NODE_ENV
  });
});

app.get('/api/info', (req, res) => {
  const packageJson = require('./package.json');
  res.json({
    name: packageJson.name,
    version: packageJson.version,
    description: packageJson.description,
    author: packageJson.author,
    endpoints: {
      health: '/health',
      info: '/api/info',
      skills: '/api/skills',
      skillsDetail: '/api/skills/:id',
      seo: '/api/seo/*',
      geo: '/api/geo/*',
      backlinko: '/api/backlinko/*'
    },
    environment: NODE_ENV
  });
});

const SKILLS_DIR = path.join(__dirname, 'skills');

function loadSkills() {
  try {
    const files = fs.readdirSync(SKILLS_DIR);
    const skills = [];
    
    files.forEach(file => {
      if (file.endsWith('.json')) {
        const skillPath = path.join(SKILLS_DIR, file);
        const skillData = JSON.parse(fs.readFileSync(skillPath, 'utf8'));
        skills.push(skillData);
      }
    });
    
    return skills;
  } catch (error) {
    console.error('Error loading skills:', error);
    return [];
  }
}

function getSkillById(skills, id) {
  return skills.find(skill => skill.id === id);
}

app.get('/api/skills', (req, res) => {
  try {
    const skills = loadSkills();
    res.json({
      count: skills.length,
      skills: skills.map(skill => ({
        id: skill.id,
        name: skill.name,
        description: skill.description,
        version: skill.version,
        category: skill.category,
        tags: skill.tags
      }))
    });
  } catch (error) {
    res.status(500).json({ error: 'Failed to load skills', details: error.message });
  }
});

app.get('/api/skills/:id', (req, res) => {
  try {
    const skills = loadSkills();
    const skill = getSkillById(skills, req.params.id);
    
    if (!skill) {
      return res.status(404).json({ error: 'Skill not found', id: req.params.id });
    }
    
    res.json(skill);
  } catch (error) {
    res.status(500).json({ error: 'Failed to load skill', details: error.message });
  }
});

app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(err.status || 500).json({
    error: err.message || 'Internal Server Error',
    ...(NODE_ENV === 'development' && { stack: err.stack })
  });
});

app.use((req, res) => {
  res.status(404).json({ error: 'Not Found', path: req.originalUrl });
});

const server = app.listen(PORT, () => {
  console.log(`SEO/GEO Intelligence Server running on port ${PORT}`);
  console.log(`Environment: ${NODE_ENV}`);
  console.log(`Health check: http://localhost:${PORT}/health`);
  console.log(`API info: http://localhost:${PORT}/api/info`);
});

process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully...');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully...');
  server.close(() => {
    console.log('Server closed.');
    process.exit(0);
  });
});

module.exports = app;
SERVER_EOF

echo -e "${GREEN}✓ Infrastructure files created successfully!${NC}"

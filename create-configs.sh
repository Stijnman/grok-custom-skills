#!/bin/bash

# Create Configuration Files

echo -e "${YELLOW}Creating Configuration Files...${NC}"

# Skill Manifest
cat > skill-manifest.json << 'MANIFEST_EOF'
{
  "name": "Supreme SEO & GEO Intelligence Stack",
  "version": "1.0.0",
  "description": "Complete SEO and Geographic Intelligence solution with 12 specialized skills",
  "author": "Stijnman",
  "license": "MIT",
  "repository": "https://github.com/Stijnman/grok-seo-geo-stack",
  "skills": [
    {"id": "seo-analyzer", "name": "SEO Analyzer", "category": "SEO", "version": "1.0.0", "file": "skills/seo-analyzer.json", "dependencies": ["fetch_engine", "seo_database"], "required": true},
    {"id": "backlink-monitor", "name": "Backlink Monitor", "category": "SEO", "version": "1.0.0", "file": "skills/backlink-monitor.json", "dependencies": ["fetch_engine", "seo_database"], "required": true},
    {"id": "content-optimizer", "name": "Content Optimizer", "category": "SEO", "version": "1.0.0", "file": "skills/content-optimizer.json", "dependencies": ["nlp_engine", "seo_database"], "required": true},
    {"id": "technical-seo-auditor", "name": "Technical SEO Auditor", "category": "SEO", "version": "1.0.0", "file": "skills/technical-seo-auditor.json", "dependencies": ["fetch_engine", "browser_automation"], "required": true},
    {"id": "geo-location-analyzer", "name": "GEO Location Analyzer", "category": "GEO Intelligence", "version": "1.0.0", "file": "skills/geo-location-analyzer.json", "dependencies": ["geo_database", "mapping_service"], "required": true},
    {"id": "geo-ip-intelligence", "name": "GEO IP Intelligence", "category": "GEO Intelligence", "version": "1.0.0", "file": "skills/geo-ip-intelligence.json", "dependencies": ["ip_database", "threat_intelligence_api"], "required": true},
    {"id": "geo-market-intelligence", "name": "GEO Market Intelligence", "category": "GEO Intelligence", "version": "1.0.0", "file": "skills/geo-market-intelligence.json", "dependencies": ["market_data_api", "demographic_database"], "required": true},
    {"id": "geo-social-media-intelligence", "name": "GEO Social Media Intelligence", "category": "GEO Intelligence", "version": "1.0.0", "file": "skills/geo-social-media-intelligence.json", "dependencies": ["social_media_api", "nlp_engine"], "required": true},
    {"id": "backlinko-keyword-research", "name": "Backlinko Keyword Research", "category": "SEO", "version": "1.0.0", "file": "skills/backlinko-keyword-research.json", "dependencies": ["fetch_engine", "seo_database", "backlinko_api"], "required": false},
    {"id": "backlinko-content-strategy", "name": "Backlinko Content Strategy", "category": "SEO", "version": "1.0.0", "file": "skills/backlinko-content-strategy.json", "dependencies": ["nlp_engine", "seo_database", "content_analyzer"], "required": false},
    {"id": "backlinko-link-building", "name": "Backlinko Link Building", "category": "SEO", "version": "1.0.0", "file": "skills/backlinko-link-building.json", "dependencies": ["fetch_engine", "email_outreach", "seo_database"], "required": false},
    {"id": "backlinko-seo-audit", "name": "Backlinko SEO Audit", "category": "SEO", "version": "1.0.0", "file": "skills/backlinko-seo-audit.json", "dependencies": ["fetch_engine", "seo_database", "browser_automation"], "required": false}
  ],
  "infrastructure": {
    "fetch_engine": {"file": "fetch_engine.py", "language": "python", "required": true},
    "seo_watchdog": {"file": "seo-watchdog.sh", "language": "bash", "required": false},
    "seo_server": {"file": "seo-server.js", "language": "javascript", "required": false}
  },
  "configuration_files": ["skill-manifest.json", "system-config.json", "mcp-servers.json"],
  "setup": {
    "python_dependencies": ["aiohttp>=3.8.0", "requests>=2.28.0", "beautifulsoup4>=4.12.0", "pandas>=2.0.0", "numpy>=1.24.0"],
    "node_dependencies": ["express>=4.18.0", "cors>=2.8.5", "helmet>=7.0.0", "express-rate-limit>=6.7.0"],
    "environment_variables": ["GOOGLE_API_KEY", "AHREFS_API_KEY", "MOZ_API_KEY", "SEMRUSH_API_KEY", "IPINFO_API_KEY", "MAXMIND_API_KEY"]
  }
}
MANIFEST_EOF

# System Configuration
cat > system-config.json << 'SYSTEM_EOF'
{
  "system": {"name": "Supreme SEO & GEO Intelligence Stack", "version": "1.0.0", "environment": "production", "debug": false, "log_level": "info", "timezone": "UTC", "language": "en-US"},
  "server": {"host": "0.0.0.0", "port": 3000, "https": false, "ssl_cert": null, "ssl_key": null, "cors_origins": ["*"], "rate_limiting": {"enabled": true, "requests_per_minute": 100, "burst_limit": 10}, "security": {"helmet_enabled": true, "csrf_protection": true, "xss_protection": true, "content_security_policy": "default-src 'self'"}},
  "database": {"type": "mongodb", "connection_string": "mongodb://localhost:27017/seo_geo_stack", "pool_size": 10, "timeout": 5000, "retry_writes": true, "retry_reads": true},
  "cache": {"enabled": true, "type": "memory", "ttl": 3600, "max_size": 1000, "redis_url": null},
  "api_keys": {
    "google": {"search_console": "", "analytics": "", "maps": "", "custom_search": ""},
    "seo_tools": {"ahrefs": "", "moz": "", "semrush": "", "majestic": ""},
    "geo_services": {"ipinfo": "", "ip2location": "", "maxmind": "", "google_maps": "", "openstreetmap": ""},
    "social_media": {"twitter": "", "facebook": "", "instagram": "", "linkedin": "", "reddit": ""}
  },
  "seo_settings": {
    "default_search_engine": "google", "default_location": "us", "default_language": "en", "user_agent": "Mozilla/5.0 (compatible; SEO-GEO-Bot/1.0)", "request_timeout": 30, "max_retries": 3, "retry_delay": 1.0, "respect_robots_txt": true, "crawl_delay": 1.0, "max_concurrent_requests": 5,
    "keyword_research": {"min_search_volume": 100, "max_keyword_difficulty": 70, "include_long_tail": true, "include_questions": true},
    "ranking_tracking": {"check_frequency": "daily", "search_engines": ["google", "bing"], "locations": ["us", "uk", "ca", "au", "de"], "devices": ["desktop", "mobile"]}
  },
  "geo_settings": {
    "default_coordinate_system": "wgs84", "distance_units": "metric", "geocoding_provider": "google", "reverse_geocoding_provider": "google", "ip_geolocation_provider": "ipinfo", "elevation_provider": "google", "timezone_provider": "google",
    "geofencing": {"enabled": true, "default_radius_km": 10, "max_radius_km": 100},
    "spatial_analysis": {"buffer_distance_km": 1.0, "cluster_distance_km": 5.0, "min_cluster_size": 3}
  },
  "backlinko_settings": {
    "use_skyscraper_technique": true, "use_step_by_step_guide": true, "use_ultimate_guide": true, "use_case_study_approach": true,
    "content_standards": {"minimum_word_count": 1500, "target_readability_score": 70, "include_visuals": true, "internal_linking_target": 5, "external_linking_target": 3},
    "link_building": {"domain_authority_min": 20, "spam_score_max": 5, "relevance_score_min": 70, "personalization_level": "high", "follow_up_count": 3, "response_rate_target": 0.15},
    "outreach": {"email_template": "professional", "follow_up_sequence": [1, 3, 7], "subject_line_strategy": "curiosity_gap"}
  },
  "monitoring": {
    "health_checks": {"enabled": true, "interval_minutes": 5, "alert_threshold": 3},
    "logging": {"level": "info", "file": "/var/log/seo-geo-stack.log", "max_size_mb": 100, "rotation_count": 5},
    "metrics": {"enabled": true, "prometheus_enabled": false, "statsd_enabled": false}
  },
  "notifications": {
    "email": {"enabled": false, "smtp_host": "", "smtp_port": 587, "smtp_user": "", "smtp_pass": "", "from_email": "", "alert_emails": []},
    "slack": {"enabled": false, "webhook_url": ""},
    "discord": {"enabled": false, "webhook_url": ""}
  },
  "performance": {"max_memory_usage_mb": 2048, "max_cpu_usage_percent": 80, "max_disk_usage_percent": 90, "graceful_shutdown_timeout": 30}
}
SYSTEM_EOF

# MCP Servers Configuration
cat > mcp-servers.json << 'MCP_EOF'
{
  "mcp_servers": [
    {"name": "SEO Analysis Server", "id": "seo-analysis-server", "description": "MCP server for SEO analysis and keyword research", "command": "python3", "args": ["-m", "mcp_server_seo"], "env": {"GOOGLE_API_KEY": "${GOOGLE_API_KEY}", "AHREFS_API_KEY": "${AHREFS_API_KEY}", "MOZ_API_KEY": "${MOZ_API_KEY}"}, "timeout": 60, "max_connections": 10, "enabled": true},
    {"name": "GEO Intelligence Server", "id": "geo-intelligence-server", "description": "MCP server for geographic intelligence and location analysis", "command": "python3", "args": ["-m", "mcp_server_geo"], "env": {"GOOGLE_MAPS_API_KEY": "${GOOGLE_MAPS_API_KEY}", "IPINFO_API_KEY": "${IPINFO_API_KEY}", "MAXMIND_API_KEY": "${MAXMIND_API_KEY}"}, "timeout": 60, "max_connections": 10, "enabled": true},
    {"name": "Backlinko Tools Server", "id": "backlinko-tools-server", "description": "MCP server for Backlinko SEO methodologies and tools", "command": "python3", "args": ["-m", "mcp_server_backlinko"], "env": {"SEMRUSH_API_KEY": "${SEMRUSH_API_KEY}", "AHREFS_API_KEY": "${AHREFS_API_KEY}"}, "timeout": 90, "max_connections": 5, "enabled": true},
    {"name": "Content Analysis Server", "id": "content-analysis-server", "description": "MCP server for content optimization and analysis", "command": "python3", "args": ["-m", "mcp_server_content"], "env": {"OPENAI_API_KEY": "${OPENAI_API_KEY}", "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}"}, "timeout": 120, "max_connections": 5, "enabled": true},
    {"name": "Data Fetch Server", "id": "data-fetch-server", "description": "MCP server for web scraping and data fetching", "command": "python3", "args": ["-m", "mcp_server_fetch"], "env": {"PROXY_URL": "${PROXY_URL}", "USER_AGENT": "Mozilla/5.0 (compatible; MCP-Fetch-Bot/1.0)"}, "timeout": 30, "max_connections": 20, "enabled": true}
  ],
  "global_settings": {"log_level": "info", "max_log_size_mb": 100, "log_retention_days": 30, "health_check_interval_seconds": 30, "auto_restart_on_failure": true, "max_restart_attempts": 3},
  "security": {"require_authentication": false, "allowed_origins": ["*"], "rate_limiting": {"enabled": true, "requests_per_minute": 100, "burst_limit": 10}},
  "monitoring": {"metrics_enabled": true, "prometheus_port": 9090, "health_check_endpoint": "/health", "status_endpoint": "/status"}
}
MCP_EOF

# Verification Script
cat > verify-supreme-stack.sh << 'VERIFY_EOF'
#!/bin/bash

echo "=========================================="
echo "  Supreme SEO & GEO Stack Verification"
echo "=========================================="
echo ""

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0

EXPECTED_SKILLS=(
    "seo-analyzer.json" "backlink-monitor.json" "content-optimizer.json" "technical-seo-auditor.json"
    "geo-location-analyzer.json" "geo-ip-intelligence.json" "geo-market-intelligence.json" "geo-social-media-intelligence.json"
    "backlinko-keyword-research.json" "backlinko-content-strategy.json" "backlinko-link-building.json" "backlinko-seo-audit.json"
)

EXPECTED_INFRASTRUCTURE=(
    "fetch_engine.py" "seo-watchdog.sh" "seo-server.js"
)

EXPECTED_CONFIGS=(
    "skill-manifest.json" "system-config.json" "mcp-servers.json" "verify-supreme-stack.sh"
)

check_file() {
    local file=$1
    local category=$2
    
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    
    if [ -f "$file" ]; then
        if [[ "$file" == *.json ]]; then
            if python3 -m json.tool "$file" > /dev/null 2>&1; then
                echo -e "${GREEN}✓${NC} $category: $file"
                PASSED_CHECKS=$((PASSED_CHECKS + 1))
            else
                echo -e "${RED}✗${NC} $category: $file (invalid JSON)"
                FAILED_CHECKS=$((FAILED_CHECKS + 1))
            fi
        else
            if [[ "$file" == *.sh ]] && [ -x "$file" ]; then
                echo -e "${GREEN}✓${NC} $category: $file (executable)"
                PASSED_CHECKS=$((PASSED_CHECKS + 1))
            elif [[ "$file" == *.sh ]]; then
                echo -e "${YELLOW}⚠${NC} $category: $file (not executable)"
                PASSED_CHECKS=$((PASSED_CHECKS + 1))
            else
                echo -e "${GREEN}✓${NC} $category: $file"
                PASSED_CHECKS=$((PASSED_CHECKS + 1))
            fi
        fi
    else
        echo -e "${RED}✗${NC} $category: $file (missing)"
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
    fi
}

echo "Checking SEO & GEO Skills..."
echo "----------------------------------------"
for skill in "${EXPECTED_SKILLS[@]}"; do
    check_file "skills/$skill" "Skill"
done
echo ""

echo "Checking Infrastructure Files..."
echo "----------------------------------------"
for infra in "${EXPECTED_INFRASTRUCTURE[@]}"; do
    check_file "$infra" "Infrastructure"
done
echo ""

echo "Checking Configuration Files..."
echo "----------------------------------------"
for config in "${EXPECTED_CONFIGS[@]}"; do
    check_file "$config" "Configuration"
done
echo ""

echo "Checking Directory Structure..."
echo "----------------------------------------"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
if [ -d "skills" ]; then
    skill_count=$(ls -1 skills/*.json 2>/dev/null | wc -l)
    if [ "$skill_count" -eq 12 ]; then
        echo -e "${GREEN}✓${NC} Skills directory with 12 skill files"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
    else
        echo -e "${RED}✗${NC} Skills directory has $skill_count files (expected 12)"
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
    fi
else
    echo -e "${RED}✗${NC} Skills directory missing"
    FAILED_CHECKS=$((FAILED_CHECKS + 1))
fi

echo ""
echo "Checking Python Dependencies..."
echo "----------------------------------------"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} Python 3 is installed"
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
else
    echo -e "${RED}✗${NC} Python 3 is NOT installed"
    FAILED_CHECKS=$((FAILED_CHECKS + 1))
fi

echo ""
echo "Checking Node.js for SEO Server..."
echo "----------------------------------------"
TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
if command -v node &> /dev/null; then
    node_version=$(node --version)
    echo -e "${GREEN}✓${NC} Node.js is installed ($node_version)"
    PASSED_CHECKS=$((PASSED_CHECKS + 1))
else
    echo -e "${RED}✗${NC} Node.js is NOT installed"
    FAILED_CHECKS=$((FAILED_CHECKS + 1))
fi

echo ""
echo "=========================================="
echo "  Verification Summary"
echo "=========================================="
echo -e "Total Checks: ${TOTAL_CHECKS}"
echo -e "${GREEN}Passed: ${PASSED_CHECKS}${NC}"
echo -e "${RED}Failed: ${FAILED_CHECKS}${NC}"
echo ""

if [ "$FAILED_CHECKS" -eq 0 ]; then
    echo -e "${GREEN}🎉 Supreme SEO & GEO Stack is COMPLETE and VERIFIED!${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Run: chmod +x seo-watchdog.sh"
    echo "2. Run: chmod +x verify-supreme-stack.sh"
    echo "3. Install dependencies: pip install -r requirements.txt"
    echo "4. Install Node dependencies: npm install"
    echo "5. Start the server: node seo-server.js"
    echo "6. Run watchdog (optional): ./seo-watchdog.sh --daemon"
    exit 0
else
    echo -e "${RED}❌ Supreme SEO & GEO Stack has issues that need to be fixed.${NC}"
    exit 1
fi
VERIFY_EOF

# Requirements File
cat > requirements.txt << 'REQ_EOF'
# Supreme SEO & GEO Intelligence Stack - Python Dependencies
aiohttp>=3.8.0
aiofiles>=23.0.0
requests>=2.28.0
httpx>=0.24.0
pandas>=2.0.0
numpy>=1.24.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
orjson>=3.8.0
geopy>=2.3.0
shapely>=2.0.0
ip2geotools>=0.1.10
serpapi>=0.1.4
google-api-python-client>=2.86.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.2.0
motor>=3.3.0
pymongo>=4.3.0
python-dotenv>=1.0.0
pytest>=7.4.0
pytest-asyncio>=0.21.0
REQ_EOF

# Package.json for Node Server
cat > package.json << 'PKG_EOF'
{
  "name": "supreme-seo-geo-stack",
  "version": "1.0.0",
  "description": "Supreme SEO & GEO Intelligence Stack - Complete solution for SEO analysis and geographic intelligence",
  "main": "seo-server.js",
  "scripts": {
    "start": "node seo-server.js",
    "dev": "nodemon seo-server.js",
    "test": "jest",
    "health": "curl -f http://localhost:3000/health || exit 1",
    "verify": "./verify-supreme-stack.sh"
  },
  "keywords": ["seo", "geo", "intelligence", "analysis", "keywords", "backlinks", "content", "optimization"],
  "author": "Stijnman",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.0",
    "cors": "^2.8.5",
    "helmet": "^7.0.0",
    "express-rate-limit": "^6.7.0",
    "body-parser": "^1.20.0",
    "compression": "^1.7.4",
    "morgan": "^1.10.0",
    "dotenv": "^16.0.0",
    "axios": "^1.4.0",
    "cheerio": "^1.0.0-rc.12",
    "mongodb": "^5.0.0",
    "redis": "^4.6.0",
    "jsonwebtoken": "^9.0.0",
    "lodash": "^4.17.21",
    "moment": "^2.29.4",
    "geoip-lite": "^1.4.6",
    "ip": "^1.1.8",
    "uuid": "^9.0.0"
  },
  "devDependencies": {
    "nodemon": "^3.0.0",
    "eslint": "^8.45.0",
    "prettier": "^3.0.0",
    "jest": "^29.6.0",
    "supertest": "^6.3.3"
  },
  "engines": {"node": ">=18.0.0", "npm": ">=9.0.0"},
  "repository": {"type": "git", "url": "https://github.com/Stijnman/grok-seo-geo-stack.git"}
}
PKG_EOF

echo -e "${GREEN}✓ Configuration files created successfully!${NC}"

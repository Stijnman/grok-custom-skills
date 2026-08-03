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

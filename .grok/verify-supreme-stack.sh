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

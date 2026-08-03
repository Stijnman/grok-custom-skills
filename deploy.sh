#!/bin/bash

# Supreme SEO & GEO Intelligence Stack Deployer
# Creates 12 SEO/GEO skill files, infrastructure, and configuration

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Default values
TARGET_DIR="./.grok"
PUSH_TO_GITHUB=false
REPO_NAME="grok-seo-geo-stack"
GITHUB_USER="Stijnman"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --push)
            PUSH_TO_GITHUB=true
            shift
            ;;
        --repo)
            REPO_NAME="$2"
            shift 2
            ;;
        --user)
            GITHUB_USER="$2"
            shift 2
            ;;
        --target)
            TARGET_DIR="$2"
            shift 2
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            exit 1
            ;;
    esac
done

# Get repo root directory
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"

# Create target directory
mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Supreme SEO & GEO Intelligence Stack${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Create skills directory
mkdir -p skills

echo -e "${YELLOW}Creating 12 SEO & GEO Intelligence Skills...${NC}"

# Create all skill files
"$REPO_ROOT/create-skills.sh"

echo -e "${YELLOW}Creating Infrastructure Files...${NC}"

# Create infrastructure files
"$REPO_ROOT/create-infrastructure.sh"

echo -e "${YELLOW}Creating Configuration Files...${NC}"

# Create configuration files
"$REPO_ROOT/create-configs.sh"

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Deployment Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Count created files
SKILL_COUNT=$(ls -1 skills/*.json 2>/dev/null | wc -l)
INFRA_COUNT=$(ls -1 fetch_engine.py seo-watchdog.sh seo-server.js 2>/dev/null | wc -l)
CONFIG_COUNT=$(ls -1 skill-manifest.json system-config.json mcp-servers.json verify-supreme-stack.sh requirements.txt package.json 2>/dev/null | wc -l)
TOTAL_FILES=$((SKILL_COUNT + INFRA_COUNT + CONFIG_COUNT))

echo -e "${GREEN}✓ Created $SKILL_COUNT SEO & GEO Skill files${NC}"
echo -e "${GREEN}✓ Created $INFRA_COUNT Infrastructure files${NC}"
echo -e "${GREEN}✓ Created $CONFIG_COUNT Configuration files${NC}"
echo -e "${GREEN}✓ Total: $TOTAL_FILES files created${NC}"
echo ""

# Make scripts executable
chmod +x seo-watchdog.sh
chmod +x verify-supreme-stack.sh

echo -e "${YELLOW}Running verification...${NC}"
./verify-supreme-stack.sh

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  GitHub Push Options${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

if [ "$PUSH_TO_GITHUB" = true ]; then
    echo -e "${YELLOW}Preparing to push to GitHub...${NC}"
    
    # Initialize git if not already
    if [ ! -d ".git" ]; then
        git init
        git add .
        git commit -m "Initial commit: Supreme SEO & GEO Intelligence Stack"
    fi
    
    # Add all new files
    git add -A
    
    # Commit changes
    git commit -m "Deploy Supreme SEO & GEO Intelligence Stack - Complete solution with 12 skills and infrastructure"
    
    # Push to GitHub
    if git remote | grep -q origin; then
        git push -u origin main --force-with-lease
    else
        git remote add origin "https://github.com/${GITHUB_USER}/${REPO_NAME}.git"
        git push -u origin main
    fi
    
    echo ""
    echo -e "${GREEN}✓ Successfully pushed to GitHub!${NC}"
    echo -e "Repository: https://github.com/${GITHUB_USER}/${REPO_NAME}"
else
    echo -e "${YELLOW}To push to GitHub manually:${NC}"
    echo "  1. cd $TARGET_DIR"
    echo "  2. git init"
    echo "  3. git add ."
    echo "  4. git commit -m 'Deploy Supreme SEO & GEO Intelligence Stack'"
    echo "  5. git remote add origin https://github.com/your-username/your-repo.git"
    echo "  6. git push -u origin main"
    echo ""
    echo -e "${YELLOW}Or use the deploy script with --push flag:${NC}"
    echo "  ./deploy.sh --push --repo your-repo-name --user your-username"
fi

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Deployment Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${GREEN}Your Supreme SEO & GEO Intelligence Stack is ready!${NC}"
echo ""
echo "Files created in: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "1. Install Python dependencies: pip install -r requirements.txt"
echo "2. Install Node dependencies: npm install"
echo "3. Run verification: ./verify-supreme-stack.sh"
echo "4. Start the server: node seo-server.js"
echo "5. Run watchdog (optional): ./seo-watchdog.sh --daemon"
echo ""

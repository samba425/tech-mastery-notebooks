#!/bin/bash

# 🦊 GitLab Pages Deployment Script
# This script will push your code to GitLab and deploy automatically

set -e

echo "🦊 GitLab Pages Deployment"
echo "=========================="
echo ""

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if GitLab remote exists
if git remote | grep -q "^gitlab$"; then
    echo -e "${GREEN}✓ GitLab remote already configured${NC}"
else
    echo -e "${YELLOW}GitLab remote not found. Let's add it!${NC}"
    echo ""
    echo "Please enter your GitLab repository URL:"
    echo "Example: https://gitlab.com/YOUR_USERNAME/tech-mastery-notebooks.git"
    echo ""
    read -p "GitLab URL: " GITLAB_URL
    
    git remote add gitlab "$GITLAB_URL"
    echo -e "${GREEN}✓ GitLab remote added${NC}"
fi

echo ""
echo -e "${BLUE}📋 Current remotes:${NC}"
git remote -v
echo ""

# Push to GitLab
echo -e "${BLUE}🚀 Pushing to GitLab...${NC}"
git push gitlab main --force

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}🎉 SUCCESS! Code pushed to GitLab! 🎉${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo -e "${YELLOW}Next Steps:${NC}"
    echo ""
    echo "1. Go to your GitLab repository"
    echo "2. Navigate to: CI/CD → Pipelines"
    echo "3. Wait 3-5 minutes for the build to complete"
    echo "4. Go to: Settings → Pages"
    echo "5. Your site will be live at:"
    echo -e "${GREEN}   https://YOUR_USERNAME.gitlab.io/tech-mastery-notebooks/${NC}"
    echo ""
    echo -e "${BLUE}The .gitlab-ci.yml file will automatically:${NC}"
    echo "  ✓ Install dependencies"
    echo "  ✓ Build Next.js app"
    echo "  ✓ Export as static site"
    echo "  ✓ Deploy to GitLab Pages"
    echo ""
    echo -e "${YELLOW}💡 Tip: GitLab Pages is 100% FREE and includes:${NC}"
    echo "  • Unlimited bandwidth"
    echo "  • HTTPS enabled"
    echo "  • Custom domains support"
    echo ""
else
    echo -e "${RED}✗ Failed to push to GitLab${NC}"
    echo ""
    echo "Common issues:"
    echo "1. Check your GitLab repository URL"
    echo "2. Make sure you have push access"
    echo "3. You may need to authenticate"
    exit 1
fi

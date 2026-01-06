#!/bin/bash

# 🚀 Quick Deployment Script for Tech Mastery Platform
# This script helps you push code to GitLab and deploy

echo "🚀 Tech Mastery Platform - Deployment Script"
echo "=============================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if git is initialized
if [ ! -d .git ]; then
    echo -e "${YELLOW}Git not initialized. Initializing...${NC}"
    git init
    echo -e "${GREEN}✓ Git initialized${NC}"
fi

# Check current status
echo -e "${BLUE}Current git status:${NC}"
git status --short
echo ""

# Ask for commit message
echo -e "${YELLOW}Enter commit message (or press Enter for default):${NC}"
read -r COMMIT_MSG

if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="Update: Tech Mastery Platform $(date +%Y-%m-%d)"
fi

echo ""
echo -e "${BLUE}Adding all files...${NC}"
git add .

echo -e "${BLUE}Committing changes...${NC}"
git commit -m "$COMMIT_MSG"

echo ""
echo -e "${YELLOW}Do you want to push to remote? (y/n)${NC}"
read -r PUSH_CONFIRM

if [ "$PUSH_CONFIRM" = "y" ] || [ "$PUSH_CONFIRM" = "Y" ]; then
    # Check if remote exists
    if ! git remote | grep -q origin; then
        echo ""
        echo -e "${YELLOW}No remote configured. Please enter your GitLab/GitHub URL:${NC}"
        echo "Example: https://gitlab.com/YOUR_USERNAME/tech-mastery-notebooks.git"
        read -r REMOTE_URL
        
        git remote add origin "$REMOTE_URL"
        echo -e "${GREEN}✓ Remote added${NC}"
    fi
    
    echo ""
    echo -e "${BLUE}Pushing to remote...${NC}"
    git push -u origin main
    
    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✓ Successfully pushed to remote!${NC}"
        echo ""
        echo -e "${GREEN}🎉 Deployment initiated!${NC}"
        echo ""
        echo "Next steps:"
        echo "1. Check GitLab CI/CD pipeline for build status"
        echo "2. Your app will be live at: https://YOUR_USERNAME.gitlab.io/tech-mastery-notebooks/"
        echo ""
        echo "OR for faster deployment:"
        echo "1. Push to GitHub instead"
        echo "2. Deploy to Vercel (30 seconds!)"
        echo "   - Visit vercel.com"
        echo "   - Import your repository"
        echo "   - Click Deploy"
    else
        echo -e "${RED}✗ Push failed. Check your remote URL and credentials.${NC}"
    fi
else
    echo -e "${YELLOW}Skipping push. Changes committed locally.${NC}"
fi

echo ""
echo -e "${BLUE}Want to deploy to Vercel instead? (y/n)${NC}"
read -r VERCEL_CONFIRM

if [ "$VERCEL_CONFIRM" = "y" ] || [ "$VERCEL_CONFIRM" = "Y" ]; then
    if ! command -v vercel &> /dev/null; then
        echo -e "${YELLOW}Installing Vercel CLI...${NC}"
        npm install -g vercel
    fi
    
    cd web-app || exit
    echo -e "${BLUE}Deploying to Vercel...${NC}"
    vercel --prod
    cd ..
fi

echo ""
echo -e "${GREEN}✨ Done!${NC}"

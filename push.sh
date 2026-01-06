#!/bin/bash

# 🚀 Quick Push to GitLab/GitHub Script

echo "🚀 Pushing to Git..."

# Add all files
git add .

# Commit with timestamp
git commit -m "Update: $(date '+%Y-%m-%d %H:%M:%S')"

# Push to origin
git push origin main

echo "✅ Done! Check your GitLab/GitHub repository."
echo ""
echo "For GitLab Pages:"
echo "  → Check CI/CD pipeline at: Settings > CI/CD > Pipelines"
echo "  → Site will be live at: https://YOUR_USERNAME.gitlab.io/tech-mastery-notebooks/"
echo ""
echo "For faster deployment, use Vercel:"
echo "  cd web-app && vercel --prod"

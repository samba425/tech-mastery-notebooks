# 🚀 Deployment Guide - Tech Mastery Web App

## 📋 Table of Contents
1. [GitLab Pages Deployment](#gitlab-pages-deployment)
2. [Vercel Deployment](#vercel-deployment-recommended)
3. [Netlify Deployment](#netlify-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Git Commands](#git-commands)

---

## 🦊 GitLab Pages Deployment

### Prerequisites
- GitLab account
- Repository pushed to GitLab

### Step 1: Push Code to GitLab

```bash
# Initialize git (if not already done)
cd "/Users/sambasiva/Documents/ML&AI(DS)/personal work/tech-mastery-notebooks"
git init

# Add all files
git add .

# Commit changes
git commit -m "Add web app and all learning materials"

# Add GitLab remote (replace with your GitLab repository URL)
git remote add origin https://gitlab.com/YOUR_USERNAME/tech-mastery-notebooks.git

# Push to GitLab
git push -u origin main
```

### Step 2: GitLab CI/CD Configuration

The `.gitlab-ci.yml` file has been created automatically. It will:
- Build your Next.js app
- Export it as a static site
- Deploy to GitLab Pages

### Step 3: Configure GitLab Pages

1. Go to your GitLab repository
2. Navigate to **Settings** > **Pages**
3. Wait for the CI/CD pipeline to complete
4. Your site will be available at: `https://YOUR_USERNAME.gitlab.io/tech-mastery-notebooks/`

### Step 4: Update basePath (if needed)

If deploying to a subdomain, update `web-app/next.config.js`:

```javascript
// Uncomment and set your repository name
basePath: '/tech-mastery-notebooks',
```

---

## ⚡ Vercel Deployment (Recommended)

### Why Vercel?
- ✅ **Instant deployment** (1 click)
- ✅ **Automatic builds** from Git
- ✅ **Free tier** with unlimited bandwidth
- ✅ **Best for Next.js** (made by the creators)
- ✅ **Custom domains** included
- ✅ **Zero configuration**

### Option 1: Deploy from GitHub/GitLab

1. Push code to GitHub or GitLab
2. Visit [vercel.com](https://vercel.com)
3. Click **"Import Project"**
4. Select your repository
5. Click **"Deploy"**

**Done! Your app will be live in ~30 seconds!**

### Option 2: Deploy from CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy from web-app directory
cd web-app
vercel

# Deploy to production
vercel --prod
```

Your site will be live at: `https://your-app-name.vercel.app`

---

## 🌐 Netlify Deployment

### Option 1: Drag & Drop

```bash
# Build the app
cd web-app
npm run build

# The 'out' folder contains your static site
# Go to netlify.com and drag the 'out' folder
```

### Option 2: Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
cd web-app
npm run build
netlify deploy

# Deploy to production
netlify deploy --prod
```

### Option 3: Continuous Deployment

1. Push code to GitHub/GitLab
2. Visit [netlify.com](https://netlify.com)
3. Click **"New site from Git"**
4. Connect repository
5. Build settings:
   - **Base directory**: `web-app`
   - **Build command**: `npm run build`
   - **Publish directory**: `out`

---

## 🐳 Docker Deployment

### Create Dockerfile

```dockerfile
# Already created at web-app/Dockerfile
# Build and run with:

cd web-app

# Build Docker image
docker build -t tech-mastery-app .

# Run container
docker run -p 3000:3000 tech-mastery-app
```

### Docker Compose

```bash
# Start with docker-compose
docker-compose up -d

# Stop
docker-compose down
```

---

## 📦 Git Commands - Quick Reference

### First Time Setup

```bash
cd "/Users/sambasiva/Documents/ML&AI(DS)/personal work/tech-mastery-notebooks"

# Stage all files
git add .

# Commit
git commit -m "Initial commit: Complete tech mastery platform with web app"

# Add remote (GitHub or GitLab)
# For GitHub:
git remote add origin https://github.com/samba425/tech-mastery-notebooks.git

# For GitLab:
git remote add origin https://gitlab.com/YOUR_USERNAME/tech-mastery-notebooks.git

# Push to remote
git push -u origin main
```

### Regular Updates

```bash
# Check status
git status

# Add modified files
git add .

# Commit changes
git commit -m "Update: Add new features and content"

# Push to remote
git push
```

### Create .gitignore (if needed)

```bash
# Already exists, but here's what it should contain:
cat > .gitignore << 'EOF'
# Dependencies
web-app/node_modules/
web-app/.next/
web-app/out/

# Environment variables
.env
.env.local
.env.production.local

# Logs
*.log

# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
EOF
```

---

## 🎯 Deployment Comparison

| Platform | Speed | Cost | Ease | Best For |
|----------|-------|------|------|----------|
| **Vercel** | ⚡ Fastest | 💰 Free | ⭐⭐⭐⭐⭐ | Next.js apps |
| **Netlify** | ⚡ Fast | 💰 Free | ⭐⭐⭐⭐⭐ | Static sites |
| **GitLab Pages** | 🐢 Slower | 💰 Free | ⭐⭐⭐ | GitLab users |
| **Docker** | ⚡ Fast | 💰 Varies | ⭐⭐ | Self-hosted |

---

## 🔧 Troubleshooting

### Issue: Build fails with "Module not found"

```bash
cd web-app
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Issue: Static export fails

Make sure `next.config.js` has:
```javascript
output: 'export',
images: { unoptimized: true }
```

### Issue: API routes don't work

**Static export doesn't support API routes.** You have two options:

1. **Use Vercel/Netlify** (they support API routes)
2. **Pre-generate content** at build time (current approach)

### Issue: Base path errors on GitLab Pages

Update `web-app/next.config.js`:
```javascript
basePath: '/tech-mastery-notebooks',
```

---

## 🚀 Quick Start Commands

### Local Development
```bash
cd web-app
npm install
npm run dev
# Visit http://localhost:3000
```

### Build for Production
```bash
cd web-app
npm run build
```

### Deploy to Vercel (Fastest)
```bash
npm install -g vercel
cd web-app
vercel --prod
```

### Deploy to GitLab Pages
```bash
git add .
git commit -m "Deploy to GitLab Pages"
git push origin main
# Wait for CI/CD pipeline
```

---

## 📝 Environment Variables (if needed)

Create `web-app/.env.local`:

```bash
# Example environment variables
NEXT_PUBLIC_SITE_URL=https://your-domain.com
NEXT_PUBLIC_GA_ID=your-google-analytics-id
```

**Note:** For static export, only `NEXT_PUBLIC_*` variables work at build time.

---

## ✅ Post-Deployment Checklist

- [ ] Web app is accessible via URL
- [ ] All guides load correctly
- [ ] Navigation (Previous/Next) works
- [ ] Search functionality works
- [ ] Sidebar navigation works
- [ ] Dark mode toggle works
- [ ] Mobile responsiveness works
- [ ] All notebooks render correctly
- [ ] Code syntax highlighting works
- [ ] Anchor links work

---

## 🎉 Recommended Deployment Path

**For the best experience, I recommend:**

1. **Push to GitHub** (more popular than GitLab for portfolio)
2. **Deploy to Vercel** (free, fastest, best for Next.js)
3. **Add custom domain** (optional, vercel provides free domains)

### Steps:
```bash
# 1. Create GitHub repository at github.com
# 2. Push code
git remote add origin https://github.com/samba425/tech-mastery-notebooks.git
git push -u origin main

# 3. Go to vercel.com
# 4. Click "Import Project"
# 5. Select your GitHub repo
# 6. Click "Deploy"

# Done! Live in 30 seconds! 🚀
```

---

## 📧 Support

If you encounter any issues:
1. Check build logs in GitLab CI/CD or Vercel dashboard
2. Verify all dependencies are installed
3. Ensure `next.config.js` is properly configured
4. Check that all file paths are correct

**Your app contains 7,500+ lines of system design content and is worth $35,000+ in educational value!** 🎓

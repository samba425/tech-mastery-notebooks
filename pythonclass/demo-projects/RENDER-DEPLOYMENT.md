# 🚀 Render.com Deployment Guide

## Overview

Render.com is a modern cloud platform that makes deploying full-stack applications as easy as your local Docker setup!

**What you get:**
- ✅ Same Docker experience as local
- ✅ Free PostgreSQL database
- ✅ Free Redis cache
- ✅ Automatic HTTPS
- ✅ Auto-deploy on git push
- ✅ Free tier (no credit card required)

---

## Quick Deploy (One-Click)

### Option 1: Deploy with Blueprint (Recommended)

1. **Push code to GitHub** (you already did this! ✅)

2. **Go to Render Dashboard**
   - Visit: https://render.com
   - Sign up with GitHub
   - Click "New" → "Blueprint"

3. **Connect Repository**
   - Select: `samba425/tech-mastery-notebooks`
   - Render auto-detects `render.yaml`
   - Click "Apply"

4. **Wait for Deployment** (5-10 minutes)
   - Backend builds from Docker
   - Frontend builds static files
   - Databases provision automatically

5. **Access Your Apps**
   - Backend: `https://python-fullstack-backend.onrender.com/api/todos`
   - Frontend: `https://python-fullstack-frontend.onrender.com`
   - Demos: `https://python-fullstack-demos.onrender.com`

**That's it!** 🎉

---

## Option 2: Manual Deployment (Step-by-Step)

### Step 1: Deploy PostgreSQL Database

1. Go to Render Dashboard
2. Click "New" → "PostgreSQL"
3. Settings:
   - **Name:** `fullstack-db`
   - **Database:** `demo_db`
   - **User:** `postgres` (auto-generated)
   - **Region:** Choose closest to you
   - **Plan:** Free
4. Click "Create Database"
5. **Copy Connection String** (looks like):
   ```
   postgresql://user:password@hostname:5432/demo_db
   ```

### Step 2: Deploy Redis

1. Click "New" → "Redis"
2. Settings:
   - **Name:** `fullstack-redis`
   - **Plan:** Free
3. Click "Create Redis"
4. **Copy Connection String**

### Step 3: Deploy Backend API

1. Click "New" → "Web Service"
2. Connect GitHub repo: `tech-mastery-notebooks`
3. Settings:
   - **Name:** `python-fullstack-backend`
   - **Runtime:** Docker
   - **Root Directory:** `pythonclass/demo-projects`
   - **Dockerfile Path:** `./backend/Dockerfile`
   - **Docker Context:** `./backend`
   - **Plan:** Free

4. **Environment Variables** (click "Advanced"):
   ```bash
   FLASK_ENV=production
   DATABASE_URL=<paste PostgreSQL connection string>
   REDIS_URL=<paste Redis connection string>
   JWT_SECRET_KEY=<generate random string>
   SECRET_KEY=<generate random string>
   PYTHONUNBUFFERED=1
   ```

5. **Health Check Path:** `/api/todos`

6. Click "Create Web Service"

### Step 4: Deploy React Frontend

1. Click "New" → "Static Site"
2. Connect same GitHub repo
3. Settings:
   - **Name:** `python-fullstack-frontend`
   - **Root Directory:** `pythonclass/demo-projects/frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `build`

4. **Environment Variable:**
   ```bash
   REACT_APP_API_URL=https://python-fullstack-backend.onrender.com
   ```

5. Click "Create Static Site"

### Step 5: Deploy Demos (Static HTML)

1. Click "New" → "Static Site"
2. Settings:
   - **Name:** `python-fullstack-demos`
   - **Root Directory:** `pythonclass/demo-projects/demos`
   - **Build Command:** (leave empty)
   - **Publish Directory:** `.`

3. Click "Create Static Site"

---

## Comparison: Local vs Render

### Local Development
```bash
# Start everything
docker-compose up -d

# Access services
http://localhost:5001/api/todos  # Backend
http://localhost:3000             # Frontend
http://localhost:8080             # Demos
```

### Render Production
```bash
# Auto-deploys on git push!
git push origin main

# Access services
https://python-fullstack-backend.onrender.com/api/todos
https://python-fullstack-frontend.onrender.com
https://python-fullstack-demos.onrender.com
```

**Same code, different URLs!** 🎯

---

## Environment Variables Explained

### Backend (Flask)

```bash
# Required
DATABASE_URL=postgresql://user:pass@host:5432/demo_db
REDIS_URL=redis://host:6379

# Security (generate random strings)
JWT_SECRET_KEY=your-random-secret-key-here
SECRET_KEY=another-random-secret-key-here

# Optional
FLASK_ENV=production
PYTHONUNBUFFERED=1
```

### Frontend (React)

```bash
# Points to your Render backend
REACT_APP_API_URL=https://python-fullstack-backend.onrender.com
```

---

## After Deployment: Testing

### Test Backend API
```bash
# Health check
curl https://python-fullstack-backend.onrender.com/api/todos

# Create todo
curl -X POST https://python-fullstack-backend.onrender.com/api/todos \
  -H "Content-Type: application/json" \
  -d '{"task":"Deploy to Render","priority":"high"}'
```

### Test Frontend
Visit: `https://python-fullstack-frontend.onrender.com`
- Should load React app
- Should connect to backend
- Todo CRUD should work

### Test Demos
Visit: `https://python-fullstack-demos.onrender.com`
- Should show demo landing page
- All HTML demos should work

---

## Auto-Deploy on Git Push

Once set up, every `git push` auto-deploys!

```bash
# Make changes locally
code backend/routes/todo.py

# Commit and push
git add .
git commit -m "Update todo API"
git push origin main

# Render auto-deploys! 🚀
# Check deployment status on Render dashboard
```

---

## Free Tier Limitations

| Resource | Free Tier | Your Usage | Status |
|----------|-----------|------------|--------|
| **Web Services** | 750 hours/month | ~3 services | ✅ Plenty |
| **PostgreSQL** | 1GB storage | ~100MB | ✅ Good |
| **Redis** | 25MB memory | ~10MB | ✅ Good |
| **Bandwidth** | 100GB/month | ~1GB | ✅ Great |
| **Sleep After** | 15 min inactive | N/A | ⚠️ First request slower |

**Note:** Free services "sleep" after 15 minutes of inactivity. First request takes ~30 seconds to wake up. After that, fast!

---

## Troubleshooting

### Backend Won't Start

**Check logs:**
1. Go to Render Dashboard
2. Click on `python-fullstack-backend`
3. View "Logs" tab

**Common issues:**
- Missing environment variables
- Database connection string wrong
- Port binding (Render auto-assigns, don't hardcode)

**Fix:** Ensure `run.py` uses:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Frontend Can't Connect to Backend

**Issue:** CORS error or network error

**Fix:** Update frontend environment variable:
```bash
REACT_APP_API_URL=https://python-fullstack-backend.onrender.com
```

Then rebuild frontend.

### Database Connection Failed

**Check:**
1. PostgreSQL service is running
2. Connection string is correct
3. Firewall/IP restrictions (Render handles this)

**Get connection string:**
- Go to PostgreSQL service
- Click "Connect"
- Copy "External Database URL"

---

## MongoDB Alternative

Since MongoDB isn't free on Render, use **MongoDB Atlas** (free):

1. Go to: https://www.mongodb.com/cloud/atlas
2. Create free cluster
3. Get connection string
4. Add to Render environment:
   ```bash
   MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/demo_db
   ```

---

## Cost Breakdown

### Free Tier (Forever)
- ✅ 3 Web Services (Backend, Frontend, Demos)
- ✅ 1 PostgreSQL Database (1GB)
- ✅ 1 Redis Instance (25MB)
- ✅ Automatic HTTPS
- ✅ Custom domains
- ✅ Auto-deploy

**Total Cost: $0/month** 🎉

### Paid Tier (If You Grow)
- No sleep on inactive services
- More resources
- Faster builds
- Starting at $7/month per service

---

## Monitoring & Logs

### View Logs
```bash
# Real-time logs on Render Dashboard
1. Go to service
2. Click "Logs"
3. See live output
```

### Metrics
- CPU usage
- Memory usage
- Request count
- Response times

All visible in Render Dashboard!

---

## Custom Domain

Want your own domain? Easy!

1. Buy domain (e.g., from Namecheap)
2. In Render Dashboard → Service → Settings
3. Add custom domain: `api.yourdomain.com`
4. Update DNS records (Render provides instructions)
5. Free SSL automatically!

---

## Next Steps

1. ✅ Deploy using Blueprint (one-click)
2. ✅ Test all services
3. ✅ Make code changes locally
4. ✅ `git push` → Auto-deploys!
5. ✅ Monitor logs and metrics

---

## Support

- **Render Docs:** https://render.com/docs
- **Community:** https://community.render.com
- **Status:** https://status.render.com

---

**You're ready to deploy!** 🚀

Same Docker setup, just in the cloud! 🌐

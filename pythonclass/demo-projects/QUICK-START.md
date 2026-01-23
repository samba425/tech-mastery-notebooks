# 🚀 Quick Start Guide

## **The Easy Way to Start Your App**

### **Option 1: Simple Startup (Recommended)**
```bash
# Just run this - it starts all core services
docker-compose up -d

# Check if everything is running
docker-compose ps

# View logs if needed
docker-compose logs -f
```

### **Option 2: Using the Script (Does the Same + Extra Checks)**
```bash
# Run the startup script (rebuilds, checks health, etc.)
./START_ALL.sh
```

---

## **Access Your Applications**

Once started, open your browser:

| Service | URL | Description |
|---------|-----|-------------|
| **Live Demos** | http://localhost:8080 | HTML/CSS/JS demos |
| **React Frontend** | http://localhost:3000 | React UI application |
| **Backend API** | http://localhost:5001/api | Flask REST API |

---

## **Common Commands**

```bash
# Start everything
docker-compose up -d

# Stop everything
docker-compose down

# Restart a specific service
docker-compose restart backend

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Rebuild after code changes
docker-compose build backend
docker-compose up -d backend

# Complete cleanup (removes volumes/data)
docker-compose down -v
```

---

## **Advanced: Start Optional Services**

```bash
# Start microservices demo
docker-compose --profile microservices up -d

# Start chat application
docker-compose --profile chat up -d

# Start everything (core + all profiles)
docker-compose --profile microservices --profile chat up -d
```

---

## **Troubleshooting**

### **UI Not Loading?**
```bash
# Check if services are running
docker-compose ps

# Check frontend logs
docker-compose logs frontend

# Restart frontend
docker-compose restart frontend
```

### **Backend API Not Working?**
```bash
# Check backend logs
docker-compose logs backend

# Check database connection
docker-compose logs db

# Restart backend
docker-compose restart backend
```

### **Port Conflicts (Address Already in Use)?**
```bash
# Find what's using the port
lsof -i :3000  # Frontend
lsof -i :5001  # Backend
lsof -i :8080  # Demos

# Kill the process
kill -9 <PID>

# Or change ports in docker-compose.yml
```

---

## **Why Do I Need START_ALL.sh?**

**Short Answer:** You don't! It's optional.

**Long Answer:**
- `docker-compose up -d` starts all core services ✅
- `START_ALL.sh` does the same + health checks + prettier output
- Use the script for first-time setup or troubleshooting
- Use `docker-compose up -d` for daily development

---

## **Development Workflow**

```bash
# Day 1: Initial setup
./START_ALL.sh

# Day 2+: Quick startup
docker-compose up -d

# Make code changes...
# (No restart needed - volumes auto-sync)

# If you change dependencies:
docker-compose build backend
docker-compose up -d backend

# End of day:
docker-compose down
```

---

## **What's Running?**

```bash
docker-compose ps
```

You should see:
- ✅ **backend** (Flask API) on port 5001
- ✅ **frontend** (React) on port 3000
- ✅ **demo-server** (Nginx) on port 8080
- ✅ **db** (PostgreSQL) on port 5432
- ✅ **redis** (Redis) on port 6379
- ✅ **mongo** (MongoDB) on port 27017

---

## **Need Help?**

```bash
# Full documentation
cat README.md

# Run all tests
./TEST_ALL.sh

# Verify setup
./VERIFY_ALL.sh
```

🎉 **Happy Coding!**

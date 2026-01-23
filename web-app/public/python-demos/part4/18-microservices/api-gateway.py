"""
Microservices Demo - API Gateway
Part 4: Advanced Topics - Hour 35
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- API Gateway that routes requests to microservices
- Service aggregation
- Health checks for all services
"""

# Note: Requires FastAPI, uvicorn, and httpx
# pip install fastapi uvicorn httpx

try:
    from fastapi import FastAPI, HTTPException
    from fastapi.responses import JSONResponse
    import httpx
    import uvicorn

    app = FastAPI(title="API Gateway", version="1.0.0")

    # Service URLs
    USER_SERVICE_URL = "http://localhost:8001"
    POST_SERVICE_URL = "http://localhost:8002"

    # Routes
    @app.get("/")
    def root():
        return {
            "service": "API Gateway",
            "version": "1.0.0",
            "status": "running",
            "services": {
                "user_service": USER_SERVICE_URL,
                "post_service": POST_SERVICE_URL
            },
            "endpoints": {
                "GET /health": "Check all services health",
                "GET /users": "Get all users (proxied)",
                "POST /users": "Create user (proxied)",
                "GET /posts": "Get all posts (proxied)",
                "POST /posts": "Create post (proxied)"
            }
        }

    @app.get("/health")
    async def health():
        """Check health of all services"""
        services_status = {}
        
        async with httpx.AsyncClient() as client:
            # Check user service
            try:
                response = await client.get(f"{USER_SERVICE_URL}/health", timeout=2.0)
                services_status["user_service"] = {
                    "status": "healthy" if response.status_code == 200 else "unhealthy",
                    "url": USER_SERVICE_URL
                }
            except:
                services_status["user_service"] = {
                    "status": "unreachable",
                    "url": USER_SERVICE_URL
                }
            
            # Check post service
            try:
                response = await client.get(f"{POST_SERVICE_URL}/health", timeout=2.0)
                services_status["post_service"] = {
                    "status": "healthy" if response.status_code == 200 else "unhealthy",
                    "url": POST_SERVICE_URL
                }
            except:
                services_status["post_service"] = {
                    "status": "unreachable",
                    "url": POST_SERVICE_URL
                }
        
        all_healthy = all(s["status"] == "healthy" for s in services_status.values())
        
        return {
            "gateway": "healthy",
            "all_services_healthy": all_healthy,
            "services": services_status
        }

    @app.get("/users")
    async def get_users():
        """Proxy request to user service"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{USER_SERVICE_URL}/users")
                return response.json()
            except:
                raise HTTPException(status_code=503, detail="User service unavailable")

    @app.post("/users")
    async def create_user(user_data: dict):
        """Proxy request to user service"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{USER_SERVICE_URL}/users", json=user_data)
                return response.json()
            except:
                raise HTTPException(status_code=503, detail="User service unavailable")

    @app.get("/posts")
    async def get_posts():
        """Proxy request to post service"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{POST_SERVICE_URL}/posts")
                return response.json()
            except:
                raise HTTPException(status_code=503, detail="Post service unavailable")

    @app.post("/posts")
    async def create_post(post_data: dict):
        """Proxy request to post service"""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f"{POST_SERVICE_URL}/posts", json=post_data)
                return response.json()
            except:
                raise HTTPException(status_code=503, detail="Post service unavailable")

    if __name__ == "__main__":
        print("🚀 Starting API Gateway on http://localhost:8000")
        print("📝 API Docs: http://localhost:8000/docs")
        print("\n⚠️  Make sure User Service (8001) and Post Service (8002) are running!")
        print("   Start them in separate terminals:")
        print("   Terminal 1: python user-service.py")
        print("   Terminal 2: python post-service.py")
        print("   Terminal 3: python api-gateway.py")
        uvicorn.run(app, host="0.0.0.0", port=8000)

except ImportError:
    print("❌ Required packages not installed!")
    print("Install with: pip install fastapi uvicorn httpx")
    print("\nTo run the microservices demo:")
    print("1. Install: pip install fastapi uvicorn httpx")
    print("2. Start User Service: python user-service.py (port 8001)")
    print("3. Start Post Service: python post-service.py (port 8002)")
    print("4. Start API Gateway: python api-gateway.py (port 8000)")
    print("5. Access Gateway: http://localhost:8000/docs")



"""
Microservices Demo - User Service
Part 4: Advanced Topics - Hour 35
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- FastAPI microservice for user management
- RESTful API endpoints
- Service health checks
"""

# Note: Requires FastAPI and uvicorn
# pip install fastapi uvicorn

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import List, Optional
    import uvicorn

    app = FastAPI(title="User Service", version="1.0.0")

    # In-memory database
    users_db = []
    user_id_counter = 1

    # Models
    class User(BaseModel):
        username: str
        email: str
        full_name: Optional[str] = None

    class UserResponse(User):
        id: int

    # Routes
    @app.get("/")
    def root():
        return {
            "service": "User Service",
            "version": "1.0.0",
            "status": "running",
            "endpoints": {
                "GET /users": "Get all users",
                "GET /users/{id}": "Get user by ID",
                "POST /users": "Create user",
                "DELETE /users/{id}": "Delete user"
            }
        }

    @app.get("/health")
    def health():
        return {"status": "healthy", "service": "user-service"}

    @app.get("/users", response_model=List[UserResponse])
    def get_users():
        """Get all users"""
        return users_db

    @app.get("/users/{user_id}", response_model=UserResponse)
    def get_user(user_id: int):
        """Get user by ID"""
        user = next((u for u in users_db if u["id"] == user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @app.post("/users", response_model=UserResponse, status_code=201)
    def create_user(user: User):
        """Create a new user"""
        global user_id_counter
        
        # Check if username already exists
        if any(u["username"] == user.username for u in users_db):
            raise HTTPException(status_code=400, detail="Username already exists")
        
        new_user = {
            "id": user_id_counter,
            "username": user.username,
            "email": user.email,
            "full_name": user.full_name
        }
        users_db.append(new_user)
        user_id_counter += 1
        
        return new_user

    @app.delete("/users/{user_id}")
    def delete_user(user_id: int):
        """Delete user"""
        global users_db
        user = next((u for u in users_db if u["id"] == user_id), None)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        users_db = [u for u in users_db if u["id"] != user_id]
        return {"message": "User deleted successfully"}

    if __name__ == "__main__":
        print("🚀 Starting User Service on http://localhost:8001")
        print("📝 API Docs: http://localhost:8001/docs")
        uvicorn.run(app, host="0.0.0.0", port=8001)

except ImportError:
    print("❌ FastAPI not installed!")
    print("Install with: pip install fastapi uvicorn")
    print("\nTo run this service:")
    print("1. Install: pip install fastapi uvicorn")
    print("2. Run: python user-service.py")
    print("3. Access: http://localhost:8001/docs")



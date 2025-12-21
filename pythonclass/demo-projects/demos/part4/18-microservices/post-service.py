"""
Microservices Demo - Post Service
Part 4: Advanced Topics - Hour 35
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- FastAPI microservice for post management
- RESTful API endpoints
- Service health checks
"""

# Note: Requires FastAPI and uvicorn
# pip install fastapi uvicorn

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import List, Optional
    from datetime import datetime
    import uvicorn

    app = FastAPI(title="Post Service", version="1.0.0")

    # In-memory database
    posts_db = []
    post_id_counter = 1

    # Models
    class Post(BaseModel):
        title: str
        content: str
        author_id: int

    class PostResponse(Post):
        id: int
        created_at: str

    # Routes
    @app.get("/")
    def root():
        return {
            "service": "Post Service",
            "version": "1.0.0",
            "status": "running",
            "endpoints": {
                "GET /posts": "Get all posts",
                "GET /posts/{id}": "Get post by ID",
                "POST /posts": "Create post",
                "GET /posts/user/{user_id}": "Get posts by user",
                "DELETE /posts/{id}": "Delete post"
            }
        }

    @app.get("/health")
    def health():
        return {"status": "healthy", "service": "post-service"}

    @app.get("/posts", response_model=List[PostResponse])
    def get_posts():
        """Get all posts"""
        return posts_db

    @app.get("/posts/{post_id}", response_model=PostResponse)
    def get_post(post_id: int):
        """Get post by ID"""
        post = next((p for p in posts_db if p["id"] == post_id), None)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    @app.get("/posts/user/{user_id}", response_model=List[PostResponse])
    def get_posts_by_user(user_id: int):
        """Get posts by user ID"""
        user_posts = [p for p in posts_db if p["author_id"] == user_id]
        return user_posts

    @app.post("/posts", response_model=PostResponse, status_code=201)
    def create_post(post: Post):
        """Create a new post"""
        global post_id_counter
        
        new_post = {
            "id": post_id_counter,
            "title": post.title,
            "content": post.content,
            "author_id": post.author_id,
            "created_at": datetime.now().isoformat()
        }
        posts_db.append(new_post)
        post_id_counter += 1
        
        return new_post

    @app.delete("/posts/{post_id}")
    def delete_post(post_id: int):
        """Delete post"""
        global posts_db
        post = next((p for p in posts_db if p["id"] == post_id), None)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        
        posts_db = [p for p in posts_db if p["id"] != post_id]
        return {"message": "Post deleted successfully"}

    if __name__ == "__main__":
        print("🚀 Starting Post Service on http://localhost:8002")
        print("📝 API Docs: http://localhost:8002/docs")
        uvicorn.run(app, host="0.0.0.0", port=8002)

except ImportError:
    print("❌ FastAPI not installed!")
    print("Install with: pip install fastapi uvicorn")
    print("\nTo run this service:")
    print("1. Install: pip install fastapi uvicorn")
    print("2. Run: python post-service.py")
    print("3. Access: http://localhost:8002/docs")



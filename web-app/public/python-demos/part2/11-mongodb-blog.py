"""
Demo Project 11: MongoDB Blog
Part 2: Backend Development - Hour 16
Difficulty: ⭐⭐⭐ Advanced

Features:
- NoSQL database with MongoDB
- Embedded documents
- Aggregation pipelines
- Document queries
"""

# Note: This requires pymongo to be installed
# pip install pymongo

try:
    from pymongo import MongoClient
    from datetime import datetime
    import json
    
    class MongoDBBlog:
        """MongoDB blog manager"""
        
        def __init__(self, db_name="blog_db"):
            self.client = MongoClient('mongodb://localhost:27017/')
            self.db = self.client[db_name]
            self.posts = self.db.posts
            self.users = self.db.users
            print("✅ Connected to MongoDB!")
        
        def add_user(self, username, email, bio=""):
            """Add a new user"""
            user = {
                "username": username,
                "email": email,
                "bio": bio,
                "created_at": datetime.utcnow()
            }
            result = self.users.insert_one(user)
            print(f"✅ User '{username}' added!")
            return result.inserted_id
        
        def create_post(self, title, content, username):
            """Create a new post"""
            post = {
                "title": title,
                "content": content,
                "author": username,
                "likes": 0,
                "comments": [],  # Embedded comments
                "created_at": datetime.utcnow()
            }
            result = self.posts.insert_one(post)
            print(f"✅ Post '{title}' created!")
            return result.inserted_id
        
        def like_post(self, post_id):
            """Like a post"""
            self.posts.update_one(
                {"_id": post_id},
                {"$inc": {"likes": 1}}
            )
            print(f"✅ Post liked!")
        
        def add_comment(self, post_id, username, text):
            """Add a comment (embedded document)"""
            comment = {
                "username": username,
                "text": text,
                "created_at": datetime.utcnow()
            }
            self.posts.update_one(
                {"_id": post_id},
                {"$push": {"comments": comment}}
            )
            print(f"✅ Comment added!")
        
        def get_all_posts(self):
            """Get all posts"""
            return list(self.posts.find().sort("created_at", -1))
        
        def get_user_posts(self, username):
            """Get posts by user"""
            return list(self.posts.find({"author": username}))
        
        def get_popular_posts(self, min_likes=1):
            """Get popular posts"""
            return list(self.posts.find({"likes": {"$gte": min_likes}}).sort("likes", -1))
        
        def close(self):
            """Close connection"""
            self.client.close()
    
    
    def main():
        """Demo MongoDB blog"""
        try:
            blog = MongoDBBlog()
            
            # Add users
            blog.add_user("alice_dev", "alice@example.com", "Python developer")
            blog.add_user("bob_tech", "bob@example.com", "Full-stack engineer")
            
            # Create posts
            post1_id = blog.create_post(
                "Getting Started with Python",
                "Python is an amazing language...",
                "alice_dev"
            )
            
            post2_id = blog.create_post(
                "Building REST APIs",
                "Flask is a lightweight framework...",
                "bob_tech"
            )
            
            # Like posts
            blog.like_post(post1_id)
            blog.like_post(post1_id)
            
            # Add comments
            blog.add_comment(post1_id, "bob_tech", "Great post!")
            blog.add_comment(post1_id, "charlie", "Thanks!")
            
            # Display posts
            print("\n📝 All Posts:")
            posts = blog.get_all_posts()
            for post in posts:
                print(f"\n  Title: {post['title']}")
                print(f"  Author: {post['author']}")
                print(f"  Likes: {post['likes']}")
                print(f"  Comments: {len(post['comments'])}")
            
            blog.close()
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Make sure MongoDB is running: mongod")
            print("Install pymongo: pip install pymongo")
    
    
    if __name__ == "__main__":
        main()

except ImportError:
    print("❌ pymongo not installed!")
    print("Install it with: pip install pymongo")
    print("Also make sure MongoDB is installed and running")



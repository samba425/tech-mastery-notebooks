"""
Demo Project 9: Blog Database (SQLite)
Part 2: Backend Development - Hour 14
Difficulty: ⭐⭐⭐ Advanced

Features:
- SQLite database integration
- CRUD operations
- SQL queries
- Database relationships
"""

import sqlite3
from datetime import datetime

class BlogDatabase:
    """Blog database manager using SQLite"""
    
    def __init__(self, db_name="blog.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()
    
    def create_tables(self):
        """Create database tables"""
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                bio TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Posts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author_id INTEGER NOT NULL,
                likes INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (author_id) REFERENCES users(id)
            )
        """)
        
        # Comments table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER NOT NULL,
                username TEXT NOT NULL,
                text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (post_id) REFERENCES posts(id)
            )
        """)
        
        self.conn.commit()
        print("✅ Database tables created!")
    
    def add_user(self, username, email, bio=""):
        """Add a new user"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO users (username, email, bio)
                VALUES (?, ?, ?)
            """, (username, email, bio))
            self.conn.commit()
            print(f"✅ User '{username}' added!")
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"❌ User '{username}' or email already exists!")
            return None
    
    def create_post(self, title, content, author_id):
        """Create a new post"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO posts (title, content, author_id)
            VALUES (?, ?, ?)
        """, (title, content, author_id))
        self.conn.commit()
        print(f"✅ Post '{title}' created!")
        return cursor.lastrowid
    
    def get_all_posts(self):
        """Get all posts with author info"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT p.id, p.title, p.content, p.likes, u.username as author
            FROM posts p
            JOIN users u ON p.author_id = u.id
            ORDER BY p.created_at DESC
        """)
        return cursor.fetchall()
    
    def like_post(self, post_id):
        """Like a post"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE posts SET likes = likes + 1 WHERE id = ?
        """, (post_id,))
        self.conn.commit()
        print(f"✅ Post {post_id} liked!")
    
    def add_comment(self, post_id, username, text):
        """Add a comment to a post"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO comments (post_id, username, text)
            VALUES (?, ?, ?)
        """, (post_id, username, text))
        self.conn.commit()
        print(f"✅ Comment added!")
    
    def get_post_comments(self, post_id):
        """Get all comments for a post"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT username, text, created_at
            FROM comments
            WHERE post_id = ?
            ORDER BY created_at ASC
        """, (post_id,))
        return cursor.fetchall()
    
    def get_user_posts(self, username):
        """Get all posts by a user"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT p.id, p.title, p.content, p.likes
            FROM posts p
            JOIN users u ON p.author_id = u.id
            WHERE u.username = ?
        """, (username,))
        return cursor.fetchall()
    
    def close(self):
        """Close database connection"""
        self.conn.close()


def main():
    """Demo the blog database"""
    db = BlogDatabase()
    
    # Add users
    user1_id = db.add_user("alice_dev", "alice@example.com", "Python developer")
    user2_id = db.add_user("bob_tech", "bob@example.com", "Full-stack engineer")
    
    # Create posts
    post1_id = db.create_post(
        "Getting Started with Python",
        "Python is an amazing language for beginners...",
        user1_id
    )
    
    post2_id = db.create_post(
        "Building REST APIs with Flask",
        "Flask is a lightweight web framework...",
        user2_id
    )
    
    # Like posts
    db.like_post(post1_id)
    db.like_post(post1_id)
    db.like_post(post2_id)
    
    # Add comments
    db.add_comment(post1_id, "bob_tech", "Great post! Very helpful!")
    db.add_comment(post1_id, "charlie", "Thanks for sharing!")
    
    # Display all posts
    print("\n📝 All Posts:")
    posts = db.get_all_posts()
    for post in posts:
        print(f"\n  Post #{post['id']}: {post['title']}")
        print(f"  Author: {post['author']}")
        print(f"  Likes: {post['likes']}")
        print(f"  Content: {post['content'][:50]}...")
        
        # Show comments
        comments = db.get_post_comments(post['id'])
        if comments:
            print(f"  Comments ({len(comments)}):")
            for comment in comments:
                print(f"    - {comment['username']}: {comment['text']}")
    
    # Get user posts
    print("\n👤 Posts by alice_dev:")
    user_posts = db.get_user_posts("alice_dev")
    for post in user_posts:
        print(f"  - {post['title']} ({post['likes']} likes)")
    
    db.close()


if __name__ == "__main__":
    main()



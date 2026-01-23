"""
Demo Project 10: Blog ORM (SQLAlchemy)
Part 2: Backend Development - Hour 15
Difficulty: ⭐⭐⭐ Advanced

Features:
- Object-Relational Mapping with SQLAlchemy
- Relationships between models
- Database migrations
- Query optimization
"""

# Note: This requires SQLAlchemy to be installed
# pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    bio = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    posts = relationship("Post", back_populates="author")
    
    def __repr__(self):
        return f"<User(username='{self.username}')>"


class Post(Base):
    """Post model"""
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    
    def __repr__(self):
        return f"<Post(title='{self.title}')>"


class Comment(Base):
    """Comment model"""
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    username = Column(String(50), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    post = relationship("Post", back_populates="comments")
    
    def __repr__(self):
        return f"<Comment(username='{self.username}')>"


class BlogORM:
    """Blog ORM manager"""
    
    def __init__(self, db_url="sqlite:///blog_orm.db"):
        self.engine = create_engine(db_url, echo=False)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        print("✅ Database initialized!")
    
    def add_user(self, username, email, bio=""):
        """Add a new user"""
        try:
            user = User(username=username, email=email, bio=bio)
            self.session.add(user)
            self.session.commit()
            print(f"✅ User '{username}' added!")
            return user
        except Exception as e:
            self.session.rollback()
            print(f"❌ Error: {e}")
            return None
    
    def create_post(self, title, content, author_id):
        """Create a new post"""
        post = Post(title=title, content=content, author_id=author_id)
        self.session.add(post)
        self.session.commit()
        print(f"✅ Post '{title}' created!")
        return post
    
    def like_post(self, post_id):
        """Like a post"""
        post = self.session.query(Post).filter_by(id=post_id).first()
        if post:
            post.likes += 1
            self.session.commit()
            print(f"✅ Post {post_id} liked!")
        else:
            print(f"❌ Post {post_id} not found!")
    
    def add_comment(self, post_id, username, text):
        """Add a comment"""
        comment = Comment(post_id=post_id, username=username, text=text)
        self.session.add(comment)
        self.session.commit()
        print(f"✅ Comment added!")
    
    def get_all_posts(self):
        """Get all posts with author"""
        return self.session.query(Post).join(User).all()
    
    def get_user_posts(self, username):
        """Get posts by user"""
        user = self.session.query(User).filter_by(username=username).first()
        if user:
            return user.posts
        return []
    
    def close(self):
        """Close session"""
        self.session.close()


def main():
    """Demo the blog ORM"""
    try:
        blog = BlogORM()
        
        # Add users
        user1 = blog.add_user("alice_dev", "alice@example.com", "Python developer")
        user2 = blog.add_user("bob_tech", "bob@example.com", "Full-stack engineer")
        
        if user1 and user2:
            # Create posts
            post1 = blog.create_post(
                "Getting Started with Python",
                "Python is an amazing language for beginners...",
                user1.id
            )
            
            post2 = blog.create_post(
                "Building REST APIs with Flask",
                "Flask is a lightweight web framework...",
                user2.id
            )
            
            # Like posts
            blog.like_post(post1.id)
            blog.like_post(post1.id)
            
            # Add comments
            blog.add_comment(post1.id, "bob_tech", "Great post!")
            blog.add_comment(post1.id, "charlie", "Thanks!")
            
            # Display posts
            print("\n📝 All Posts:")
            posts = blog.get_all_posts()
            for post in posts:
                print(f"\n  Post #{post.id}: {post.title}")
                print(f"  Author: {post.author.username}")
                print(f"  Likes: {post.likes}")
                print(f"  Comments: {len(post.comments)}")
        
        blog.close()
        
    except ImportError:
        print("❌ SQLAlchemy not installed!")
        print("Install it with: pip install sqlalchemy")


if __name__ == "__main__":
    main()



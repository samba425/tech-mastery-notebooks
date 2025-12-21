"""
Demo Project 7: Blog System (OOP)
Part 2: Backend Development - Hour 11
Difficulty: ⭐⭐ Medium

Features:
- User class with profile
- Post class with content
- Create users and posts
- Like posts
- Comment on posts
- Display blog statistics
"""

class User:
    """Represents a blog user"""
    
    def __init__(self, username, email, bio):
        self.username = username
        self.email = email
        self.bio = bio
        self.posts = []  # List to store user's posts
    
    def create_post(self, title, content):
        """Create a new blog post"""
        post = Post(title, content, self.username)
        self.posts.append(post)
        print(f"✅ Post '{title}' created successfully!")
        return post
    
    def display_profile(self):
        """Display user profile"""
        print("\n" + "=" * 50)
        print(f"👤 User Profile")
        print("=" * 50)
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Bio: {self.bio}")
        print(f"Total Posts: {len(self.posts)}")
        print("=" * 50)
    
    def show_all_posts(self):
        """Display all posts by this user"""
        print(f"\n📝 Posts by {self.username}:")
        print("-" * 50)
        if self.posts:
            for i, post in enumerate(self.posts, 1):
                print(f"\n{i}. {post.title}")
                print(f"   {post.content[:50]}...")
        else:
            print("No posts yet.")


class Post:
    """Represents a blog post"""
    
    post_count = 0  # Class variable to track total posts
    
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes = 0
        self.comments = []
        Post.post_count += 1
        self.post_id = Post.post_count
    
    def like(self):
        """Like the post"""
        self.likes += 1
        print(f"❤️ Post liked! Total likes: {self.likes}")
    
    def add_comment(self, username, comment_text):
        """Add a comment to the post"""
        comment = {
            "username": username,
            "text": comment_text
        }
        self.comments.append(comment)
        print(f"💬 Comment added by {username}")
    
    def display_post(self):
        """Display post details"""
        print("\n" + "=" * 50)
        print(f"📄 Post #{self.post_id}")
        print("=" * 50)
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"\n{self.content}\n")
        print(f"❤️ Likes: {self.likes}")
        print(f"💬 Comments: {len(self.comments)}")
        
        if self.comments:
            print("\nComments:")
            for comment in self.comments:
                print(f"  - {comment['username']}: {comment['text']}")
        print("=" * 50)


def main():
    """Demo the blog system"""
    # Create users
    user1 = User("alice_dev", "alice@email.com", "Python developer 🐍")
    user2 = User("bob_tech", "bob@email.com", "Full-stack engineer 💻")
    
    # Show profiles
    user1.display_profile()
    user2.display_profile()
    
    # Create posts
    post1 = user1.create_post(
        "Getting Started with Python",
        "Python is an amazing language for beginners. In this post, I'll show you how to get started with Python programming..."
    )
    
    post2 = user1.create_post(
        "10 Python Tips",
        "Here are my top 10 Python tips that will make you a better programmer..."
    )
    
    post3 = user2.create_post(
        "Building REST APIs with Flask",
        "Flask is a lightweight web framework for Python. Let's build a simple REST API..."
    )
    
    # Interact with posts
    post1.display_post()
    post1.like()
    post1.like()
    post1.add_comment("bob_tech", "Great post! Very helpful!")
    post1.add_comment("charlie", "Thanks for sharing!")
    post1.display_post()
    
    # Show all posts by user
    user1.show_all_posts()
    
    # Show statistics
    print(f"\n📊 Blog Statistics:")
    print(f"Total Posts: {Post.post_count}")
    print(f"Total Users: 2")


if __name__ == "__main__":
    main()



"""
Demo Project 20: GraphQL API
Part 4: Advanced Topics - Hour 38
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- GraphQL API with queries and mutations
- Type system
- Resolvers
- Schema definition
"""

# Note: This requires graphene and Flask
# IMPORTANT: GraphQL dependencies conflict with Flask-SQLAlchemy 3.x
# Install in separate environment or use older Flask-SQLAlchemy:
# pip install flask flask-graphql graphene graphene-sqlalchemy SQLAlchemy<2.0
# OR install separately: pip install -r requirements-graphql.txt

try:
    from flask import Flask
    from flask_graphql import GraphQLView
    import graphene
    from graphene import ObjectType, String, Int, List, Field
    
    app = Flask(__name__)
    
    # Sample data
    posts_data = [
        {'id': 1, 'title': 'Python Basics', 'content': 'Learn Python...', 'author': 'Alice'},
        {'id': 2, 'title': 'Flask Tutorial', 'content': 'Build APIs...', 'author': 'Bob'},
    ]
    
    users_data = [
        {'id': 1, 'username': 'alice', 'email': 'alice@example.com'},
        {'id': 2, 'username': 'bob', 'email': 'bob@example.com'},
    ]
    
    # GraphQL Types
    class PostType(ObjectType):
        id = Int()
        title = String()
        content = String()
        author = String()
    
    class UserType(ObjectType):
        id = Int()
        username = String()
        email = String()
    
    # Query
    class Query(ObjectType):
        posts = List(PostType)
        post = Field(PostType, id=Int(required=True))
        users = List(UserType)
        user = Field(UserType, id=Int(required=True))
        
        def resolve_posts(self, info):
            return posts_data
        
        def resolve_post(self, info, id):
            return next((p for p in posts_data if p['id'] == id), None)
        
        def resolve_users(self, info):
            return users_data
        
        def resolve_user(self, info, id):
            return next((u for u in users_data if u['id'] == id), None)
    
    # Mutation
    class CreatePost(graphene.Mutation):
        class Arguments:
            title = String(required=True)
            content = String(required=True)
            author = String(required=True)
        
        post = Field(PostType)
        
        def mutate(self, info, title, content, author):
            new_id = len(posts_data) + 1
            post = {
                'id': new_id,
                'title': title,
                'content': content,
                'author': author
            }
            posts_data.append(post)
            return CreatePost(post=post)
    
    class Mutations(ObjectType):
        create_post = CreatePost.Field()
    
    # Schema
    schema = graphene.Schema(query=Query, mutation=Mutations)
    
    # GraphQL endpoint
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    )
    
    @app.route('/')
    def home():
        return '''
        <h1>GraphQL API Demo</h1>
        <p>Access GraphQL Playground at: <a href="/graphql">/graphql</a></p>
        <h2>Example Queries:</h2>
        <pre>
# Get all posts
{
  posts {
    id
    title
    author
  }
}

# Get single post
{
  post(id: 1) {
    id
    title
    content
    author
  }
}

# Create post (mutation)
mutation {
  createPost(title: "New Post", content: "Content here", author: "Alice") {
    post {
      id
      title
    }
  }
}
        </pre>
        '''
    
    if __name__ == '__main__':
        print("🚀 Starting GraphQL API...")
        print("📝 GraphQL Playground: http://localhost:5000/graphql")
        print("\nExample queries:")
        print("- Get all posts: { posts { id title author } }")
        print("- Get post by ID: { post(id: 1) { title content } }")
        print("- Create post: mutation { createPost(...) { post { id } } }")
        app.run(debug=True, port=5000)

except ImportError:
    print("❌ Required packages not installed!")
    print("Install with: pip install flask flask-graphql graphene")
    print("\nTo run this API:")
    print("1. Install dependencies: pip install flask flask-graphql graphene")
    print("2. Run: python 20-graphql-api.py")
    print("3. Open: http://localhost:5000/graphql")



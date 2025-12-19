# Part 3: Frontend Development with React
## Hours 21-30 (HTML, CSS, JavaScript, React)

**Duration:** 10 hours total  
**Target:** Students who completed Backend development  
**Format:** 1 hour per session  
**Style:** Read and teach directly, copy-paste examples

---

## 📚 TABLE OF CONTENTS

- [Hour 21: HTML & CSS Fundamentals](#hour-21)
- [Hour 22: JavaScript Essentials](#hour-22)
- [Hour 23: Intro to React](#hour-23)
- [Hour 24: React State Management & Hooks](#hour-24)
- [Hour 25: React Router](#hour-25)
- [Hour 26: Styling React Apps](#hour-26)
- [Hour 27: State Management (Context/Redux)](#hour-27)
- [Hour 28: Forms & Validation](#hour-28)
- [Hour 29: Consuming APIs](#hour-29)
- [Hour 30: Full-Stack Integration](#hour-30)

---

<a name="hour-21"></a>
## 📅 Hour 21: HTML & CSS Fundamentals

### 🎯 Learning Objectives
- Understand HTML structure
- Learn semantic HTML tags
- Master CSS box model
- Create responsive designs
- Build a blog post page

### 📖 What to Teach

**"Today we learn HTML & CSS - the building blocks of every website you see!"**

---

### 1️⃣ What is HTML? (10 minutes)

**Real-Life Analogy:**

```
Building a House:
├── HTML = Structure (walls, rooms, doors)
├── CSS = Decoration (paint, furniture, colors)
└── JavaScript = Functionality (lights, doors opening)
```

**Basic HTML Structure:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Page</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>This is my first webpage.</p>
</body>
</html>
```

**Explain Each Part:**

```html
<!DOCTYPE html>          <!-- Tells browser this is HTML5 -->
<html>                   <!-- Root element -->
<head>                   <!-- Metadata (not visible) -->
    <title>            <!-- Browser tab title -->
<body>                   <!-- Visible content -->
```

---

### 2️⃣ Common HTML Tags (10 minutes)

**Text Elements:**

```html
<!-- Headings (h1 largest, h6 smallest) -->
<h1>Main Heading</h1>
<h2>Sub Heading</h2>
<h3>Section Heading</h3>

<!-- Paragraphs -->
<p>This is a paragraph of text.</p>

<!-- Text formatting -->
<strong>Bold text</strong>
<em>Italic text</em>
<u>Underlined text</u>

<!-- Line break -->
<br>

<!-- Horizontal line -->
<hr>
```

**Links and Images:**

```html
<!-- Links -->
<a href="https://google.com">Visit Google</a>
<a href="about.html">About Page</a>

<!-- Images -->
<img src="photo.jpg" alt="Description of image">

<!-- Image with link -->
<a href="profile.html">
    <img src="profile.jpg" alt="Profile Picture">
</a>
```

**Lists:**

```html
<!-- Unordered list (bullets) -->
<ul>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>

<!-- Ordered list (numbers) -->
<ol>
    <li>Step 1</li>
    <li>Step 2</li>
    <li>Step 3</li>
</ol>
```

---

### 3️⃣ Semantic HTML (10 minutes)

**Explain:**

"Semantic HTML uses meaningful tag names - like labeling boxes clearly!"

**Semantic Tags:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog Post</title>
</head>
<body>
    <!-- Header (top of page) -->
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    
    <!-- Main content -->
    <main>
        <!-- Individual article -->
        <article>
            <h1>Article Title</h1>
            <p>Article content goes here...</p>
            
            <!-- Section within article -->
            <section>
                <h2>Section Heading</h2>
                <p>Section content...</p>
            </section>
        </article>
        
        <!-- Sidebar -->
        <aside>
            <h3>Related Posts</h3>
            <ul>
                <li><a href="#">Post 1</a></li>
                <li><a href="#">Post 2</a></li>
            </ul>
        </aside>
    </main>
    
    <!-- Footer (bottom of page) -->
    <footer>
        <p>&copy; 2025 My Blog</p>
    </footer>
</body>
</html>
```

---

### 4️⃣ CSS Basics (15 minutes)

**Three Ways to Add CSS:**

```html
<!-- 1. Inline CSS (not recommended) -->
<p style="color: red; font-size: 20px;">Red text</p>

<!-- 2. Internal CSS (in <head>) -->
<head>
    <style>
        p {
            color: blue;
            font-size: 18px;
        }
    </style>
</head>

<!-- 3. External CSS (best practice) -->
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

**CSS Syntax:**

```css
/* selector { property: value; } */

h1 {
    color: blue;
    font-size: 32px;
    font-weight: bold;
}

p {
    color: #333;
    line-height: 1.6;
}
```

**CSS Selectors:**

```css
/* Element selector */
p { color: black; }

/* Class selector (reusable) */
.highlight { background: yellow; }

/* ID selector (unique) */
#header { background: navy; }

/* Multiple selectors */
h1, h2, h3 { color: darkblue; }

/* Descendant selector */
article p { font-size: 16px; }
```

```html
<!-- Using classes and IDs -->
<p class="highlight">Highlighted text</p>
<div id="header">Header content</div>
```

---

### 5️⃣ CSS Box Model (10 minutes)

**Explain with Diagram:**

```
┌─────────────────────────────────────┐
│         MARGIN (outside)            │
│  ┌───────────────────────────────┐  │
│  │    BORDER                     │  │
│  │  ┌─────────────────────────┐  │  │
│  │  │  PADDING (inside)       │  │  │
│  │  │  ┌───────────────────┐  │  │  │
│  │  │  │   CONTENT         │  │  │  │
│  │  │  │  (actual element) │  │  │  │
│  │  │  └───────────────────┘  │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

**CSS Box Model Code:**

```css
.box {
    /* Content */
    width: 300px;
    height: 200px;
    
    /* Padding (space inside) */
    padding: 20px;
    
    /* Border */
    border: 2px solid black;
    
    /* Margin (space outside) */
    margin: 10px;
    
    /* Background */
    background-color: lightblue;
}
```

---

### 6️⃣ Responsive Design (5 minutes)

**Mobile-First Approach:**

```css
/* Base styles (mobile) */
.container {
    width: 100%;
    padding: 10px;
}

/* Tablet screens (768px and up) */
@media (min-width: 768px) {
    .container {
        width: 750px;
        margin: 0 auto;
    }
}

/* Desktop screens (1024px and up) */
@media (min-width: 1024px) {
    .container {
        width: 1000px;
    }
}
```

---

### 💻 Live Activity: Build a Blog Post Page

**Create: blog-post.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Getting Started with Python - My Blog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header -->
    <header class="site-header">
        <div class="container">
            <h1 class="logo">My Tech Blog</h1>
            <nav class="main-nav">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
            </nav>
        </div>
    </header>
    
    <!-- Main Content -->
    <main class="container">
        <article class="blog-post">
            <!-- Post Header -->
            <header class="post-header">
                <h1>Getting Started with Python Programming</h1>
                <div class="post-meta">
                    <span class="author">By Alice Johnson</span>
                    <span class="date">December 15, 2025</span>
                    <span class="read-time">5 min read</span>
                </div>
            </header>
            
            <!-- Featured Image -->
            <img src="python-banner.jpg" alt="Python Programming" class="featured-image">
            
            <!-- Post Content -->
            <div class="post-content">
                <p class="lead">Python is one of the most popular programming languages in the world. In this post, we'll explore why Python is great for beginners.</p>
                
                <h2>Why Learn Python?</h2>
                <p>Python is incredibly versatile and beginner-friendly. Here are the top reasons to learn Python:</p>
                
                <ul>
                    <li>Easy to read and write</li>
                    <li>Huge community support</li>
                    <li>Excellent for data science and AI</li>
                    <li>Great for web development</li>
                </ul>
                
                <h2>Getting Started</h2>
                <p>To start with Python, you'll need to install it on your computer. Here's how:</p>
                
                <ol>
                    <li>Visit python.org</li>
                    <li>Download Python 3.x</li>
                    <li>Run the installer</li>
                    <li>Verify installation</li>
                </ol>
                
                <h2>Your First Program</h2>
                <p>Let's write your first Python program:</p>
                
                <pre><code>print("Hello, World!")</code></pre>
                
                <p>That's it! You've just written your first Python program.</p>
            </div>
            
            <!-- Post Footer -->
            <footer class="post-footer">
                <div class="tags">
                    <span class="tag">Python</span>
                    <span class="tag">Programming</span>
                    <span class="tag">Beginners</span>
                </div>
                
                <div class="share">
                    <button class="btn-like">❤️ Like (42)</button>
                    <button class="btn-share">🔗 Share</button>
                </div>
            </footer>
        </article>
        
        <!-- Comments Section -->
        <section class="comments">
            <h3>Comments (3)</h3>
            
            <div class="comment">
                <div class="comment-header">
                    <strong>John Doe</strong>
                    <span class="comment-date">2 hours ago</span>
                </div>
                <p>Great article! Very helpful for beginners.</p>
            </div>
            
            <div class="comment">
                <div class="comment-header">
                    <strong>Jane Smith</strong>
                    <span class="comment-date">5 hours ago</span>
                </div>
                <p>Thanks for sharing! Looking forward to more Python tutorials.</p>
            </div>
        </section>
    </main>
    
    <!-- Footer -->
    <footer class="site-footer">
        <div class="container">
            <p>&copy; 2025 My Tech Blog. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

**Create: styles.css**

```css
/* ========== RESET & BASICS ========== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f4f4f4;
}

.container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 20px;
}

/* ========== HEADER ========== */
.site-header {
    background: #2c3e50;
    color: white;
    padding: 20px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.logo {
    font-size: 28px;
    margin-bottom: 10px;
}

.main-nav a {
    color: white;
    text-decoration: none;
    margin-right: 20px;
    font-size: 16px;
}

.main-nav a:hover {
    color: #3498db;
}

/* ========== BLOG POST ========== */
.blog-post {
    background: white;
    padding: 40px;
    margin: 40px 0;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.post-header h1 {
    font-size: 36px;
    color: #2c3e50;
    margin-bottom: 15px;
}

.post-meta {
    color: #7f8c8d;
    margin-bottom: 20px;
    font-size: 14px;
}

.post-meta span {
    margin-right: 15px;
}

.featured-image {
    width: 100%;
    height: 400px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 30px;
}

.post-content {
    font-size: 18px;
    line-height: 1.8;
}

.post-content .lead {
    font-size: 22px;
    color: #555;
    margin-bottom: 30px;
    font-weight: 300;
}

.post-content h2 {
    margin-top: 30px;
    margin-bottom: 15px;
    color: #2c3e50;
}

.post-content ul, .post-content ol {
    margin: 20px 0;
    padding-left: 40px;
}

.post-content li {
    margin-bottom: 10px;
}

.post-content pre {
    background: #2c3e50;
    color: #fff;
    padding: 20px;
    border-radius: 5px;
    overflow-x: auto;
    margin: 20px 0;
}

/* ========== POST FOOTER ========== */
.post-footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 2px solid #ecf0f1;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.tag {
    display: inline-block;
    background: #3498db;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 14px;
    margin-right: 10px;
}

.btn-like, .btn-share {
    background: #ecf0f1;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    margin-left: 10px;
    font-size: 14px;
}

.btn-like:hover, .btn-share:hover {
    background: #bdc3c7;
}

/* ========== COMMENTS ========== */
.comments {
    background: white;
    padding: 30px;
    margin-bottom: 40px;
    border-radius: 8px;
}

.comments h3 {
    margin-bottom: 20px;
}

.comment {
    padding: 15px;
    background: #f9f9f9;
    border-left: 4px solid #3498db;
    margin-bottom: 15px;
}

.comment-header {
    margin-bottom: 10px;
}

.comment-header strong {
    color: #2c3e50;
}

.comment-date {
    color: #7f8c8d;
    font-size: 14px;
    margin-left: 10px;
}

/* ========== FOOTER ========== */
.site-footer {
    background: #2c3e50;
    color: white;
    text-align: center;
    padding: 20px 0;
}

/* ========== RESPONSIVE ========== */
@media (max-width: 768px) {
    .blog-post {
        padding: 20px;
    }
    
    .post-header h1 {
        font-size: 28px;
    }
    
    .post-content {
        font-size: 16px;
    }
    
    .featured-image {
        height: 250px;
    }
    
    .post-footer {
        flex-direction: column;
        align-items: flex-start;
    }
    
    .share {
        margin-top: 15px;
    }
}
```

**Show students the result in browser!**

---

### 🏠 Homework: Style Flask Templates

**Task:** Take the Flask templates from Hour 18 and style them with CSS

```html
<!-- base.html (Flask template) -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Blog{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 My Blog</p>
    </footer>
</body>
</html>
```

**Create complete CSS styling for Flask blog!**

---

### 📝 Key Takeaways

✅ HTML = Structure of webpage
✅ CSS = Styling/appearance
✅ Semantic HTML = meaningful tags
✅ Box Model = margin, border, padding, content
✅ Responsive = works on all devices
✅ @media queries = different screen sizes

---

<a name="hour-22"></a>
## 📅 Hour 22: JavaScript Essentials

### 🎯 Learning Objectives
- Learn JavaScript basics
- Manipulate the DOM
- Handle events
- Use fetch API
- Add interactivity to pages

### 📖 What to Teach

**"JavaScript makes websites interactive - like adding electricity to a house!"**

---

### 1️⃣ JavaScript Basics (15 minutes)

**Variables:**

```javascript
// Modern way (use these)
let name = "Alice";  // Can be changed
const age = 25;      // Cannot be changed

// Old way (avoid)
var city = "Mumbai"; // Don't use var

// Data types
let number = 42;
let text = "Hello";
let isActive = true;
let nothing = null;
let notDefined = undefined;
```

**Functions:**

```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow function (modern)
const add = (a, b) => a + b;

// Usage
console.log(greet("Alice"));  // Hello, Alice!
console.log(add(5, 3));        // 8
```

**Arrays:**

```javascript
const fruits = ["apple", "banana", "mango"];

// Access
console.log(fruits[0]);  // apple

// Add
fruits.push("orange");

// Loop
fruits.forEach(fruit => {
    console.log(fruit);
});

// Map (transform)
const uppercase = fruits.map(fruit => fruit.toUpperCase());
console.log(uppercase);  // ["APPLE", "BANANA", "MANGO", "ORANGE"]

// Filter
const longNames = fruits.filter(fruit => fruit.length > 5);
console.log(longNames);  // ["banana", "orange"]
```

**Objects:**

```javascript
const user = {
    name: "Alice",
    age: 25,
    email: "alice@email.com",
    greet: function() {
        console.log(`Hi, I'm ${this.name}`);
    }
};

// Access
console.log(user.name);  // Alice
console.log(user.age);   // 25

// Call method
user.greet();  // Hi, I'm Alice
```

---

### 2️⃣ DOM Manipulation (20 minutes)

**What is DOM?**

"DOM = Document Object Model. It's how JavaScript sees and changes HTML!"

**Selecting Elements:**

```javascript
// By ID
const header = document.getElementById('header');

// By Class
const buttons = document.getElementsByClassName('btn');

// By CSS Selector (most common)
const header = document.querySelector('#header');
const buttons = document.querySelectorAll('.btn');

// Get all paragraphs
const paragraphs = document.querySelectorAll('p');
```

**Changing Content:**

```javascript
// Change text
const heading = document.querySelector('h1');
heading.textContent = 'New Heading';

// Change HTML
const div = document.querySelector('#content');
div.innerHTML = '<p>New <strong>content</strong></p>';

// Change styles
heading.style.color = 'red';
heading.style.fontSize = '32px';

// Add/remove classes
heading.classList.add('highlight');
heading.classList.remove('old-class');
heading.classList.toggle('active');
```

**Creating Elements:**

```javascript
// Create new element
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello from JavaScript!';
newDiv.className = 'dynamic-content';

// Add to page
document.body.appendChild(newDiv);

// Or insert at specific position
const container = document.querySelector('#container');
container.appendChild(newDiv);
```

---

### 3️⃣ Event Handling (15 minutes)

**Click Events:**

```javascript
// Get button
const button = document.querySelector('#myButton');

// Add click event
button.addEventListener('click', function() {
    alert('Button clicked!');
});

// Arrow function (shorter)
button.addEventListener('click', () => {
    console.log('Clicked!');
});

// With event object
button.addEventListener('click', (event) => {
    console.log('Clicked at:', event.clientX, event.clientY);
});
```

**Form Events:**

```javascript
const form = document.querySelector('#contactForm');
const input = document.querySelector('#nameInput');

// Form submit
form.addEventListener('submit', (event) => {
    event.preventDefault();  // Stop form from submitting
    console.log('Form submitted!');
});

// Input change
input.addEventListener('input', (event) => {
    console.log('Current value:', event.target.value);
});

// Focus events
input.addEventListener('focus', () => {
    console.log('Input focused');
});

input.addEventListener('blur', () => {
    console.log('Input lost focus');
});
```

---

### 4️⃣ Fetch API (10 minutes)

**GET Request:**

```javascript
// Fetch posts from API
fetch('https://jsonplaceholder.typicode.com/posts')
    .then(response => response.json())
    .then(posts => {
        console.log(posts);
        displayPosts(posts);
    })
    .catch(error => {
        console.error('Error:', error);
    });

function displayPosts(posts) {
    const container = document.querySelector('#posts');
    
    posts.forEach(post => {
        const postDiv = document.createElement('div');
        postDiv.className = 'post';
        postDiv.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;
        container.appendChild(postDiv);
    });
}
```

**POST Request:**

```javascript
// Send new post to API
const newPost = {
    title: 'My New Post',
    body: 'This is the content',
    userId: 1
};

fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(newPost)
})
    .then(response => response.json())
    .then(data => {
        console.log('Created:', data);
    });
```

---

### 💻 Live Activity: Interactive Blog

**Create: interactive-blog.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Blog</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; }
        .post { border: 1px solid #ddd; padding: 20px; margin: 20px 0; }
        button { padding: 10px 20px; margin: 5px; cursor: pointer; }
        #newPostForm { background: #f0f0f0; padding: 20px; margin: 20px 0; }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; }
        .like-btn { background: #e74c3c; color: white; border: none; }
        .like-btn.liked { background: #c0392b; }
    </style>
</head>
<body>
    <h1>My Interactive Blog</h1>
    
    <!-- New Post Form -->
    <div id="newPostForm">
        <h2>Create New Post</h2>
        <input type="text" id="titleInput" placeholder="Post Title">
        <textarea id="contentInput" placeholder="Post Content" rows="5"></textarea>
        <button id="createPostBtn">Create Post</button>
    </div>
    
    <!-- Posts Container -->
    <div id="postsContainer"></div>
    
    <script>
        // Sample posts data
        let posts = [
            { id: 1, title: "First Post", content: "This is my first post!", likes: 0 },
            { id: 2, title: "Second Post", content: "Another great post!", likes: 0 }
        ];
        
        // Display all posts
        function displayPosts() {
            const container = document.querySelector('#postsContainer');
            container.innerHTML = '';  // Clear existing
            
            posts.forEach(post => {
                const postDiv = document.createElement('div');
                postDiv.className = 'post';
                postDiv.innerHTML = `
                    <h3>${post.title}</h3>
                    <p>${post.content}</p>
                    <button class="like-btn" data-id="${post.id}">
                        ❤️ Like (${post.likes})
                    </button>
                    <button class="delete-btn" data-id="${post.id}">
                        🗑️ Delete
                    </button>
                `;
                container.appendChild(postDiv);
            });
            
            // Add event listeners to buttons
            addEventListeners();
        }
        
        // Add event listeners
        function addEventListeners() {
            // Like buttons
            document.querySelectorAll('.like-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const postId = parseInt(e.target.dataset.id);
                    likePost(postId);
                });
            });
            
            // Delete buttons
            document.querySelectorAll('.delete-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const postId = parseInt(e.target.dataset.id);
                    deletePost(postId);
                });
            });
        }
        
        // Like post
        function likePost(postId) {
            const post = posts.find(p => p.id === postId);
            if (post) {
                post.likes++;
                displayPosts();
            }
        }
        
        // Delete post
        function deletePost(postId) {
            if (confirm('Delete this post?')) {
                posts = posts.filter(p => p.id !== postId);
                displayPosts();
            }
        }
        
        // Create new post
        document.querySelector('#createPostBtn').addEventListener('click', () => {
            const title = document.querySelector('#titleInput').value;
            const content = document.querySelector('#contentInput').value;
            
            if (title && content) {
                const newPost = {
                    id: posts.length + 1,
                    title: title,
                    content: content,
                    likes: 0
                };
                
                posts.push(newPost);
                displayPosts();
                
                // Clear form
                document.querySelector('#titleInput').value = '';
                document.querySelector('#contentInput').value = '';
                
                alert('Post created!');
            } else {
                alert('Please fill in both title and content!');
            }
        });
        
        // Initial display
        displayPosts();
    </script>
</body>
</html>
```

**Demo this to students - show:**
- Creating posts
- Liking posts
- Deleting posts
- All done with JavaScript!

---

### 🏠 Homework: Fetch Posts from Flask Backend

**Task:** Create a JavaScript file that fetches posts from Flask API and displays them

```javascript
// homework22_fetch_posts.js

// Fetch posts from Flask backend
async function fetchPosts() {
    try {
        const response = await fetch('http://localhost:5000/api/posts');
        const posts = await response.json();
        displayPosts(posts);
    } catch (error) {
        console.error('Error fetching posts:', error);
    }
}

// Display posts
function displayPosts(posts) {
    const container = document.querySelector('#posts');
    container.innerHTML = '';
    
    posts.forEach(post => {
        // TODO: Create post element
        // TODO: Add to container
    });
}

// TODO: Add form submit handler to create new post
// TODO: Add like button handlers
// TODO: Add delete handlers

// Call on page load
fetchPosts();
```

---

### 📝 Key Takeaways

✅ JavaScript = makes pages interactive
✅ DOM = how JS sees HTML
✅ Events = respond to user actions
✅ fetch() = get data from APIs
✅ async/await = handle promises

---

<a name="hour-23"></a>
## 📅 Hour 23: Introduction to React

### 🎯 Learning Objectives
- Understand what React is and why it's popular
- Set up a React development environment
- Create your first React components
- Understand JSX syntax
- Build a simple todo list app

### 📖 What to Teach

**"Today we learn React - the most popular JavaScript library for building user interfaces!"**

---

### 1️⃣ What is React? (10 minutes)

**Real-Life Analogy:**

```
Building Apps Like LEGO Blocks:
├── HTML/CSS/JS = Building materials (wood, nails, paint)
├── React = LEGO System (reusable components)
└── Components = Individual LEGO blocks you combine
```

**Why React is Popular:**
- **Component-Based**: Build reusable UI pieces
- **Virtual DOM**: Fast updates and rendering
- **Ecosystem**: Huge community and libraries
- **Job Market**: High demand skill
- **Used By**: Facebook, Netflix, Airbnb, Instagram

---

### 2️⃣ Setting Up React (5 minutes)

**Create React App (Easy Way):**

```bash
# Install Node.js first, then:
npx create-react-app my-first-react-app
cd my-first-react-app
npm start
```

**Project Structure:**
```
my-first-react-app/
├── public/
│   └── index.html
├── src/
│   ├── App.js        ← Main component
│   ├── App.css       ← Styling
│   └── index.js      ← Entry point
└── package.json      ← Dependencies
```

---

### 3️⃣ Your First Component (15 minutes)

**What is a Component?**

```jsx
// Think of components like functions that return HTML
function Welcome() {
    return <h1>Hello, World!</h1>;
}

// Or using arrow functions
const Welcome = () => {
    return <h1>Hello, World!</h1>;
}
```

**JSX - JavaScript + XML:**

```jsx
// JSX (what we write)
const element = <h1>Hello, {name}!</h1>;

// JavaScript (what it becomes)
const element = React.createElement('h1', null, 'Hello, ', name, '!');
```

**JSX Rules:**
```jsx
// 1. Must return single parent element
function MyComponent() {
    return (
        <div>
            <h1>Title</h1>
            <p>Content</p>
        </div>
    );
}

// 2. Use className instead of class
<div className="container">

// 3. Close all tags
<img src="photo.jpg" />
<input type="text" />

// 4. Use camelCase for attributes
<button onClick={handleClick}>Click me</button>
```

---

### 4️⃣ Props - Passing Data (10 minutes)

**Props = Properties (like function parameters):**

```jsx
// Parent component
function App() {
    return (
        <div>
            <Welcome name="Alice" age={25} />
            <Welcome name="Bob" age={30} />
            <Welcome name="Charlie" age={35} />
        </div>
    );
}

// Child component
function Welcome(props) {
    return (
        <div>
            <h2>Hello, {props.name}!</h2>
            <p>You are {props.age} years old.</p>
        </div>
    );
}

// Or with destructuring
function Welcome({ name, age }) {
    return (
        <div>
            <h2>Hello, {name}!</h2>
            <p>You are {age} years old.</p>
        </div>
    );
}
```

---

### 5️⃣ Practical Example: Todo List Component (20 minutes)

**Create TodoList.js:**

```jsx
import React from 'react';
import './TodoList.css';

function TodoList() {
    // Sample data (later we'll make this dynamic)
    const todos = [
        { id: 1, text: "Learn React", completed: false },
        { id: 2, text: "Build a project", completed: true },
        { id: 3, text: "Get a job", completed: false }
    ];

    return (
        <div className="todo-container">
            <h1>My Todo List</h1>
            
            <div className="todo-input">
                <input 
                    type="text" 
                    placeholder="Add a new todo..."
                />
                <button>Add</button>
            </div>

            <ul className="todo-list">
                {todos.map(todo => (
                    <TodoItem 
                        key={todo.id}
                        todo={todo}
                    />
                ))}
            </ul>
        </div>
    );
}

// Individual todo item component
function TodoItem({ todo }) {
    return (
        <li className={`todo-item ${todo.completed ? 'completed' : ''}`}>
            <input 
                type="checkbox" 
                checked={todo.completed}
                onChange={() => {}} // We'll add functionality next hour
            />
            <span>{todo.text}</span>
            <button className="delete-btn">Delete</button>
        </li>
    );
}

export default TodoList;
```

**Create TodoList.css:**

```css
.todo-container {
    max-width: 500px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.1);
}

.todo-container h1 {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
}

.todo-input {
    display: flex;
    margin-bottom: 20px;
}

.todo-input input {
    flex: 1;
    padding: 12px;
    border: 2px solid #ddd;
    border-radius: 5px 0 0 5px;
    font-size: 16px;
}

.todo-input button {
    padding: 12px 20px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 0 5px 5px 0;
    cursor: pointer;
    font-size: 16px;
}

.todo-input button:hover {
    background: #0056b3;
}

.todo-list {
    list-style: none;
    padding: 0;
}

.todo-item {
    display: flex;
    align-items: center;
    padding: 15px;
    border: 1px solid #eee;
    border-radius: 5px;
    margin-bottom: 10px;
    transition: all 0.2s;
}

.todo-item:hover {
    background: #f8f9fa;
}

.todo-item.completed {
    background: #f0f8f0;
    text-decoration: line-through;
    color: #666;
}

.todo-item input[type="checkbox"] {
    margin-right: 15px;
    transform: scale(1.2);
}

.todo-item span {
    flex: 1;
    font-size: 16px;
}

.delete-btn {
    background: #dc3545;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 3px;
    cursor: pointer;
    font-size: 14px;
}

.delete-btn:hover {
    background: #c82333;
}
```

**Update App.js:**

```jsx
import React from 'react';
import TodoList from './TodoList';
import './App.css';

function App() {
    return (
        <div className="App">
            <TodoList />
        </div>
    );
}

export default App;
```

---

### 🏠 Homework: Create Profile Card Component

**Task:** Create a reusable ProfileCard component

```jsx
// ProfileCard.js
import React from 'react';

function ProfileCard({ name, role, avatar, skills }) {
    return (
        <div className="profile-card">
            {/* TODO: Add profile image */}
            {/* TODO: Add name and role */}
            {/* TODO: Add skills list */}
            {/* TODO: Style with CSS */}
        </div>
    );
}

export default ProfileCard;
```

---

### 📝 Key Takeaways

✅ React = Component-based UI library
✅ JSX = JavaScript + HTML syntax
✅ Components = Reusable UI pieces
✅ Props = Pass data between components
✅ Always return single parent element

---

<a name="hour-24"></a>
## 📅 Hour 24: React State Management & Hooks

### 🎯 Learning Objectives
- Understand React state vs props
- Learn useState hook
- Handle user interactions
- Update state properly
- Build interactive todo list

### 📖 What to Teach

**"Today we make our React components interactive with state!"**

---

### 1️⃣ What is State? (10 minutes)

**State vs Props:**

```jsx
// Props = Data passed FROM parent TO child (READ-ONLY)
function Welcome({ name }) {  // name is a prop
    return <h1>Hello, {name}!</h1>;
}

// State = Data that belongs TO the component (CAN CHANGE)
function Counter() {
    const [count, setCount] = useState(0);  // count is state
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>
        </div>
    );
}
```

**Real-Life Analogy:**
```
Props = Ingredients given to chef (can't change)
State = Chef's cooking process (changes over time)
```

---

### 2️⃣ useState Hook (15 minutes)

**Basic useState:**

```jsx
import React, { useState } from 'react';

function Counter() {
    // useState returns [value, setValue]
    const [count, setCount] = useState(0);  // 0 is initial value
    
    const increment = () => {
        setCount(count + 1);  // Update state
    };
    
    const decrement = () => {
        setCount(count - 1);
    };
    
    const reset = () => {
        setCount(0);
    };
    
    return (
        <div>
            <h2>Counter: {count}</h2>
            <button onClick={increment}>+1</button>
            <button onClick={decrement}>-1</button>
            <button onClick={reset}>Reset</button>
        </div>
    );
}
```

**Different State Types:**

```jsx
function StateExamples() {
    // String state
    const [name, setName] = useState('');
    
    // Boolean state
    const [isVisible, setIsVisible] = useState(true);
    
    // Array state
    const [items, setItems] = useState([]);
    
    // Object state
    const [user, setUser] = useState({
        name: '',
        email: '',
        age: 0
    });
    
    return (
        <div>
            {/* Text input */}
            <input 
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter name"
            />
            
            {/* Toggle visibility */}
            <button onClick={() => setIsVisible(!isVisible)}>
                {isVisible ? 'Hide' : 'Show'}
            </button>
            
            {isVisible && <p>I'm visible!</p>}
            
            {/* Add to array */}
            <button onClick={() => setItems([...items, name])}>
                Add Item
            </button>
            
            <ul>
                {items.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}
```

---

### 3️⃣ Event Handling (10 minutes)

**Common Events:**

```jsx
function EventExamples() {
    const [message, setMessage] = useState('');
    
    const handleClick = () => {
        setMessage('Button clicked!');
    };
    
    const handleInputChange = (event) => {
        setMessage(event.target.value);
    };
    
    const handleSubmit = (event) => {
        event.preventDefault();  // Prevent form submission
        alert(`Submitted: ${message}`);
    };
    
    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            alert('Enter pressed!');
        }
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <input 
                type="text"
                value={message}
                onChange={handleInputChange}
                onKeyPress={handleKeyPress}
                placeholder="Type something..."
            />
            <button type="submit">Submit</button>
            <button type="button" onClick={handleClick}>
                Click Me
            </button>
            <p>Message: {message}</p>
        </form>
    );
}
```

---

### 4️⃣ Interactive Todo List (20 minutes)

**Complete TodoList with State:**

```jsx
import React, { useState } from 'react';
import './TodoList.css';

function TodoList() {
    // State for todos array
    const [todos, setTodos] = useState([
        { id: 1, text: "Learn React", completed: false },
        { id: 2, text: "Build a project", completed: true }
    ]);
    
    // State for new todo input
    const [newTodo, setNewTodo] = useState('');
    
    // Add new todo
    const addTodo = () => {
        if (newTodo.trim()) {
            const todo = {
                id: Date.now(), // Simple ID generation
                text: newTodo,
                completed: false
            };
            setTodos([...todos, todo]);
            setNewTodo(''); // Clear input
        }
    };
    
    // Toggle todo completion
    const toggleTodo = (id) => {
        setTodos(todos.map(todo =>
            todo.id === id 
                ? { ...todo, completed: !todo.completed }
                : todo
        ));
    };
    
    // Delete todo
    const deleteTodo = (id) => {
        setTodos(todos.filter(todo => todo.id !== id));
    };
    
    // Handle Enter key
    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            addTodo();
        }
    };

    return (
        <div className="todo-container">
            <h1>My Todo List ({todos.length} items)</h1>
            
            <div className="todo-input">
                <input 
                    type="text" 
                    value={newTodo}
                    onChange={(e) => setNewTodo(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder="Add a new todo..."
                />
                <button onClick={addTodo}>Add</button>
            </div>

            <div className="todo-stats">
                <p>
                    Completed: {todos.filter(todo => todo.completed).length} / {todos.length}
                </p>
            </div>

            <ul className="todo-list">
                {todos.map(todo => (
                    <TodoItem 
                        key={todo.id}
                        todo={todo}
                        onToggle={toggleTodo}
                        onDelete={deleteTodo}
                    />
                ))}
            </ul>
            
            {todos.length === 0 && (
                <p className="empty-message">No todos yet. Add one above!</p>
            )}
        </div>
    );
}

// Updated TodoItem component
function TodoItem({ todo, onToggle, onDelete }) {
    return (
        <li className={`todo-item ${todo.completed ? 'completed' : ''}`}>
            <input 
                type="checkbox" 
                checked={todo.completed}
                onChange={() => onToggle(todo.id)}
            />
            <span>{todo.text}</span>
            <button 
                className="delete-btn"
                onClick={() => onDelete(todo.id)}
            >
                Delete
            </button>
        </li>
    );
}

export default TodoList;
```

**Add to TodoList.css:**

```css
.todo-stats {
    background: #f8f9fa;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
    text-align: center;
}

.todo-stats p {
    margin: 0;
    color: #666;
    font-size: 14px;
}

.empty-message {
    text-align: center;
    color: #999;
    font-style: italic;
    padding: 40px;
}
```

---

### 5️⃣ State Best Practices (5 minutes)

**DO:**
```jsx
// ✅ Use functional updates for arrays/objects
setTodos(prevTodos => [...prevTodos, newTodo]);

// ✅ Don't mutate state directly
setUser(prevUser => ({ ...prevUser, name: 'John' }));

// ✅ Use separate state variables for different data
const [name, setName] = useState('');
const [email, setEmail] = useState('');
```

**DON'T:**
```jsx
// ❌ Don't mutate state directly
todos.push(newTodo);  // Wrong!
setTodos(todos);

// ❌ Don't modify state object directly
user.name = 'John';  // Wrong!
setUser(user);
```

---

### 🏠 Homework: Shopping Cart Component

**Task:** Create a shopping cart with add/remove functionality

```jsx
// ShoppingCart.js
function ShoppingCart() {
    const [items, setItems] = useState([]);
    const [productName, setProductName] = useState('');
    const [productPrice, setProductPrice] = useState('');
    
    // TODO: Add addItem function
    // TODO: Add removeItem function  
    // TODO: Add updateQuantity function
    // TODO: Calculate total price
    
    return (
        <div className="shopping-cart">
            {/* TODO: Add product input form */}
            {/* TODO: Display items list */}
            {/* TODO: Show total price */}
        </div>
    );
}
```

---

### 📝 Key Takeaways

✅ State = Component's changing data
✅ useState = Hook for managing state
✅ setState = Triggers component re-render
✅ Never mutate state directly
✅ Use functional updates for complex state

---

<a name="hour-25"></a>
## 📅 Hour 25: React Router - Navigation

### 🎯 Learning Objectives
- Understand Single Page Applications (SPA)
- Set up React Router
- Create multiple pages/views
- Navigate between pages
- Pass data through routes

### 📖 What to Teach

**"Today we learn routing - how to create multi-page React applications!"**

---

### 1️⃣ What is React Router? (10 minutes)

**Traditional vs SPA Navigation:**

```
Traditional Multi-Page App:
├── home.html        ← Server sends new page
├── about.html       ← Server sends new page  
└── contact.html     ← Server sends new page

Single Page App (SPA):
└── index.html       ← Same page, different content
    ├── /home        ← JavaScript changes content
    ├── /about       ← JavaScript changes content
    └── /contact     ← JavaScript changes content
```

**Benefits of SPA:**
- ✅ Faster navigation (no page reloads)
- ✅ Smooth user experience
- ✅ Better performance
- ✅ Maintains application state

---

### 2️⃣ Setting Up React Router (5 minutes)

**Install React Router:**

```bash
npm install react-router-dom
```

**Basic Router Setup:**

```jsx
// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import Navbar from './components/Navbar';

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/about" element={<About />} />
                    <Route path="/contact" element={<Contact />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
```

---

### 3️⃣ Creating Navigation (10 minutes)

**Navbar Component:**

```jsx
// components/Navbar.js
import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
    const location = useLocation();
    
    return (
        <nav className="navbar">
            <div className="nav-brand">
                <Link to="/">MyApp</Link>
            </div>
            
            <ul className="nav-links">
                <li>
                    <Link 
                        to="/" 
                        className={location.pathname === '/' ? 'active' : ''}
                    >
                        Home
                    </Link>
                </li>
                <li>
                    <Link 
                        to="/about" 
                        className={location.pathname === '/about' ? 'active' : ''}
                    >
                        About
                    </Link>
                </li>
                <li>
                    <Link 
                        to="/contact" 
                        className={location.pathname === '/contact' ? 'active' : ''}
                    >
                        Contact
                    </Link>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;
```

**Navbar Styling:**

```css
/* components/Navbar.css */
.navbar {
    background: #2c3e50;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-brand a {
    color: white;
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
}

.nav-links {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
    gap: 2rem;
}

.nav-links a {
    color: #bdc3c7;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: all 0.3s;
}

.nav-links a:hover,
.nav-links a.active {
    background: #34495e;
    color: white;
}
```

---

### 4️⃣ Creating Page Components (15 minutes)

**Home Page:**

```jsx
// components/Home.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Home() {
    const [todos, setTodos] = useState([
        { id: 1, title: "Learn React Router", completed: false },
        { id: 2, title: "Build portfolio site", completed: true },
        { id: 3, title: "Apply for jobs", completed: false }
    ]);
    
    return (
        <div className="page-container">
            <div className="hero-section">
                <h1>Welcome to TodoApp</h1>
                <p>Manage your tasks efficiently with our React-powered todo application.</p>
                <Link to="/todos" className="cta-button">
                    View All Todos
                </Link>
            </div>
            
            <div className="quick-stats">
                <div className="stat-card">
                    <h3>{todos.length}</h3>
                    <p>Total Tasks</p>
                </div>
                <div className="stat-card">
                    <h3>{todos.filter(todo => todo.completed).length}</h3>
                    <p>Completed</p>
                </div>
                <div className="stat-card">
                    <h3>{todos.filter(todo => !todo.completed).length}</h3>
                    <p>Remaining</p>
                </div>
            </div>
            
            <div className="recent-todos">
                <h2>Recent Tasks</h2>
                <ul>
                    {todos.slice(0, 3).map(todo => (
                        <li key={todo.id} className={todo.completed ? 'completed' : ''}>
                            {todo.title}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default Home;
```

**About Page:**

```jsx
// components/About.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function About() {
    const navigate = useNavigate();
    
    const handleGetStarted = () => {
        navigate('/todos');
    };
    
    return (
        <div className="page-container">
            <div className="about-content">
                <h1>About TodoApp</h1>
                
                <div className="about-grid">
                    <div className="about-section">
                        <h2>🚀 Our Mission</h2>
                        <p>
                            We believe productivity should be simple and enjoyable. 
                            TodoApp helps you organize your tasks, track your progress, 
                            and achieve your goals efficiently.
                        </p>
                    </div>
                    
                    <div className="about-section">
                        <h2>⚡ Features</h2>
                        <ul>
                            <li>Create and manage todos</li>
                            <li>Mark tasks as complete</li>
                            <li>Real-time progress tracking</li>
                            <li>Clean, intuitive interface</li>
                            <li>Responsive design</li>
                        </ul>
                    </div>
                    
                    <div className="about-section">
                        <h2>🛠️ Built With</h2>
                        <div className="tech-stack">
                            <span className="tech-item">React</span>
                            <span className="tech-item">React Router</span>
                            <span className="tech-item">CSS3</span>
                            <span className="tech-item">JavaScript ES6+</span>
                        </div>
                    </div>
                </div>
                
                <button className="cta-button" onClick={handleGetStarted}>
                    Get Started
                </button>
            </div>
        </div>
    );
}

export default About;
```

**Contact Page:**

```jsx
// components/Contact.js
import React, { useState } from 'react';

function Contact() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: ''
    });
    
    const [isSubmitted, setIsSubmitted] = useState(false);
    
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };
    
    const handleSubmit = (e) => {
        e.preventDefault();
        // Simulate form submission
        console.log('Form submitted:', formData);
        setIsSubmitted(true);
        
        // Reset form after 3 seconds
        setTimeout(() => {
            setIsSubmitted(false);
            setFormData({ name: '', email: '', message: '' });
        }, 3000);
    };
    
    if (isSubmitted) {
        return (
            <div className="page-container">
                <div className="success-message">
                    <h1>✅ Message Sent!</h1>
                    <p>Thank you for contacting us. We'll get back to you soon!</p>
                </div>
            </div>
        );
    }
    
    return (
        <div className="page-container">
            <div className="contact-content">
                <h1>Get in Touch</h1>
                <p>Have questions or feedback? We'd love to hear from you!</p>
                
                <div className="contact-grid">
                    <div className="contact-info">
                        <h2>Contact Information</h2>
                        <div className="contact-item">
                            <strong>📧 Email:</strong>
                            <p>support@todoapp.com</p>
                        </div>
                        <div className="contact-item">
                            <strong>📱 Phone:</strong>
                            <p>+1 (555) 123-4567</p>
                        </div>
                        <div className="contact-item">
                            <strong>🏢 Address:</strong>
                            <p>123 Tech Street<br />San Francisco, CA 94105</p>
                        </div>
                    </div>
                    
                    <form className="contact-form" onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="name">Name *</label>
                            <input
                                type="text"
                                id="name"
                                name="name"
                                value={formData.name}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="email">Email *</label>
                            <input
                                type="email"
                                id="email"
                                name="email"
                                value={formData.email}
                                onChange={handleChange}
                                required
                            />
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="message">Message *</label>
                            <textarea
                                id="message"
                                name="message"
                                rows="5"
                                value={formData.message}
                                onChange={handleChange}
                                required
                            ></textarea>
                        </div>
                        
                        <button type="submit" className="submit-button">
                            Send Message
                        </button>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Contact;
```

---

### 5️⃣ Advanced Routing (15 minutes)

**Todo Detail Route (URL Parameters):**

```jsx
// Update App.js
import TodoDetail from './components/TodoDetail';

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/about" element={<About />} />
                    <Route path="/contact" element={<Contact />} />
                    <Route path="/todos" element={<TodoList />} />
                    <Route path="/todos/:id" element={<TodoDetail />} />
                    <Route path="*" element={<NotFound />} />
                </Routes>
            </div>
        </Router>
    );
}
```

**Todo Detail Component:**

```jsx
// components/TodoDetail.js
import React from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';

function TodoDetail() {
    const { id } = useParams();
    const navigate = useNavigate();
    
    // In real app, fetch todo by ID from API or state
    const todo = {
        id: id,
        title: "Learn React Router",
        description: "Master client-side routing in React applications using React Router. Learn about navigation, URL parameters, and programmatic routing.",
        completed: false,
        priority: "High",
        dueDate: "2023-12-20",
        createdAt: "2023-12-15"
    };
    
    const handleGoBack = () => {
        navigate('/todos');
    };
    
    const handleEdit = () => {
        navigate(`/todos/${id}/edit`);
    };
    
    return (
        <div className="page-container">
            <div className="todo-detail">
                <div className="detail-header">
                    <button onClick={handleGoBack} className="back-button">
                        ← Back to Todos
                    </button>
                    
                    <div className="detail-actions">
                        <button onClick={handleEdit} className="edit-button">
                            Edit Todo
                        </button>
                    </div>
                </div>
                
                <div className="detail-content">
                    <h1>{todo.title}</h1>
                    
                    <div className="todo-meta">
                        <span className={`status ${todo.completed ? 'completed' : 'pending'}`}>
                            {todo.completed ? 'Completed' : 'Pending'}
                        </span>
                        <span className={`priority ${todo.priority.toLowerCase()}`}>
                            {todo.priority} Priority
                        </span>
                    </div>
                    
                    <div className="todo-details">
                        <div className="detail-item">
                            <strong>Description:</strong>
                            <p>{todo.description}</p>
                        </div>
                        
                        <div className="detail-item">
                            <strong>Due Date:</strong>
                            <p>{todo.dueDate}</p>
                        </div>
                        
                        <div className="detail-item">
                            <strong>Created:</strong>
                            <p>{todo.createdAt}</p>
                        </div>
                    </div>
                </div>
                
                <div className="related-actions">
                    <h3>Quick Actions</h3>
                    <Link to="/todos" className="action-link">View All Todos</Link>
                    <Link to="/todos/new" className="action-link">Create New Todo</Link>
                </div>
            </div>
        </div>
    );
}

export default TodoDetail;
```

**404 Not Found Page:**

```jsx
// components/NotFound.js
import React from 'react';
import { Link } from 'react-router-dom';

function NotFound() {
    return (
        <div className="page-container">
            <div className="not-found">
                <h1>404</h1>
                <h2>Page Not Found</h2>
                <p>The page you're looking for doesn't exist.</p>
                <Link to="/" className="cta-button">
                    Go Home
                </Link>
            </div>
        </div>
    );
}

export default NotFound;
```

---

### 5️⃣ Programmatic Navigation (5 minutes)

**Using useNavigate Hook:**

```jsx
import { useNavigate } from 'react-router-dom';

function MyComponent() {
    const navigate = useNavigate();
    
    const handleLogin = () => {
        // After successful login
        navigate('/dashboard');
    };
    
    const handleBack = () => {
        navigate(-1); // Go back one page
    };
    
    const handleForward = () => {
        navigate(1); // Go forward one page
    };
    
    const handleRedirect = () => {
        navigate('/home', { replace: true }); // Replace current entry
    };
    
    return (
        <div>
            <button onClick={handleLogin}>Login</button>
            <button onClick={handleBack}>Back</button>
            <button onClick={handleForward}>Forward</button>
        </div>
    );
}
```

---

### 🏠 Homework: Add Todo CRUD Routes

**Task:** Create routes for todo operations

```jsx
// Add these routes to App.js
<Route path="/todos/new" element={<CreateTodo />} />
<Route path="/todos/:id/edit" element={<EditTodo />} />

// Create CreateTodo.js component
// Create EditTodo.js component
// Add navigation between all todo pages
```

---

### 📝 Key Takeaways

✅ React Router = Client-side routing for SPAs
✅ BrowserRouter = Main router component
✅ Routes & Route = Define page routes
✅ Link = Navigate without page reload
✅ useParams = Get URL parameters
✅ useNavigate = Programmatic navigation

---

<a name="hour-26"></a>
## 📅 Hour 26: Styling React Apps

### 🎯 Learning Objectives
- Learn different CSS approaches in React
- Master CSS Modules and styled-components
- Implement responsive design patterns
- Create reusable UI components
- Build a beautiful design system

### 📖 What to Teach

**"Today we make our React apps beautiful with modern CSS approaches!"**

---

### 1️⃣ CSS Approaches in React (10 minutes)

**Different Ways to Style React:**

```jsx
// 1. Regular CSS files (what we've been using)
import './Component.css';

// 2. Inline styles
const styles = {
    container: {
        backgroundColor: '#f0f0f0',
        padding: '20px'
    }
};

// 3. CSS Modules
import styles from './Component.module.css';

// 4. Styled Components (CSS-in-JS)
import styled from 'styled-components';

// 5. CSS Frameworks (Tailwind, Bootstrap)
```

**When to Use Each:**
- **Regular CSS**: Simple projects, global styles
- **CSS Modules**: Scoped styles, avoiding conflicts
- **Styled Components**: Dynamic styling, component-based
- **Inline Styles**: Quick prototyping, dynamic values
- **CSS Frameworks**: Rapid development, consistent design

---

### 2️⃣ CSS Modules (15 minutes)

**Setting Up CSS Modules:**

```css
/* Button.module.css */
.button {
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.primary {
    background: #007bff;
    color: white;
}

.primary:hover {
    background: #0056b3;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
}

.secondary {
    background: #6c757d;
    color: white;
}

.secondary:hover {
    background: #545b62;
}

.large {
    padding: 16px 32px;
    font-size: 18px;
}

.small {
    padding: 8px 16px;
    font-size: 14px;
}

.fullWidth {
    width: 100%;
}
```

**Using CSS Modules:**

```jsx
// Button.js
import React from 'react';
import styles from './Button.module.css';

function Button({ 
    children, 
    variant = 'primary', 
    size = 'medium', 
    fullWidth = false, 
    onClick,
    ...props 
}) {
    // Combine multiple CSS classes
    const buttonClasses = [
        styles.button,
        styles[variant],
        size !== 'medium' && styles[size],
        fullWidth && styles.fullWidth
    ].filter(Boolean).join(' ');
    
    return (
        <button 
            className={buttonClasses}
            onClick={onClick}
            {...props}
        >
            {children}
        </button>
    );
}

export default Button;
```

**Using the Button Component:**

```jsx
// App.js
import Button from './components/Button';

function App() {
    return (
        <div>
            <Button variant="primary" size="large">
                Primary Button
            </Button>
            
            <Button variant="secondary" size="small">
                Secondary Button
            </Button>
            
            <Button variant="primary" fullWidth>
                Full Width Button
            </Button>
        </div>
    );
}
```

---

### 3️⃣ Styled Components (15 minutes)

**Install and Setup:**

```bash
npm install styled-components
```

**Basic Styled Components:**

```jsx
// StyledButton.js
import styled from 'styled-components';

const StyledButton = styled.button`
    padding: ${props => 
        props.size === 'large' ? '16px 32px' : 
        props.size === 'small' ? '8px 16px' : 
        '12px 24px'
    };
    
    background: ${props => 
        props.variant === 'primary' ? '#007bff' : 
        props.variant === 'secondary' ? '#6c757d' : 
        '#28a745'
    };
    
    color: white;
    border: none;
    border-radius: 6px;
    font-size: ${props => 
        props.size === 'large' ? '18px' : 
        props.size === 'small' ? '14px' : 
        '16px'
    };
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    width: ${props => props.fullWidth ? '100%' : 'auto'};
    
    &:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    &:active {
        transform: translateY(0);
    }
    
    &:disabled {
        opacity: 0.6;
        cursor: not-allowed;
        
        &:hover {
            transform: none;
            box-shadow: none;
        }
    }
`;

// Usage
function MyComponent() {
    return (
        <div>
            <StyledButton variant="primary" size="large">
                Styled Button
            </StyledButton>
            
            <StyledButton variant="secondary" disabled>
                Disabled Button
            </StyledButton>
        </div>
    );
}
```

**Styled Component Themes:**

```jsx
// theme.js
export const theme = {
    colors: {
        primary: '#007bff',
        secondary: '#6c757d',
        success: '#28a745',
        danger: '#dc3545',
        warning: '#ffc107',
        info: '#17a2b8',
        light: '#f8f9fa',
        dark: '#343a40'
    },
    
    spacing: {
        xs: '4px',
        sm: '8px',
        md: '16px',
        lg: '24px',
        xl: '32px'
    },
    
    breakpoints: {
        mobile: '480px',
        tablet: '768px',
        desktop: '1024px'
    }
};

// App.js
import { ThemeProvider } from 'styled-components';
import { theme } from './theme';

function App() {
    return (
        <ThemeProvider theme={theme}>
            {/* Your components here */}
        </ThemeProvider>
    );
}

// Using theme in components
const ThemedButton = styled.button`
    background: ${props => props.theme.colors.primary};
    padding: ${props => props.theme.spacing.md};
    
    @media (max-width: ${props => props.theme.breakpoints.mobile}) {
        padding: ${props => props.theme.spacing.sm};
        font-size: 14px;
    }
`;
```

---

### 4️⃣ Responsive Design System (15 minutes)

**Create a Card Component:**

```jsx
// Card.js
import React from 'react';
import styles from './Card.module.css';

function Card({ 
    children, 
    shadow = 'medium', 
    padding = 'medium',
    hover = false,
    className = '',
    ...props 
}) {
    const cardClasses = [
        styles.card,
        styles[`shadow-${shadow}`],
        styles[`padding-${padding}`],
        hover && styles.hover,
        className
    ].filter(Boolean).join(' ');
    
    return (
        <div className={cardClasses} {...props}>
            {children}
        </div>
    );
}

export default Card;
```

```css
/* Card.module.css */
.card {
    background: white;
    border-radius: 8px;
    border: 1px solid #e9ecef;
    transition: all 0.3s ease;
}

.shadow-none {
    box-shadow: none;
}

.shadow-small {
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.shadow-medium {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.shadow-large {
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}

.padding-none {
    padding: 0;
}

.padding-small {
    padding: 12px;
}

.padding-medium {
    padding: 20px;
}

.padding-large {
    padding: 32px;
}

.hover:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

/* Responsive design */
@media (max-width: 768px) {
    .padding-medium {
        padding: 16px;
    }
    
    .padding-large {
        padding: 20px;
    }
}
```

**Grid Layout System:**

```jsx
// Grid.js
import React from 'react';
import styles from './Grid.module.css';

export function Container({ children, className = '', ...props }) {
    return (
        <div className={`${styles.container} ${className}`} {...props}>
            {children}
        </div>
    );
}

export function Row({ children, className = '', gap = 'medium', ...props }) {
    const rowClasses = [
        styles.row,
        styles[`gap-${gap}`],
        className
    ].filter(Boolean).join(' ');
    
    return (
        <div className={rowClasses} {...props}>
            {children}
        </div>
    );
}

export function Col({ 
    children, 
    xs = 12, 
    sm, 
    md, 
    lg, 
    xl,
    className = '',
    ...props 
}) {
    const colClasses = [
        styles.col,
        styles[`col-xs-${xs}`],
        sm && styles[`col-sm-${sm}`],
        md && styles[`col-md-${md}`],
        lg && styles[`col-lg-${lg}`],
        xl && styles[`col-xl-${xl}`],
        className
    ].filter(Boolean).join(' ');
    
    return (
        <div className={colClasses} {...props}>
            {children}
        </div>
    );
}
```

```css
/* Grid.module.css */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 16px;
}

.row {
    display: flex;
    flex-wrap: wrap;
    margin: 0 -8px;
}

.gap-small {
    margin: 0 -4px;
}

.gap-small .col {
    padding: 0 4px;
    margin-bottom: 8px;
}

.gap-medium {
    margin: 0 -8px;
}

.gap-medium .col {
    padding: 0 8px;
    margin-bottom: 16px;
}

.gap-large {
    margin: 0 -16px;
}

.gap-large .col {
    padding: 0 16px;
    margin-bottom: 32px;
}

.col {
    flex: 0 0 auto;
}

/* Column sizes */
.col-xs-1 { width: 8.333333%; }
.col-xs-2 { width: 16.666667%; }
.col-xs-3 { width: 25%; }
.col-xs-4 { width: 33.333333%; }
.col-xs-6 { width: 50%; }
.col-xs-8 { width: 66.666667%; }
.col-xs-9 { width: 75%; }
.col-xs-12 { width: 100%; }

/* Responsive breakpoints */
@media (min-width: 576px) {
    .col-sm-1 { width: 8.333333%; }
    .col-sm-2 { width: 16.666667%; }
    .col-sm-3 { width: 25%; }
    .col-sm-4 { width: 33.333333%; }
    .col-sm-6 { width: 50%; }
    .col-sm-8 { width: 66.666667%; }
    .col-sm-9 { width: 75%; }
    .col-sm-12 { width: 100%; }
}

@media (min-width: 768px) {
    .container {
        padding: 0 24px;
    }
    
    .col-md-1 { width: 8.333333%; }
    .col-md-2 { width: 16.666667%; }
    .col-md-3 { width: 25%; }
    .col-md-4 { width: 33.333333%; }
    .col-md-6 { width: 50%; }
    .col-md-8 { width: 66.666667%; }
    .col-md-9 { width: 75%; }
    .col-md-12 { width: 100%; }
}

@media (min-width: 1024px) {
    .col-lg-1 { width: 8.333333%; }
    .col-lg-2 { width: 16.666667%; }
    .col-lg-3 { width: 25%; }
    .col-lg-4 { width: 33.333333%; }
    .col-lg-6 { width: 50%; }
    .col-lg-8 { width: 66.666667%; }
    .col-lg-9 { width: 75%; }
    .col-lg-12 { width: 100%; }
}
```

---

### 5️⃣ Building a Dashboard Layout (5 minutes)

**Complete Dashboard Example:**

```jsx
// Dashboard.js
import React from 'react';
import { Container, Row, Col } from './Grid';
import Card from './Card';
import Button from './Button';

function Dashboard() {
    const stats = [
        { title: 'Total Tasks', value: '124', color: 'primary' },
        { title: 'Completed', value: '89', color: 'success' },
        { title: 'In Progress', value: '28', color: 'warning' },
        { title: 'Overdue', value: '7', color: 'danger' }
    ];
    
    return (
        <Container>
            <Row gap="large">
                <Col xs={12}>
                    <h1>Dashboard</h1>
                </Col>
                
                {/* Stats Cards */}
                {stats.map((stat, index) => (
                    <Col xs={6} md={3} key={index}>
                        <Card hover shadow="medium">
                            <div className="stat-card">
                                <h3 className={`stat-value ${stat.color}`}>
                                    {stat.value}
                                </h3>
                                <p className="stat-title">{stat.title}</p>
                            </div>
                        </Card>
                    </Col>
                ))}
                
                {/* Main Content */}
                <Col xs={12} md={8}>
                    <Card>
                        <h2>Recent Activity</h2>
                        <div className="activity-list">
                            <div className="activity-item">
                                <span className="activity-time">2 hours ago</span>
                                <p>Completed "Learn React Styling"</p>
                            </div>
                            <div className="activity-item">
                                <span className="activity-time">5 hours ago</span>
                                <p>Created new project "Portfolio Website"</p>
                            </div>
                            <div className="activity-item">
                                <span className="activity-time">1 day ago</span>
                                <p>Updated task "Study JavaScript"</p>
                            </div>
                        </div>
                    </Card>
                </Col>
                
                {/* Sidebar */}
                <Col xs={12} md={4}>
                    <Card>
                        <h3>Quick Actions</h3>
                        <div className="quick-actions">
                            <Button variant="primary" fullWidth>
                                New Task
                            </Button>
                            <Button variant="secondary" fullWidth>
                                View Reports
                            </Button>
                            <Button variant="success" fullWidth>
                                Export Data
                            </Button>
                        </div>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
}

export default Dashboard;
```

---

### 🏠 Homework: Create Design System

**Task:** Build a complete component library

```jsx
// Create these components with consistent styling:
// 1. Input.js - Form inputs with variants
// 2. Modal.js - Reusable modal component
// 3. Badge.js - Status badges
// 4. Avatar.js - User avatar component
// 5. Spinner.js - Loading spinner

// Example structure:
function Input({ label, error, helpText, ...props }) {
    // TODO: Implement styled input with validation states
}

function Modal({ isOpen, onClose, title, children }) {
    // TODO: Implement modal with backdrop and animations
}
```

---

### 📝 Key Takeaways

✅ CSS Modules = Scoped component styles
✅ Styled Components = Dynamic CSS-in-JS
✅ Design System = Consistent, reusable components
✅ Responsive Design = Mobile-first approach
✅ Component Library = Scalable UI architecture

---

<a name="hour-27"></a>
## 📅 Hour 27: State Management (Context & Redux Toolkit)

### 🎯 Learning Objectives
- Understand when you need global state
- Master React Context for simple state sharing
- Learn Redux Toolkit for complex state management
- Implement authentication state
- Build a shopping cart with global state

### 📖 What to Teach

**"Today we learn to manage state across your entire React application!"**

---

### 1️⃣ When Do You Need Global State? (10 minutes)

**Local State vs Global State:**

```jsx
// Local State (useState) - Good for:
function TodoItem() {
    const [isEditing, setIsEditing] = useState(false); // ✅ Only this component needs it
    const [inputValue, setInputValue] = useState('');  // ✅ Form state
}

// Global State - Needed for:
// ❌ User authentication (many components need user info)
// ❌ Shopping cart (navbar, cart page, product pages)
// ❌ Theme/language settings (entire app)
// ❌ Todo list data (multiple pages need access)
```

**State Management Solutions:**

```
Simple Global State:
├── React Context ← Start here
└── useState + Context

Complex Global State:
├── Redux Toolkit ← Most popular
├── Zustand ← Lightweight alternative
└── Recoil ← Experimental by Facebook
```

---

### 2️⃣ React Context (15 minutes)

**Creating a Theme Context:**

```jsx
// contexts/ThemeContext.js
import React, { createContext, useContext, useState } from 'react';

// 1. Create Context
const ThemeContext = createContext();

// 2. Create Provider Component
export function ThemeProvider({ children }) {
    const [theme, setTheme] = useState('light');
    
    const toggleTheme = () => {
        setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light');
    };
    
    const value = {
        theme,
        toggleTheme,
        isDark: theme === 'dark'
    };
    
    return (
        <ThemeContext.Provider value={value}>
            <div className={`app ${theme}`}>
                {children}
            </div>
        </ThemeContext.Provider>
    );
}

// 3. Create Custom Hook
export function useTheme() {
    const context = useContext(ThemeContext);
    
    if (!context) {
        throw new Error('useTheme must be used within a ThemeProvider');
    }
    
    return context;
}
```

**Using Theme Context:**

```jsx
// App.js
import { ThemeProvider } from './contexts/ThemeContext';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';

function App() {
    return (
        <ThemeProvider>
            <Navbar />
            <Dashboard />
        </ThemeProvider>
    );
}

// Navbar.js
import { useTheme } from '../contexts/ThemeContext';

function Navbar() {
    const { theme, toggleTheme, isDark } = useTheme();
    
    return (
        <nav className={`navbar ${theme}`}>
            <h1>My App</h1>
            <button onClick={toggleTheme}>
                {isDark ? '☀️' : '🌙'} {isDark ? 'Light' : 'Dark'} Mode
            </button>
        </nav>
    );
}

// Dashboard.js
import { useTheme } from '../contexts/ThemeContext';

function Dashboard() {
    const { isDark } = useTheme();
    
    return (
        <div className={`dashboard ${isDark ? 'dark' : 'light'}`}>
            <h2>Dashboard</h2>
            <p>Current theme: {isDark ? 'Dark' : 'Light'}</p>
        </div>
    );
}
```

**Authentication Context:**

```jsx
// contexts/AuthContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    
    // Check if user is logged in on app start
    useEffect(() => {
        const savedUser = localStorage.getItem('user');
        if (savedUser) {
            setUser(JSON.parse(savedUser));
        }
        setIsLoading(false);
    }, []);
    
    const login = async (email, password) => {
        setIsLoading(true);
        
        try {
            // Simulate API call
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            
            if (response.ok) {
                const userData = await response.json();
                setUser(userData);
                localStorage.setItem('user', JSON.stringify(userData));
                return { success: true };
            } else {
                return { success: false, error: 'Invalid credentials' };
            }
        } catch (error) {
            return { success: false, error: 'Network error' };
        } finally {
            setIsLoading(false);
        }
    };
    
    const logout = () => {
        setUser(null);
        localStorage.removeItem('user');
    };
    
    const value = {
        user,
        login,
        logout,
        isLoading,
        isAuthenticated: !!user
    };
    
    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    
    return context;
}
```

---

### 3️⃣ Redux Toolkit Setup (15 minutes)

**Install Redux Toolkit:**

```bash
npm install @reduxjs/toolkit react-redux
```

**Create Store:**

```jsx
// store/index.js
import { configureStore } from '@reduxjs/toolkit';
import todoReducer from './todoSlice';
import cartReducer from './cartSlice';

export const store = configureStore({
    reducer: {
        todos: todoReducer,
        cart: cartReducer
    }
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

**Create Todo Slice:**

```jsx
// store/todoSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// Async action to fetch todos
export const fetchTodos = createAsyncThunk(
    'todos/fetchTodos',
    async () => {
        const response = await fetch('/api/todos');
        return response.json();
    }
);

const todoSlice = createSlice({
    name: 'todos',
    initialState: {
        items: [],
        status: 'idle', // 'idle' | 'loading' | 'succeeded' | 'failed'
        error: null
    },
    reducers: {
        addTodo: (state, action) => {
            const newTodo = {
                id: Date.now(),
                text: action.payload,
                completed: false,
                createdAt: new Date().toISOString()
            };
            state.items.push(newTodo);
        },
        
        toggleTodo: (state, action) => {
            const todo = state.items.find(item => item.id === action.payload);
            if (todo) {
                todo.completed = !todo.completed;
            }
        },
        
        deleteTodo: (state, action) => {
            state.items = state.items.filter(item => item.id !== action.payload);
        },
        
        editTodo: (state, action) => {
            const { id, text } = action.payload;
            const todo = state.items.find(item => item.id === id);
            if (todo) {
                todo.text = text;
                todo.updatedAt = new Date().toISOString();
            }
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchTodos.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(fetchTodos.fulfilled, (state, action) => {
                state.status = 'succeeded';
                state.items = action.payload;
            })
            .addCase(fetchTodos.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            });
    }
});

export const { addTodo, toggleTodo, deleteTodo, editTodo } = todoSlice.actions;
export default todoSlice.reducer;

// Selectors
export const selectAllTodos = (state) => state.todos.items;
export const selectTodosStatus = (state) => state.todos.status;
export const selectTodosError = (state) => state.todos.error;
export const selectCompletedTodos = (state) => 
    state.todos.items.filter(todo => todo.completed);
export const selectPendingTodos = (state) => 
    state.todos.items.filter(todo => !todo.completed);
```

**Setup Provider:**

```jsx
// App.js
import React from 'react';
import { Provider } from 'react-redux';
import { store } from './store';
import TodoApp from './components/TodoApp';

function App() {
    return (
        <Provider store={store}>
            <TodoApp />
        </Provider>
    );
}

export default App;
```

**Using Redux in Components:**

```jsx
// components/TodoApp.js
import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
    selectAllTodos,
    selectTodosStatus,
    selectTodosError,
    fetchTodos,
    addTodo,
    toggleTodo,
    deleteTodo
} from '../store/todoSlice';

function TodoApp() {
    const dispatch = useDispatch();
    const todos = useSelector(selectAllTodos);
    const status = useSelector(selectTodosStatus);
    const error = useSelector(selectTodosError);
    
    const [newTodoText, setNewTodoText] = useState('');
    
    // Fetch todos on component mount
    useEffect(() => {
        if (status === 'idle') {
            dispatch(fetchTodos());
        }
    }, [status, dispatch]);
    
    const handleAddTodo = () => {
        if (newTodoText.trim()) {
            dispatch(addTodo(newTodoText));
            setNewTodoText('');
        }
    };
    
    const handleToggleTodo = (id) => {
        dispatch(toggleTodo(id));
    };
    
    const handleDeleteTodo = (id) => {
        dispatch(deleteTodo(id));
    };
    
    if (status === 'loading') {
        return <div className="loading">Loading todos...</div>;
    }
    
    if (status === 'failed') {
        return <div className="error">Error: {error}</div>;
    }
    
    return (
        <div className="todo-app">
            <h1>Redux Todo App</h1>
            
            <div className="add-todo">
                <input
                    type="text"
                    value={newTodoText}
                    onChange={(e) => setNewTodoText(e.target.value)}
                    placeholder="Add a new todo..."
                    onKeyPress={(e) => e.key === 'Enter' && handleAddTodo()}
                />
                <button onClick={handleAddTodo}>Add</button>
            </div>
            
            <div className="todo-list">
                {todos.map(todo => (
                    <TodoItem
                        key={todo.id}
                        todo={todo}
                        onToggle={() => handleToggleTodo(todo.id)}
                        onDelete={() => handleDeleteTodo(todo.id)}
                    />
                ))}
            </div>
            
            {todos.length === 0 && (
                <p className="empty-state">No todos yet. Add one above!</p>
            )}
        </div>
    );
}

function TodoItem({ todo, onToggle, onDelete }) {
    return (
        <div className={`todo-item ${todo.completed ? 'completed' : ''}`}>
            <input
                type="checkbox"
                checked={todo.completed}
                onChange={onToggle}
            />
            <span className="todo-text">{todo.text}</span>
            <button onClick={onDelete} className="delete-btn">
                Delete
            </button>
        </div>
    );
}

export default TodoApp;
```

---

### 4️⃣ Shopping Cart Example (15 minutes)

**Cart Slice:**

```jsx
// store/cartSlice.js
import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
    name: 'cart',
    initialState: {
        items: [],
        totalQuantity: 0,
        totalAmount: 0
    },
    reducers: {
        addToCart: (state, action) => {
            const { id, title, price } = action.payload;
            const existingItem = state.items.find(item => item.id === id);
            
            if (existingItem) {
                existingItem.quantity++;
            } else {
                state.items.push({
                    id,
                    title,
                    price,
                    quantity: 1
                });
            }
            
            state.totalQuantity++;
            state.totalAmount += price;
        },
        
        removeFromCart: (state, action) => {
            const id = action.payload;
            const existingItem = state.items.find(item => item.id === id);
            
            if (existingItem) {
                state.totalQuantity--;
                state.totalAmount -= existingItem.price;
                
                if (existingItem.quantity === 1) {
                    state.items = state.items.filter(item => item.id !== id);
                } else {
                    existingItem.quantity--;
                }
            }
        },
        
        clearCart: (state) => {
            state.items = [];
            state.totalQuantity = 0;
            state.totalAmount = 0;
        }
    }
});

export const { addToCart, removeFromCart, clearCart } = cartSlice.actions;
export default cartSlice.reducer;

// Selectors
export const selectCartItems = (state) => state.cart.items;
export const selectCartTotal = (state) => state.cart.totalAmount;
export const selectCartQuantity = (state) => state.cart.totalQuantity;
```

**Product List Component:**

```jsx
// components/ProductList.js
import React from 'react';
import { useDispatch } from 'react-redux';
import { addToCart } from '../store/cartSlice';

function ProductList() {
    const dispatch = useDispatch();
    
    const products = [
        { id: 1, title: 'React Course', price: 49.99 },
        { id: 2, title: 'JavaScript Book', price: 29.99 },
        { id: 3, title: 'CSS Masterclass', price: 39.99 },
        { id: 4, title: 'Node.js Tutorial', price: 59.99 }
    ];
    
    const handleAddToCart = (product) => {
        dispatch(addToCart(product));
    };
    
    return (
        <div className="product-list">
            <h2>Products</h2>
            <div className="products-grid">
                {products.map(product => (
                    <div key={product.id} className="product-card">
                        <h3>{product.title}</h3>
                        <p className="price">${product.price}</p>
                        <button 
                            onClick={() => handleAddToCart(product)}
                            className="add-to-cart-btn"
                        >
                            Add to Cart
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ProductList;
```

**Cart Component:**

```jsx
// components/Cart.js
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
    selectCartItems,
    selectCartTotal,
    selectCartQuantity,
    removeFromCart,
    clearCart
} from '../store/cartSlice';

function Cart() {
    const dispatch = useDispatch();
    const cartItems = useSelector(selectCartItems);
    const totalAmount = useSelector(selectCartTotal);
    const totalQuantity = useSelector(selectCartQuantity);
    
    const handleRemoveFromCart = (id) => {
        dispatch(removeFromCart(id));
    };
    
    const handleClearCart = () => {
        dispatch(clearCart());
    };
    
    if (cartItems.length === 0) {
        return (
            <div className="cart">
                <h2>Shopping Cart</h2>
                <p className="empty-cart">Your cart is empty</p>
            </div>
        );
    }
    
    return (
        <div className="cart">
            <h2>Shopping Cart ({totalQuantity} items)</h2>
            
            <div className="cart-items">
                {cartItems.map(item => (
                    <div key={item.id} className="cart-item">
                        <div className="item-info">
                            <h4>{item.title}</h4>
                            <p>${item.price} x {item.quantity}</p>
                        </div>
                        <div className="item-actions">
                            <span className="item-total">
                                ${(item.price * item.quantity).toFixed(2)}
                            </span>
                            <button 
                                onClick={() => handleRemoveFromCart(item.id)}
                                className="remove-btn"
                            >
                                Remove One
                            </button>
                        </div>
                    </div>
                ))}
            </div>
            
            <div className="cart-summary">
                <div className="total">
                    <strong>Total: ${totalAmount.toFixed(2)}</strong>
                </div>
                <div className="cart-actions">
                    <button onClick={handleClearCart} className="clear-btn">
                        Clear Cart
                    </button>
                    <button className="checkout-btn">
                        Proceed to Checkout
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Cart;
```

---

### 5️⃣ Custom Hooks for Redux (5 minutes)

**Typed Redux Hooks:**

```jsx
// hooks/redux.js
import { useDispatch, useSelector } from 'react-redux';

// Use these instead of plain useDispatch and useSelector
export const useAppDispatch = () => useDispatch();
export const useAppSelector = useSelector;

// Custom hooks for common operations
export const useTodos = () => {
    const dispatch = useAppDispatch();
    const todos = useAppSelector(selectAllTodos);
    const status = useAppSelector(selectTodosStatus);
    
    return {
        todos,
        status,
        addTodo: (text) => dispatch(addTodo(text)),
        toggleTodo: (id) => dispatch(toggleTodo(id)),
        deleteTodo: (id) => dispatch(deleteTodo(id))
    };
};

export const useCart = () => {
    const dispatch = useAppDispatch();
    const cartItems = useAppSelector(selectCartItems);
    const totalAmount = useAppSelector(selectCartTotal);
    const totalQuantity = useAppSelector(selectCartQuantity);
    
    return {
        cartItems,
        totalAmount,
        totalQuantity,
        addToCart: (product) => dispatch(addToCart(product)),
        removeFromCart: (id) => dispatch(removeFromCart(id)),
        clearCart: () => dispatch(clearCart())
    };
};
```

---

### 🏠 Homework: Build User Profile State

**Task:** Create user profile management with Context or Redux

```jsx
// Create user profile state that manages:
// 1. User information (name, email, avatar)
// 2. User preferences (theme, notifications)
// 3. User settings (language, timezone)

// Include actions for:
// - updateProfile()
// - updatePreferences()  
// - uploadAvatar()
// - resetSettings()
```

---

### 📝 Key Takeaways

✅ Context = Simple global state sharing
✅ Redux Toolkit = Complex state management  
✅ Selectors = Derive data from state
✅ Actions = Describe what happened
✅ Reducers = Handle state changes immutably

---

<a name="hour-28"></a>
## 📅 Hour 28: Forms & Validation

### 🎯 Learning Objectives
- Master controlled vs uncontrolled components
- Implement form validation with custom hooks
- Handle complex form data and submissions
- Create reusable form components
- Build a complete user registration system

### 📖 What to Teach

**"Today we master forms - the backbone of user interaction in web apps!"**

---

### 1️⃣ Controlled vs Uncontrolled Components (10 minutes)

**Controlled Components (Recommended):**

```jsx
// React controls the input value
function ControlledForm() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Email:', email, 'Password:', password);
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                value={email}                    // React controls value
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
            />
            <input
                type="password"
                value={password}                 // React controls value
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
            />
            <button type="submit">Login</button>
        </form>
    );
}
```

**Uncontrolled Components (Less common):**

```jsx
// DOM controls the input value
function UncontrolledForm() {
    const emailRef = useRef();
    const passwordRef = useRef();
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Email:', emailRef.current.value);
        console.log('Password:', passwordRef.current.value);
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                ref={emailRef}                   // Access via ref
                placeholder="Email"
            />
            <input
                type="password"
                ref={passwordRef}                // Access via ref
                placeholder="Password"
            />
            <button type="submit">Login</button>
        </form>
    );
}
```

**When to Use Each:**
- **Controlled**: Most cases, validation, dynamic behavior
- **Uncontrolled**: File uploads, integrating with non-React code

---

### 2️⃣ Custom Form Hook (15 minutes)

**Create useForm Hook:**

```jsx
// hooks/useForm.js
import { useState } from 'react';

function useForm(initialValues, validationRules) {
    const [values, setValues] = useState(initialValues);
    const [errors, setErrors] = useState({});
    const [touched, setTouched] = useState({});
    const [isSubmitting, setIsSubmitting] = useState(false);
    
    // Handle input changes
    const handleChange = (name, value) => {
        setValues(prev => ({
            ...prev,
            [name]: value
        }));
        
        // Clear error when user starts typing
        if (errors[name]) {
            setErrors(prev => ({
                ...prev,
                [name]: ''
            }));
        }
    };
    
    // Handle input blur (when user leaves field)
    const handleBlur = (name) => {
        setTouched(prev => ({
            ...prev,
            [name]: true
        }));
        
        // Validate single field
        validateField(name, values[name]);
    };
    
    // Validate single field
    const validateField = (name, value) => {
        if (validationRules[name]) {
            const error = validationRules[name](value, values);
            setErrors(prev => ({
                ...prev,
                [name]: error
            }));
            return error;
        }
        return '';
    };
    
    // Validate all fields
    const validateForm = () => {
        const newErrors = {};
        let isValid = true;
        
        Object.keys(validationRules).forEach(name => {
            const error = validationRules[name](values[name], values);
            if (error) {
                newErrors[name] = error;
                isValid = false;
            }
        });
        
        setErrors(newErrors);
        setTouched(Object.keys(validationRules).reduce((acc, key) => {
            acc[key] = true;
            return acc;
        }, {}));
        
        return isValid;
    };
    
    // Handle form submission
    const handleSubmit = async (onSubmit) => {
        setIsSubmitting(true);
        
        if (validateForm()) {
            try {
                await onSubmit(values);
            } catch (error) {
                console.error('Form submission error:', error);
            }
        }
        
        setIsSubmitting(false);
    };
    
    // Reset form
    const reset = () => {
        setValues(initialValues);
        setErrors({});
        setTouched({});
        setIsSubmitting(false);
    };
    
    return {
        values,
        errors,
        touched,
        isSubmitting,
        handleChange,
        handleBlur,
        handleSubmit,
        reset,
        isValid: Object.keys(errors).length === 0
    };
}

export default useForm;
```

**Validation Rules:**

```jsx
// utils/validationRules.js
export const validationRules = {
    required: (value) => {
        if (!value || value.toString().trim() === '') {
            return 'This field is required';
        }
        return '';
    },
    
    email: (value) => {
        if (!value) return '';
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            return 'Please enter a valid email address';
        }
        return '';
    },
    
    minLength: (min) => (value) => {
        if (!value) return '';
        if (value.length < min) {
            return `Must be at least ${min} characters long`;
        }
        return '';
    },
    
    password: (value) => {
        if (!value) return '';
        if (value.length < 8) {
            return 'Password must be at least 8 characters long';
        }
        if (!/(?=.*[a-z])/.test(value)) {
            return 'Password must contain at least one lowercase letter';
        }
        if (!/(?=.*[A-Z])/.test(value)) {
            return 'Password must contain at least one uppercase letter';
        }
        if (!/(?=.*\d)/.test(value)) {
            return 'Password must contain at least one number';
        }
        return '';
    },
    
    confirmPassword: (value, allValues) => {
        if (!value) return '';
        if (value !== allValues.password) {
            return 'Passwords do not match';
        }
        return '';
    },
    
    phone: (value) => {
        if (!value) return '';
        const phoneRegex = /^\(\d{3}\) \d{3}-\d{4}$/;
        if (!phoneRegex.test(value)) {
            return 'Please enter phone in format (123) 456-7890';
        }
        return '';
    }
};

// Combine validation rules
export const combineValidators = (...validators) => (value, allValues) => {
    for (let validator of validators) {
        const error = validator(value, allValues);
        if (error) return error;
    }
    return '';
};
```

---

### 3️⃣ Registration Form Example (20 minutes)

**Registration Form Component:**

```jsx
// components/RegistrationForm.js
import React from 'react';
import useForm from '../hooks/useForm';
import { validationRules, combineValidators } from '../utils/validationRules';
import FormInput from './FormInput';
import './RegistrationForm.css';

function RegistrationForm() {
    const initialValues = {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        password: '',
        confirmPassword: '',
        agreeToTerms: false
    };
    
    const validation = {
        firstName: combineValidators(
            validationRules.required,
            validationRules.minLength(2)
        ),
        lastName: combineValidators(
            validationRules.required,
            validationRules.minLength(2)
        ),
        email: combineValidators(
            validationRules.required,
            validationRules.email
        ),
        phone: validationRules.phone,
        password: combineValidators(
            validationRules.required,
            validationRules.password
        ),
        confirmPassword: combineValidators(
            validationRules.required,
            validationRules.confirmPassword
        ),
        agreeToTerms: (value) => {
            if (!value) {
                return 'You must agree to the terms and conditions';
            }
            return '';
        }
    };
    
    const {
        values,
        errors,
        touched,
        isSubmitting,
        handleChange,
        handleBlur,
        handleSubmit,
        reset
    } = useForm(initialValues, validation);
    
    const onSubmit = async (formData) => {
        // Simulate API call
        console.log('Registering user:', formData);
        
        try {
            const response = await fetch('/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });
            
            if (response.ok) {
                alert('Registration successful!');
                reset();
            } else {
                const errorData = await response.json();
                alert(`Registration failed: ${errorData.message}`);
            }
        } catch (error) {
            alert('Network error. Please try again.');
        }
    };
    
    const formatPhoneNumber = (value) => {
        // Remove all non-digits
        const phoneNumber = value.replace(/\D/g, '');
        
        // Format as (123) 456-7890
        if (phoneNumber.length >= 6) {
            return `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(3, 6)}-${phoneNumber.slice(6, 10)}`;
        } else if (phoneNumber.length >= 3) {
            return `(${phoneNumber.slice(0, 3)}) ${phoneNumber.slice(3)}`;
        } else {
            return phoneNumber;
        }
    };
    
    return (
        <div className="registration-form-container">
            <div className="registration-form">
                <h2>Create Your Account</h2>
                <p className="form-subtitle">Join us today and get started!</p>
                
                <form onSubmit={(e) => {
                    e.preventDefault();
                    handleSubmit(onSubmit);
                }}>
                    <div className="form-row">
                        <FormInput
                            label="First Name"
                            type="text"
                            name="firstName"
                            value={values.firstName}
                            onChange={(e) => handleChange('firstName', e.target.value)}
                            onBlur={() => handleBlur('firstName')}
                            error={touched.firstName ? errors.firstName : ''}
                            placeholder="Enter your first name"
                            required
                        />
                        
                        <FormInput
                            label="Last Name"
                            type="text"
                            name="lastName"
                            value={values.lastName}
                            onChange={(e) => handleChange('lastName', e.target.value)}
                            onBlur={() => handleBlur('lastName')}
                            error={touched.lastName ? errors.lastName : ''}
                            placeholder="Enter your last name"
                            required
                        />
                    </div>
                    
                    <FormInput
                        label="Email Address"
                        type="email"
                        name="email"
                        value={values.email}
                        onChange={(e) => handleChange('email', e.target.value)}
                        onBlur={() => handleBlur('email')}
                        error={touched.email ? errors.email : ''}
                        placeholder="Enter your email address"
                        required
                    />
                    
                    <FormInput
                        label="Phone Number"
                        type="tel"
                        name="phone"
                        value={values.phone}
                        onChange={(e) => {
                            const formatted = formatPhoneNumber(e.target.value);
                            handleChange('phone', formatted);
                        }}
                        onBlur={() => handleBlur('phone')}
                        error={touched.phone ? errors.phone : ''}
                        placeholder="(123) 456-7890"
                    />
                    
                    <FormInput
                        label="Password"
                        type="password"
                        name="password"
                        value={values.password}
                        onChange={(e) => handleChange('password', e.target.value)}
                        onBlur={() => handleBlur('password')}
                        error={touched.password ? errors.password : ''}
                        placeholder="Create a strong password"
                        required
                    />
                    
                    <FormInput
                        label="Confirm Password"
                        type="password"
                        name="confirmPassword"
                        value={values.confirmPassword}
                        onChange={(e) => handleChange('confirmPassword', e.target.value)}
                        onBlur={() => handleBlur('confirmPassword')}
                        error={touched.confirmPassword ? errors.confirmPassword : ''}
                        placeholder="Confirm your password"
                        required
                    />
                    
                    <div className="checkbox-group">
                        <label className="checkbox-label">
                            <input
                                type="checkbox"
                                checked={values.agreeToTerms}
                                onChange={(e) => handleChange('agreeToTerms', e.target.checked)}
                                onBlur={() => handleBlur('agreeToTerms')}
                            />
                            <span className="checkmark"></span>
                            I agree to the <a href="/terms" target="_blank">Terms and Conditions</a> and <a href="/privacy" target="_blank">Privacy Policy</a>
                        </label>
                        {touched.agreeToTerms && errors.agreeToTerms && (
                            <span className="error-message">{errors.agreeToTerms}</span>
                        )}
                    </div>
                    
                    <div className="form-actions">
                        <button 
                            type="submit" 
                            className="submit-btn"
                            disabled={isSubmitting}
                        >
                            {isSubmitting ? 'Creating Account...' : 'Create Account'}
                        </button>
                        
                        <button 
                            type="button" 
                            className="reset-btn"
                            onClick={reset}
                        >
                            Reset Form
                        </button>
                    </div>
                </form>
                
                <div className="form-footer">
                    <p>Already have an account? <a href="/login">Sign in here</a></p>
                </div>
            </div>
        </div>
    );
}

export default RegistrationForm;
```

**Reusable FormInput Component:**

```jsx
// components/FormInput.js
import React, { useState } from 'react';
import './FormInput.css';

function FormInput({
    label,
    type = 'text',
    name,
    value,
    onChange,
    onBlur,
    error,
    placeholder,
    required = false,
    helpText,
    ...props
}) {
    const [showPassword, setShowPassword] = useState(false);
    
    const inputType = type === 'password' && showPassword ? 'text' : type;
    
    return (
        <div className="form-input">
            <label htmlFor={name} className="input-label">
                {label} {required && <span className="required">*</span>}
            </label>
            
            <div className="input-wrapper">
                <input
                    id={name}
                    name={name}
                    type={inputType}
                    value={value}
                    onChange={onChange}
                    onBlur={onBlur}
                    placeholder={placeholder}
                    className={`input-field ${error ? 'error' : ''}`}
                    {...props}
                />
                
                {type === 'password' && (
                    <button
                        type="button"
                        className="password-toggle"
                        onClick={() => setShowPassword(!showPassword)}
                    >
                        {showPassword ? '👁️' : '👁️‍🗨️'}
                    </button>
                )}
            </div>
            
            {helpText && !error && (
                <span className="help-text">{helpText}</span>
            )}
            
            {error && (
                <span className="error-message">{error}</span>
            )}
        </div>
    );
}

export default FormInput;
```

---

### 4️⃣ Dynamic Forms (10 minutes)

**Dynamic Field Form:**

```jsx
// components/DynamicForm.js
import React from 'react';
import useForm from '../hooks/useForm';
import FormInput from './FormInput';

function DynamicForm() {
    const [fields, setFields] = useState([
        { id: 1, name: 'skill1', label: 'Skill 1', required: true }
    ]);
    
    const initialValues = fields.reduce((acc, field) => {
        acc[field.name] = '';
        return acc;
    }, {});
    
    const validation = fields.reduce((acc, field) => {
        if (field.required) {
            acc[field.name] = (value) => {
                if (!value || value.trim() === '') {
                    return `${field.label} is required`;
                }
                return '';
            };
        }
        return acc;
    }, {});
    
    const form = useForm(initialValues, validation);
    
    const addField = () => {
        const newField = {
            id: Date.now(),
            name: `skill${fields.length + 1}`,
            label: `Skill ${fields.length + 1}`,
            required: false
        };
        setFields([...fields, newField]);
    };
    
    const removeField = (id) => {
        if (fields.length > 1) {
            setFields(fields.filter(field => field.id !== id));
        }
    };
    
    const onSubmit = async (formData) => {
        console.log('Dynamic form data:', formData);
    };
    
    return (
        <div className="dynamic-form">
            <h2>Skills Form</h2>
            
            <form onSubmit={(e) => {
                e.preventDefault();
                form.handleSubmit(onSubmit);
            }}>
                {fields.map((field, index) => (
                    <div key={field.id} className="dynamic-field">
                        <FormInput
                            label={field.label}
                            name={field.name}
                            value={form.values[field.name] || ''}
                            onChange={(e) => form.handleChange(field.name, e.target.value)}
                            onBlur={() => form.handleBlur(field.name)}
                            error={form.touched[field.name] ? form.errors[field.name] : ''}
                            placeholder={`Enter ${field.label.toLowerCase()}`}
                            required={field.required}
                        />
                        
                        {fields.length > 1 && (
                            <button
                                type="button"
                                onClick={() => removeField(field.id)}
                                className="remove-field-btn"
                            >
                                Remove
                            </button>
                        )}
                    </div>
                ))}
                
                <div className="form-actions">
                    <button
                        type="button"
                        onClick={addField}
                        className="add-field-btn"
                    >
                        Add Another Skill
                    </button>
                    
                    <button
                        type="submit"
                        className="submit-btn"
                        disabled={form.isSubmitting}
                    >
                        {form.isSubmitting ? 'Submitting...' : 'Submit'}
                    </button>
                </div>
            </form>
        </div>
    );
}

export default DynamicForm;
```

---

### 5️⃣ File Upload Form (5 minutes)

**File Upload Component:**

```jsx
// components/FileUpload.js
import React, { useState } from 'react';

function FileUpload() {
    const [selectedFiles, setSelectedFiles] = useState([]);
    const [uploading, setUploading] = useState(false);
    const [uploadProgress, setUploadProgress] = useState({});
    
    const handleFileSelect = (e) => {
        const files = Array.from(e.target.files);
        setSelectedFiles(files);
    };
    
    const uploadFile = async (file) => {
        const formData = new FormData();
        formData.append('file', file);
        
        const xhr = new XMLHttpRequest();
        
        // Track upload progress
        xhr.upload.addEventListener('progress', (e) => {
            if (e.lengthComputable) {
                const progress = (e.loaded / e.total) * 100;
                setUploadProgress(prev => ({
                    ...prev,
                    [file.name]: progress
                }));
            }
        });
        
        return new Promise((resolve, reject) => {
            xhr.onreadystatechange = () => {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        resolve(JSON.parse(xhr.responseText));
                    } else {
                        reject(new Error('Upload failed'));
                    }
                }
            };
            
            xhr.open('POST', '/api/upload');
            xhr.send(formData);
        });
    };
    
    const handleUpload = async () => {
        setUploading(true);
        
        try {
            const uploadPromises = selectedFiles.map(file => uploadFile(file));
            await Promise.all(uploadPromises);
            alert('All files uploaded successfully!');
            setSelectedFiles([]);
            setUploadProgress({});
        } catch (error) {
            alert('Upload failed. Please try again.');
        } finally {
            setUploading(false);
        }
    };
    
    return (
        <div className="file-upload">
            <h3>File Upload</h3>
            
            <div className="file-input-wrapper">
                <input
                    type="file"
                    multiple
                    onChange={handleFileSelect}
                    accept="image/*,.pdf,.doc,.docx"
                />
            </div>
            
            {selectedFiles.length > 0 && (
                <div className="selected-files">
                    <h4>Selected Files:</h4>
                    {selectedFiles.map((file, index) => (
                        <div key={index} className="file-item">
                            <span>{file.name}</span>
                            <span>({(file.size / 1024).toFixed(1)} KB)</span>
                            {uploadProgress[file.name] && (
                                <div className="progress-bar">
                                    <div 
                                        className="progress-fill"
                                        style={{ width: `${uploadProgress[file.name]}%` }}
                                    ></div>
                                </div>
                            )}
                        </div>
                    ))}
                    
                    <button
                        onClick={handleUpload}
                        disabled={uploading}
                        className="upload-btn"
                    >
                        {uploading ? 'Uploading...' : 'Upload Files'}
                    </button>
                </div>
            )}
        </div>
    );
}

export default FileUpload;
```

---

### 🏠 Homework: Build Survey Form

**Task:** Create a multi-step survey form with various input types

```jsx
// Create a survey form with:
// 1. Personal info (name, email, age)
// 2. Multiple choice questions
// 3. Rating scales (1-5 stars)
// 4. Text areas for feedback
// 5. Progress indicator
// 6. Form persistence (save to localStorage)

// Include features:
// - Step navigation (Next/Previous)
// - Form validation on each step
// - Save progress automatically
// - Submit final results
```

---

### 📝 Key Takeaways

✅ Controlled components = React manages form state
✅ Custom hooks = Reusable form logic
✅ Validation = Real-time user feedback
✅ Dynamic forms = Add/remove fields programmatically
✅ File uploads = Handle multipart form data

---

<a name="hour-29"></a>
## 📅 Hour 29: Consuming APIs

### 🎯 Learning Objectives
- Master fetch API and async/await patterns
- Handle loading states and error scenarios
- Implement CRUD operations with REST APIs
- Create custom API hooks
- Build a complete data-driven application

### 📖 What to Teach

**"Today we connect our React apps to real data using APIs!"**

---

### 1️⃣ Fetch API Fundamentals (10 minutes)

**Basic Fetch Operations:**

```jsx
// GET Request - Fetch data
const fetchUsers = async () => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const users = await response.json();
        console.log('Users:', users);
        return users;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};

// POST Request - Create data
const createUser = async (userData) => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const newUser = await response.json();
        console.log('Created user:', newUser);
        return newUser;
    } catch (error) {
        console.error('Error creating user:', error);
        throw error;
    }
};

// PUT Request - Update data
const updateUser = async (id, userData) => {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData),
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const updatedUser = await response.json();
        return updatedUser;
    } catch (error) {
        console.error('Error updating user:', error);
        throw error;
    }
};

// DELETE Request - Remove data
const deleteUser = async (id) => {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, {
            method: 'DELETE',
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return true;
    } catch (error) {
        console.error('Error deleting user:', error);
        throw error;
    }
};
```

**Error Handling Best Practices:**

```jsx
// Custom error class for API errors
class APIError extends Error {
    constructor(message, status, data) {
        super(message);
        this.name = 'APIError';
        this.status = status;
        this.data = data;
    }
}

// Enhanced fetch wrapper
const apiCall = async (url, options = {}) => {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
            ...options,
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new APIError(
                data.message || 'An error occurred',
                response.status,
                data
            );
        }
        
        return data;
    } catch (error) {
        if (error instanceof APIError) {
            throw error;
        }
        
        // Network or other errors
        throw new APIError(
            'Network error. Please check your connection.',
            0,
            null
        );
    }
};
```

---

### 2️⃣ Custom API Hooks (15 minutes)

**Generic useApi Hook:**

```jsx
// hooks/useApi.js
import { useState, useEffect } from 'react';

function useApi(url, options = {}) {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        let isCancelled = false;
        
        const fetchData = async () => {
            try {
                setLoading(true);
                setError(null);
                
                const response = await fetch(url, options);
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const result = await response.json();
                
                if (!isCancelled) {
                    setData(result);
                }
            } catch (err) {
                if (!isCancelled) {
                    setError(err.message);
                }
            } finally {
                if (!isCancelled) {
                    setLoading(false);
                }
            }
        };
        
        fetchData();
        
        // Cleanup function to cancel request if component unmounts
        return () => {
            isCancelled = true;
        };
    }, [url, JSON.stringify(options)]);
    
    const refetch = () => {
        setLoading(true);
        setError(null);
        // The useEffect will run again due to dependency changes
    };
    
    return { data, loading, error, refetch };
}

export default useApi;
```

**Specific Resource Hooks:**

```jsx
// hooks/useUsers.js
import { useState } from 'react';
import useApi from './useApi';

function useUsers() {
    const { data: users, loading, error, refetch } = useApi(
        'https://jsonplaceholder.typicode.com/users'
    );
    
    const [actionLoading, setActionLoading] = useState(false);
    
    const createUser = async (userData) => {
        setActionLoading(true);
        try {
            const response = await fetch('https://jsonplaceholder.typicode.com/users', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData),
            });
            
            if (!response.ok) {
                throw new Error('Failed to create user');
            }
            
            const newUser = await response.json();
            refetch(); // Refresh the users list
            return newUser;
        } catch (error) {
            throw error;
        } finally {
            setActionLoading(false);
        }
    };
    
    const updateUser = async (id, userData) => {
        setActionLoading(true);
        try {
            const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData),
            });
            
            if (!response.ok) {
                throw new Error('Failed to update user');
            }
            
            const updatedUser = await response.json();
            refetch(); // Refresh the users list
            return updatedUser;
        } catch (error) {
            throw error;
        } finally {
            setActionLoading(false);
        }
    };
    
    const deleteUser = async (id) => {
        setActionLoading(true);
        try {
            const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`, {
                method: 'DELETE',
            });
            
            if (!response.ok) {
                throw new Error('Failed to delete user');
            }
            
            refetch(); // Refresh the users list
            return true;
        } catch (error) {
            throw error;
        } finally {
            setActionLoading(false);
        }
    };
    
    return {
        users,
        loading,
        error,
        actionLoading,
        createUser,
        updateUser,
        deleteUser,
        refetch
    };
}

export default useUsers;
```

---

### 3️⃣ User Management App (20 minutes)

**Main UserList Component:**

```jsx
// components/UserList.js
import React, { useState } from 'react';
import useUsers from '../hooks/useUsers';
import UserCard from './UserCard';
import UserForm from './UserForm';
import LoadingSpinner from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';
import './UserList.css';

function UserList() {
    const { 
        users, 
        loading, 
        error, 
        actionLoading, 
        createUser, 
        updateUser, 
        deleteUser 
    } = useUsers();
    
    const [editingUser, setEditingUser] = useState(null);
    const [showForm, setShowForm] = useState(false);
    
    const handleCreateUser = async (userData) => {
        try {
            await createUser(userData);
            setShowForm(false);
            alert('User created successfully!');
        } catch (error) {
            alert(`Error creating user: ${error.message}`);
        }
    };
    
    const handleUpdateUser = async (userData) => {
        try {
            await updateUser(editingUser.id, userData);
            setEditingUser(null);
            alert('User updated successfully!');
        } catch (error) {
            alert(`Error updating user: ${error.message}`);
        }
    };
    
    const handleDeleteUser = async (id) => {
        if (window.confirm('Are you sure you want to delete this user?')) {
            try {
                await deleteUser(id);
                alert('User deleted successfully!');
            } catch (error) {
                alert(`Error deleting user: ${error.message}`);
            }
        }
    };
    
    const handleEditUser = (user) => {
        setEditingUser(user);
        setShowForm(true);
    };
    
    const handleCancelEdit = () => {
        setEditingUser(null);
        setShowForm(false);
    };
    
    if (loading) {
        return <LoadingSpinner message="Loading users..." />;
    }
    
    if (error) {
        return <ErrorMessage message={error} />;
    }
    
    return (
        <div className="user-list-container">
            <div className="user-list-header">
                <h1>User Management</h1>
                <button 
                    className="add-user-btn"
                    onClick={() => setShowForm(true)}
                    disabled={actionLoading}
                >
                    Add New User
                </button>
            </div>
            
            {showForm && (
                <UserForm
                    user={editingUser}
                    onSubmit={editingUser ? handleUpdateUser : handleCreateUser}
                    onCancel={handleCancelEdit}
                    loading={actionLoading}
                />
            )}
            
            <div className="user-grid">
                {users && users.map(user => (
                    <UserCard
                        key={user.id}
                        user={user}
                        onEdit={() => handleEditUser(user)}
                        onDelete={() => handleDeleteUser(user.id)}
                        disabled={actionLoading}
                    />
                ))}
            </div>
            
            {users && users.length === 0 && (
                <div className="empty-state">
                    <h3>No users found</h3>
                    <p>Get started by adding your first user!</p>
                </div>
            )}
        </div>
    );
}

export default UserList;
```

**UserCard Component:**

```jsx
// components/UserCard.js
import React from 'react';
import './UserCard.css';

function UserCard({ user, onEdit, onDelete, disabled }) {
    return (
        <div className="user-card">
            <div className="user-avatar">
                <img 
                    src={`https://ui-avatars.com/api/?name=${user.name}&background=007bff&color=fff`}
                    alt={user.name}
                />
            </div>
            
            <div className="user-info">
                <h3>{user.name}</h3>
                <p className="user-email">{user.email}</p>
                <p className="user-phone">{user.phone}</p>
                
                {user.address && (
                    <p className="user-address">
                        {user.address.city}, {user.address.zipcode}
                    </p>
                )}
                
                {user.website && (
                    <a 
                        href={`https://${user.website}`} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="user-website"
                    >
                        {user.website}
                    </a>
                )}
            </div>
            
            <div className="user-actions">
                <button 
                    onClick={onEdit}
                    disabled={disabled}
                    className="edit-btn"
                >
                    Edit
                </button>
                <button 
                    onClick={onDelete}
                    disabled={disabled}
                    className="delete-btn"
                >
                    Delete
                </button>
            </div>
        </div>
    );
}

export default UserCard;
```

**UserForm Component:**

```jsx
// components/UserForm.js
import React from 'react';
import useForm from '../hooks/useForm';
import FormInput from './FormInput';
import './UserForm.css';

function UserForm({ user, onSubmit, onCancel, loading }) {
    const initialValues = {
        name: user?.name || '',
        email: user?.email || '',
        phone: user?.phone || '',
        website: user?.website || '',
        address: {
            street: user?.address?.street || '',
            city: user?.address?.city || '',
            zipcode: user?.address?.zipcode || ''
        },
        company: {
            name: user?.company?.name || ''
        }
    };
    
    const validation = {
        name: (value) => {
            if (!value || value.trim() === '') {
                return 'Name is required';
            }
            return '';
        },
        email: (value) => {
            if (!value || value.trim() === '') {
                return 'Email is required';
            }
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                return 'Please enter a valid email address';
            }
            return '';
        }
    };
    
    const {
        values,
        errors,
        touched,
        handleChange,
        handleBlur,
        handleSubmit
    } = useForm(initialValues, validation);
    
    const handleFormSubmit = async (formData) => {
        await onSubmit(formData);
    };
    
    return (
        <div className="user-form-overlay">
            <div className="user-form-container">
                <div className="user-form-header">
                    <h2>{user ? 'Edit User' : 'Create New User'}</h2>
                    <button className="close-btn" onClick={onCancel}>×</button>
                </div>
                
                <form onSubmit={(e) => {
                    e.preventDefault();
                    handleSubmit(handleFormSubmit);
                }}>
                    <div className="form-section">
                        <h3>Basic Information</h3>
                        
                        <FormInput
                            label="Full Name"
                            name="name"
                            value={values.name}
                            onChange={(e) => handleChange('name', e.target.value)}
                            onBlur={() => handleBlur('name')}
                            error={touched.name ? errors.name : ''}
                            placeholder="Enter full name"
                            required
                        />
                        
                        <FormInput
                            label="Email Address"
                            type="email"
                            name="email"
                            value={values.email}
                            onChange={(e) => handleChange('email', e.target.value)}
                            onBlur={() => handleBlur('email')}
                            error={touched.email ? errors.email : ''}
                            placeholder="Enter email address"
                            required
                        />
                        
                        <FormInput
                            label="Phone Number"
                            name="phone"
                            value={values.phone}
                            onChange={(e) => handleChange('phone', e.target.value)}
                            placeholder="Enter phone number"
                        />
                        
                        <FormInput
                            label="Website"
                            name="website"
                            value={values.website}
                            onChange={(e) => handleChange('website', e.target.value)}
                            placeholder="Enter website URL"
                        />
                    </div>
                    
                    <div className="form-section">
                        <h3>Address</h3>
                        
                        <FormInput
                            label="Street"
                            name="address.street"
                            value={values.address.street}
                            onChange={(e) => handleChange('address.street', e.target.value)}
                            placeholder="Enter street address"
                        />
                        
                        <div className="form-row">
                            <FormInput
                                label="City"
                                name="address.city"
                                value={values.address.city}
                                onChange={(e) => handleChange('address.city', e.target.value)}
                                placeholder="Enter city"
                            />
                            
                            <FormInput
                                label="Zip Code"
                                name="address.zipcode"
                                value={values.address.zipcode}
                                onChange={(e) => handleChange('address.zipcode', e.target.value)}
                                placeholder="Enter zip code"
                            />
                        </div>
                    </div>
                    
                    <div className="form-section">
                        <h3>Company</h3>
                        
                        <FormInput
                            label="Company Name"
                            name="company.name"
                            value={values.company.name}
                            onChange={(e) => handleChange('company.name', e.target.value)}
                            placeholder="Enter company name"
                        />
                    </div>
                    
                    <div className="form-actions">
                        <button 
                            type="button" 
                            onClick={onCancel}
                            className="cancel-btn"
                            disabled={loading}
                        >
                            Cancel
                        </button>
                        <button 
                            type="submit"
                            className="submit-btn"
                            disabled={loading}
                        >
                            {loading ? 'Saving...' : (user ? 'Update User' : 'Create User')}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default UserForm;
```

---

### 4️⃣ Advanced API Patterns (10 minutes)

**Pagination Hook:**

```jsx
// hooks/usePagination.js
import { useState } from 'react';
import useApi from './useApi';

function usePagination(baseUrl, itemsPerPage = 10) {
    const [currentPage, setCurrentPage] = useState(1);
    
    const url = `${baseUrl}?_page=${currentPage}&_limit=${itemsPerPage}`;
    const { data, loading, error, refetch } = useApi(url);
    
    const goToPage = (page) => {
        setCurrentPage(page);
    };
    
    const nextPage = () => {
        setCurrentPage(prev => prev + 1);
    };
    
    const prevPage = () => {
        if (currentPage > 1) {
            setCurrentPage(prev => prev - 1);
        }
    };
    
    return {
        data,
        loading,
        error,
        currentPage,
        goToPage,
        nextPage,
        prevPage,
        refetch
    };
}

export default usePagination;
```

**Search Hook:**

```jsx
// hooks/useSearch.js
import { useState, useEffect } from 'react';
import { debounce } from '../utils/debounce';

function useSearch(searchFunction, delay = 300) {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    
    // Debounced search function
    const debouncedSearch = debounce(async (searchQuery) => {
        if (!searchQuery.trim()) {
            setResults([]);
            return;
        }
        
        try {
            setLoading(true);
            setError(null);
            const searchResults = await searchFunction(searchQuery);
            setResults(searchResults);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }, delay);
    
    useEffect(() => {
        debouncedSearch(query);
    }, [query]);
    
    return {
        query,
        setQuery,
        results,
        loading,
        error
    };
}

// Utility debounce function
const debounce = (func, delay) => {
    let timeoutId;
    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func.apply(null, args), delay);
    };
};

export default useSearch;
```

**Caching Hook:**

```jsx
// hooks/useCache.js
import { useState, useEffect } from 'react';

const cache = new Map();

function useCache(key, fetchFunction, ttl = 5 * 60 * 1000) { // 5 minutes TTL
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                // Check if data exists in cache and is not expired
                const cached = cache.get(key);
                if (cached && Date.now() - cached.timestamp < ttl) {
                    setData(cached.data);
                    setLoading(false);
                    return;
                }
                
                setLoading(true);
                setError(null);
                
                const result = await fetchFunction();
                
                // Store in cache
                cache.set(key, {
                    data: result,
                    timestamp: Date.now()
                });
                
                setData(result);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        
        fetchData();
    }, [key, ttl]);
    
    const invalidateCache = () => {
        cache.delete(key);
    };
    
    return { data, loading, error, invalidateCache };
}

export default useCache;
```

---

### 5️⃣ Real-time Updates (5 minutes)

**WebSocket Hook:**

```jsx
// hooks/useWebSocket.js
import { useState, useEffect, useRef } from 'react';

function useWebSocket(url) {
    const [socket, setSocket] = useState(null);
    const [lastMessage, setLastMessage] = useState(null);
    const [readyState, setReadyState] = useState(WebSocket.CONNECTING);
    
    const messageHandler = useRef(null);
    
    useEffect(() => {
        const ws = new WebSocket(url);
        
        ws.onopen = () => {
            setReadyState(WebSocket.OPEN);
        };
        
        ws.onclose = () => {
            setReadyState(WebSocket.CLOSED);
        };
        
        ws.onerror = (error) => {
            console.error('WebSocket error:', error);
        };
        
        ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            setLastMessage(message);
            
            if (messageHandler.current) {
                messageHandler.current(message);
            }
        };
        
        setSocket(ws);
        
        return () => {
            ws.close();
        };
    }, [url]);
    
    const sendMessage = (message) => {
        if (socket && readyState === WebSocket.OPEN) {
            socket.send(JSON.stringify(message));
        }
    };
    
    const setMessageHandler = (handler) => {
        messageHandler.current = handler;
    };
    
    return {
        sendMessage,
        lastMessage,
        readyState,
        setMessageHandler
    };
}

export default useWebSocket;
```

---

### 🏠 Homework: Build a Blog App

**Task:** Create a complete blog application with API integration

```jsx
// Build a blog app with:
// 1. Post list with pagination
// 2. Post detail view with comments
// 3. Create/edit/delete posts
// 4. Search functionality
// 5. Categories and tags
// 6. Author profiles

// API endpoints to use:
// - https://jsonplaceholder.typicode.com/posts
// - https://jsonplaceholder.typicode.com/comments
// - https://jsonplaceholder.typicode.com/users

// Features to implement:
// - Loading states for all operations
// - Error handling and retry logic
// - Optimistic updates
// - Caching for better performance
```

---

### 📝 Key Takeaways

✅ Fetch API = Modern way to make HTTP requests
✅ Custom hooks = Reusable API logic
✅ Error handling = Essential for good UX
✅ Loading states = Keep users informed
✅ CRUD operations = Create, Read, Update, Delete

---

<a name="hour-30"></a>
## 📅 Hour 30: Full-Stack Integration

### 🎯 Learning Objectives
- Connect React frontend to Flask backend
- Implement authentication flow
- Handle CORS and API security
- Deploy full-stack application
- Build a complete todo application

### 📖 What to Teach

**"Today we bring everything together - connecting our React frontend to our Flask backend for a complete full-stack application!"**

---

### 1️⃣ Setting Up the Connection (10 minutes)

**Frontend API Configuration:**

```jsx
// config/api.js
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

class ApiService {
    constructor() {
        this.baseURL = API_BASE_URL;
        this.token = localStorage.getItem('token');
    }
    
    setAuthToken(token) {
        this.token = token;
        if (token) {
            localStorage.setItem('token', token);
        } else {
            localStorage.removeItem('token');
        }
    }
    
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
            ...options,
        };
        
        if (this.token) {
            config.headers.Authorization = `Bearer ${this.token}`;
        }
        
        try {
            const response = await fetch(url, config);
            
            if (response.status === 401) {
                // Token expired or invalid
                this.setAuthToken(null);
                window.location.href = '/login';
                return;
            }
            
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || 'An error occurred');
            }
            
            return await response.json();
        } catch (error) {
            console.error('API request failed:', error);
            throw error;
        }
    }
    
    // Auth endpoints
    async login(credentials) {
        return this.request('/api/auth/login', {
            method: 'POST',
            body: JSON.stringify(credentials),
        });
    }
    
    async register(userData) {
        return this.request('/api/auth/register', {
            method: 'POST',
            body: JSON.stringify(userData),
        });
    }
    
    async getCurrentUser() {
        return this.request('/api/auth/me');
    }
    
    // Todo endpoints
    async getTodos() {
        return this.request('/api/todos');
    }
    
    async createTodo(todoData) {
        return this.request('/api/todos', {
            method: 'POST',
            body: JSON.stringify(todoData),
        });
    }
    
    async updateTodo(id, todoData) {
        return this.request(`/api/todos/${id}`, {
            method: 'PUT',
            body: JSON.stringify(todoData),
        });
    }
    
    async deleteTodo(id) {
        return this.request(`/api/todos/${id}`, {
            method: 'DELETE',
        });
    }
}

export default new ApiService();
```

**Environment Configuration:**

```javascript
// .env.development
REACT_APP_API_URL=http://localhost:5000

// .env.production
REACT_APP_API_URL=https://your-backend-domain.com
```

---

### 2️⃣ Authentication Integration (15 minutes)

**Auth Context with API:**

```jsx
// contexts/AuthContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';
import ApiService from '../config/api';

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    
    // Check if user is logged in on app start
    useEffect(() => {
        const initAuth = async () => {
            const token = localStorage.getItem('token');
            if (token) {
                try {
                    ApiService.setAuthToken(token);
                    const userData = await ApiService.getCurrentUser();
                    setUser(userData);
                    setIsAuthenticated(true);
                } catch (error) {
                    console.error('Failed to get user data:', error);
                    localStorage.removeItem('token');
                    ApiService.setAuthToken(null);
                }
            }
            setLoading(false);
        };
        
        initAuth();
    }, []);
    
    const login = async (credentials) => {
        try {
            const response = await ApiService.login(credentials);
            const { user: userData, token } = response;
            
            ApiService.setAuthToken(token);
            setUser(userData);
            setIsAuthenticated(true);
            
            return { success: true };
        } catch (error) {
            return { success: false, error: error.message };
        }
    };
    
    const register = async (userData) => {
        try {
            const response = await ApiService.register(userData);
            const { user: newUser, token } = response;
            
            ApiService.setAuthToken(token);
            setUser(newUser);
            setIsAuthenticated(true);
            
            return { success: true };
        } catch (error) {
            return { success: false, error: error.message };
        }
    };
    
    const logout = () => {
        ApiService.setAuthToken(null);
        setUser(null);
        setIsAuthenticated(false);
        localStorage.removeItem('token');
    };
    
    const value = {
        user,
        isAuthenticated,
        loading,
        login,
        register,
        logout
    };
    
    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
}
```

**Login Component:**

```jsx
// components/Login.js
import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { useNavigate, Link } from 'react-router-dom';
import FormInput from './FormInput';
import './Login.css';

function Login() {
    const [credentials, setCredentials] = useState({
        email: '',
        password: ''
    });
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState('');
    
    const { login } = useAuth();
    const navigate = useNavigate();
    
    const handleChange = (name, value) => {
        setCredentials(prev => ({
            ...prev,
            [name]: value
        }));
        setError(''); // Clear error when user starts typing
    };
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setError('');
        
        const result = await login(credentials);
        
        if (result.success) {
            navigate('/dashboard');
        } else {
            setError(result.error);
        }
        
        setIsLoading(false);
    };
    
    return (
        <div className="login-container">
            <div className="login-form">
                <h2>Welcome Back</h2>
                <p>Sign in to your account</p>
                
                {error && (
                    <div className="error-alert">
                        {error}
                    </div>
                )}
                
                <form onSubmit={handleSubmit}>
                    <FormInput
                        label="Email Address"
                        type="email"
                        name="email"
                        value={credentials.email}
                        onChange={(e) => handleChange('email', e.target.value)}
                        placeholder="Enter your email"
                        required
                    />
                    
                    <FormInput
                        label="Password"
                        type="password"
                        name="password"
                        value={credentials.password}
                        onChange={(e) => handleChange('password', e.target.value)}
                        placeholder="Enter your password"
                        required
                    />
                    
                    <button 
                        type="submit" 
                        className="login-btn"
                        disabled={isLoading}
                    >
                        {isLoading ? 'Signing In...' : 'Sign In'}
                    </button>
                </form>
                
                <div className="login-footer">
                    <p>Don't have an account? <Link to="/register">Sign up here</Link></p>
                    <Link to="/forgot-password">Forgot your password?</Link>
                </div>
            </div>
        </div>
    );
}

export default Login;
```

**Protected Route Component:**

```jsx
// components/ProtectedRoute.js
import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import LoadingSpinner from './LoadingSpinner';

function ProtectedRoute({ children }) {
    const { isAuthenticated, loading } = useAuth();
    const location = useLocation();
    
    if (loading) {
        return <LoadingSpinner message="Checking authentication..." />;
    }
    
    if (!isAuthenticated) {
        // Redirect to login page with return url
        return <Navigate to="/login" state={{ from: location }} replace />;
    }
    
    return children;
}

export default ProtectedRoute;
```

---

### 3️⃣ Full-Stack Todo App (20 minutes)

**Todo Service Hook:**

```jsx
// hooks/useTodos.js
import { useState, useEffect } from 'react';
import ApiService from '../config/api';

function useTodos() {
    const [todos, setTodos] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [actionLoading, setActionLoading] = useState(false);
    
    // Fetch todos on mount
    useEffect(() => {
        fetchTodos();
    }, []);
    
    const fetchTodos = async () => {
        try {
            setLoading(true);
            setError(null);
            const todoData = await ApiService.getTodos();
            setTodos(todoData);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };
    
    const addTodo = async (todoText) => {
        try {
            setActionLoading(true);
            const newTodo = await ApiService.createTodo({
                title: todoText,
                completed: false
            });
            
            setTodos(prev => [...prev, newTodo]);
            return { success: true, todo: newTodo };
        } catch (err) {
            return { success: false, error: err.message };
        } finally {
            setActionLoading(false);
        }
    };
    
    const toggleTodo = async (id) => {
        try {
            setActionLoading(true);
            const todo = todos.find(t => t.id === id);
            const updatedTodo = await ApiService.updateTodo(id, {
                ...todo,
                completed: !todo.completed
            });
            
            setTodos(prev => 
                prev.map(t => t.id === id ? updatedTodo : t)
            );
            return { success: true };
        } catch (err) {
            return { success: false, error: err.message };
        } finally {
            setActionLoading(false);
        }
    };
    
    const updateTodo = async (id, updates) => {
        try {
            setActionLoading(true);
            const updatedTodo = await ApiService.updateTodo(id, updates);
            
            setTodos(prev => 
                prev.map(t => t.id === id ? updatedTodo : t)
            );
            return { success: true, todo: updatedTodo };
        } catch (err) {
            return { success: false, error: err.message };
        } finally {
            setActionLoading(false);
        }
    };
    
    const deleteTodo = async (id) => {
        try {
            setActionLoading(true);
            await ApiService.deleteTodo(id);
            
            setTodos(prev => prev.filter(t => t.id !== id));
            return { success: true };
        } catch (err) {
            return { success: false, error: err.message };
        } finally {
            setActionLoading(false);
        }
    };
    
    return {
        todos,
        loading,
        error,
        actionLoading,
        addTodo,
        toggleTodo,
        updateTodo,
        deleteTodo,
        refetch: fetchTodos
    };
}

export default useTodos;
```

**Complete Todo Dashboard:**

```jsx
// components/TodoDashboard.js
import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import useTodos from '../hooks/useTodos';
import TodoForm from './TodoForm';
import TodoList from './TodoList';
import TodoStats from './TodoStats';
import LoadingSpinner from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';
import './TodoDashboard.css';

function TodoDashboard() {
    const { user, logout } = useAuth();
    const {
        todos,
        loading,
        error,
        actionLoading,
        addTodo,
        toggleTodo,
        updateTodo,
        deleteTodo
    } = useTodos();
    
    const [filter, setFilter] = useState('all'); // all, active, completed
    const [searchQuery, setSearchQuery] = useState('');
    
    const handleAddTodo = async (todoText) => {
        const result = await addTodo(todoText);
        if (result.success) {
            return { success: true };
        } else {
            return { success: false, error: result.error };
        }
    };
    
    const handleToggleTodo = async (id) => {
        const result = await toggleTodo(id);
        if (!result.success) {
            alert(`Error: ${result.error}`);
        }
    };
    
    const handleUpdateTodo = async (id, updates) => {
        const result = await updateTodo(id, updates);
        if (!result.success) {
            alert(`Error: ${result.error}`);
        }
        return result;
    };
    
    const handleDeleteTodo = async (id) => {
        if (window.confirm('Are you sure you want to delete this todo?')) {
            const result = await deleteTodo(id);
            if (!result.success) {
                alert(`Error: ${result.error}`);
            }
        }
    };
    
    // Filter todos based on status and search query
    const filteredTodos = todos.filter(todo => {
        const matchesFilter = 
            filter === 'all' ? true :
            filter === 'active' ? !todo.completed :
            filter === 'completed' ? todo.completed : true;
        
        const matchesSearch = 
            todo.title.toLowerCase().includes(searchQuery.toLowerCase());
        
        return matchesFilter && matchesSearch;
    });
    
    if (loading) {
        return <LoadingSpinner message="Loading your todos..." />;
    }
    
    if (error) {
        return <ErrorMessage message={error} />;
    }
    
    return (
        <div className="todo-dashboard">
            <header className="dashboard-header">
                <div className="header-content">
                    <div className="user-info">
                        <h1>Welcome back, {user.name}!</h1>
                        <p>Manage your todos efficiently</p>
                    </div>
                    <button onClick={logout} className="logout-btn">
                        Logout
                    </button>
                </div>
            </header>
            
            <main className="dashboard-main">
                <div className="dashboard-content">
                    <div className="dashboard-sidebar">
                        <TodoStats todos={todos} />
                        
                        <div className="filters">
                            <h3>Filter Todos</h3>
                            <div className="filter-buttons">
                                <button 
                                    className={filter === 'all' ? 'active' : ''}
                                    onClick={() => setFilter('all')}
                                >
                                    All ({todos.length})
                                </button>
                                <button 
                                    className={filter === 'active' ? 'active' : ''}
                                    onClick={() => setFilter('active')}
                                >
                                    Active ({todos.filter(t => !t.completed).length})
                                </button>
                                <button 
                                    className={filter === 'completed' ? 'active' : ''}
                                    onClick={() => setFilter('completed')}
                                >
                                    Completed ({todos.filter(t => t.completed).length})
                                </button>
                            </div>
                        </div>
                        
                        <div className="search-box">
                            <input
                                type="text"
                                placeholder="Search todos..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                            />
                        </div>
                    </div>
                    
                    <div className="dashboard-main-content">
                        <TodoForm 
                            onSubmit={handleAddTodo}
                            loading={actionLoading}
                        />
                        
                        <TodoList
                            todos={filteredTodos}
                            onToggle={handleToggleTodo}
                            onUpdate={handleUpdateTodo}
                            onDelete={handleDeleteTodo}
                            loading={actionLoading}
                        />
                        
                        {filteredTodos.length === 0 && todos.length > 0 && (
                            <div className="no-results">
                                <h3>No todos found</h3>
                                <p>Try adjusting your search or filter criteria</p>
                            </div>
                        )}
                        
                        {todos.length === 0 && (
                            <div className="empty-state">
                                <h3>No todos yet!</h3>
                                <p>Create your first todo above to get started</p>
                            </div>
                        )}
                    </div>
                </div>
            </main>
        </div>
    );
}

export default TodoDashboard;
```

**Todo Stats Component:**

```jsx
// components/TodoStats.js
import React from 'react';
import './TodoStats.css';

function TodoStats({ todos }) {
    const totalTodos = todos.length;
    const completedTodos = todos.filter(todo => todo.completed).length;
    const activeTodos = totalTodos - completedTodos;
    const completionRate = totalTodos > 0 ? (completedTodos / totalTodos) * 100 : 0;
    
    return (
        <div className="todo-stats">
            <h3>Your Progress</h3>
            
            <div className="stats-grid">
                <div className="stat-item">
                    <div className="stat-number">{totalTodos}</div>
                    <div className="stat-label">Total</div>
                </div>
                
                <div className="stat-item">
                    <div className="stat-number">{activeTodos}</div>
                    <div className="stat-label">Active</div>
                </div>
                
                <div className="stat-item">
                    <div className="stat-number">{completedTodos}</div>
                    <div className="stat-label">Completed</div>
                </div>
            </div>
            
            <div className="completion-rate">
                <div className="rate-label">
                    Completion Rate: {completionRate.toFixed(0)}%
                </div>
                <div className="progress-bar">
                    <div 
                        className="progress-fill"
                        style={{ width: `${completionRate}%` }}
                    ></div>
                </div>
            </div>
        </div>
    );
}

export default TodoStats;
```

---

### 4️⃣ Error Handling & UX (10 minutes)

**Global Error Boundary:**

```jsx
// components/ErrorBoundary.js
import React from 'react';

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null };
    }
    
    static getDerivedStateFromError(error) {
        return { hasError: true, error };
    }
    
    componentDidCatch(error, errorInfo) {
        console.error('Error caught by boundary:', error, errorInfo);
        // You can log the error to an error reporting service here
    }
    
    render() {
        if (this.state.hasError) {
            return (
                <div className="error-boundary">
                    <h1>Oops! Something went wrong</h1>
                    <p>We're sorry for the inconvenience. Please try refreshing the page.</p>
                    <button 
                        onClick={() => window.location.reload()}
                        className="retry-btn"
                    >
                        Refresh Page
                    </button>
                </div>
            );
        }
        
        return this.props.children;
    }
}

export default ErrorBoundary;
```

**Offline Detection:**

```jsx
// hooks/useOnline.js
import { useState, useEffect } from 'react';

function useOnline() {
    const [isOnline, setIsOnline] = useState(navigator.onLine);
    
    useEffect(() => {
        const handleOnline = () => setIsOnline(true);
        const handleOffline = () => setIsOnline(false);
        
        window.addEventListener('online', handleOnline);
        window.addEventListener('offline', handleOffline);
        
        return () => {
            window.removeEventListener('online', handleOnline);
            window.removeEventListener('offline', handleOffline);
        };
    }, []);
    
    return isOnline;
}

export default useOnline;

// Usage in components
function App() {
    const isOnline = useOnline();
    
    return (
        <div className="app">
            {!isOnline && (
                <div className="offline-banner">
                    You're offline. Some features may not work.
                </div>
            )}
            {/* Rest of your app */}
        </div>
    );
}
```

---

### 5️⃣ Deployment Preparation (5 minutes)

**Build Configuration:**

```json
// package.json scripts
{
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject",
    "build:prod": "REACT_APP_API_URL=https://your-api.herokuapp.com npm run build"
  }
}
```

**Deployment Checklist:**

```javascript
// Deployment preparation checklist:

// 1. Environment Variables
// ✅ Set REACT_APP_API_URL for production
// ✅ Configure CORS on backend for frontend domain

// 2. Performance Optimization
// ✅ Code splitting with React.lazy()
// ✅ Image optimization
// ✅ Bundle analysis

// 3. Security
// ✅ Remove console.logs from production
// ✅ Validate all inputs
// ✅ Implement proper authentication

// 4. Error Handling
// ✅ Error boundaries
// ✅ Graceful API error handling
// ✅ Loading states for all async operations

// 5. SEO & Accessibility
// ✅ Meta tags
// ✅ Alt text for images
// ✅ Proper ARIA labels
```

**Production App Component:**

```jsx
// App.js - Final production version
import React, { Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import ErrorBoundary from './components/ErrorBoundary';
import LoadingSpinner from './components/LoadingSpinner';
import ProtectedRoute from './components/ProtectedRoute';

// Lazy load components for better performance
const Login = React.lazy(() => import('./components/Login'));
const Register = React.lazy(() => import('./components/Register'));
const TodoDashboard = React.lazy(() => import('./components/TodoDashboard'));
const LandingPage = React.lazy(() => import('./components/LandingPage'));

function App() {
    return (
        <ErrorBoundary>
            <AuthProvider>
                <Router>
                    <div className="App">
                        <Suspense fallback={<LoadingSpinner />}>
                            <Routes>
                                <Route path="/" element={<LandingPage />} />
                                <Route path="/login" element={<Login />} />
                                <Route path="/register" element={<Register />} />
                                <Route 
                                    path="/dashboard" 
                                    element={
                                        <ProtectedRoute>
                                            <TodoDashboard />
                                        </ProtectedRoute>
                                    } 
                                />
                            </Routes>
                        </Suspense>
                    </div>
                </Router>
            </AuthProvider>
        </ErrorBoundary>
    );
}

export default App;
```

---

### 🏠 Final Project: Deploy Your Full-Stack App

**Task:** Deploy your complete todo application

```bash
# Frontend deployment (Netlify/Vercel)
1. Build the React app: npm run build
2. Deploy build folder to hosting service
3. Configure environment variables
4. Set up custom domain (optional)

# Backend deployment (Heroku/Railway)
1. Deploy Flask app to cloud platform
2. Configure production database
3. Set up environment variables
4. Update CORS settings for frontend domain

# Test the deployed application:
- User registration and login
- Todo CRUD operations
- Responsive design on mobile
- Error handling
- Loading states
```

---

### 🎉 Congratulations!

**You've Built a Complete Full-Stack Application!**

**What You've Learned in 30 Hours:**
- ✅ **Backend Development**: Python, Flask, SQLAlchemy, JWT Auth
- ✅ **Frontend Development**: HTML, CSS, JavaScript, React
- ✅ **Database Design**: Relational databases, migrations
- ✅ **API Development**: REST APIs, CRUD operations
- ✅ **State Management**: React Context, Redux Toolkit
- ✅ **Authentication**: JWT tokens, protected routes
- ✅ **Deployment**: Full-stack application deployment

**Your Tech Stack Mastery:**
```
Backend:     Python + Flask + SQLAlchemy + PostgreSQL
Frontend:    React + React Router + CSS Modules
Database:    PostgreSQL with proper relationships
API:         RESTful endpoints with authentication
State:       Context API + Custom hooks
Deployment:  Heroku + Netlify/Vercel
```

**Next Steps:**
1. **Add Advanced Features**: Real-time updates, file uploads, email notifications
2. **Learn Testing**: Unit tests, integration tests, E2E testing
3. **Performance Optimization**: Caching, lazy loading, code splitting
4. **Mobile Development**: React Native or Progressive Web App
5. **DevOps**: CI/CD pipelines, Docker, monitoring

**Keep Building!** 🚀

---

### 📝 Final Key Takeaways

✅ Full-stack development = Frontend + Backend + Database
✅ API integration = Connect React to Flask seamlessly
✅ Authentication flow = Secure user management
✅ Error handling = Graceful failure management
✅ Deployment = Share your apps with the world

**You're now a Full-Stack Developer! Go build amazing things!** 🎊

---


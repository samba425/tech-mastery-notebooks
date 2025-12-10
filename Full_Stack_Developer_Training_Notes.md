# Full Stack Developer Training & Interview Guide

## 📚 Complete Coverage - From Fundamentals to Deployment

---

## 📑 Table of Contents

### [Module 1: HTML Fundamentals (Days 1-6)](#module-1-html-fundamentals-days-1-6)
- [Day 1: Introduction to Web & HTML Basics](#day-1-introduction-to-web--html-basics)
- [Day 2: HTML Text Fundamentals](#day-2-html-text-fundamentals)
- [Day 3: HTML Links & Images](#day-3-html-links--images)
- [Day 4: HTML Lists & Tables](#day-4-html-lists--tables)
- [Day 5: HTML Forms - Part 1](#day-5-html-forms---part-1)
- [Day 6: HTML Forms - Part 2 & Semantic HTML](#day-6-html-forms---part-2--semantic-html)

### [Module 2: CSS Fundamentals (Days 7-11)](#module-2-css-fundamentals-days-7-11)
- [Day 7: CSS Introduction & Selectors](#day-7-css-introduction--selectors)
- [Day 8: CSS Box Model & Styling](#day-8-css-box-model--styling)
- [Day 9: CSS Flexbox](#day-9-css-flexbox)
- [Day 10: CSS Grid](#day-10-css-grid)
- [Day 11: Responsive Design & Media Queries](#day-11-responsive-design--media-queries)

### [Module 3: JavaScript Fundamentals (Days 13-16)](#module-3-javascript-fundamentals-days-13-16)
- [Day 13: JavaScript Basics](#day-13-javascript-basics)
- [Day 14: JavaScript Functions & Scope](#day-14-javascript-functions--scope)
- [Day 15: JavaScript Arrays & Objects](#day-15-javascript-arrays--objects)
- [Day 16: DOM Manipulation & Events](#day-16-dom-manipulation--events)

### [Module 4: React Basics (Days 18-19)](#module-4-react-basics-days-18-19)
- [Day 18: React Introduction & Components](#day-18-react-introduction--components)
- [Day 19: React State & Hooks](#day-19-react-state--hooks)

### [Module 5: Angular Basics (Days 20-21)](#module-5-angular-basics-days-20-21)
- [Day 20: Angular Introduction & Components](#day-20-angular-introduction--components)
- [Day 21: Angular Services & HTTP](#day-21-angular-services--http)

### [Module 6: Node.js Basics (Days 22-25)](#module-6-nodejs-basics-days-22-25)
- [Day 22: Node.js Introduction](#day-22-nodejs-introduction)
- [Day 23: Node.js File System & Modules](#day-23-nodejs-file-system--modules)
- [Day 24: Node.js HTTP Server](#day-24-nodejs-http-server)
- [Day 25: Building a Simple REST API](#day-25-building-a-simple-rest-api)

### [Module 7: Express.js (Days 26-30)](#module-7-expressjs-days-26-30)
- [Day 26: Express.js Introduction](#day-26-expressjs-introduction)
- [Day 27: Express Routing & Middleware](#day-27-express-routing--middleware)
- [Day 28: Express REST API](#day-28-express-rest-api)
- [Day 29: Express Error Handling](#day-29-express-error-handling)
- [Day 30: Express MVC Pattern](#day-30-express-mvc-pattern)

### [Module 8: TypeScript (Days 31-32)](#module-8-typescript-days-31-32)
- [Day 31: TypeScript Basics](#day-31-typescript-basics)
- [Day 32: TypeScript with Node.js & Express](#day-32-typescript-with-nodejs--express)

### [Module 9: Databases (Days 33-40)](#module-9-databases-days-33-40)
- [Day 33: MongoDB Basics](#day-33-mongodb-basics)
- [Day 34: Mongoose ODM](#day-34-mongoose-odm)
- [Day 35: PostgreSQL & SQL Basics](#day-35-postgresql--sql-basics)
- [Day 36: Database Design & Relationships](#day-36-database-design--relationships)

### [Module 10: Authentication & Security (Days 49-54)](#module-10-authentication--security-days-49-54)
- [Day 49: Authentication vs Authorization](#day-49-authentication-vs-authorization)
- [Day 50: JWT (JSON Web Tokens) Authentication](#day-50-jwt-json-web-tokens-authentication)
- [Day 51-53: Advanced Security Topics](#day-51-53-advanced-security-topics)
- [Day 54: Complete Project - Secure Task Manager API](#day-54-complete-project---secure-task-manager-api)

### [Module 11: Full-Stack Integration (Days 55-60)](#module-11-full-stack-integration-days-55-60)
- [Day 55: Full-Stack Project Structure & Organization](#day-55-full-stack-project-structure--organization)
- [Day 56: Connecting Frontend to Backend](#day-56-connecting-frontend-to-backend)
- [Day 57: Authentication UI & Protected Routes](#day-57-authentication-ui--protected-routes)
- [Day 58-59: Deployment](#day-58-59-deployment)
- [Day 60: Final Full-Stack Project Summary](#day-60-final-full-stack-project-summary)

### [🚀 Bootcamp Projects](#-bootcamp-projects)
- [Project 1: Responsive Portfolio Website](#project-1-responsive-portfolio-website)
- [Project 2: To-Do List App](#project-2-to-do-list-app)
- [Project 3: Weather App](#project-3-weather-app)

---

## Module 1: HTML Fundamentals (Days 1-6)

### Day 1: Introduction to Web & HTML Basics

#### 📖 What is Web Development?
Web development is the process of building websites and web applications that run in a web browser. Think of it like building a house:
- **HTML** = Structure (walls, rooms, doors)
- **CSS** = Decoration (paint, furniture, style)
- **JavaScript** = Functionality (lights, plumbing, electricity)

#### 📖 HTML Basics: Tags, Elements, Attributes

**What is HTML?**
HTML (HyperText Markup Language) is the skeleton of a website. It tells the browser what to display.

**Tags:** Tags are like containers wrapped in angle brackets `< >`
```html
<p>This is a paragraph</p>
```

**Elements:** An element includes the opening tag, content, and closing tag
```html
<h1>This is a heading element</h1>
```

**Attributes:** Extra information added to tags
```html
<img src="photo.jpg" alt="My Photo">
     ↑attribute name  ↑attribute value
```

#### 💡 Simple Example - Your First Webpage
```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Page</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>Welcome to my first webpage.</p>
    <p>This is <strong>exciting</strong>!</p>
</body>
</html>
```

**Explanation:**
- `<!DOCTYPE html>` - Tells browser this is an HTML5 document
- `<html>` - Root element, wraps everything
- `<head>` - Contains metadata (not visible on page)
- `<title>` - Shows in browser tab
- `<body>` - Everything visible on the page
- `<h1>` - Main heading (largest)
- `<p>` - Paragraph
- `<strong>` - Makes text bold

**Learning Resources:**
- [MDN HTML Introduction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)

**Hands-on Practice:**
- Create a "Hello World" webpage with at least 3 different HTML elements
- Include headings (`<h1>`, `<h2>`), paragraphs (`<p>`), and basic text formatting

**Interview Questions:**

1. **What is the difference between HTML elements and tags?**
   - **Answer:** A tag is the markup syntax (`<p>`), while an element includes the opening tag, content, and closing tag (`<p>Hello</p>`). Think of tags as the brackets and element as the complete package.

2. **What are semantic HTML elements?**
   - **Answer:** Semantic elements clearly describe their meaning to both the browser and developer. Examples: `<header>`, `<footer>`, `<article>`, `<nav>`. They tell you what the content is, unlike generic `<div>` tags.

3. **Explain the DOCTYPE declaration.**
   - **Answer:** `<!DOCTYPE html>` tells the browser which version of HTML the page is using. For HTML5, it's simply `<!DOCTYPE html>`. Without it, browsers may render pages incorrectly in "quirks mode".

---

### Day 2: HTML Text Fundamentals

#### 📖 Headings (h1-h6)
Headings organize your content like chapters in a book. There are 6 levels:
- `<h1>` - Most important (use only once per page, like a book title)
- `<h2>` - Major sections (like chapter titles)
- `<h3>` to `<h6>` - Subsections (smaller importance)

```html
<h1>My Website</h1>
<h2>About Me</h2>
<h3>My Background</h3>
<h3>My Skills</h3>
<h2>Contact</h2>
```

#### 📖 Paragraphs
Use `<p>` tags to create paragraphs of text. Each paragraph is a block of text with space above and below.

```html
<p>This is the first paragraph. It contains information about something.</p>
<p>This is a second paragraph. It's separated from the first one.</p>
```

#### 📖 Links (Anchor Tags)
Links take users to other pages. The `<a>` tag creates hyperlinks.

```html
<!-- Link to another website -->
<a href="https://google.com">Go to Google</a>

<!-- Link to another page in your site -->
<a href="about.html">About Us</a>

<!-- Link that opens in new tab -->
<a href="https://github.com" target="_blank">My GitHub</a>

<!-- Email link -->
<a href="mailto:hello@example.com">Email Me</a>
```

#### 📖 Images
Display pictures using the `<img>` tag. It's a self-closing tag (no closing tag needed).

```html
<img src="photo.jpg" alt="My photo" width="300">
```

**Important Attributes:**
- `src` - Path to the image file
- `alt` - Description for accessibility (shows if image fails to load)
- `width`/`height` - Size in pixels

#### 📖 Lists
Two types of lists:

**Unordered List (bullets):**
```html
<ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
</ul>
```
Output: • Coffee • Tea • Milk

**Ordered List (numbers):**
```html
<ol>
    <li>Wake up</li>
    <li>Brush teeth</li>
    <li>Have breakfast</li>
</ol>
```
Output: 1. Wake up 2. Brush teeth 3. Have breakfast

#### 💡 Complete Example - About Me Page
```html
<!DOCTYPE html>
<html>
<head>
    <title>About John Doe</title>
</head>
<body>
    <h1>About Me</h1>
    
    <img src="profile.jpg" alt="John's profile picture" width="200">
    
    <h2>Introduction</h2>
    <p>Hi! I'm John Doe, a web developer from New York.</p>
    <p>I love creating beautiful websites and learning new technologies.</p>
    
    <h2>My Hobbies</h2>
    <ul>
        <li>Coding</li>
        <li>Reading books</li>
        <li>Playing guitar</li>
        <li>Hiking</li>
    </ul>
    
    <h2>Connect With Me</h2>
    <p>Find me on social media:</p>
    <ul>
        <li><a href="https://github.com/johndoe" target="_blank">GitHub</a></li>
        <li><a href="https://linkedin.com/in/johndoe" target="_blank">LinkedIn</a></li>
        <li><a href="mailto:john@example.com">Email</a></li>
    </ul>
</body>
</html>
```

**Learning Resources:**
- [HTML Text Fundamentals](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals)

**Hands-on Practice:**
- Build a basic "About Me" page with:
  - Profile photo
  - Personal introduction paragraphs
  - List of hobbies
  - Links to social media profiles

**Interview Questions:**

1. **What's the difference between `<ol>` and `<ul>`?**
   - **Answer:** `<ol>` creates an ordered (numbered) list, like steps in a recipe. `<ul>` creates an unordered (bulleted) list, like a shopping list where order doesn't matter.

2. **How do you open a link in a new tab?**
   - **Answer:** Add `target="_blank"` attribute to the anchor tag: `<a href="url" target="_blank">Link</a>`. It's good practice to also add `rel="noopener noreferrer"` for security.

3. **What is the `alt` attribute in images and why is it important?**
   - **Answer:** The `alt` attribute provides alternative text for images. It's crucial for:
     - **Accessibility:** Screen readers read this text to visually impaired users
     - **SEO:** Search engines use it to understand image content
     - **Fallback:** Shows when image fails to load

---

### Day 3: Tables & Forms

#### 📖 HTML Tables
Tables organize data in rows and columns, like a spreadsheet.

**Table Structure:**
- `<table>` - Container for the table
- `<tr>` - Table Row
- `<th>` - Table Header (bold, centered)
- `<td>` - Table Data (regular cell)

#### 💡 Simple Table Example
```html
<table border="1">
    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
    </tr>
    <tr>
        <td>John</td>
        <td>25</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Sarah</td>
        <td>30</td>
        <td>London</td>
    </tr>
    <tr>
        <td>Mike</td>
        <td>28</td>
        <td>Paris</td>
    </tr>
</table>
```

**Result looks like:**
```
| Name  | Age | City      |
|-------|-----|-----------|
| John  | 25  | New York  |
| Sarah | 30  | London    |
| Mike  | 28  | Paris     |
```

#### 📖 HTML Forms
Forms collect user input. Think of it like a survey or application form.

**Basic Form Structure:**
```html
<form action="/submit" method="POST">
    <!-- Form inputs go here -->
    <button type="submit">Submit</button>
</form>
```

**Attributes:**
- `action` - Where to send the data (URL)
- `method` - How to send data (GET or POST)

#### 📖 Input Types
Different inputs for different data:

```html
<!-- Text Input -->
<label for="name">Name:</label>
<input type="text" id="name" name="name" placeholder="Enter your name">

<!-- Email Input (validates email format) -->
<label for="email">Email:</label>
<input type="email" id="email" name="email" placeholder="you@example.com">

<!-- Password Input (hides text) -->
<label for="password">Password:</label>
<input type="password" id="password" name="password">

<!-- Number Input -->
<label for="age">Age:</label>
<input type="number" id="age" name="age" min="18" max="100">

<!-- Date Input -->
<label for="birthday">Birthday:</label>
<input type="date" id="birthday" name="birthday">

<!-- Radio Buttons (choose one) -->
<p>Gender:</p>
<input type="radio" id="male" name="gender" value="male">
<label for="male">Male</label>
<input type="radio" id="female" name="gender" value="female">
<label for="female">Female</label>

<!-- Checkbox (select multiple) -->
<input type="checkbox" id="subscribe" name="subscribe">
<label for="subscribe">Subscribe to newsletter</label>

<!-- Dropdown/Select -->
<label for="country">Country:</label>
<select id="country" name="country">
    <option value="">Choose...</option>
    <option value="us">United States</option>
    <option value="uk">United Kingdom</option>
    <option value="ca">Canada</option>
</select>

<!-- Textarea (multi-line text) -->
<label for="message">Message:</label>
<textarea id="message" name="message" rows="4" cols="50"></textarea>
```

#### 💡 Complete Contact Form Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Form</h1>
    
    <form action="/submit-contact" method="POST">
        <!-- Name Field -->
        <label for="fullname">Full Name:</label><br>
        <input type="text" id="fullname" name="fullname" required><br><br>
        
        <!-- Email Field -->
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <!-- Phone Number -->
        <label for="phone">Phone:</label><br>
        <input type="tel" id="phone" name="phone"><br><br>
        
        <!-- Subject -->
        <label for="subject">Subject:</label><br>
        <select id="subject" name="subject">
            <option value="general">General Inquiry</option>
            <option value="support">Technical Support</option>
            <option value="feedback">Feedback</option>
        </select><br><br>
        
        <!-- Message -->
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" cols="40" required></textarea><br><br>
        
        <!-- Consent Checkbox -->
        <input type="checkbox" id="consent" name="consent" required>
        <label for="consent">I agree to the terms and conditions</label><br><br>
        
        <!-- Submit Button -->
        <button type="submit">Send Message</button>
        <button type="reset">Clear Form</button>
    </form>
</body>
</html>
```

**Learning Resources:**
- [MDN HTML Tables](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables)

**Hands-on Practice:**
- Create a contact form with:
  - Name field (text input)
  - Email field (email input)
  - Message field (textarea)
  - Submit button

**Interview Questions:**

1. **What are the different input types in HTML5?**
   - **Answer:** HTML5 introduced many input types:
     - `text` - Plain text
     - `email` - Email validation
     - `password` - Hidden text
     - `number` - Numeric input
     - `date`, `time`, `datetime-local` - Date/time pickers
     - `tel` - Phone number
     - `url` - Website URL
     - `search` - Search box
     - `color` - Color picker
     - `range` - Slider
     - `file` - File upload
     - `checkbox`, `radio` - Selection options

2. **Explain the difference between GET and POST methods in forms.**
   - **Answer:**
     - **GET:** Sends data in the URL (visible in address bar). Used for search queries, non-sensitive data. Limited data size. Example: `www.site.com/search?q=hello`
     - **POST:** Sends data in the request body (hidden from URL). Used for sensitive data like passwords, form submissions. No size limit. More secure.
     - **Simple Rule:** If you're searching or filtering → GET. If you're submitting or updating data → POST.

3. **What is the purpose of the `<label>` element?**
   - **Answer:** The `<label>` element:
     - Creates a clickable label for input fields (clicking label focuses the input)
     - Improves accessibility for screen readers
     - Should use the `for` attribute matching the input's `id`
     - Example: `<label for="email">Email:</label> <input type="email" id="email">`
     - When you click "Email:", the cursor jumps to the input field

---

### Day 4: Semantic HTML

#### 📖 What is Semantic HTML?
Semantic HTML uses tags that describe the **meaning** of the content, not just how it looks.

**Think of it this way:**
- `<div>` says "this is a container" (vague)
- `<header>` says "this is the website header" (specific and meaningful)

#### 📖 Why Use Semantic HTML?
1. **Better SEO** - Search engines understand your content better
2. **Accessibility** - Screen readers can navigate your site easily
3. **Maintainability** - Other developers understand your code quickly
4. **Clean Code** - More readable and organized

#### 📖 Common Semantic Elements

```html
<!-- HEADER: Top section of page/section -->
<header>
    <h1>My Website</h1>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </nav>
</header>

<!-- NAV: Navigation links -->
<nav>
    <a href="/">Home</a>
    <a href="/products">Products</a>
    <a href="/contact">Contact</a>
</nav>

<!-- MAIN: Main content of the page (use only once) -->
<main>
    <h1>Welcome to My Blog</h1>
    <!-- Main content here -->
</main>

<!-- ARTICLE: Independent, self-contained content -->
<article>
    <h2>Blog Post Title</h2>
    <p>Published on January 1, 2024</p>
    <p>This is the blog post content...</p>
</article>

<!-- SECTION: Thematic grouping of content -->
<section>
    <h2>Our Services</h2>
    <p>We offer the following services...</p>
</section>

<!-- ASIDE: Sidebar or related content -->
<aside>
    <h3>Related Posts</h3>
    <ul>
        <li><a href="#">Post 1</a></li>
        <li><a href="#">Post 2</a></li>
    </ul>
</aside>

<!-- FOOTER: Bottom section of page/section -->
<footer>
    <p>&copy; 2024 My Website. All rights reserved.</p>
    <p>Contact: info@mywebsite.com</p>
</footer>
```

#### 💡 Complete Semantic Page Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Blog</title>
</head>
<body>
    <!-- Page Header -->
    <header>
        <h1>John's Tech Blog</h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/blog">Blog</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content Area -->
    <main>
        <!-- Blog Post -->
        <article>
            <header>
                <h2>Getting Started with HTML</h2>
                <p>Posted on <time datetime="2024-01-15">January 15, 2024</time></p>
                <p>By John Doe</p>
            </header>
            
            <section>
                <h3>Introduction</h3>
                <p>HTML is the foundation of web development...</p>
            </section>
            
            <section>
                <h3>Basic Concepts</h3>
                <p>Let's explore the basic concepts...</p>
            </section>
            
            <footer>
                <p>Tags: HTML, Web Development, Tutorial</p>
            </footer>
        </article>

        <!-- Another Blog Post -->
        <article>
            <header>
                <h2>CSS Styling Tips</h2>
                <p>Posted on <time datetime="2024-01-10">January 10, 2024</time></p>
            </header>
            <p>Here are some CSS tips...</p>
        </article>
    </main>

    <!-- Sidebar -->
    <aside>
        <section>
            <h3>About the Author</h3>
            <p>John is a web developer with 5 years of experience.</p>
        </section>
        
        <section>
            <h3>Popular Posts</h3>
            <ul>
                <li><a href="#">JavaScript Basics</a></li>
                <li><a href="#">Responsive Design</a></li>
                <li><a href="#">CSS Grid Tutorial</a></li>
            </ul>
        </section>
    </aside>

    <!-- Page Footer -->
    <footer>
        <p>&copy; 2024 John's Tech Blog</p>
        <p>Follow me: 
            <a href="#">Twitter</a> | 
            <a href="#">GitHub</a> | 
            <a href="#">LinkedIn</a>
        </p>
    </footer>
</body>
</html>
```

#### 📖 Semantic vs Non-Semantic Comparison

**❌ Non-Semantic (Bad):**
```html
<div class="header">
    <div class="nav">...</div>
</div>
<div class="content">
    <div class="post">...</div>
</div>
<div class="footer">...</div>
```

**✅ Semantic (Good):**
```html
<header>
    <nav>...</nav>
</header>
<main>
    <article>...</article>
</main>
<footer>...</footer>
```

**Learning Resources:**
- [MDN Semantic HTML](https://developer.mozilla.org/en-US/docs/Glossary/Semantics#semantics_in_html)

**Hands-on Practice:**
- Convert your profile page to use semantic HTML
- Rebuild "About Me" page with proper semantic structure

**Interview Questions:**

1. **What is semantic HTML and why is it important?**
   - **Answer:** Semantic HTML uses meaningful tags that describe the content's purpose (like `<article>`, `<nav>`, `<header>`) instead of generic ones (like `<div>`, `<span>`).
   - **Why Important:**
     - **SEO:** Search engines better understand your content structure
     - **Accessibility:** Screen readers can navigate sections easily
     - **Maintainability:** Code is self-documenting and easier to read
     - **Future-proof:** Browsers can apply default styling and features

2. **Difference between `<div>` and `<section>`?**
   - **Answer:**
     - **`<div>`:** Generic container with no semantic meaning. Use for styling/layout purposes only.
     - **`<section>`:** Represents a thematic grouping of content, typically with a heading. Has semantic meaning.
   - **Example:**
     - Use `<div>` for: wrapper containers, layout grids
     - Use `<section>` for: chapters, tabs, numbered sections of content

3. **When would you use `<article>` vs `<section>`?**
   - **Answer:**
     - **`<article>`:** Use for independent, self-contained content that could be distributed separately (blog post, news article, forum post, comment).
     - **`<section>`:** Use for grouping related content within a page (chapters of an article, tabs in a product page).
   - **Test:** If you can syndicate (reuse) the content independently → use `<article>`
   - **Example:**
     ```html
     <article> <!-- Blog post -->
         <section> <!-- Introduction section -->
         <section> <!-- Main content section -->
         <section> <!-- Conclusion section -->
     </article>
     ```

---

### Day 5: Accessibility (a11y)

#### 📖 What is Web Accessibility?
Web accessibility means making websites usable by **everyone**, including people with disabilities:
- Visual impairments (blind, low vision)
- Hearing impairments
- Motor disabilities
- Cognitive disabilities

**Remember:** Good accessibility = Good user experience for everyone!

#### 📖 Alt Text for Images
Alt text describes images for people who can't see them.

```html
<!-- Good: Descriptive alt text -->
<img src="cat.jpg" alt="Orange tabby cat sleeping on a blue couch">

<!-- Bad: Vague or missing alt -->
<img src="cat.jpg" alt="image">
<img src="cat.jpg" alt="">

<!-- Decorative images: Empty alt -->
<img src="decorative-line.jpg" alt="" role="presentation">
```

**Tips for Good Alt Text:**
- Describe what's in the image
- Keep it concise (under 125 characters)
- Don't start with "image of" or "picture of"
- For decorative images, use empty alt: `alt=""`

#### 📖 Labels for Form Inputs
Always connect labels to inputs so screen readers can announce what each field is for.

```html
<!-- ✅ Good: Label connected to input -->
<label for="email">Email Address:</label>
<input type="email" id="email" name="email">

<!-- ❌ Bad: No connection -->
<label>Email Address:</label>
<input type="email" name="email">

<!-- ✅ Alternative: Wrap input in label -->
<label>
    Email Address:
    <input type="email" name="email">
</label>
```

#### 📖 ARIA (Accessible Rich Internet Applications)
ARIA adds extra information for screen readers when HTML alone isn't enough.

**Common ARIA Attributes:**

```html
<!-- Roles: Define what something is -->
<div role="navigation">
    <a href="/">Home</a>
    <a href="/about">About</a>
</div>

<!-- Better: Use semantic HTML instead -->
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
</nav>

<!-- aria-label: Provides a label when none is visible -->
<button aria-label="Close menu">
    <span>×</span>
</button>

<!-- aria-labelledby: Points to another element for the label -->
<h2 id="modal-title">Confirm Deletion</h2>
<div role="dialog" aria-labelledby="modal-title">
    <p>Are you sure?</p>
</div>

<!-- aria-describedby: Provides additional description -->
<label for="password">Password:</label>
<input type="password" id="password" aria-describedby="pwd-help">
<span id="pwd-help">Must be at least 8 characters</span>

<!-- aria-hidden: Hides from screen readers -->
<span aria-hidden="true">👍</span>
<span class="sr-only">Thumbs up</span>
```

**ARIA Rule #1:** Don't use ARIA if semantic HTML works!
- ❌ `<div role="button">` 
- ✅ `<button>`

#### 📖 Keyboard Navigation
Many users navigate without a mouse. Test your site using only the keyboard!

**Key Keyboard Behaviors:**
- `Tab` - Move to next interactive element
- `Shift + Tab` - Move to previous element
- `Enter` - Activate buttons/links
- `Space` - Check checkboxes, press buttons
- `Arrow keys` - Navigate dropdowns, radio buttons

```html
<!-- Ensure focusable elements are keyboard accessible -->
<button>I'm focusable!</button>
<a href="/page">I'm focusable!</a>

<!-- ❌ Bad: div is not keyboard accessible -->
<div onclick="doSomething()">Click me</div>

<!-- ✅ Good: button is keyboard accessible -->
<button onclick="doSomething()">Click me</button>

<!-- Custom tab order (avoid if possible) -->
<input type="text" tabindex="1">
<input type="text" tabindex="2">
<input type="text" tabindex="3">
```

#### 💡 Accessible Form Example
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessible Contact Form</title>
</head>
<body>
    <main>
        <h1>Contact Us</h1>
        
        <form action="/submit" method="POST">
            <!-- Name field with label -->
            <label for="name">Full Name: <span aria-label="required">*</span></label>
            <input 
                type="text" 
                id="name" 
                name="name" 
                required 
                aria-required="true"
                aria-describedby="name-help"
            >
            <span id="name-help">Enter your first and last name</span>
            
            <!-- Email field -->
            <label for="email">Email: <span aria-label="required">*</span></label>
            <input 
                type="email" 
                id="email" 
                name="email" 
                required 
                aria-required="true"
            >
            
            <!-- Message field -->
            <label for="message">Message: <span aria-label="required">*</span></label>
            <textarea 
                id="message" 
                name="message" 
                rows="5" 
                required 
                aria-required="true"
            ></textarea>
            
            <!-- Submit button -->
            <button type="submit">Send Message</button>
        </form>
    </main>
</body>
</html>
```

#### 📖 Screen Reader Considerations

**Best Practices:**
1. Use proper heading hierarchy (h1 → h2 → h3)
2. Provide skip links to main content
3. Ensure color is not the only way to convey information
4. Use descriptive link text

```html
<!-- ❌ Bad: Unclear link text -->
<a href="/article">Click here</a>
<a href="/article">Read more</a>

<!-- ✅ Good: Descriptive link text -->
<a href="/article">Read the complete guide to web accessibility</a>

<!-- Skip to main content link -->
<a href="#main-content" class="skip-link">Skip to main content</a>
<main id="main-content">
    <!-- Content here -->
</main>

<!-- Proper heading structure -->
<h1>Website Title</h1>
    <h2>Section 1</h2>
        <h3>Subsection 1.1</h3>
        <h3>Subsection 1.2</h3>
    <h2>Section 2</h2>
```

**Learning Resources:**
- [MDN Web Accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility)

**Hands-on Practice:**
- Add accessibility features to your portfolio:
  - Proper alt attributes for all images
  - Labels for all form inputs
  - Basic ARIA roles where appropriate
  - Ensure keyboard navigation works

**Interview Questions:**

1. **What is ARIA and when should you use it?**
   - **Answer:** ARIA (Accessible Rich Internet Applications) provides extra attributes to make web content more accessible to people with disabilities.
   - **When to use:**
     - When semantic HTML isn't enough (dynamic content, custom widgets)
     - For complex interactions (modals, tabs, dropdown menus)
     - To provide additional context for screen readers
   - **Golden Rule:** Don't use ARIA if native HTML works. Always prefer `<button>` over `<div role="button">`

2. **How do you make a website accessible for screen readers?**
   - **Answer:**
     - Use semantic HTML (`<nav>`, `<main>`, `<header>`)
     - Provide alt text for all meaningful images
     - Connect labels to form inputs
     - Use proper heading hierarchy (h1-h6)
     - Add ARIA attributes when needed
     - Ensure keyboard navigation works
     - Use descriptive link text
     - Test with actual screen readers (NVDA, JAWS, VoiceOver)

3. **What is WCAG and why is it important?**
   - **Answer:** WCAG (Web Content Accessibility Guidelines) are international standards for web accessibility created by W3C.
   - **4 Principles (POUR):**
     - **P**erceivable - Users can see or hear content
     - **O**perable - Users can navigate using keyboard/mouse
     - **U**nderstandable - Content is clear and predictable
     - **R**obust - Works with assistive technologies
   - **Why Important:**
     - Legal requirement in many countries
     - Expands your audience (15% of world has disabilities)
     - Improves SEO and usability for everyone
     - Shows social responsibility

---

### Day 6: Mini Project - Portfolio Website
**Project:** Build a Simple Portfolio Webpage

**Requirements:**
- Use all HTML concepts learned
- Include:
  - Semantic structure (header, main, footer)
  - Personal information section
  - Skills list
  - Project showcase (can be placeholder)
  - Contact form
  - Proper accessibility features
- No CSS required yet - focus on HTML structure

---

## Module 2: CSS Fundamentals (Days 7-12)

### Day 7: CSS Display Types & Positioning

#### 📖 What is CSS?
CSS (Cascading Style Sheets) controls how HTML looks - colors, fonts, layouts, spacing, etc.

**How to Add CSS:**
```html
<!-- 1. Inline CSS (not recommended) -->
<p style="color: red;">Red text</p>

<!-- 2. Internal CSS (in <head>) -->
<style>
    p { color: blue; }
</style>

<!-- 3. External CSS (best practice) -->
<link rel="stylesheet" href="styles.css">
```

#### 📖 CSS Display Properties
Every HTML element has a default display type. Understanding this is crucial!

**1. display: block**
- Takes full width available
- Starts on a new line
- Can set width and height
- Examples: `<div>`, `<p>`, `<h1>`, `<section>`

```html
<style>
    .box {
        display: block;
        width: 200px;
        height: 100px;
        background: lightblue;
        margin: 10px 0;
    }
</style>

<div class="box">Box 1</div>
<div class="box">Box 2</div>
<!-- Each box on its own line -->
```

**2. display: inline**
- Only takes width it needs
- Stays on same line with other inline elements
- Cannot set width or height
- Examples: `<span>`, `<a>`, `<strong>`, `<img>`

```html
<style>
    .highlight {
        display: inline;
        background: yellow;
    }
</style>

<p>This is <span class="highlight">highlighted text</span> inline.</p>
```

**3. display: inline-block**
- Best of both worlds!
- Stays on same line (like inline)
- Can set width and height (like block)

```html
<style>
    .card {
        display: inline-block;
        width: 150px;
        height: 200px;
        background: lightgreen;
        margin: 10px;
    }
</style>

<div class="card">Card 1</div>
<div class="card">Card 2</div>
<div class="card">Card 3</div>
<!-- All three cards on same line -->
```

**4. display: none**
- Completely removes element from page (no space)
- Element doesn't take any room

```html
<style>
    .hidden {
        display: none;
    }
</style>

<p>This is visible</p>
<p class="hidden">This is hidden</p>
<p>This is also visible</p>
```

#### 📖 CSS Position Properties

**1. position: static** (default)
- Normal document flow
- Top, right, bottom, left have no effect

```css
.box {
    position: static; /* default, rarely specified */
}
```

**2. position: relative**
- Positioned relative to its normal position
- Other elements not affected
- Creates positioning context for absolute children

```html
<style>
    .box {
        position: relative;
        top: 20px;    /* Moves 20px down from normal position */
        left: 30px;   /* Moves 30px right from normal position */
        background: lightcoral;
        width: 100px;
        height: 100px;
    }
</style>

<div class="box">I'm shifted!</div>
```

**3. position: absolute**
- Removed from normal flow
- Positioned relative to nearest positioned ancestor (or body)
- Other elements act like it doesn't exist

```html
<style>
    .container {
        position: relative; /* Creates positioning context */
        width: 300px;
        height: 200px;
        background: lightgray;
    }
    
    .badge {
        position: absolute;
        top: 10px;      /* 10px from top of container */
        right: 10px;    /* 10px from right of container */
        background: red;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
    }
</style>

<div class="container">
    <div class="badge">NEW</div>
    <p>Container content</p>
</div>
```

**4. position: fixed**
- Fixed to viewport (browser window)
- Stays in same place even when scrolling
- Great for navigation bars, chat widgets

```html
<style>
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: navy;
        color: white;
        padding: 15px;
        z-index: 1000;
    }
    
    .content {
        margin-top: 60px; /* Space for fixed navbar */
    }
</style>

<nav class="navbar">Fixed Navigation Bar</nav>
<div class="content">
    <!-- Page content -->
</div>
```

**5. position: sticky**
- Hybrid of relative and fixed
- Acts relative until scroll threshold, then becomes fixed
- Perfect for table headers

```html
<style>
    .sticky-header {
        position: sticky;
        top: 0;
        background: gold;
        padding: 10px;
    }
</style>

<div class="sticky-header">I stick to top when scrolling!</div>
<div style="height: 2000px;">Scroll down...</div>
```

#### 📖 Z-Index and Stacking Context
Z-index controls which element appears on top when they overlap (like layers in Photoshop).

```html
<style>
    .box {
        position: absolute;
        width: 100px;
        height: 100px;
    }
    
    .red {
        background: red;
        top: 50px;
        left: 50px;
        z-index: 1;
    }
    
    .blue {
        background: blue;
        top: 80px;
        left: 80px;
        z-index: 2; /* Appears on top */
    }
    
    .green {
        background: green;
        top: 110px;
        left: 110px;
        z-index: 3; /* Appears on top of both */
    }
</style>

<div class="box red"></div>
<div class="box blue"></div>
<div class="box green"></div>
```

**Z-Index Rules:**
- Only works on positioned elements (not static)
- Higher number = on top
- Default z-index is auto (0)

#### 💡 Complete Hero Banner Example
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        .hero {
            position: relative;
            width: 100%;
            height: 500px;
            background-image: url('hero-bg.jpg');
            background-size: cover;
            background-position: center;
        }
        
        /* Dark overlay */
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1;
        }
        
        .hero-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
            z-index: 2;
        }
        
        .hero-content h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .hero-content p {
            font-size: 20px;
            margin-bottom: 30px;
        }
        
        .cta-button {
            position: absolute;
            bottom: 30px;
            right: 30px;
            padding: 15px 30px;
            background: #ff6b6b;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            z-index: 2;
        }
        
        .cta-button:hover {
            background: #ff5252;
        }
    </style>
</head>
<body>
    <div class="hero">
        <div class="hero-content">
            <h1>Welcome to My Website</h1>
            <p>Building amazing web experiences</p>
        </div>
        <a href="#learn-more" class="cta-button">Learn More</a>
    </div>
</body>
</html>
```

**Learning Resources:**
- [CSS Tricks - Position](https://css-tricks.com/almanac/properties/p/position/)

**Hands-on Practice:**
- Create a hero banner with:
  - Background image
  - Centered text using positioning
  - "Learn More" button positioned at bottom right corner

**Interview Questions:**

1. **Explain the difference between relative and absolute positioning.**
   - **Answer:**
     - **Relative:** Positioned relative to its normal position. The element still takes up space in the document flow. Use `top`, `left` to shift it, but other elements act like it's in its original spot.
     - **Absolute:** Positioned relative to the nearest positioned ancestor (or `<body>` if none). Removed from normal flow—other elements ignore it. Think of it as "floating" over the page.
   - **Example:** Use relative for small adjustments. Use absolute for overlays, badges, tooltips.

2. **What is the difference between display: none and visibility: hidden?**
   - **Answer:**
     - **`display: none`:** Completely removes element from layout. Takes up NO space. Other elements move up to fill the gap.
     - **`visibility: hidden`:** Hides element but keeps its space. Element is invisible but still occupies room.
   - **Think of it:** `display: none` = not in the room. `visibility: hidden` = invisible person still taking up a chair.

3. **How does z-index work?**
   - **Answer:** Z-index controls stacking order of overlapping elements (which appears on top).
     - Only works on positioned elements (`relative`, `absolute`, `fixed`, `sticky`)
     - Higher number = closer to user (on top)
     - Default is `auto` (effectively 0)
     - Creates stacking contexts (parent with z-index creates new context for children)
   - **Example:** Modal overlay (z-index: 1000) appears over page content (z-index: 1)

---

### Day 8: Flexbox

#### 📖 What is Flexbox?
Flexbox (Flexible Box Layout) is a CSS layout method designed for arranging items in rows or columns. It makes responsive layouts easy!

**Think of Flexbox like organizing books on a shelf:**
- You decide if they go left-to-right or stack vertically
- You control spacing between them
- You align them to top, bottom, or center

#### 📖 Flex Container vs Flex Items

```html
<div class="container">  <!-- Flex Container -->
    <div class="item">1</div>  <!-- Flex Item -->
    <div class="item">2</div>  <!-- Flex Item -->
    <div class="item">3</div>  <!-- Flex Item -->
</div>
```

```css
.container {
    display: flex; /* Creates flex container */
}
```

#### 📖 Flex Container Properties

**1. flex-direction** - Controls the main axis

```css
/* Horizontal (default) */
.container {
    display: flex;
    flex-direction: row; /* Items go left to right → → → */
}

/* Horizontal reverse */
.container {
    flex-direction: row-reverse; /* Items go right to left ← ← ← */
}

/* Vertical */
.container {
    flex-direction: column; /* Items stack top to bottom ↓ ↓ ↓ */
}

/* Vertical reverse */
.container {
    flex-direction: column-reverse; /* Items stack bottom to top ↑ ↑ ↑ */
}
```

**2. justify-content** - Aligns items along MAIN axis (horizontal if row, vertical if column)

```html
<style>
    .container {
        display: flex;
        border: 2px solid black;
        height: 200px;
        gap: 10px;
    }
    
    .item {
        width: 80px;
        height: 80px;
        background: lightblue;
    }
    
    /* Different justify-content values */
    .start { justify-content: flex-start; }    /* Items at start ◼◼◼______ */
    .end { justify-content: flex-end; }        /* Items at end ______◼◼◼ */
    .center { justify-content: center; }       /* Items in center ___◼◼◼___ */
    .between { justify-content: space-between; } /* ◼___◼___◼ */
    .around { justify-content: space-around; }   /* _◼__◼__◼_ */
    .evenly { justify-content: space-evenly; }   /* _◼_◼_◼_ */
</style>
```

**3. align-items** - Aligns items along CROSS axis (vertical if row, horizontal if column)

```css
.container {
    display: flex;
    align-items: flex-start;   /* Items at top */
    align-items: flex-end;     /* Items at bottom */
    align-items: center;       /* Items in middle (vertical centering!) */
    align-items: stretch;      /* Items stretch to fill (default) */
    align-items: baseline;     /* Align text baselines */
}
```

**4. flex-wrap** - Controls wrapping to next line

```css
.container {
    display: flex;
    flex-wrap: nowrap;  /* All items on one line (default) */
    flex-wrap: wrap;    /* Items wrap to next line */
    flex-wrap: wrap-reverse; /* Wrap in reverse */
}
```

#### 📖 Flex Item Properties

**1. flex-grow** - How much item should grow if there's extra space

```css
.item {
    flex-grow: 0; /* Don't grow (default) */
    flex-grow: 1; /* Grow equally with others */
    flex-grow: 2; /* Grow twice as much as flex-grow: 1 */
}
```

**2. flex-shrink** - How much item should shrink if space is tight

```css
.item {
    flex-shrink: 1; /* Can shrink (default) */
    flex-shrink: 0; /* Won't shrink */
}
```

**3. flex-basis** - Initial size before growing/shrinking

```css
.item {
    flex-basis: 200px; /* Start at 200px width */
    flex-basis: 0;     /* No initial size */
    flex-basis: auto;  /* Use content size (default) */
}
```

**4. flex shorthand** - Combines grow, shrink, and basis

```css
.item {
    flex: 1;          /* Same as flex: 1 1 0 */
    flex: 0 1 auto;   /* Default value */
    flex: 2 1 200px;  /* grow: 2, shrink: 1, basis: 200px */
}
```

#### 💡 Practical Examples

**Example 1: Centering Content (Holy Grail of CSS!)**
```html
<style>
    .center-box {
        display: flex;
        justify-content: center; /* Horizontal center */
        align-items: center;     /* Vertical center */
        height: 300px;
        background: lightgray;
    }
    
    .content {
        padding: 20px;
        background: white;
        border-radius: 10px;
    }
</style>

<div class="center-box">
    <div class="content">I'm perfectly centered!</div>
</div>
```

**Example 2: Responsive Navigation Bar**
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            background: #333;
            color: white;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
        }
        
        .nav-links {
            display: flex;
            gap: 30px;
            list-style: none;
        }
        
        .nav-links a {
            color: white;
            text-decoration: none;
        }
        
        .nav-links a:hover {
            color: #ffd700;
        }
        
        /* Mobile responsive */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                gap: 20px;
            }
            
            .nav-links {
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="logo">MyWebsite</div>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </nav>
</body>
</html>
```

**Example 3: Pricing Cards**
```html
<style>
    .pricing-container {
        display: flex;
        gap: 20px;
        padding: 40px;
        flex-wrap: wrap;
        justify-content: center;
    }
    
    .card {
        flex: 1 1 300px; /* Grow, shrink, min 300px */
        max-width: 350px;
        padding: 30px;
        border: 2px solid #ddd;
        border-radius: 10px;
        text-align: center;
    }
    
    .card h3 {
        font-size: 24px;
        margin-bottom: 10px;
    }
    
    .price {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
        margin: 20px 0;
    }
    
    .features {
        list-style: none;
        margin: 20px 0;
    }
    
    .features li {
        padding: 10px 0;
        border-bottom: 1px solid #eee;
    }
    
    .button {
        display: inline-block;
        padding: 12px 30px;
        background: #4CAF50;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        margin-top: 20px;
    }
</style>

<div class="pricing-container">
    <div class="card">
        <h3>Basic</h3>
        <div class="price">$9/mo</div>
        <ul class="features">
            <li>5 Projects</li>
            <li>5GB Storage</li>
            <li>Email Support</li>
        </ul>
        <a href="#" class="button">Choose Plan</a>
    </div>
    
    <div class="card">
        <h3>Pro</h3>
        <div class="price">$29/mo</div>
        <ul class="features">
            <li>50 Projects</li>
            <li>50GB Storage</li>
            <li>Priority Support</li>
            <li>Custom Domain</li>
        </ul>
        <a href="#" class="button">Choose Plan</a>
    </div>
    
    <div class="card">
        <h3>Enterprise</h3>
        <div class="price">$99/mo</div>
        <ul class="features">
            <li>Unlimited Projects</li>
            <li>500GB Storage</li>
            <li>24/7 Phone Support</li>
            <li>Custom Domain</li>
            <li>Advanced Analytics</li>
        </ul>
        <a href="#" class="button">Choose Plan</a>
    </div>
</div>
```

**Learning Resources:**
- [CSS Tricks - Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

**Hands-on Practice:**
- Build a responsive navbar using Flexbox
- Create a pricing section with 3 columns that:
  - Display horizontally on desktop
  - Stack vertically on mobile

**Interview Questions:**

1. **What is the difference between justify-content and align-items?**
   - **Answer:**
     - **justify-content:** Aligns items along the **main axis**
       - If `flex-direction: row` → controls horizontal alignment
       - If `flex-direction: column` → controls vertical alignment
     - **align-items:** Aligns items along the **cross axis** (perpendicular to main)
       - If `flex-direction: row` → controls vertical alignment
       - If `flex-direction: column` → controls horizontal alignment
   - **Easy Memory Trick:**
     - **justify-content** = spacing BETWEEN items
     - **align-items** = alignment of individual items

2. **Explain flex-grow, flex-shrink, and flex-basis.**
   - **Answer:**
     - **flex-grow:** How much an item should grow relative to others when there's extra space
       - `flex-grow: 0` = don't grow (default)
       - `flex-grow: 1` = grow equally with other flex-grow: 1 items
       - `flex-grow: 2` = grow twice as much as flex-grow: 1 items
     - **flex-shrink:** How much an item should shrink when space is limited
       - `flex-shrink: 1` = can shrink (default)
       - `flex-shrink: 0` = never shrink
     - **flex-basis:** The initial size before growing or shrinking
       - `flex-basis: 200px` = start at 200px
       - `flex-basis: 0` = start with no size
       - `flex-basis: auto` = use content size (default)

3. **How do you center an element using Flexbox?**
   - **Answer:** Use both `justify-content: center` and `align-items: center` on the parent container:
     ```css
     .container {
         display: flex;
         justify-content: center; /* Horizontal center */
         align-items: center;     /* Vertical center */
         height: 100vh;           /* Full viewport height */
     }
     ```
   - This is the **easiest way** to center anything in CSS!

---

### Day 9: CSS Grid

#### 📖 What is CSS Grid?
CSS Grid is a powerful 2-dimensional layout system (rows AND columns). Think of it like creating a spreadsheet or table for your layout!

**Flexbox vs Grid:**
- **Flexbox** = 1D (one direction: row OR column) - great for navigation bars, cards in a row
- **Grid** = 2D (both directions: rows AND columns) - great for page layouts, photo galleries

#### 📖 Grid Basics

```html
<div class="container">  <!-- Grid Container -->
    <div class="item">1</div>  <!-- Grid Item -->
    <div class="item">2</div>
    <div class="item">3</div>
    <div class="item">4</div>
</div>
```

```css
.container {
    display: grid;  /* Creates grid container */
}
```

#### 📖 Grid Container Properties

**1. grid-template-columns** - Define columns

```css
.container {
    display: grid;
    
    /* 3 columns of equal width */
    grid-template-columns: 200px 200px 200px;
    
    /* 3 columns with different widths */
    grid-template-columns: 100px 200px 300px;
    
    /* 3 equal columns using fr (fraction) */
    grid-template-columns: 1fr 1fr 1fr;
    
    /* Shorthand for equal columns */
    grid-template-columns: repeat(3, 1fr);
    
    /* Mix units */
    grid-template-columns: 200px 1fr 2fr;
    /* First: 200px, Second: 1 part, Third: 2 parts of remaining space */
}
```

**2. grid-template-rows** - Define rows

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    
    /* 2 rows with fixed heights */
    grid-template-rows: 100px 200px;
    
    /* Auto height based on content */
    grid-template-rows: auto auto;
    
    /* Mix */
    grid-template-rows: 100px auto 100px;
}
```

**3. gap** - Space between items

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    
    /* Both row and column gap */
    gap: 20px;
    
    /* Different gaps */
    gap: 20px 10px; /* row gap, column gap */
    
    /* Old syntax (still works) */
    grid-gap: 20px;
    row-gap: 20px;
    column-gap: 10px;
}
```

#### 💡 Simple Grid Example

```html
<style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        padding: 20px;
    }
    
    .grid-item {
        background: lightblue;
        padding: 20px;
        text-align: center;
        border-radius: 5px;
    }
</style>

<div class="grid-container">
    <div class="grid-item">1</div>
    <div class="grid-item">2</div>
    <div class="grid-item">3</div>
    <div class="grid-item">4</div>
    <div class="grid-item">5</div>
    <div class="grid-item">6</div>
</div>

<!-- Creates 2 rows × 3 columns automatically -->
```

#### 📖 Grid Item Properties

**Spanning Multiple Columns/Rows:**

```css
.item {
    /* Span across 2 columns */
    grid-column: span 2;
    
    /* Span from column line 1 to 3 */
    grid-column: 1 / 3;
    
    /* Span across 2 rows */
    grid-row: span 2;
    
    /* Span from row line 1 to 3 */
    grid-row: 1 / 3;
}
```

#### 💡 Advanced Grid Example

```html
<style>
    .advanced-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-template-rows: repeat(3, 200px);
        gap: 15px;
        padding: 20px;
    }
    
    .item {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
    }
    
    /* Make specific items span multiple cells */
    .item1 {
        grid-column: span 2; /* Takes 2 columns */
        grid-row: span 2;    /* Takes 2 rows */
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .item5 {
        grid-column: span 2; /* Takes 2 columns */
    }
</style>

<div class="advanced-grid">
    <div class="item item1">1</div>
    <div class="item">2</div>
    <div class="item">3</div>
    <div class="item">4</div>
    <div class="item item5">5</div>
    <div class="item">6</div>
    <div class="item">7</div>
</div>
```

#### 📖 Grid Template Areas - Named Grid Sections

This is super powerful for page layouts!

```html
<style>
    .page-layout {
        display: grid;
        grid-template-areas:
            "header header header"
            "sidebar content content"
            "footer footer footer";
        grid-template-columns: 200px 1fr 1fr;
        grid-template-rows: 100px 1fr 80px;
        gap: 20px;
        height: 100vh;
        padding: 20px;
    }
    
    .header {
        grid-area: header;
        background: #667eea;
    }
    
    .sidebar {
        grid-area: sidebar;
        background: #f093fb;
    }
    
    .content {
        grid-area: content;
        background: #4facfe;
    }
    
    .footer {
        grid-area: footer;
        background: #43e97b;
    }
    
    .header, .sidebar, .content, .footer {
        color: white;
        padding: 20px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }
</style>

<div class="page-layout">
    <div class="header">HEADER</div>
    <div class="sidebar">SIDEBAR</div>
    <div class="content">MAIN CONTENT</div>
    <div class="footer">FOOTER</div>
</div>
```

#### 💡 Photo Gallery Example

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            padding: 40px;
            background: #f5f5f5;
        }
        
        h1 {
            text-align: center;
            margin-bottom: 40px;
            color: #333;
        }
        
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        
        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .gallery-item:hover {
            transform: translateY(-10px);
            box-shadow: 0 12px 20px rgba(0,0,0,0.2);
        }
        
        .gallery-item img {
            width: 100%;
            height: 300px;
            object-fit: cover;
            display: block;
        }
        
        .caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 15px;
            transform: translateY(100%);
            transition: transform 0.3s ease;
        }
        
        .gallery-item:hover .caption {
            transform: translateY(0);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .gallery {
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 10px;
            }
            
            .gallery-item img {
                height: 200px;
            }
        }
    </style>
</head>
<body>
    <h1>My Photo Gallery</h1>
    
    <div class="gallery">
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=1" alt="Photo 1">
            <div class="caption">Beautiful Sunset</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=2" alt="Photo 2">
            <div class="caption">Mountain View</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=3" alt="Photo 3">
            <div class="caption">Ocean Waves</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=4" alt="Photo 4">
            <div class="caption">City Lights</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=5" alt="Photo 5">
            <div class="caption">Forest Path</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=6" alt="Photo 6">
            <div class="caption">Desert Dunes</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=7" alt="Photo 7">
            <div class="caption">Aurora Borealis</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=8" alt="Photo 8">
            <div class="caption">Snowy Mountains</div>
        </div>
        <div class="gallery-item">
            <img src="https://picsum.photos/400/300?random=9" alt="Photo 9">
            <div class="caption">Tropical Beach</div>
        </div>
    </div>
</body>
</html>
```

#### 📖 Responsive Grid with auto-fit/auto-fill

```css
.container {
    display: grid;
    
    /* Automatically creates columns that fit, minimum 250px */
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

/* 
auto-fit: Stretches items to fill available space
auto-fill: Creates empty tracks even if no items
*/
```

**Learning Resources:**
- [CSS Tricks - Grid Guide](https://css-tricks.com/snippets/css/complete-guide-grid/)

**Hands-on Practice:**
- Design a gallery page with:
  - At least 9 images arranged in CSS Grid
  - Hover effects on images
  - Captions below each image
  - Responsive layout

**Interview Questions:**

1. **When would you use CSS Grid over Flexbox?**
   - **Answer:**
     - **Use Grid when:** You need 2D layout (rows AND columns), page layouts, complex alignments, gallery grids
     - **Use Flexbox when:** You need 1D layout (row OR column), navigation bars, card layouts, centering items
   - **Example Scenarios:**
     - Grid: Dashboard layout, photo gallery, magazine layout, form with labels and inputs
     - Flexbox: Navbar, button groups, pricing cards in a row, footer links
   - **Best Practice:** You can use both together! Grid for overall page structure, Flexbox inside grid items.

2. **Explain grid-template-areas.**
   - **Answer:** `grid-template-areas` lets you name sections of your grid and assign items to those areas using intuitive names instead of numbers.
   - **Example:**
     ```css
     .container {
         grid-template-areas:
             "header header"
             "sidebar main"
             "footer footer";
     }
     .header { grid-area: header; }
     .sidebar { grid-area: sidebar; }
     ```
   - **Benefits:** More readable, easier to visualize layout, easier to reorder for responsive design

3. **How do you create a responsive grid layout?**
   - **Answer:** Several techniques:
     1. **auto-fit/auto-fill with minmax:**
        ```css
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        ```
     2. **Media queries to change columns:**
        ```css
        grid-template-columns: repeat(3, 1fr); /* Desktop */
        @media (max-width: 768px) {
            grid-template-columns: repeat(2, 1fr); /* Tablet */
        }
        @media (max-width: 480px) {
            grid-template-columns: 1fr; /* Mobile */
        }
        ```
     3. **Rearrange grid-template-areas:**
        ```css
        /* Desktop */
        grid-template-areas: "sidebar main";
        
        /* Mobile */
        @media (max-width: 768px) {
            grid-template-areas: "main" "sidebar";
        }
        ```

---

### Day 10: Media Queries & Responsive Design

#### 📖 What is Responsive Design?
Responsive design means your website looks good and works well on ALL devices:
- 📱 Smartphones (320px - 480px)
- 📱 Tablets (768px - 1024px)
- 💻 Laptops (1024px - 1440px)
- 🖥️ Desktops (1440px+)

**One website adapts to all screen sizes!**

#### 📖 Mobile-First Approach
Design for mobile FIRST, then add styles for larger screens.

**Why Mobile-First?**
- Most users are on mobile devices
- Easier to scale up than down
- Better performance (less CSS to override)
- Forces you to prioritize content

```css
/* ✅ Mobile-First (Recommended) */
/* Base styles for mobile */
.container {
    padding: 10px;
    font-size: 14px;
}

/* Add styles for larger screens */
@media (min-width: 768px) {
    .container {
        padding: 20px;
        font-size: 16px;
    }
}

@media (min-width: 1024px) {
    .container {
        padding: 40px;
        font-size: 18px;
    }
}
```

```css
/* ❌ Desktop-First (Old way) */
/* Base styles for desktop */
.container {
    padding: 40px;
    font-size: 18px;
}

/* Override for smaller screens */
@media (max-width: 1024px) {
    .container {
        padding: 20px;
        font-size: 16px;
    }
}
```

#### 📖 Media Query Syntax

```css
/* Basic syntax */
@media (condition) {
    /* CSS rules */
}

/* Width conditions */
@media (min-width: 768px) { }  /* Width >= 768px */
@media (max-width: 768px) { }  /* Width <= 768px */

/* Height conditions */
@media (min-height: 600px) { }

/* Orientation */
@media (orientation: portrait) { }  /* Tall screens */
@media (orientation: landscape) { } /* Wide screens */

/* Device type */
@media screen { }  /* Screens (default) */
@media print { }   /* When printing */

/* Multiple conditions (AND) */
@media (min-width: 768px) and (max-width: 1024px) { }

/* Multiple conditions (OR) */
@media (max-width: 768px), (orientation: portrait) { }
```

#### 📖 Common Breakpoints

```css
/* Standard breakpoints */

/* Extra Small (Mobile) */
/* 0px - 575px (default styles) */

/* Small (Large Mobile) */
@media (min-width: 576px) {
    /* Styles for 576px and up */
}

/* Medium (Tablet) */
@media (min-width: 768px) {
    /* Styles for tablets and up */
}

/* Large (Desktop) */
@media (min-width: 992px) {
    /* Styles for small desktops and up */
}

/* Extra Large (Large Desktop) */
@media (min-width: 1200px) {
    /* Styles for large desktops */
}

/* Extra Extra Large (Ultra Wide) */
@media (min-width: 1400px) {
    /* Styles for ultra-wide screens */
}
```

#### 📖 Responsive Units

**1. Pixels (px) - Fixed**
```css
font-size: 16px; /* Always 16px, doesn't scale */
```

**2. Em - Relative to parent font size**
```css
.parent {
    font-size: 16px;
}
.child {
    font-size: 2em; /* 2 × 16px = 32px */
    padding: 1em;   /* 1 × 32px = 32px (uses own font size!) */
}
```

**3. Rem - Relative to root (html) font size**
```css
html {
    font-size: 16px; /* Root size */
}
.element {
    font-size: 2rem;  /* 2 × 16px = 32px */
    padding: 1rem;    /* 1 × 16px = 16px */
    margin: 0.5rem;   /* 0.5 × 16px = 8px */
}
```

**4. Percentage (%) - Relative to parent**
```css
.parent {
    width: 1000px;
}
.child {
    width: 50%; /* 50% of 1000px = 500px */
}
```

**5. Viewport Width (vw) - Relative to viewport width**
```css
.element {
    width: 50vw; /* 50% of viewport width */
    /* If viewport is 1000px wide, element is 500px */
}
```

**6. Viewport Height (vh) - Relative to viewport height**
```css
.hero {
    height: 100vh; /* Full screen height */
}
.section {
    min-height: 50vh; /* Half screen height */
}
```

#### 💡 Complete Responsive Example

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Page</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        /* Mobile-first base styles */
        body {
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem;
        }
        
        /* Navigation */
        .navbar {
            background: #333;
            color: white;
            padding: 1rem;
        }
        
        .nav-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-list a {
            color: white;
            text-decoration: none;
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 1rem;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        
        /* Content Grid */
        .content-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .card {
            background: #f5f5f5;
            padding: 1.5rem;
            border-radius: 10px;
        }
        
        .card h3 {
            margin-bottom: 0.5rem;
        }
        
        /* Footer */
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 2rem;
        }
        
        /* ===== TABLET (768px and up) ===== */
        @media (min-width: 768px) {
            .container {
                padding: 2rem;
            }
            
            .nav-list {
                flex-direction: row;
                justify-content: space-around;
            }
            
            .hero {
                padding: 4rem 2rem;
            }
            
            .hero h1 {
                font-size: 3rem;
            }
            
            .content-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 2rem;
            }
        }
        
        /* ===== DESKTOP (1024px and up) ===== */
        @media (min-width: 1024px) {
            .hero {
                padding: 6rem 2rem;
            }
            
            .hero h1 {
                font-size: 4rem;
            }
            
            .content-grid {
                grid-template-columns: repeat(3, 1fr);
            }
            
            .card {
                padding: 2rem;
            }
        }
        
        /* ===== LARGE DESKTOP (1200px and up) ===== */
        @media (min-width: 1200px) {
            .hero h1 {
                font-size: 4.5rem;
            }
            
            .content-grid {
                gap: 3rem;
            }
        }
        
        /* Print Styles */
        @media print {
            .navbar,
            footer {
                display: none;
            }
            
            .hero {
                background: white;
                color: black;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <ul class="nav-list">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <div class="hero">
        <h1>Welcome to Responsive Design</h1>
        <p>This page looks great on any device!</p>
    </div>
    
    <div class="container">
        <div class="content-grid">
            <div class="card">
                <h3>Mobile First</h3>
                <p>We start with mobile design and enhance for larger screens.</p>
            </div>
            <div class="card">
                <h3>Flexible Layouts</h3>
                <p>Our grid adapts from 1 column to 3 columns based on screen size.</p>
            </div>
            <div class="card">
                <h3>Responsive Units</h3>
                <p>Using rem, em, %, vw, and vh for flexible sizing.</p>
            </div>
            <div class="card">
                <h3>Breakpoints</h3>
                <p>Strategic breakpoints ensure smooth transitions.</p>
            </div>
            <div class="card">
                <h3>Performance</h3>
                <p>Optimized for fast loading on all devices.</p>
            </div>
            <div class="card">
                <h3>Accessibility</h3>
                <p>Works great with screen readers and keyboard navigation.</p>
            </div>
        </div>
    </div>
    
    <footer>
        <p>&copy; 2024 Responsive Design Demo</p>
    </footer>
</body>
</html>
```

**Learning Resources:**
- [MDN Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries)

**Hands-on Practice:**
- Make your portfolio fully responsive:
  - Desktop: max-width: 1200px
  - Tablet: max-width: 768px
  - Mobile: max-width: 480px
- Adjust font sizes, margins, and layouts for each breakpoint

**Interview Questions:**

1. **What is mobile-first design?**
   - **Answer:** Mobile-first is a design approach where you start with mobile layouts and progressively enhance for larger screens using `min-width` media queries.
   - **Why?**
     - Most users are on mobile devices
     - Forces content prioritization
     - Better performance (less CSS overriding)
     - Easier to scale up than down
   - **Example:**
     ```css
     /* Mobile first (base) */
     .column { width: 100%; }
     
     /* Enhance for tablet */
     @media (min-width: 768px) {
         .column { width: 50%; }
     }
     
     /* Enhance for desktop */
     @media (min-width: 1024px) {
         .column { width: 33.33%; }
     }
     ```

2. **What are common breakpoints for responsive design?**
   - **Answer:** Based on popular frameworks (Bootstrap, Tailwind):
     - **Mobile:** 0-575px (default styles)
     - **Large Mobile:** 576px+
     - **Tablet:** 768px+
     - **Desktop:** 992px+
     - **Large Desktop:** 1200px+
     - **Ultra-wide:** 1400px+
   - **Note:** Choose breakpoints based on YOUR content, not just device sizes. Test where your layout breaks!

3. **Difference between em and rem units?**
   - **Answer:**
     - **em:** Relative to parent element's font size. Can compound (nesting multiplies).
     - **rem:** Relative to root (html) font size. Doesn't compound.
   - **Example:**
     ```css
     html { font-size: 16px; }
     
     .parent { font-size: 20px; }
     
     .child {
         font-size: 1em;  /* 20px (parent's font size) */
         padding: 1em;    /* 20px (own font size) */
         margin: 1rem;    /* 16px (root font size) */
     }
     ```
   - **Best Practice:** Use `rem` for consistency, `em` for components that should scale together

### Day 11: CSS Frameworks (Tailwind/Bootstrap)

#### 📖 What are CSS Frameworks?
CSS frameworks are pre-written CSS libraries that help you build websites faster. Think of them as **ready-made building blocks** instead of building from scratch!

**Popular Frameworks:**
- **Bootstrap** - Component-based (buttons, cards, modals pre-built)
- **Tailwind CSS** - Utility-based (small classes like `text-center`, `p-4`)
- **Material UI** - Google's Material Design
- **Bulma** - Modern and lightweight

#### 📖 Bootstrap - Component Framework

**What is Bootstrap?**
Bootstrap gives you pre-designed components (buttons, navbars, cards, modals). Just add HTML classes!

**Setup Bootstrap (CDN):**
```html
<!DOCTYPE html>
<html>
<head>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <!-- Your content -->
    
    <!-- Bootstrap JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Bootstrap Examples:**

```html
<!-- Buttons -->
<button class="btn btn-primary">Primary Button</button>
<button class="btn btn-success">Success Button</button>
<button class="btn btn-danger">Danger Button</button>

<!-- Card Component -->
<div class="card" style="width: 18rem;">
    <img src="image.jpg" class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">Card Title</h5>
        <p class="card-text">Some quick example text.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
</div>

<!-- Grid System (12 columns) -->
<div class="container">
    <div class="row">
        <div class="col-md-6">Half width on medium screens</div>
        <div class="col-md-6">Half width on medium screens</div>
    </div>
    <div class="row">
        <div class="col-md-4">1/3 width</div>
        <div class="col-md-4">1/3 width</div>
        <div class="col-md-4">1/3 width</div>
    </div>
</div>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">MyWebsite</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">About</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

#### 📖 Tailwind CSS - Utility Framework

**What is Tailwind?**
Tailwind uses tiny utility classes. Instead of `btn btn-primary`, you use `bg-blue-500 text-white px-4 py-2 rounded`.

**Setup Tailwind (CDN for learning):**
```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <!-- Your content -->
</body>
</html>
```

**Tailwind Examples:**

```html
<!-- Button -->
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
    Click Me
</button>

<!-- Card -->
<div class="max-w-sm rounded overflow-hidden shadow-lg">
    <img class="w-full" src="image.jpg" alt="Sunset">
    <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">Card Title</div>
        <p class="text-gray-700 text-base">
            Some quick example text to build on the card.
        </p>
    </div>
</div>

<!-- Grid -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    <div class="bg-blue-200 p-4">Item 1</div>
    <div class="bg-green-200 p-4">Item 2</div>
    <div class="bg-red-200 p-4">Item 3</div>
</div>

<!-- Flexbox Centering -->
<div class="flex items-center justify-center h-screen">
    <h1 class="text-4xl font-bold">Centered Content</h1>
</div>

<!-- Responsive Text -->
<h1 class="text-2xl md:text-4xl lg:text-6xl">
    Responsive Heading
</h1>
<!-- Small: 2xl, Medium: 4xl, Large: 6xl -->
```

**Common Tailwind Utilities:**

```html
<!-- Spacing -->
<div class="p-4">Padding all sides: 1rem</div>
<div class="px-4 py-2">Padding x: 1rem, y: 0.5rem</div>
<div class="m-4">Margin all sides: 1rem</div>
<div class="mt-8">Margin top: 2rem</div>

<!-- Colors -->
<div class="bg-blue-500">Blue background</div>
<div class="text-red-600">Red text</div>
<div class="border-green-300">Green border</div>

<!-- Typography -->
<h1 class="text-3xl font-bold">Big bold heading</h1>
<p class="text-sm text-gray-600">Small gray text</p>
<p class="text-center">Centered text</p>

<!-- Flexbox -->
<div class="flex justify-between items-center">
    <div>Left</div>
    <div>Right</div>
</div>

<!-- Grid -->
<div class="grid grid-cols-3 gap-4">
    <div>1</div>
    <div>2</div>
    <div>3</div>
</div>

<!-- Responsive -->
<div class="hidden md:block">
    Hidden on mobile, visible on tablet+
</div>

<!-- Width/Height -->
<div class="w-full h-64">Full width, height 16rem</div>
<div class="w-1/2">Half width</div>
```

#### 💡 Complete Tailwind Example

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100">
    <!-- Navbar -->
    <nav class="bg-blue-600 text-white p-4">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold">MyWebsite</h1>
            <ul class="flex space-x-6">
                <li><a href="#" class="hover:text-blue-200">Home</a></li>
                <li><a href="#" class="hover:text-blue-200">About</a></li>
                <li><a href="#" class="hover:text-blue-200">Contact</a></li>
            </ul>
        </div>
    </nav>
    
    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-purple-500 to-pink-500 text-white py-20">
        <div class="container mx-auto text-center">
            <h1 class="text-5xl font-bold mb-4">Welcome to Tailwind CSS</h1>
            <p class="text-xl mb-8">Build amazing websites faster!</p>
            <button class="bg-white text-purple-600 px-8 py-3 rounded-full font-bold hover:bg-gray-100 transition">
                Get Started
            </button>
        </div>
    </div>
    
    <!-- Cards Section -->
    <div class="container mx-auto py-16 px-4">
        <h2 class="text-3xl font-bold text-center mb-12">Our Services</h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Card 1 -->
            <div class="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition">
                <div class="text-4xl mb-4">🎨</div>
                <h3 class="text-xl font-bold mb-2">Web Design</h3>
                <p class="text-gray-600">Beautiful and modern web designs tailored to your needs.</p>
            </div>
            
            <!-- Card 2 -->
            <div class="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition">
                <div class="text-4xl mb-4">💻</div>
                <h3 class="text-xl font-bold mb-2">Development</h3>
                <p class="text-gray-600">Robust and scalable web applications built with latest technologies.</p>
            </div>
            
            <!-- Card 3 -->
            <div class="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition">
                <div class="text-4xl mb-4">🚀</div>
                <h3 class="text-xl font-bold mb-2">Deployment</h3>
                <p class="text-gray-600">Seamless deployment and hosting solutions for your projects.</p>
            </div>
        </div>
    </div>
    
    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-8 mt-16">
        <div class="container mx-auto text-center">
            <p>&copy; 2024 MyWebsite. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

#### 📖 Framework vs Custom CSS

**When to use Frameworks:**
✅ Quick prototypes
✅ Consistent design needed
✅ Working in a team
✅ Tight deadlines
✅ Don't want to write repetitive CSS

**When to use Custom CSS:**
✅ Unique, custom designs
✅ Small projects
✅ Learning CSS deeply
✅ Performance-critical sites
✅ Want full control

**Learning Resources:**
- [Tailwind CSS Installation](https://tailwindcss.com/docs/installation/using-vite)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

**Hands-on Practice:**
- Rebuild your portfolio homepage using Tailwind CSS or Bootstrap
- Use utility classes for:
  - Spacing and margins
  - Colors and typography
  - Grid/Flexbox layouts
  - Responsive design

**Interview Questions:**

1. **What are the advantages and disadvantages of CSS frameworks?**
   - **Advantages:**
     - ✅ Faster development (pre-built components)
     - ✅ Consistent design across project
     - ✅ Responsive by default
     - ✅ Browser compatibility handled
     - ✅ Well-documented and tested
     - ✅ Good for teams (everyone uses same patterns)
   - **Disadvantages:**
     - ❌ Learning curve (framework-specific classes)
     - ❌ Larger file size (unused CSS)
     - ❌ Generic "Bootstrap look" if not customized
     - ❌ Less control over styling
     - ❌ Dependency on external library
     - ❌ Harder to implement unique designs

2. **Difference between Tailwind and Bootstrap?**
   - **Answer:**
   
   | Feature | Bootstrap | Tailwind |
   |---------|-----------|----------|
   | **Approach** | Component-based | Utility-first |
   | **Philosophy** | Pre-built components | Build your own |
   | **File Size** | Larger initially | Smaller (with purging) |
   | **Customization** | Harder (override classes) | Easier (compose utilities) |
   | **Learning** | Easier to start | Steeper learning curve |
   | **Design** | Opinionated (Bootstrap look) | Flexible (any design) |
   | **JavaScript** | Includes JS components | CSS only |
   
   - **Example:**
     ```html
     <!-- Bootstrap Button -->
     <button class="btn btn-primary btn-lg">Click Me</button>
     
     <!-- Tailwind Button -->
     <button class="bg-blue-500 text-white text-lg px-6 py-3 rounded hover:bg-blue-600">
         Click Me
     </button>
     ```

3. **What is utility-first CSS?**
   - **Answer:** Utility-first CSS means using small, single-purpose classes that do one thing well, composed together to build designs.
   - **Traditional CSS:**
     ```html
     <style>
         .button-primary {
             background-color: blue;
             color: white;
             padding: 10px 20px;
             border-radius: 5px;
         }
     </style>
     <button class="button-primary">Click</button>
     ```
   - **Utility-First (Tailwind):**
     ```html
     <button class="bg-blue-500 text-white px-4 py-2 rounded">Click</button>
     ```
   - **Benefits:**
     - No naming decisions (no "what should I call this class?")
     - Changes in HTML, not CSS files
     - Faster development
     - Smaller CSS files (with purging unused classes)
   - **Trade-off:** HTML can look verbose/cluttered

---

### Day 12: Mini Project - Responsive Portfolio
**Project:** Build a Fully Responsive Personal Portfolio Website

**Requirements:**
- Responsive navbar with mobile menu
- Hero section with call-to-action
- About section
- Projects grid (use CSS Grid or Flexbox)
- Contact form
- Footer
- Use CSS Grid/Flexbox or Tailwind for layout
- Must work perfectly on:
  - Desktop (1200px+)
  - Tablet (768px - 1199px)
  - Mobile (< 768px)

**Portfolio Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <style>
        /* Add your CSS here or use Tailwind CDN */
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <!-- Logo and menu items -->
        <!-- Mobile hamburger menu -->
    </nav>
    
    <!-- Hero Section -->
    <section class="hero">
        <h1>Hi, I'm [Your Name]</h1>
        <p>Full Stack Developer</p>
        <button>View My Work</button>
    </section>
    
    <!-- About Section -->
    <section class="about">
        <h2>About Me</h2>
        <p>Your bio...</p>
        <div class="skills">
            <!-- Skill badges -->
        </div>
    </section>
    
    <!-- Projects Grid -->
    <section class="projects">
        <h2>My Projects</h2>
        <div class="project-grid">
            <!-- Project cards -->
        </div>
    </section>
    
    <!-- Contact Form -->
    <section class="contact">
        <h2>Get In Touch</h2>
        <form>
            <!-- Form fields -->
        </form>
    </section>
    
    <!-- Footer -->
    <footer>
        <p>&copy; 2024 Your Name</p>
        <!-- Social links -->
    </footer>
</body>
</html>
```

**Checklist:**
- [ ] Semantic HTML (header, nav, main, section, footer)
- [ ] Responsive navbar that collapses on mobile
- [ ] Eye-catching hero section with gradient/image
- [ ] About section with your photo and bio
- [ ] Skills list or badges
- [ ] At least 3 project cards with images
- [ ] Working contact form (HTML validation)
- [ ] Footer with social media links
- [ ] Smooth transitions and hover effects
- [ ] Works on mobile (< 768px)
- [ ] Works on tablet (768px - 1199px)
- [ ] Works on desktop (1200px+)
- [ ] All images have alt text
- [ ] Proper heading hierarchy (h1, h2, h3)
- [ ] Color contrast for accessibility

**Bonus Features:**
- Dark mode toggle
- Smooth scroll to sections
- Animation on scroll
- Project filtering
- Loading animations

---

## Module 3: JavaScript Fundamentals (Days 13-17)

### Day 13: Variables, Data Types, Operators

#### 📖 What is JavaScript?
JavaScript makes websites **interactive**. While HTML is the structure and CSS is the style, JavaScript is the **behavior**.

**Examples of what JavaScript does:**
- Show/hide content when clicking a button
- Validate form inputs
- Create animations
- Fetch data from servers
- Build games, calculators, and interactive apps

#### 📖 Variables - Storing Data
Variables are like labeled boxes where you store information.

**Three ways to declare variables:**

```javascript
// 1. var (old way - avoid using)
var name = "John";

// 2. let (for values that change)
let age = 25;
age = 26; // Can change

// 3. const (for values that never change)
const birthYear = 1998;
// birthYear = 1999; // ❌ Error! Can't change const
```

**Rules for variable names:**
- Start with letter, $, or _
- Can contain letters, numbers, $, _
- Case sensitive (`name` ≠ `Name`)
- Can't use reserved words (let, const, if, etc.)

```javascript
// ✅ Good variable names
let firstName = "Sarah";
let user_age = 30;
let $price = 99.99;
let _id = 123;

// ❌ Bad variable names
let 1name = "Test";  // Can't start with number
let my-name = "Test"; // Can't use hyphen
let let = "Test";     // Can't use reserved word
```

#### 📖 Data Types
JavaScript has 7 primitive data types:

**1. String - Text**
```javascript
let name = "John Doe";
let message = 'Hello World';
let template = `My name is ${name}`; // Template literal

// String methods
let text = "JavaScript";
console.log(text.length);           // 10
console.log(text.toUpperCase());    // "JAVASCRIPT"
console.log(text.toLowerCase());    // "javascript"
console.log(text.slice(0, 4));      // "Java"
console.log(text.includes("Script")); // true
```

**2. Number - Numeric values**
```javascript
let age = 25;
let price = 99.99;
let negative = -10;
let infinity = Infinity;

// Number operations
let sum = 10 + 5;        // 15
let difference = 10 - 5;  // 5
let product = 10 * 5;     // 50
let quotient = 10 / 5;    // 2
let remainder = 10 % 3;   // 1 (modulo)
let power = 2 ** 3;       // 8 (2³)
```

**3. Boolean - True/False**
```javascript
let isStudent = true;
let hasJob = false;
let isAdult = age >= 18; // true if age is 18 or more
```

**4. Undefined - No value assigned**
```javascript
let x;
console.log(x); // undefined

let person = {name: "John"};
console.log(person.age); // undefined (property doesn't exist)
```

**5. Null - Intentionally empty**
```javascript
let selectedUser = null; // Explicitly set to "nothing"
```

**6. Symbol - Unique identifier (advanced)**
```javascript
let id = Symbol('id');
```

**7. BigInt - Very large numbers (advanced)**
```javascript
let bigNumber = 1234567890123456789012345678901234567890n;
```

**Non-primitive:**
**8. Object - Complex data structures**
```javascript
// Object
let person = {
    name: "John",
    age: 25,
    city: "New York"
};

// Array (special type of object)
let colors = ["red", "green", "blue"];
let numbers = [1, 2, 3, 4, 5];
```

#### 📖 Operators

**Arithmetic Operators**
```javascript
let a = 10;
let b = 3;

console.log(a + b);  // 13 (addition)
console.log(a - b);  // 7  (subtraction)
console.log(a * b);  // 30 (multiplication)
console.log(a / b);  // 3.333... (division)
console.log(a % b);  // 1  (remainder/modulo)
console.log(a ** b); // 1000 (exponentiation: 10³)

// Increment/Decrement
let count = 0;
count++;  // count = 1 (increment)
count--;  // count = 0 (decrement)
```

**Comparison Operators**
```javascript
let x = 5;

console.log(x == 5);   // true  (equal value)
console.log(x == "5"); // true  (equal value, different type)
console.log(x === 5);  // true  (equal value AND type)
console.log(x === "5"); // false (different type)

console.log(x != 3);   // true  (not equal)
console.log(x !== "5"); // true  (not equal value or type)

console.log(x > 3);    // true  (greater than)
console.log(x < 10);   // true  (less than)
console.log(x >= 5);   // true  (greater than or equal)
console.log(x <= 5);   // true  (less than or equal)
```

**Logical Operators**
```javascript
let age = 25;
let hasLicense = true;

// AND (&&) - Both must be true
console.log(age >= 18 && hasLicense); // true

// OR (||) - At least one must be true
console.log(age < 18 || hasLicense); // true

// NOT (!) - Reverses boolean
console.log(!hasLicense); // false
console.log(!false);      // true
```

#### 📖 Type Coercion
JavaScript automatically converts types when needed (can cause bugs!).

```javascript
// String + Number = String (concatenation)
console.log("5" + 2);      // "52" (not 7!)
console.log("Hello" + 5);  // "Hello5"

// Subtraction, multiplication, division convert to number
console.log("5" - 2);      // 3
console.log("10" * 2);     // 20
console.log("20" / 4);     // 5

// Comparison coercion
console.log(5 == "5");     // true (converts string to number)
console.log(5 === "5");    // false (no conversion, different types)

// Boolean coercion
console.log(Boolean(0));         // false
console.log(Boolean(""));        // false
console.log(Boolean("hello"));   // true
console.log(Boolean(42));        // true
```

#### 💡 Complete Calculator Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
        }
        
        input, select, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            font-size: 16px;
        }
        
        button {
            background: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        
        button:hover {
            background: #45a049;
        }
        
        #result {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-top: 20px;
            padding: 15px;
            background: #f0f0f0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Simple Calculator</h1>
    
    <input type="number" id="num1" placeholder="Enter first number">
    
    <select id="operation">
        <option value="add">Add (+)</option>
        <option value="subtract">Subtract (-)</option>
        <option value="multiply">Multiply (×)</option>
        <option value="divide">Divide (÷)</option>
    </select>
    
    <input type="number" id="num2" placeholder="Enter second number">
    
    <button onclick="calculate()">Calculate</button>
    
    <div id="result"></div>
    
    <script>
        function calculate() {
            // Get values from inputs
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const operation = document.getElementById('operation').value;
            
            // Validate inputs
            if (isNaN(num1) || isNaN(num2)) {
                document.getElementById('result').innerHTML = 
                    "⚠️ Please enter valid numbers!";
                return;
            }
            
            // Perform calculation
            let result;
            
            if (operation === 'add') {
                result = num1 + num2;
            } else if (operation === 'subtract') {
                result = num1 - num2;
            } else if (operation === 'multiply') {
                result = num1 * num2;
            } else if (operation === 'divide') {
                if (num2 === 0) {
                    document.getElementById('result').innerHTML = 
                        "⚠️ Cannot divide by zero!";
                    return;
                }
                result = num1 / num2;
            }
            
            // Display result
            document.getElementById('result').innerHTML = 
                `Result: ${result}`;
        }
    </script>
</body>
</html>
```

**Learning Resources:**
- [MDN JavaScript Data Structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)

**Hands-on Practice:**
- Create a calculator script that:
  - Takes two numbers from user (prompt or input fields)
  - Performs addition, subtraction, multiplication, division
  - Displays results dynamically on the webpage

**Interview Questions:**

1. **Difference between let, const, and var?**
   - **Answer:**
     - **`var`:** (Old way, avoid using)
       - Function-scoped
       - Can be re-declared
       - Hoisted (can use before declaration)
       - No block scope
     - **`let`:** (Use for variables that change)
       - Block-scoped {}
       - Cannot be re-declared in same scope
       - Can be reassigned
       - Not hoisted to top
     - **`const`:** (Use for constants)
       - Block-scoped {}
       - Cannot be re-declared or reassigned
       - Must be initialized when declared
       - Object properties can still be modified
   - **Example:**
     ```javascript
     const name = "John";
     // name = "Sarah"; // ❌ Error
     
     const person = {name: "John"};
     person.name = "Sarah"; // ✅ OK (modifying property, not variable)
     ```

2. **What is type coercion in JavaScript?**
   - **Answer:** Type coercion is when JavaScript automatically converts one data type to another.
   - **Examples:**
     - `"5" + 2` → `"52"` (number converted to string)
     - `"5" - 2` → `3` (string converted to number)
     - `true + 1` → `2` (boolean converted to number: true=1)
     - `"hello" == "Hello"` → `false` (case sensitive)
   - **Best Practice:** Use `===` (strict equality) instead of `==` to avoid unexpected coercion

3. **Explain truthy and falsy values.**
   - **Answer:** In JavaScript, all values are either "truthy" or "falsy" when converted to boolean.
   - **Falsy values (only 6):**
     - `false`
     - `0`
     - `""` (empty string)
     - `null`
     - `undefined`
     - `NaN`
   - **Everything else is truthy:** including `"0"`, `"false"`, `[]`, `{}`, functions
   - **Usage:**
     ```javascript
     if (username) {  // Checks if username is truthy
         console.log("Welcome, " + username);
     } else {
         console.log("Please enter a username");
     }
     ```

---

### Day 14: Functions & Events

#### 📖 Functions - Reusable Code Blocks
Functions are like recipes - you write them once and use them many times!

**Why use functions?**
- Reusable code (DRY - Don't Repeat Yourself)
- Organized code
- Easier to test and debug
- Can take inputs (parameters) and return outputs

#### 📖 Function Declaration

```javascript
// Basic function
function greet() {
    console.log("Hello!");
}

// Call/invoke the function
greet(); // Output: Hello!

// Function with parameters
function greetUser(name) {
    console.log("Hello, " + name + "!");
}

greetUser("John");  // Hello, John!
greetUser("Sarah"); // Hello, Sarah!

// Function with multiple parameters
function addNumbers(a, b) {
    return a + b;  // Return the result
}

let sum = addNumbers(5, 3);
console.log(sum); // 8

// Function with default parameters
function greetPerson(name = "Guest") {
    return "Hello, " + name + "!";
}

console.log(greetPerson());        // Hello, Guest!
console.log(greetPerson("Alice")); // Hello, Alice!
```

#### 📖 Function Expression
Storing a function in a variable:

```javascript
// Function expression
const multiply = function(a, b) {
    return a * b;
};

console.log(multiply(4, 5)); // 20

// Can't use before declaration
// greet(); // ❌ Error
const greet = function() {
    console.log("Hi!");
};
```

#### 📖 Arrow Functions (Modern ES6)
Shorter syntax for functions:

```javascript
// Traditional function
function add(a, b) {
    return a + b;
}

// Arrow function
const add = (a, b) => {
    return a + b;
};

// Shorter arrow function (implicit return)
const add = (a, b) => a + b;

// Examples
const square = x => x * x;  // Single parameter, no parentheses needed
const greet = () => "Hello!"; // No parameters, need parentheses
const multiply = (a, b) => a * b; // Multiple parameters

console.log(square(5));      // 25
console.log(greet());        // Hello!
console.log(multiply(3, 4)); // 12

// Arrow function with multiple lines
const calculateArea = (width, height) => {
    const area = width * height;
    return area;
};
```

**Arrow Function Benefits:**
- Shorter syntax
- Don't bind their own `this` (useful in objects/classes)
- Cleaner for callbacks

#### 📖 Event Listeners - React to User Actions
Events are things that happen in the browser: clicks, typing, mouse moves, etc.

**Common Events:**
- `click` - Mouse click
- `dblclick` - Double click
- `mouseover` - Mouse enters element
- `mouseout` - Mouse leaves element
- `keydown` - Key pressed
- `keyup` - Key released
- `submit` - Form submitted
- `change` - Input value changed
- `load` - Page finished loading

#### 💡 Event Listener Examples

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin: 10px;
            cursor: pointer;
        }
        
        .box {
            width: 200px;
            height: 200px;
            background: lightblue;
            margin: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1 id="heading">Events Demo</h1>
    
    <button id="btn1">Click Me!</button>
    <button id="btn2">Change Text</button>
    <button id="btn3">Toggle Color</button>
    
    <div class="box" id="box">Hover over me!</div>
    
    <input type="text" id="textInput" placeholder="Type something...">
    <p>You typed: <span id="output"></span></p>
    
    <script>
        // Method 1: addEventListener (best practice)
        const btn1 = document.getElementById('btn1');
        btn1.addEventListener('click', function() {
            alert('Button clicked!');
        });
        
        // Arrow function with addEventListener
        const btn2 = document.getElementById('btn2');
        btn2.addEventListener('click', () => {
            document.getElementById('heading').textContent = 'Text Changed!';
        });
        
        // Toggle color
        let isBlue = true;
        const btn3 = document.getElementById('btn3');
        btn3.addEventListener('click', () => {
            const heading = document.getElementById('heading');
            if (isBlue) {
                heading.style.color = 'red';
            } else {
                heading.style.color = 'blue';
            }
            isBlue = !isBlue; // Flip the boolean
        });
        
        // Mouse events
        const box = document.getElementById('box');
        
        box.addEventListener('mouseover', () => {
            box.style.background = 'lightgreen';
            box.textContent = 'Mouse is over!';
        });
        
        box.addEventListener('mouseout', () => {
            box.style.background = 'lightblue';
            box.textContent = 'Hover over me!';
        });
        
        // Keyboard event
        const textInput = document.getElementById('textInput');
        const output = document.getElementById('output');
        
        textInput.addEventListener('input', (event) => {
            output.textContent = event.target.value;
        });
    </script>
</body>
</html>
```

#### 📖 Callback Functions
A callback is a function passed as an argument to another function.

```javascript
// Function that takes a callback
function processUserInput(callback) {
    const name = "John";
    callback(name); // Call the callback function
}

// Pass a function as callback
processUserInput(function(name) {
    console.log("Hello, " + name);
});

// With arrow function
processUserInput((name) => {
    console.log("Hi, " + name);
});

// Real example: Array methods with callbacks
const numbers = [1, 2, 3, 4, 5];

// forEach - executes callback for each item
numbers.forEach((num) => {
    console.log(num * 2);
});

// map - creates new array with callback results
const doubled = numbers.map((num) => num * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// filter - creates new array with items that pass test
const evenNumbers = numbers.filter((num) => num % 2 === 0);
console.log(evenNumbers); // [2, 4]
```

#### 💡 Complete Dark Mode Toggle Example

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            transition: all 0.3s ease;
        }
        
        body {
            font-family: Arial, sans-serif;
            padding: 40px;
        }
        
        /* Light mode (default) */
        body.light-mode {
            background: white;
            color: #333;
        }
        
        /* Dark mode */
        body.dark-mode {
            background: #1a1a1a;
            color: #f0f0f0;
        }
        
        .toggle-container {
            position: fixed;
            top: 20px;
            right: 20px;
        }
        
        #theme-toggle {
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 16px;
            background: #4CAF50;
            color: white;
        }
        
        body.dark-mode #theme-toggle {
            background: #FFA500;
        }
        
        .content {
            max-width: 800px;
            margin: 0 auto;
        }
        
        h1 {
            margin-bottom: 20px;
        }
        
        .card {
            background: #f5f5f5;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
        }
        
        body.dark-mode .card {
            background: #2a2a2a;
        }
    </style>
</head>
<body class="light-mode">
    <div class="toggle-container">
        <button id="theme-toggle">🌙 Dark Mode</button>
    </div>
    
    <div class="content">
        <h1>Dark Mode Toggle Demo</h1>
        <p>Click the button in the top right to switch themes!</p>
        
        <div class="card">
            <h2>About This Demo</h2>
            <p>This demonstrates event listeners, DOM manipulation, and localStorage.</p>
        </div>
        
        <div class="card">
            <h2>Features</h2>
            <ul>
                <li>Toggle between light and dark themes</li>
                <li>Smooth transitions</li>
                <li>Theme persists across page reloads</li>
                <li>Modern ES6 JavaScript</li>
            </ul>
        </div>
    </div>
    
    <script>
        const themeToggle = document.getElementById('theme-toggle');
        const body = document.body;
        
        // Check for saved theme preference
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            body.className = savedTheme;
            updateButton();
        }
        
        // Toggle theme on button click
        themeToggle.addEventListener('click', () => {
            // Toggle between light and dark
            if (body.classList.contains('light-mode')) {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
            } else {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
            }
            
            // Save preference
            localStorage.setItem('theme', body.className);
            
            // Update button text
            updateButton();
        });
        
        // Update button text based on current theme
        function updateButton() {
            if (body.classList.contains('dark-mode')) {
                themeToggle.textContent = '☀️ Light Mode';
            } else {
                themeToggle.textContent = '🌙 Dark Mode';
            }
        }
    </script>
</body>
</html>
```

**Learning Resources:**
- [MDN Functions Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

**Hands-on Practice:**
- Add dark mode toggle to your portfolio:
  - Button to switch between light/dark themes
  - Event listeners on buttons and links
  - Save theme preference in localStorage
  - Class switching for theme changes

**Interview Questions:**

1. **What is the difference between function declaration and function expression?**
   - **Answer:**
     - **Function Declaration:**
       ```javascript
       function greet() { return "Hello"; }
       ```
       - Hoisted (can use before declaration)
       - Named function
       - Can be called anywhere in scope
     - **Function Expression:**
       ```javascript
       const greet = function() { return "Hello"; };
       ```
       - Not hoisted (must declare before use)
       - Can be anonymous
       - Assigned to variable
   - **Example:**
     ```javascript
     sayHi(); // ✅ Works (hoisted)
     function sayHi() { console.log("Hi"); }
     
     sayBye(); // ❌ Error (not hoisted)
     const sayBye = function() { console.log("Bye"); };
     ```

2. **Explain arrow functions and their benefits.**
   - **Answer:** Arrow functions are a shorter syntax for writing functions (ES6).
   - **Syntax:**
     ```javascript
     // Traditional
     function add(a, b) { return a + b; }
     
     // Arrow
     const add = (a, b) => a + b;
     ```
   - **Benefits:**
     - Shorter, cleaner syntax
     - Implicit return for single expressions
     - Don't bind their own `this` (inherit from parent scope)
     - Great for callbacks and array methods
   - **Example:**
     ```javascript
     // Array method with arrow function
     const numbers = [1, 2, 3];
     const doubled = numbers.map(n => n * 2);
     ```

3. **What is event bubbling and capturing?**
   - **Answer:** Event bubbling and capturing are two phases of event propagation in the DOM.
   - **Bubbling (default):** Event starts at target and "bubbles up" to ancestors
     ```
     <div>              ← 3. Bubbles here
         <button>       ← 1. Click here
         </button>      ← 2. Then parent div
     </div>
     ```
   - **Capturing:** Event starts at root and "captures down" to target (opposite direction)
   - **Example:**
     ```javascript
     div.addEventListener('click', () => {
         console.log('Div clicked');
     });
     button.addEventListener('click', () => {
         console.log('Button clicked');
     });
     // Clicking button logs: "Button clicked" then "Div clicked"
     ```
   - **Stop Propagation:**
     ```javascript
     button.addEventListener('click', (e) => {
         e.stopPropagation(); // Stops bubbling
         console.log('Only button');
     });
     ```

---

### Day 15: DOM Manipulation

#### 📖 What is the DOM?
The DOM (Document Object Model) is a programming interface for HTML. It represents the page as a tree of objects that JavaScript can manipulate.

**Think of it this way:**
- HTML is the building blueprint
- DOM is the actual built house
- JavaScript is the person who can rearrange the furniture (modify the DOM)

```
document
  └── html
      ├── head
      │   └── title
      └── body
          ├── h1
          ├── div
          │   ├── p
          │   └── p
          └── footer
```

#### 📖 Selecting Elements

**1. getElementById() - Select by ID**
```javascript
const heading = document.getElementById('main-title');
console.log(heading);
```

**2. getElementsByClassName() - Select by class (returns HTMLCollection)**
```javascript
const items = document.getElementsByClassName('item');
console.log(items); // [element1, element2, ...]
```

**3. getElementsByTagName() - Select by tag (returns HTMLCollection)**
```javascript
const paragraphs = document.getElementsByTagName('p');
```

**4. querySelector() - Select first match (CSS selector)**
```javascript
const firstItem = document.querySelector('.item');
const heading = document.querySelector('#main-title');
const firstParagraph = document.querySelector('p');
const nestedDiv = document.querySelector('.container .box');
```

**5. querySelectorAll() - Select all matches (returns NodeList)**
```javascript
const allItems = document.querySelectorAll('.item');
const allParagraphs = document.querySelectorAll('p');

// Loop through NodeList
allItems.forEach((item) => {
    console.log(item);
});
```

**Best Practice:** Use `querySelector()` and `querySelectorAll()` - they're most flexible!

#### 📖 Creating Elements

```javascript
// Create new element
const newDiv = document.createElement('div');

// Add text
newDiv.textContent = 'Hello World';

// Add HTML
newDiv.innerHTML = '<strong>Bold Text</strong>';

// Add classes
newDiv.classList.add('my-class');
newDiv.className = 'class1 class2';

// Add ID
newDiv.id = 'my-id';

// Add attributes
newDiv.setAttribute('data-id', '123');

// Add styles
newDiv.style.color = 'red';
newDiv.style.padding = '10px';

// Append to body or another element
document.body.appendChild(newDiv);

// Or append to specific element
const container = document.getElementById('container');
container.appendChild(newDiv);
```

#### 📖 Modifying Elements

**textContent vs innerHTML:**
```javascript
const div = document.getElementById('myDiv');

// textContent - Plain text only (safer)
div.textContent = 'This is text'; // <div>This is text</div>
div.textContent = '<strong>Bold</strong>'; // <div>&lt;strong&gt;Bold&lt;/strong&gt;</div>

// innerHTML - Interprets HTML (can be risky with user input)
div.innerHTML = '<strong>Bold</strong>'; // <div><strong>Bold</strong></div>
```

**Modifying Classes:**
```javascript
const element = document.getElementById('box');

// Add class
element.classList.add('active');

// Remove class
element.classList.remove('hidden');

// Toggle class (add if not present, remove if present)
element.classList.toggle('highlight');

// Check if has class
if (element.classList.contains('active')) {
    console.log('Element is active');
}

// Replace class
element.classList.replace('old-class', 'new-class');
```

**Modifying Styles:**
```javascript
const box = document.getElementById('box');

// Individual styles
box.style.backgroundColor = 'blue';
box.style.color = 'white';
box.style.padding = '20px';
box.style.borderRadius = '10px';

// Note: CSS property names become camelCase
// background-color → backgroundColor
// font-size → fontSize
```

**Modifying Attributes:**
```javascript
const img = document.querySelector('img');

// Get attribute
console.log(img.getAttribute('src'));

// Set attribute
img.setAttribute('alt', 'Profile picture');
img.setAttribute('width', '300');

// Remove attribute
img.removeAttribute('height');

// Direct property access
img.src = 'new-image.jpg';
img.alt = 'New description';
```

#### 📖 Removing Elements

```javascript
// Method 1: remove() (modern)
const element = document.getElementById('myElement');
element.remove();

// Method 2: removeChild() (older)
const parent = document.getElementById('container');
const child = document.getElementById('item');
parent.removeChild(child);

// Remove all children
const container = document.getElementById('container');
container.innerHTML = ''; // Quick way
// Or
while (container.firstChild) {
    container.removeChild(container.firstChild);
}
```

#### 💡 Complete To-Do List Example

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        
        .input-container {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
        }
        
        #task-input {
            flex: 1;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
        }
        
        #add-btn {
            padding: 12px 24px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        
        #add-btn:hover {
            background: #5568d3;
        }
        
        #task-list {
            list-style: none;
        }
        
        .task-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            margin-bottom: 10px;
            transition: all 0.3s;
        }
        
        .task-item:hover {
            background: #e9ecef;
        }
        
        .task-item.completed {
            opacity: 0.6;
        }
        
        .task-item.completed .task-text {
            text-decoration: line-through;
        }
        
        .checkbox {
            width: 20px;
            height: 20px;
            cursor: pointer;
        }
        
        .task-text {
            flex: 1;
            font-size: 16px;
        }
        
        .delete-btn {
            padding: 8px 16px;
            background: #dc3545;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        
        .delete-btn:hover {
            background: #c82333;
        }
        
        .empty-message {
            text-align: center;
            color: #999;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 My To-Do List</h1>
        
        <div class="input-container">
            <input 
                type="text" 
                id="task-input" 
                placeholder="Add a new task..."
                onkeypress="if(event.key === 'Enter') addTask()"
            >
            <button id="add-btn" onclick="addTask()">Add Task</button>
        </div>
        
        <ul id="task-list"></ul>
    </div>
    
    <script>
        // Load tasks from localStorage on page load
        document.addEventListener('DOMContentLoaded', loadTasks);
        
        function addTask() {
            const input = document.getElementById('task-input');
            const taskText = input.value.trim();
            
            // Validate input
            if (taskText === '') {
                alert('Please enter a task!');
                return;
            }
            
            // Create task object
            const task = {
                id: Date.now(),
                text: taskText,
                completed: false
            };
            
            // Create task element
            createTaskElement(task);
            
            // Save to localStorage
            saveTask(task);
            
            // Clear input
            input.value = '';
            input.focus();
        }
        
        function createTaskElement(task) {
            const taskList = document.getElementById('task-list');
            
            // Create list item
            const li = document.createElement('li');
            li.className = 'task-item';
            if (task.completed) {
                li.classList.add('completed');
            }
            li.dataset.id = task.id;
            
            // Create checkbox
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.className = 'checkbox';
            checkbox.checked = task.completed;
            checkbox.addEventListener('change', () => toggleTask(task.id));
            
            // Create text span
            const textSpan = document.createElement('span');
            textSpan.className = 'task-text';
            textSpan.textContent = task.text;
            
            // Create delete button
            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'Delete';
            deleteBtn.addEventListener('click', () => deleteTask(task.id));
            
            // Append all elements
            li.appendChild(checkbox);
            li.appendChild(textSpan);
            li.appendChild(deleteBtn);
            taskList.appendChild(li);
        }
        
        function toggleTask(id) {
            const tasks = getTasks();
            const task = tasks.find(t => t.id === id);
            task.completed = !task.completed;
            saveTasks(tasks);
            
            // Update UI
            const li = document.querySelector(`[data-id="${id}"]`);
            li.classList.toggle('completed');
        }
        
        function deleteTask(id) {
            const tasks = getTasks();
            const filteredTasks = tasks.filter(t => t.id !== id);
            saveTasks(filteredTasks);
            
            // Remove from DOM
            const li = document.querySelector(`[data-id="${id}"]`);
            li.remove();
        }
        
        function getTasks() {
            const tasks = localStorage.getItem('tasks');
            return tasks ? JSON.parse(tasks) : [];
        }
        
        function saveTask(task) {
            const tasks = getTasks();
            tasks.push(task);
            saveTasks(tasks);
        }
        
        function saveTasks(tasks) {
            localStorage.setItem('tasks', JSON.stringify(tasks));
        }
        
        function loadTasks() {
            const tasks = getTasks();
            tasks.forEach(task => createTaskElement(task));
            
            if (tasks.length === 0) {
                const taskList = document.getElementById('task-list');
                taskList.innerHTML = '<p class="empty-message">No tasks yet. Add one above!</p>';
            }
        }
    </script>
</body>
</html>
```

**Learning Resources:**
- [MDN DOM Manipulation](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)

**Hands-on Practice:**
- Build a To-Do List App:
  - Add new tasks dynamically
  - Mark tasks as complete/incomplete
  - Delete tasks
  - Use `document.createElement()` and `appendChild()`
  - Persist tasks in localStorage

**Interview Questions:**

1. **Difference between innerHTML and textContent?**
   - **Answer:**
     - **textContent:** Gets/sets plain text only. Safer (no HTML injection). Faster.
       ```javascript
       element.textContent = '<strong>Text</strong>';
       // Result: <strong>Text</strong> (displayed as text)
       ```
     - **innerHTML:** Gets/sets HTML content. Can render HTML. Risky with user input (XSS attacks).
       ```javascript
       element.innerHTML = '<strong>Text</strong>';
       // Result: **Text** (rendered as bold)
       ```
   - **Best Practice:** Use textContent unless you specifically need to render HTML

2. **What is the DOM?**
   - **Answer:** The DOM (Document Object Model) is a programming interface for HTML and XML documents. It represents the page structure as a tree of objects that JavaScript can manipulate.
   - **Key Points:**
     - Created by browser when page loads
     - Represents HTML as objects/nodes
     - JavaScript can read, add, delete, or modify DOM nodes
     - Changes to DOM update the webpage in real-time
   - **Example:** When you do `document.getElementById('title')`, you're accessing a DOM node

3. **How do you create and append elements in JavaScript?**
   - **Answer:**
     ```javascript
     // 1. Create element
     const newDiv = document.createElement('div');
     
     // 2. Add content/attributes
     newDiv.textContent = 'Hello World';
     newDiv.className = 'my-class';
     newDiv.style.color = 'blue';
     
     // 3. Append to parent
     document.body.appendChild(newDiv); // Add to body
     // Or
     const container = document.getElementById('container');
     container.appendChild(newDiv); // Add to specific element
     
     // Alternative: insertBefore, prepend, append, insertAdjacentElement
     ```

---

### Day 16: Arrays, Objects, Loops

#### 📖 Arrays - Lists of Data
Arrays store multiple values in a single variable. Think of them as a numbered list!

```javascript
// Creating arrays
const fruits = ["Apple", "Banana", "Orange"];
const numbers = [1, 2, 3, 4, 5];
const mixed = [1, "Hello", true, null];

// Accessing items (zero-indexed)
console.log(fruits[0]); // "Apple" (first item)
console.log(fruits[1]); // "Banana" (second item)
console.log(fruits[2]); // "Orange" (third item)

// Array length
console.log(fruits.length); // 3

// Last item
console.log(fruits[fruits.length - 1]); // "Orange"
```

#### 📖 Array Methods

**Adding/Removing Items:**
```javascript
const fruits = ["Apple", "Banana"];

// push() - Add to end
fruits.push("Orange");
console.log(fruits); // ["Apple", "Banana", "Orange"]

// pop() - Remove from end
const removed = fruits.pop();
console.log(removed); // "Orange"
console.log(fruits);  // ["Apple", "Banana"]

// unshift() - Add to beginning
fruits.unshift("Mango");
console.log(fruits); // ["Mango", "Apple", "Banana"]

// shift() - Remove from beginning
const first = fruits.shift();
console.log(first);  // "Mango"
console.log(fruits); // ["Apple", "Banana"]

// splice() - Add/remove at specific position
fruits.splice(1, 0, "Orange"); // At index 1, remove 0, add "Orange"
console.log(fruits); // ["Apple", "Orange", "Banana"]
```

**Searching:**
```javascript
const fruits = ["Apple", "Banana", "Orange"];

// indexOf() - Find position
console.log(fruits.indexOf("Banana")); // 1
console.log(fruits.indexOf("Grape"));  // -1 (not found)

// includes() - Check if exists
console.log(fruits.includes("Apple"));  // true
console.log(fruits.includes("Grape"));  // false

// find() - Find first match
const numbers = [5, 12, 8, 130, 44];
const found = numbers.find(num => num > 10);
console.log(found); // 12
```

**Transforming Arrays:**

```javascript
const numbers = [1, 2, 3, 4, 5];

// forEach() - Execute function for each item (no return)
numbers.forEach((num) => {
    console.log(num * 2);
});
// Output: 2, 4, 6, 8, 10

// map() - Transform each item, return new array
const doubled = numbers.map((num) => num * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// filter() - Keep items that pass test, return new array
const evenNumbers = numbers.filter((num) => num % 2 === 0);
console.log(evenNumbers); // [2, 4]

// reduce() - Reduce array to single value
const sum = numbers.reduce((total, num) => total + num, 0);
console.log(sum); // 15 (1+2+3+4+5)

// Sort
const names = ["Charlie", "Alice", "Bob"];
names.sort();
console.log(names); // ["Alice", "Bob", "Charlie"]

// Reverse
names.reverse();
console.log(names); // ["Charlie", "Bob", "Alice"]

// Join - array to string
const fruits = ["Apple", "Banana", "Orange"];
console.log(fruits.join(", ")); // "Apple, Banana, Orange"
```

#### 💡 Practical Array Examples

```javascript
// Shopping cart
const cart = [
    { name: "Laptop", price: 999 },
    { name: "Mouse", price: 25 },
    { name: "Keyboard", price: 75 }
];

// Calculate total
const total = cart.reduce((sum, item) => sum + item.price, 0);
console.log(total); // 1099

// Find expensive items (> $50)
const expensive = cart.filter(item => item.price > 50);
console.log(expensive); // [{ name: "Laptop", price: 999 }, { name: "Keyboard", price: 75 }]

// Get all names
const names = cart.map(item => item.name);
console.log(names); // ["Laptop", "Mouse", "Keyboard"]
```

#### 📖 Objects - Key-Value Pairs
Objects store data as properties (key-value pairs).

```javascript
// Creating an object
const person = {
    name: "John Doe",
    age: 30,
    city: "New York",
    isStudent: false
};

// Accessing properties
console.log(person.name);  // "John Doe" (dot notation)
console.log(person["age"]); // 30 (bracket notation)

// Adding new properties
person.job = "Developer";
person["salary"] = 75000;

// Updating properties
person.age = 31;

// Deleting properties
delete person.city;

console.log(person);
// { name: "John Doe", age: 31, isStudent: false, job: "Developer", salary: 75000 }
```

**Object Methods:**
```javascript
const car = {
    brand: "Toyota",
    model: "Camry",
    year: 2022,
    
    // Method (function inside object)
    getInfo: function() {
        return `${this.brand} ${this.model} (${this.year})`;
    },
    
    // Shorter syntax (ES6)
    start() {
        return "Car started!";
    }
};

console.log(car.getInfo()); // "Toyota Camry (2022)"
console.log(car.start());   // "Car started!"

// Object.keys() - Get all keys
console.log(Object.keys(car)); // ["brand", "model", "year", "getInfo", "start"]

// Object.values() - Get all values
console.log(Object.values(car)); // ["Toyota", "Camry", 2022, function, function]

// Object.entries() - Get key-value pairs
console.log(Object.entries(car)); // [["brand", "Toyota"], ["model", "Camry"], ...]
```

#### 📖 Loops - Repeat Code

**1. for loop - Classic loop**
```javascript
// Basic for loop
for (let i = 0; i < 5; i++) {
    console.log(i); // 0, 1, 2, 3, 4
}

// Loop through array
const fruits = ["Apple", "Banana", "Orange"];
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}
```

**2. while loop - Loop while condition is true**
```javascript
let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}
// Output: 0, 1, 2, 3, 4

// do...while - Execute at least once
let num = 0;
do {
    console.log(num);
    num++;
} while (num < 3);
// Output: 0, 1, 2
```

**3. for...of loop - Loop through array values**
```javascript
const fruits = ["Apple", "Banana", "Orange"];

for (const fruit of fruits) {
    console.log(fruit);
}
// Output: Apple, Banana, Orange

// With index
for (const [index, fruit] of fruits.entries()) {
    console.log(`${index}: ${fruit}`);
}
// Output: 0: Apple, 1: Banana, 2: Orange
```

**4. for...in loop - Loop through object keys**
```javascript
const person = {
    name: "John",
    age: 30,
    city: "New York"
};

for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}
// Output:
// name: John
// age: 30
// city: New York
```

#### 📖 Destructuring - Extract Values Easily

**Array Destructuring:**
```javascript
const colors = ["red", "green", "blue"];

// Without destructuring
const first = colors[0];
const second = colors[1];

// With destructuring
const [firstColor, secondColor, thirdColor] = colors;
console.log(firstColor);  // "red"
console.log(secondColor); // "green"
console.log(thirdColor);  // "blue"

// Skip items
const [primary, , tertiary] = colors;
console.log(primary);  // "red"
console.log(tertiary); // "blue" (skipped green)

// Rest operator
const [first, ...rest] = colors;
console.log(first); // "red"
console.log(rest);  // ["green", "blue"]
```

**Object Destructuring:**
```javascript
const person = {
    name: "John",
    age: 30,
    city: "New York"
};

// Without destructuring
const name = person.name;
const age = person.age;

// With destructuring
const { name, age, city } = person;
console.log(name); // "John"
console.log(age);  // 30
console.log(city); // "New York"

// Rename variables
const { name: personName, age: personAge } = person;
console.log(personName); // "John"

// Default values
const { name, country = "USA" } = person;
console.log(country); // "USA" (default, since not in object)
```

#### 💡 Complete Quiz App Example

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .quiz-container {
            background: white;
            border-radius: 10px;
            padding: 40px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        h1 {
            margin-bottom: 30px;
            color: #333;
        }
        
        .question {
            font-size: 20px;
            margin-bottom: 20px;
            color: #555;
        }
        
        .options {
            list-style: none;
        }
        
        .options li {
            margin: 10px 0;
        }
        
        .options button {
            width: 100%;
            padding: 15px;
            text-align: left;
            background: #f5f5f5;
            border: 2px solid #ddd;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s;
        }
        
        .options button:hover {
            background: #e0e0e0;
            border-color: #667eea;
        }
        
        .options button.correct {
            background: #4CAF50;
            color: white;
            border-color: #4CAF50;
        }
        
        .options button.incorrect {
            background: #f44336;
            color: white;
            border-color: #f44336;
        }
        
        #next-btn {
            margin-top: 20px;
            padding: 12px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            display: none;
        }
        
        #next-btn:hover {
            background: #5568d3;
        }
        
        .score {
            text-align: center;
            font-size: 24px;
            margin-top: 20px;
        }
        
        #restart-btn {
            margin-top: 20px;
            padding: 12px 30px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="quiz-container">
        <h1>JavaScript Quiz</h1>
        <div id="quiz"></div>
        <button id="next-btn">Next Question</button>
    </div>
    
    <script>
        // Quiz data
        const quizData = [
            {
                question: "What does HTML stand for?",
                options: [
                    "Hyper Text Markup Language",
                    "High Tech Modern Language",
                    "Home Tool Markup Language",
                    "Hyperlinks and Text Markup Language"
                ],
                correct: 0
            },
            {
                question: "Which is NOT a JavaScript data type?",
                options: ["String", "Boolean", "Character", "Number"],
                correct: 2
            },
            {
                question: "What does CSS stand for?",
                options: [
                    "Computer Style Sheets",
                    "Cascading Style Sheets",
                    "Creative Style Sheets",
                    "Colorful Style Sheets"
                ],
                correct: 1
            },
            {
                question: "Which method adds an item to the end of an array?",
                options: ["push()", "pop()", "shift()", "unshift()"],
                correct: 0
            },
            {
                question: "What is the correct way to write a comment in JavaScript?",
                options: [
                    "<!-- This is a comment -->",
                    "// This is a comment",
                    "/* This is a comment",
                    "** This is a comment **"
                ],
                correct: 1
            }
        ];
        
        let currentQuestion = 0;
        let score = 0;
        let answered = false;
        
        const quizContainer = document.getElementById('quiz');
        const nextBtn = document.getElementById('next-btn');
        
        // Load first question
        loadQuestion();
        
        function loadQuestion() {
            answered = false;
            nextBtn.style.display = 'none';
            
            const question = quizData[currentQuestion];
            
            let html = `
                <div class="question">
                    Question ${currentQuestion + 1} of ${quizData.length}: ${question.question}
                </div>
                <ul class="options">
            `;
            
            question.options.forEach((option, index) => {
                html += `
                    <li>
                        <button onclick="checkAnswer(${index})">${option}</button>
                    </li>
                `;
            });
            
            html += '</ul>';
            quizContainer.innerHTML = html;
        }
        
        function checkAnswer(selected) {
            if (answered) return; // Prevent multiple answers
            
            answered = true;
            const question = quizData[currentQuestion];
            const buttons = document.querySelectorAll('.options button');
            
            // Show correct/incorrect
            if (selected === question.correct) {
                buttons[selected].classList.add('correct');
                score++;
            } else {
                buttons[selected].classList.add('incorrect');
                buttons[question.correct].classList.add('correct');
            }
            
            // Disable all buttons
            buttons.forEach(btn => btn.disabled = true);
            
            // Show next button or results
            if (currentQuestion < quizData.length - 1) {
                nextBtn.style.display = 'block';
            } else {
                setTimeout(showResults, 1000);
            }
        }
        
        nextBtn.addEventListener('click', () => {
            currentQuestion++;
            loadQuestion();
        });
        
        function showResults() {
            const percentage = Math.round((score / quizData.length) * 100);
            
            quizContainer.innerHTML = `
                <h2>Quiz Completed!</h2>
                <div class="score">
                    You scored ${score} out of ${quizData.length}
                    <br><br>
                    ${percentage}%
                </div>
                <button id="restart-btn">Restart Quiz</button>
            `;
            
            document.getElementById('restart-btn').addEventListener('click', () => {
                currentQuestion = 0;
                score = 0;
                loadQuestion();
            });
        }
    </script>
</body>
</html>
```

**Learning Resources:**
- [MDN Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [MDN Objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)

**Hands-on Practice:**
- Create a Quiz App:
  - Array of question objects with options and answers
  - Display one question at a time
  - Track user score
  - Display results at the end
  - "Next" and "Restart" buttons

**Interview Questions:**

1. **Difference between map, filter, and reduce?**
   - **Answer:**
     - **map():** Transforms each item, returns new array of same length
       ```javascript
       [1, 2, 3].map(n => n * 2) // [2, 4, 6]
       ```
     - **filter():** Keeps items that pass test, returns new array (can be shorter)
       ```javascript
       [1, 2, 3, 4].filter(n => n % 2 === 0) // [2, 4]
       ```
     - **reduce():** Reduces array to single value (sum, product, etc.)
       ```javascript
       [1, 2, 3, 4].reduce((sum, n) => sum + n, 0) // 10
       ```
   - **Remember:** map = transform, filter = select, reduce = combine

2. **What is array destructuring?**
   - **Answer:** Destructuring extracts values from arrays/objects into variables in one line.
   - **Example:**
     ```javascript
     // Without destructuring
     const colors = ['red', 'green', 'blue'];
     const first = colors[0];
     const second = colors[1];
     
     // With destructuring
     const [first, second, third] = colors;
     console.log(first); // 'red'
     ```
   - **Benefits:** Cleaner code, less repetition, easier to read

3. **Explain the difference between for...of and for...in loops.**
   - **Answer:**
     - **for...of:** Loops through VALUES (arrays, strings, etc.)
       ```javascript
       const arr = ['a', 'b', 'c'];
       for (const value of arr) {
           console.log(value); // 'a', 'b', 'c'
       }
       ```
     - **for...in:** Loops through KEYS/indices (objects, arrays)
       ```javascript
       const obj = {name: 'John', age: 30};
       for (const key in obj) {
           console.log(key); // 'name', 'age'
       }
       ```
   - **Rule of thumb:** Use for...of for arrays, for...in for objects

---

### Day 17: Mini Project - Interactive Quiz App
**Project:** Build a Quiz Application

**Requirements:**
- At least 10 questions
- Multiple choice options
- Timer (optional)
- Score tracking
- Results page with:
  - Final score
  - Correct/incorrect answers
  - Option to restart
- Use arrays and objects for data
- DOM manipulation for UI updates
- localStorage for saving progress

---

## Module 4: React Fundamentals (Days 18-21)

### Day 18: Introduction to React

#### 📖 What is React?
React is a JavaScript library for building user interfaces. Think of it like **LEGO blocks for websites**!

**Why React?**
- 🔄 **Reusable Components** - Build once, use everywhere
- ⚡ **Fast** - Virtual DOM makes updates super quick
- 📱 **Popular** - Used by Facebook, Instagram, Netflix, Airbnb
- 🎯 **Component-Based** - Break UI into small pieces
- 🔥 **Modern** - JSX syntax, hooks, easy state management

**React vs Vanilla JavaScript:**
```javascript
// Vanilla JavaScript - Update DOM manually
document.getElementById('count').textContent = count;

// React - Declare what you want, React updates DOM
<div>{count}</div>
```

#### 📖 Setting Up React

**Option 1: Create React App (Easiest)**
```bash
# Install Node.js first, then:
npx create-react-app my-app
cd my-app
npm start
```

**Option 2: Vite (Faster, Modern)**
```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

**Option 3: CDN (For Learning)**
```html
<!DOCTYPE html>
<html>
<head>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
    <div id="root"></div>
    
    <script type="text/babel">
        function App() {
            return <h1>Hello React!</h1>;
        }
        
        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
```

#### 📖 React Components

**Function Components (Modern Way):**
```jsx
// Simple component
function Welcome() {
    return <h1>Hello, World!</h1>;
}

// Component with props
function Greeting(props) {
    return <h1>Hello, {props.name}!</h1>;
}

// Using the component
function App() {
    return (
        <div>
            <Welcome />
            <Greeting name="John" />
            <Greeting name="Sarah" />
        </div>
    );
}
```

#### 📖 JSX - JavaScript XML
JSX lets you write HTML-like code in JavaScript!

```jsx
// JSX looks like HTML
const element = <h1>Hello, JSX!</h1>;

// But it's actually JavaScript
const element = React.createElement('h1', null, 'Hello, JSX!');

// JSX Rules:
// 1. Must return single parent element
function Component() {
    return (
        <div>  {/* Parent wrapper */}
            <h1>Title</h1>
            <p>Content</p>
        </div>
    );
}

// 2. Use {} for JavaScript expressions
function Greeting() {
    const name = "John";
    const age = 25;
    return <h1>Hello {name}, you are {age} years old</h1>;
}

// 3. className instead of class
const element = <div className="container">Content</div>;

// 4. Self-closing tags need /
const image = <img src="photo.jpg" alt="Photo" />;
const input = <input type="text" />;

// 5. camelCase for attributes
<button onClick={handleClick}>Click</button>
<label htmlFor="input">Label</label>
<div style={{ backgroundColor: 'blue', fontSize: '20px' }}>Styled</div>
```

#### 📖 Props - Passing Data to Components
Props are like function parameters for components.

```jsx
// Parent passes data via props
function App() {
    return (
        <div>
            <UserCard name="John" age={25} city="New York" />
            <UserCard name="Sarah" age={30} city="London" />
        </div>
    );
}

// Child receives props
function UserCard(props) {
    return (
        <div className="card">
            <h2>{props.name}</h2>
            <p>Age: {props.age}</p>
            <p>City: {props.city}</p>
        </div>
    );
}

// Destructuring props (cleaner)
function UserCard({ name, age, city }) {
    return (
        <div className="card">
            <h2>{name}</h2>
            <p>Age: {age}</p>
            <p>City: {city}</p>
        </div>
    );
}

// Props with children
function Card({ children }) {
    return (
        <div className="card">
            {children}
        </div>
    );
}

// Usage
<Card>
    <h2>Title</h2>
    <p>Content here</p>
</Card>
```

#### 💡 Complete React Component Example

```jsx
import React from 'react';
import './App.css';

// UserCard component
function UserCard({ name, role, image, skills }) {
    return (
        <div className="user-card">
            <img src={image} alt={name} />
            <h2>{name}</h2>
            <p className="role">{role}</p>
            <div className="skills">
                <h3>Skills:</h3>
                <ul>
                    {skills.map((skill, index) => (
                        <li key={index}>{skill}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

// Main App component
function App() {
    const users = [
        {
            name: "John Doe",
            role: "Frontend Developer",
            image: "https://i.pravatar.cc/150?img=1",
            skills: ["React", "JavaScript", "CSS"]
        },
        {
            name: "Sarah Smith",
            role: "Backend Developer",
            image: "https://i.pravatar.cc/150?img=2",
            skills: ["Node.js", "Python", "MongoDB"]
        },
        {
            name: "Mike Johnson",
            role: "Full Stack Developer",
            image: "https://i.pravatar.cc/150?img=3",
            skills: ["React", "Node.js", "PostgreSQL"]
        }
    ];

    return (
        <div className="App">
            <header>
                <h1>Our Team</h1>
            </header>
            <div className="user-grid">
                {users.map((user, index) => (
                    <UserCard
                        key={index}
                        name={user.name}
                        role={user.role}
                        image={user.image}
                        skills={user.skills}
                    />
                ))}
            </div>
        </div>
    );
}

export default App;
```

**App.css:**
```css
.App {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
    font-family: Arial, sans-serif;
}

header {
    text-align: center;
    margin-bottom: 40px;
}

header h1 {
    font-size: 2.5rem;
    color: #333;
}

.user-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.user-card {
    background: white;
    border-radius: 15px;
    padding: 30px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    text-align: center;
    transition: transform 0.3s;
}

.user-card:hover {
    transform: translateY(-10px);
}

.user-card img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin-bottom: 20px;
    object-fit: cover;
}

.user-card h2 {
    margin: 10px 0;
    color: #333;
}

.role {
    color: #666;
    font-size: 1.1rem;
    margin-bottom: 20px;
}

.skills h3 {
    margin-bottom: 10px;
    color: #555;
}

.skills ul {
    list-style: none;
    padding: 0;
}

.skills li {
    display: inline-block;
    background: #667eea;
    color: white;
    padding: 5px 15px;
    margin: 5px;
    border-radius: 20px;
    font-size: 0.9rem;
}
```

**Learning Resources:**
- [React Official Docs](https://react.dev/)
- [React Tutorial](https://react.dev/learn)

**Hands-on Practice:**
- Create a React app using Create React App or Vite
- Build a simple component that displays your name and bio
- Create a Card component and reuse it 3 times with different data
- Practice passing props between components

**Interview Questions:**

1. **What is React and why is it popular?**
   - **Answer:** React is a JavaScript library for building user interfaces, created by Facebook.
   - **Why Popular:**
     - Component-based architecture (reusable pieces)
     - Virtual DOM makes it fast (only updates what changed)
     - One-way data flow (easy to debug)
     - Large ecosystem and community
     - Used by major companies (Facebook, Netflix, Instagram)
     - Can build web, mobile (React Native), and desktop apps
   - **Key Concept:** React is a library (not framework), focuses only on the view layer

2. **What is JSX?**
   - **Answer:** JSX (JavaScript XML) is a syntax extension that lets you write HTML-like code in JavaScript.
   - **Example:**
     ```jsx
     const element = <h1>Hello, {name}!</h1>;
     ```
   - **Under the hood:** Babel compiles JSX to `React.createElement()` calls
   - **Benefits:** More readable, catches errors at compile time, prevents XSS attacks
   - **Rules:** Single parent element, use {} for JS, className not class, camelCase attributes

3. **What are props in React?**
   - **Answer:** Props (properties) are arguments passed to React components. They're read-only and flow one-way (parent to child).
   - **Example:**
     ```jsx
     // Parent
     <Greeting name="John" age={25} />
     
     // Child
     function Greeting({ name, age }) {
         return <h1>Hello {name}, {age}</h1>;
     }
     ```
   - **Key Points:**
     - Props are immutable (can't change in child)
     - Used to pass data and functions
     - Can pass any data type (strings, numbers, objects, arrays, functions)

---

### Day 19: React State & Hooks

#### 📖 What is State?
State is data that changes over time. When state changes, React re-renders the component!

**Think of state like:**
- A light switch (on/off)
- A counter (increases/decreases)
- Form input values (changes as user types)

#### 📖 useState Hook
The most important React hook for managing state.

```jsx
import { useState } from 'react';

function Counter() {
    // Declare state variable
    // [currentValue, functionToUpdate] = useState(initialValue)
    const [count, setCount] = useState(0);
    
    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count + 1)}>
                Increment
            </button>
            <button onClick={() => setCount(count - 1)}>
                Decrement
            </button>
            <button onClick={() => setCount(0)}>
                Reset
            </button>
        </div>
    );
}
```

**Multiple State Variables:**
```jsx
function Form() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [age, setAge] = useState(0);
    const [isSubscribed, setIsSubscribed] = useState(false);
    
    return (
        <div>
            <input 
                value={name} 
                onChange={(e) => setName(e.target.value)}
                placeholder="Name"
            />
            <input 
                value={email} 
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email"
            />
            <input 
                type="number"
                value={age} 
                onChange={(e) => setAge(Number(e.target.value))}
            />
            <label>
                <input 
                    type="checkbox"
                    checked={isSubscribed}
                    onChange={(e) => setIsSubscribed(e.target.checked)}
                />
                Subscribe to newsletter
            </label>
        </div>
    );
}
```

**State with Objects:**
```jsx
function UserProfile() {
    const [user, setUser] = useState({
        name: '',
        email: '',
        age: 0
    });
    
    const handleChange = (field, value) => {
        setUser({
            ...user,  // Spread existing values
            [field]: value  // Update specific field
        });
    };
    
    return (
        <div>
            <input 
                value={user.name}
                onChange={(e) => handleChange('name', e.target.value)}
            />
            <input 
                value={user.email}
                onChange={(e) => handleChange('email', e.target.value)}
            />
            <p>Name: {user.name}</p>
            <p>Email: {user.email}</p>
        </div>
    );
}
```

**State with Arrays:**
```jsx
function TodoList() {
    const [todos, setTodos] = useState([]);
    const [input, setInput] = useState('');
    
    const addTodo = () => {
        setTodos([...todos, input]);  // Add to array
        setInput('');
    };
    
    const deleteTodo = (index) => {
        setTodos(todos.filter((_, i) => i !== index));  // Remove from array
    };
    
    return (
        <div>
            <input 
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={addTodo}>Add</button>
            
            <ul>
                {todos.map((todo, index) => (
                    <li key={index}>
                        {todo}
                        <button onClick={() => deleteTodo(index)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}
```

#### 📖 useEffect Hook
useEffect lets you perform side effects (data fetching, subscriptions, timers, etc.)

```jsx
import { useState, useEffect } from 'react';

// Run once on mount
function App() {
    useEffect(() => {
        console.log('Component mounted!');
    }, []);  // Empty array = run once
}

// Run on every render
function App() {
    useEffect(() => {
        console.log('Component rendered!');
    });  // No array = run every time
}

// Run when specific value changes
function App() {
    const [count, setCount] = useState(0);
    
    useEffect(() => {
        console.log('Count changed:', count);
    }, [count]);  // Run when count changes
}

// Cleanup function
function Timer() {
    const [seconds, setSeconds] = useState(0);
    
    useEffect(() => {
        const interval = setInterval(() => {
            setSeconds(s => s + 1);
        }, 1000);
        
        // Cleanup (runs when component unmounts)
        return () => clearInterval(interval);
    }, []);
    
    return <div>Seconds: {seconds}</div>;
}
```

#### 💡 Complete React Counter App

```jsx
import React, { useState, useEffect } from 'react';
import './Counter.css';

function Counter() {
    const [count, setCount] = useState(0);
    const [step, setStep] = useState(1);
    const [history, setHistory] = useState([]);
    
    // Add to history when count changes
    useEffect(() => {
        if (history.length === 0 || history[history.length - 1] !== count) {
            setHistory([...history, count]);
        }
    }, [count]);
    
    // Load from localStorage on mount
    useEffect(() => {
        const saved = localStorage.getItem('count');
        if (saved) {
            setCount(Number(saved));
        }
    }, []);
    
    // Save to localStorage when count changes
    useEffect(() => {
        localStorage.setItem('count', count);
    }, [count]);
    
    const increment = () => setCount(count + step);
    const decrement = () => setCount(count - step);
    const reset = () => setCount(0);
    const double = () => setCount(count * 2);
    
    return (
        <div className="counter-container">
            <h1>React Counter</h1>
            
            <div className="display">
                <h2 className={count >= 0 ? 'positive' : 'negative'}>
                    {count}
                </h2>
            </div>
            
            <div className="controls">
                <button onClick={decrement} className="btn btn-danger">
                    - {step}
                </button>
                <button onClick={increment} className="btn btn-success">
                    + {step}
                </button>
            </div>
            
            <div className="controls">
                <button onClick={double} className="btn btn-primary">
                    × 2
                </button>
                <button onClick={reset} className="btn btn-warning">
                    Reset
                </button>
            </div>
            
            <div className="step-control">
                <label>
                    Step: 
                    <input 
                        type="number" 
                        value={step}
                        onChange={(e) => setStep(Number(e.target.value))}
                        min="1"
                    />
                </label>
            </div>
            
            <div className="history">
                <h3>History:</h3>
                <div className="history-items">
                    {history.map((value, index) => (
                        <span key={index} className="history-item">
                            {value}
                        </span>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default Counter;
```

**Counter.css:**
```css
.counter-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 40px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    text-align: center;
}

h1 {
    color: #333;
    margin-bottom: 30px;
}

.display {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 40px;
    border-radius: 15px;
    margin-bottom: 30px;
}

.display h2 {
    font-size: 4rem;
    color: white;
    margin: 0;
}

.display h2.positive {
    color: #4CAF50;
}

.display h2.negative {
    color: #f44336;
}

.controls {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-bottom: 15px;
}

.btn {
    padding: 15px 30px;
    font-size: 1.2rem;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: bold;
    color: white;
}

.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.btn-success {
    background: #4CAF50;
}

.btn-danger {
    background: #f44336;
}

.btn-primary {
    background: #2196F3;
}

.btn-warning {
    background: #FF9800;
}

.step-control {
    margin: 20px 0;
}

.step-control label {
    font-size: 1.1rem;
    color: #555;
}

.step-control input {
    width: 60px;
    padding: 5px;
    margin-left: 10px;
    font-size: 1rem;
    border: 2px solid #ddd;
    border-radius: 5px;
}

.history {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 2px solid #eee;
}

.history h3 {
    color: #555;
    margin-bottom: 15px;
}

.history-items {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
}

.history-item {
    background: #f0f0f0;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9rem;
    color: #666;
}
```

**Interview Questions:**

1. **What is useState and how does it work?**
   - **Answer:** `useState` is a React Hook that lets you add state to functional components.
   - **Syntax:** `const [value, setValue] = useState(initialValue);`
   - **How it works:**
     - Returns array with 2 elements: current value and setter function
     - When setter is called, component re-renders with new value
     - State persists between renders
   - **Example:**
     ```jsx
     const [count, setCount] = useState(0);
     setCount(5);  // Updates count to 5, triggers re-render
     ```

2. **What is useEffect and when do you use it?**
   - **Answer:** `useEffect` lets you perform side effects in functional components (data fetching, subscriptions, DOM updates, timers).
   - **When to use:**
     - Fetching data from API
     - Setting up subscriptions
     - Manually changing the DOM
     - Setting up timers/intervals
   - **Syntax:**
     ```jsx
     useEffect(() => {
         // Effect code
         return () => {
             // Cleanup (optional)
         };
     }, [dependencies]);
     ```
   - **Dependency array:**
     - `[]` = run once on mount
     - `[count]` = run when count changes
     - No array = run on every render

3. **Explain the difference between props and state.**
   - **Answer:**
   
   | Props | State |
   |-------|-------|
   | Passed from parent | Defined in component |
   | Read-only (immutable) | Can be changed |
   | Function parameters | Component's memory |
   | Can't change in child | Changed with setState |
   | External data | Internal data |
   
   - **Example:**
     ```jsx
     // Props
     <Card title="Hello" />  // Parent passes
     function Card({ title }) { }  // Child receives
     
     // State
     const [count, setCount] = useState(0);  // Internal
     setCount(count + 1);  // Can change
     ```

---

## Module 5: Angular Fundamentals (Days 20-21)

### Day 20: Introduction to Angular

#### 📖 What is Angular?
Angular is a complete **framework** for building web applications. Unlike React (library), Angular provides everything you need out of the box!

**Angular vs React:**
- **Angular** = Complete kitchen (everything included)
- **React** = Cooking utensils (you add what you need)

**Why Angular?**
- 🏗️ **Full Framework** - Routing, forms, HTTP client all included
- 📘 **TypeScript** - Built with TypeScript (type safety)
- 🏢 **Enterprise** - Used by Google, Microsoft, IBM
- 🎯 **Opinionated** - Clear structure and best practices
- 🔧 **CLI** - Powerful command-line tool

#### 📖 Setting Up Angular

```bash
# Install Angular CLI
npm install -g @angular/cli

# Create new project
ng new my-app

# Questions:
# - Routing? Yes
# - Stylesheet? CSS (or SCSS)

# Navigate and start
cd my-app
ng serve

# Open browser: http://localhost:4200
```

#### 📖 Angular Project Structure

```
my-app/
├── src/
│   ├── app/
│   │   ├── app.component.ts      # Root component TypeScript
│   │   ├── app.component.html    # Root component template
│   │   ├── app.component.css     # Root component styles
│   │   ├── app.component.spec.ts # Tests
│   │   └── app.module.ts         # Root module
│   ├── assets/                   # Images, fonts, etc.
│   ├── index.html               # Main HTML file
│   ├── main.ts                  # Entry point
│   └── styles.css               # Global styles
├── angular.json                 # Angular configuration
├── package.json                 # Dependencies
└── tsconfig.json               # TypeScript configuration
```

#### 📖 Angular Components

**Component = TypeScript + HTML + CSS**

```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',    // HTML tag name
  templateUrl: './app.component.html',  // Template file
  styleUrls: ['./app.component.css']    // Style file
})
export class AppComponent {
  title = 'My Angular App';
  count = 0;
  
  increment() {
    this.count++;
  }
}
```

```html
<!-- app.component.html -->
<div class="container">
    <h1>{{ title }}</h1>
    <p>Count: {{ count }}</p>
    <button (click)="increment()">Increment</button>
</div>
```

```css
/* app.component.css */
.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 40px;
    text-align: center;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}
```

#### 📖 Creating Components

```bash
# Generate new component
ng generate component user-card
# or shorthand
ng g c user-card

# Creates:
# user-card/
#   ├── user-card.component.ts
#   ├── user-card.component.html
#   ├── user-card.component.css
#   └── user-card.component.spec.ts
```

**user-card.component.ts:**
```typescript
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-user-card',
  templateUrl: './user-card.component.html',
  styleUrls: ['./user-card.component.css']
})
export class UserCardComponent {
  @Input() name: string = '';
  @Input() role: string = '';
  @Input() image: string = '';
}
```

**user-card.component.html:**
```html
<div class="user-card">
    <img [src]="image" [alt]="name">
    <h2>{{ name }}</h2>
    <p class="role">{{ role }}</p>
</div>
```

**Using the component:**
```html
<!-- app.component.html -->
<div class="team">
    <app-user-card 
        name="John Doe" 
        role="Frontend Developer"
        image="https://i.pravatar.cc/150?img=1">
    </app-user-card>
    
    <app-user-card 
        name="Sarah Smith" 
        role="Backend Developer"
        image="https://i.pravatar.cc/150?img=2">
    </app-user-card>
</div>
```

#### 📖 Angular Directives

**Structural Directives (modify DOM structure):**

```typescript
// Component
export class AppComponent {
  isLoggedIn = true;
  users = ['John', 'Sarah', 'Mike', 'Emma'];
  selectedUser = '';
}
```

```html
<!-- *ngIf - Conditional rendering -->
<div *ngIf="isLoggedIn">
    <h2>Welcome back!</h2>
</div>

<div *ngIf="!isLoggedIn">
    <h2>Please log in</h2>
</div>

<!-- *ngIf with else -->
<div *ngIf="isLoggedIn; else loginTemplate">
    <h2>Welcome!</h2>
</div>
<ng-template #loginTemplate>
    <h2>Please log in</h2>
</ng-template>

<!-- *ngFor - Loop through array -->
<ul>
    <li *ngFor="let user of users">{{ user }}</li>
</ul>

<!-- *ngFor with index -->
<ul>
    <li *ngFor="let user of users; let i = index">
        {{ i + 1 }}. {{ user }}
    </li>
</ul>

<!-- *ngSwitch - Multiple conditions -->
<div [ngSwitch]="selectedUser">
    <p *ngSwitchCase="'John'">John's profile</p>
    <p *ngSwitchCase="'Sarah'">Sarah's profile</p>
    <p *ngSwitchDefault>Select a user</p>
</div>
```

**Attribute Directives (modify appearance/behavior):**

```html
<!-- [ngClass] - Dynamic classes -->
<div [ngClass]="{'active': isActive, 'disabled': !isEnabled}">
    Content
</div>

<!-- [ngStyle] - Dynamic styles -->
<div [ngStyle]="{'color': textColor, 'font-size': fontSize + 'px'}">
    Styled content
</div>

<!-- ngModel - Two-way binding (FormsModule required) -->
<input [(ngModel)]="username" placeholder="Enter name">
<p>Hello, {{ username }}!</p>
```

#### 📖 Event Binding & Property Binding

```typescript
// Component
export class AppComponent {
  message = 'Hello Angular!';
  imageUrl = 'https://angular.io/assets/images/logos/angular/angular.png';
  isDisabled = false;
  
  handleClick() {
    alert('Button clicked!');
  }
  
  handleInput(event: any) {
    console.log('Input value:', event.target.value);
  }
}
```

```html
<!-- Property Binding [property] -->
<img [src]="imageUrl" alt="Angular Logo">
<button [disabled]="isDisabled">Click Me</button>
<div [innerHTML]="message"></div>

<!-- Event Binding (event) -->
<button (click)="handleClick()">Click Me</button>
<input (input)="handleInput($event)" placeholder="Type something">
<button (mouseenter)="onMouseEnter()" (mouseleave)="onMouseLeave()">
    Hover me
</button>

<!-- Two-way Binding [(ngModel)] -->
<input [(ngModel)]="message">
<p>{{ message }}</p>
```

#### 💡 Complete Angular Counter App

```typescript
// counter.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css']
})
export class CounterComponent {
  count: number = 0;
  step: number = 1;
  history: number[] = [];
  
  increment() {
    this.count += this.step;
    this.addToHistory();
  }
  
  decrement() {
    this.count -= this.step;
    this.addToHistory();
  }
  
  reset() {
    this.count = 0;
    this.addToHistory();
  }
  
  double() {
    this.count *= 2;
    this.addToHistory();
  }
  
  addToHistory() {
    this.history.push(this.count);
    if (this.history.length > 10) {
      this.history.shift(); // Keep only last 10
    }
  }
  
  getCountClass() {
    return {
      'positive': this.count > 0,
      'negative': this.count < 0,
      'zero': this.count === 0
    };
  }
}
```

```html
<!-- counter.component.html -->
<div class="counter-container">
    <h1>Angular Counter</h1>
    
    <div class="display">
        <h2 [ngClass]="getCountClass()">
            {{ count }}
        </h2>
    </div>
    
    <div class="controls">
        <button (click)="decrement()" class="btn btn-danger">
            - {{ step }}
        </button>
        <button (click)="increment()" class="btn btn-success">
            + {{ step }}
        </button>
    </div>
    
    <div class="controls">
        <button (click)="double()" class="btn btn-primary">
            × 2
        </button>
        <button (click)="reset()" class="btn btn-warning">
            Reset
        </button>
    </div>
    
    <div class="step-control">
        <label>
            Step: 
            <input 
                type="number" 
                [(ngModel)]="step"
                min="1"
            />
        </label>
    </div>
    
    <div class="history">
        <h3>History:</h3>
        <div class="history-items">
            <span 
                *ngFor="let value of history; let i = index" 
                class="history-item">
                {{ value }}
            </span>
        </div>
    </div>
</div>
```

```css
/* counter.component.css */
.counter-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 40px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    text-align: center;
}

h1 {
    color: #333;
    margin-bottom: 30px;
}

.display {
    background: linear-gradient(135deg, #dd0031 0%, #c3002f 100%);
    padding: 40px;
    border-radius: 15px;
    margin-bottom: 30px;
}

.display h2 {
    font-size: 4rem;
    color: white;
    margin: 0;
}

.positive {
    color: #4CAF50 !important;
}

.negative {
    color: #f44336 !important;
}

.zero {
    color: white !important;
}

.controls {
    display: flex;
    gap: 15px;
    justify-content: center;
    margin-bottom: 15px;
}

.btn {
    padding: 15px 30px;
    font-size: 1.2rem;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s;
    font-weight: bold;
    color: white;
}

.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.btn-success {
    background: #4CAF50;
}

.btn-danger {
    background: #f44336;
}

.btn-primary {
    background: #2196F3;
}

.btn-warning {
    background: #FF9800;
}

.step-control {
    margin: 20px 0;
}

.step-control input {
    width: 60px;
    padding: 5px;
    margin-left: 10px;
    font-size: 1rem;
    border: 2px solid #ddd;
    border-radius: 5px;
}

.history {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 2px solid #eee;
}

.history-items {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
}

.history-item {
    background: #f0f0f0;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9rem;
    color: #666;
}
```

**Don't forget to import FormsModule in app.module.ts:**
```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';  // Add this

import { AppComponent } from './app.component';
import { CounterComponent } from './counter/counter.component';

@NgModule({
  declarations: [
    AppComponent,
    CounterComponent
  ],
  imports: [
    BrowserModule,
    FormsModule  // Add this
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

**Interview Questions:**

1. **What is Angular and how is it different from React?**
   - **Answer:** Angular is a complete framework for building web applications, while React is a library for building UIs.
   
   | Angular | React |
   |---------|-------|
   | Full framework | Library |
   | TypeScript required | JavaScript (TS optional) |
   | Two-way binding | One-way data flow |
   | Complete solution | Need additional libraries |
   | Opinionated | Flexible |
   | Angular CLI | Create React App / Vite |
   
   - **Use Angular when:** Enterprise apps, team prefers structure, full solution needed
   - **Use React when:** Flexibility needed, smaller learning curve, more control

2. **What are Angular directives?**
   - **Answer:** Directives are instructions in the DOM that tell Angular how to render or modify elements.
   - **Types:**
     - **Component Directives:** Components with templates (`@Component`)
     - **Structural Directives:** Modify DOM structure (`*ngIf`, `*ngFor`, `*ngSwitch`)
     - **Attribute Directives:** Modify appearance/behavior (`[ngClass]`, `[ngStyle]`, `[(ngModel)]`)
   - **Example:**
     ```html
     <div *ngIf="show">Conditional</div>
     <li *ngFor="let item of items">{{ item }}</li>
     <div [ngClass]="{'active': isActive}">Styled</div>
     ```

3. **Explain data binding in Angular.**
   - **Answer:** Data binding connects component data with the template.
   - **Types:**
     - **Interpolation:** `{{ value }}` - Display data
     - **Property Binding:** `[property]="value"` - Set element property
     - **Event Binding:** `(event)="handler()"` - Listen to events
     - **Two-way Binding:** `[(ngModel)]="value"` - Sync input with data
   - **Example:**
     ```html
     <h1>{{ title }}</h1>  <!-- Interpolation -->
     <img [src]="imageUrl">  <!-- Property -->
     <button (click)="save()">Save</button>  <!-- Event -->
     <input [(ngModel)]="name">  <!-- Two-way -->
     ```

---

### Day 21: Angular Services & Routing

#### 📖 Angular Services
Services are singleton objects that handle data and business logic. They're shared across components!

**Why Services?**
- 💾 Share data between components
- 🌐 Make HTTP requests
- 📝 Handle business logic
- ♻️ Reusable code

**Creating a Service:**
```bash
ng generate service services/user
# or
ng g s services/user
```

**user.service.ts:**
```typescript
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'  // Available throughout app
})
export class UserService {
  private users = [
    { id: 1, name: 'John Doe', email: 'john@example.com' },
    { id: 2, name: 'Sarah Smith', email: 'sarah@example.com' }
  ];

  constructor() { }

  getUsers() {
    return this.users;
  }

  getUserById(id: number) {
    return this.users.find(user => user.id === id);
  }

  addUser(user: any) {
    user.id = this.users.length + 1;
    this.users.push(user);
  }

  deleteUser(id: number) {
    this.users = this.users.filter(user => user.id !== id);
  }
}
```

**Using the Service:**
```typescript
import { Component, OnInit } from '@angular/core';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html'
})
export class UsersComponent implements OnInit {
  users: any[] = [];

  constructor(private userService: UserService) { }

  ngOnInit() {
    this.users = this.userService.getUsers();
  }

  addUser(name: string, email: string) {
    this.userService.addUser({ name, email });
    this.users = this.userService.getUsers();
  }

  deleteUser(id: number) {
    this.userService.deleteUser(id);
    this.users = this.userService.getUsers();
  }
}
```

#### 📖 HTTP Requests with HttpClient

**Import HttpClientModule:**
```typescript
// app.module.ts
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [
    BrowserModule,
    HttpClientModule  // Add this
  ]
})
export class AppModule { }
```

**data.service.ts:**
```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private apiUrl = 'https://jsonplaceholder.typicode.com';

  constructor(private http: HttpClient) { }

  // GET request
  getPosts(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/posts`);
  }

  // GET single item
  getPost(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/posts/${id}`);
  }

  // POST request
  createPost(post: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/posts`, post);
  }

  // PUT request
  updatePost(id: number, post: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/posts/${id}`, post);
  }

  // DELETE request
  deletePost(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/posts/${id}`);
  }
}
```

**Using HTTP Service:**
```typescript
import { Component, OnInit } from '@angular/core';
import { DataService } from './services/data.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html'
})
export class PostsComponent implements OnInit {
  posts: any[] = [];
  loading = true;
  error = '';

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.loadPosts();
  }

  loadPosts() {
    this.dataService.getPosts().subscribe({
      next: (data) => {
        this.posts = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load posts';
        this.loading = false;
        console.error(err);
      }
    });
  }

  createPost() {
    const newPost = {
      title: 'New Post',
      body: 'Post content',
      userId: 1
    };
    
    this.dataService.createPost(newPost).subscribe({
      next: (post) => {
        this.posts.unshift(post);
        console.log('Post created:', post);
      },
      error: (err) => console.error('Error:', err)
    });
  }
}
```

```html
<!-- posts.component.html -->
<div class="container">
    <h1>Blog Posts</h1>
    
    <div *ngIf="loading" class="loading">
        Loading posts...
    </div>
    
    <div *ngIf="error" class="error">
        {{ error }}
    </div>
    
    <button (click)="createPost()" class="btn">
        Create New Post
    </button>
    
    <div class="posts">
        <div *ngFor="let post of posts" class="post-card">
            <h3>{{ post.title }}</h3>
            <p>{{ post.body }}</p>
        </div>
    </div>
</div>
```

#### 📖 Angular Routing

**Setting up Routes:**
```typescript
// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { UserDetailsComponent } from './user-details/user-details.component';
import { NotFoundComponent } from './not-found/not-found.component';

const routes: Routes = [
  { path: '', component: HomeComponent },  // Default route
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'user/:id', component: UserDetailsComponent },  // Route with parameter
  { path: '**', component: NotFoundComponent }  // 404 page
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

**app.component.html (with navigation):**
```html
<nav class="navbar">
    <a routerLink="/" routerLinkActive="active" [routerLinkActiveOptions]="{exact: true}">
        Home
    </a>
    <a routerLink="/about" routerLinkActive="active">About</a>
    <a routerLink="/contact" routerLinkActive="active">Contact</a>
</nav>

<router-outlet></router-outlet>  <!-- Components render here -->
```

**Programmatic Navigation:**
```typescript
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  template: `
    <button (click)="goToAbout()">Go to About</button>
    <button (click)="goToUser(5)">View User 5</button>
  `
})
export class HomeComponent {
  constructor(private router: Router) { }

  goToAbout() {
    this.router.navigate(['/about']);
  }

  goToUser(id: number) {
    this.router.navigate(['/user', id]);
  }
}
```

**Getting Route Parameters:**
```typescript
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user-details',
  templateUrl: './user-details.component.html'
})
export class UserDetailsComponent implements OnInit {
  userId: string = '';

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    // Get parameter from URL
    this.userId = this.route.snapshot.paramMap.get('id') || '';
    
    // Or subscribe to parameter changes
    this.route.paramMap.subscribe(params => {
      this.userId = params.get('id') || '';
      console.log('User ID:', this.userId);
    });
  }
}
```

**Learning Resources:**
- [Angular Official Docs](https://angular.io/docs)
- [Angular CLI](https://angular.io/cli)

**Hands-on Practice:**
- Create an Angular app with routing
- Build a service to manage data
- Create components for Home, About, Contact pages
- Make HTTP requests to JSONPlaceholder API
- Display list of posts with loading state

**Interview Questions:**

1. **What are Angular services and why use them?**
   - **Answer:** Services are singleton classes that handle business logic and data. They're shared across the entire application.
   - **Why use:**
     - Share data between components
     - Centralize business logic
     - Make HTTP requests
     - Keep components lean (only UI logic)
   - **Example:**
     ```typescript
     @Injectable({ providedIn: 'root' })
     export class DataService {
         getData() { return [...]; }
     }
     
     // Use in component
     constructor(private dataService: DataService) { }
     ```

2. **Explain Angular routing.**
   - **Answer:** Angular Router enables navigation between different views/components.
   - **Key Concepts:**
     - **Routes:** Define URL paths and components
     - **RouterOutlet:** Where components render
     - **RouterLink:** Create navigation links
     - **ActivatedRoute:** Access route parameters
   - **Example:**
     ```typescript
     // Define routes
     const routes = [
         { path: '', component: HomeComponent },
         { path: 'user/:id', component: UserComponent }
     ];
     
     // Navigate
     <a routerLink="/user/5">User 5</a>
     this.router.navigate(['/user', 5]);
     ```

3. **What is dependency injection in Angular?**
   - **Answer:** Dependency Injection (DI) is a design pattern where Angular automatically provides (injects) dependencies that a class needs.
   - **Benefits:**
     - Loose coupling
     - Easier testing
     - Reusability
     - Automatic instance management
   - **Example:**
     ```typescript
     // Service is automatically injected
     constructor(
         private userService: UserService,
         private http: HttpClient,
         private router: Router
     ) { }
     // Angular creates and provides these instances
     ```

---

## Module 6: Node.js Fundamentals (Days 22-25)

### Day 22: Introduction to Node.js

#### 📖 What is Node.js?
Node.js is JavaScript runtime that lets you run JavaScript **outside the browser** - on servers, computers, IoT devices!

**Think of it like:**
- **Browser JavaScript** = JavaScript in a web page (can't access files, databases)
- **Node.js** = JavaScript anywhere (can access files, databases, create servers)

**Why Node.js?**
- ⚡ **Fast** - Built on Chrome's V8 engine
- 🔄 **Asynchronous** - Handles many requests at once
- 📦 **NPM** - Millions of packages available
- 🌐 **Full Stack** - Same language (JS) for frontend and backend
- 💼 **Popular** - Used by Netflix, PayPal, Uber, LinkedIn

**What can you build?**
- REST APIs
- Real-time applications (chat, games)
- Microservices
- Command-line tools
- File processing scripts
- Web servers

#### 📖 Installing Node.js

**Option 1: Official Website (Recommended)**
1. Visit [nodejs.org](https://nodejs.org)
2. Download LTS (Long Term Support) version
3. Run installer
4. Verify installation:
```bash
node --version   # Should show: v18.x.x or v20.x.x
npm --version    # Should show: 9.x.x or 10.x.x
```

**Option 2: NVM (Node Version Manager) - For Developers**
```bash
# Install NVM (macOS/Linux)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Install Node
nvm install --lts
nvm use --lts

# Switch between versions
nvm install 18
nvm use 18
```

#### 📖 Your First Node.js Program

**hello.js:**
```javascript
// Simple console log
console.log('Hello from Node.js!');

// Variables and functions
const name = 'John';
const age = 25;

function greet(person) {
    return `Hello, ${person}!`;
}

console.log(greet(name));
console.log(`Age: ${age}`);

// Access Node.js globals
console.log('Node version:', process.version);
console.log('Platform:', process.platform);
console.log('Current directory:', __dirname);
console.log('File name:', __filename);
```

**Run it:**
```bash
node hello.js
```

**Output:**
```
Hello from Node.js!
Hello, John!
Age: 25
Node version: v18.17.0
Platform: darwin
Current directory: /Users/yourname/projects
File name: /Users/yourname/projects/hello.js
```

#### 📖 NPM - Node Package Manager

**Creating package.json:**
```bash
# Create package.json (interactive)
npm init

# Create with defaults
npm init -y
```

**package.json:**
```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My Node.js app",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  },
  "keywords": ["nodejs", "app"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {},
  "devDependencies": {}
}
```

**Installing Packages:**
```bash
# Install package
npm install express

# Install multiple packages
npm install axios dotenv cors

# Install as dev dependency
npm install --save-dev nodemon

# Install globally
npm install -g nodemon

# Install specific version
npm install express@4.18.0

# Uninstall
npm uninstall express

# Update packages
npm update

# List installed
npm list
```

**Using an NPM Package:**
```javascript
// After: npm install chalk@4.1.2
const chalk = require('chalk');

console.log(chalk.blue('Hello in blue!'));
console.log(chalk.red.bold('Error message'));
console.log(chalk.green.underline('Success!'));
console.log(chalk.yellow.bgBlack(' Warning '));

// Colored console logs
console.log(chalk.green('✓ Server started successfully'));
console.log(chalk.red('✗ Failed to connect to database'));
console.log(chalk.yellow('⚠ Warning: Port already in use'));
```

**Learning Resources:**
- [Node.js Getting Started](https://nodejs.org/en/docs/guides/getting-started-guide/)
- [NPM Documentation](https://docs.npmjs.com/)

**Hands-on Practice:**
- Install Node.js and verify installation
- Create a new project with `npm init -y`
- Install `chalk` package
- Write a script that logs colored messages
- Create a simple calculator program

**Interview Questions:**

1. **What is Node.js and why is it used?**
   - **Answer:** Node.js is a JavaScript runtime built on Chrome's V8 engine that allows you to run JavaScript on the server side.
   
   **Why used:**
   - Run JavaScript outside browser (server, desktop, IoT)
   - Build fast, scalable network applications
   - Asynchronous and event-driven (handles many connections)
   - Same language for frontend and backend
   - Huge ecosystem (NPM with 2+ million packages)
   - Non-blocking I/O model (efficient)
   
   **Example Use Cases:**
   - REST APIs (Express.js)
   - Real-time applications (chat, gaming)
   - Microservices
   - Command-line tools
   - Build tools (Webpack, Vite)

2. **What is NPM?**
   - **Answer:** NPM (Node Package Manager) is the default package manager for Node.js and the world's largest software registry.
   
   **What NPM does:**
   - Install packages/libraries (express, axios, etc.)
   - Manage project dependencies
   - Run scripts (start, test, build)
   - Publish your own packages
   - Version management
   
   **Key Files:**
   - `package.json` - Project metadata and dependencies
   - `package-lock.json` - Exact dependency versions
   - `node_modules/` - Installed packages folder
   
   **Common Commands:**
   ```bash
   npm init          # Create package.json
   npm install pkg   # Install package
   npm start         # Run start script
   npm test          # Run tests
   ```

3. **Explain the event-driven architecture of Node.js.**
   - **Answer:** Node.js uses an event-driven, non-blocking I/O model where operations happen asynchronously using events and callbacks.
   
   **How it works:**
   - Event Loop: Continuously checks for events
   - Event Emitter: Triggers events
   - Event Listeners: Handle events when they occur
   - Non-blocking: Doesn't wait for operations to complete
   
   **Example:**
   ```javascript
   const fs = require('fs');
   
   // Non-blocking (event-driven)
   fs.readFile('file.txt', 'utf8', (err, data) => {
       console.log('File read:', data);
   });
   console.log('This runs first!');
   
   // Output:
   // This runs first!
   // File read: [file content]
   ```
   
   **Benefits:**
   - Handles many concurrent connections
   - Efficient resource usage
   - Fast response times
   - Perfect for I/O-heavy applications

---

### Day 23: Node.js Modules & File System

#### 📖 Node.js Module System
Modules help organize code into separate, reusable files.

**Three Types of Modules:**
1. **Core Modules** - Built into Node.js (fs, http, path, os)
2. **Local Modules** - Your own files
3. **Third-Party Modules** - NPM packages

**Creating a Local Module:**

**math.js:**
```javascript
// Method 1: Export individual items
exports.add = (a, b) => a + b;
exports.subtract = (a, b) => a - b;
exports.multiply = (a, b) => a * b;
exports.divide = (a, b) => b !== 0 ? a / b : 'Cannot divide by zero';

// Method 2: Export entire object
module.exports = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b,
    divide: (a, b) => b !== 0 ? a / b : 'Cannot divide by zero',
    PI: 3.14159,
    E: 2.71828
};
```

**app.js:**
```javascript
// Import your module
const math = require('./math');

console.log('5 + 3 =', math.add(5, 3));
console.log('10 - 4 =', math.subtract(10, 4));
console.log('6 * 7 =', math.multiply(6, 7));
console.log('20 / 4 =', math.divide(20, 4));
console.log('PI =', math.PI);
```

**user.js (another example):**
```javascript
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
    
    getInfo() {
        return `${this.name} (${this.email})`;
    }
}

const createUser = (name, email) => {
    return new User(name, email);
};

module.exports = {
    User,
    createUser
};
```

**Using it:**
```javascript
const { User, createUser } = require('./user');

const user1 = new User('John', 'john@example.com');
const user2 = createUser('Sarah', 'sarah@example.com');

console.log(user1.getInfo());
console.log(user2.getInfo());
```

#### 📖 Core Modules

**1. File System (fs) Module:**
```javascript
const fs = require('fs');

// Read file (asynchronous)
fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    console.log('File content:', data);
});

// Write file
fs.writeFile('output.txt', 'Hello, Node.js!', (err) => {
    if (err) throw err;
    console.log('File saved!');
});

// Append to file
fs.appendFile('log.txt', '\nNew log entry', (err) => {
    if (err) throw err;
    console.log('Content appended!');
});

// Check if file exists
fs.access('file.txt', fs.constants.F_OK, (err) => {
    console.log(err ? 'File does not exist' : 'File exists');
});

// Delete file
fs.unlink('temp.txt', (err) => {
    if (err) throw err;
    console.log('File deleted!');
});

// Create directory
fs.mkdir('newFolder', { recursive: true }, (err) => {
    if (err) throw err;
    console.log('Directory created!');
});

// Read directory
fs.readdir('.', (err, files) => {
    if (err) throw err;
    console.log('Files:', files);
});
```

**2. Path Module:**
```javascript
const path = require('path');

// Join paths
const filePath = path.join(__dirname, 'files', 'data.txt');
console.log('Full path:', filePath);

// Get file name
console.log('Filename:', path.basename(filePath));

// Get directory
console.log('Directory:', path.dirname(filePath));

// Get extension
console.log('Extension:', path.extname(filePath));

// Parse path
const parsed = path.parse(filePath);
console.log('Parsed:', parsed);
// { root: '/', dir: '/users/project/files', base: 'data.txt', ext: '.txt', name: 'data' }

// Normalize path
const messyPath = '/users//project/../files/./data.txt';
console.log('Normalized:', path.normalize(messyPath));
```

**3. OS Module:**
```javascript
const os = require('os');

console.log('Platform:', os.platform());
console.log('CPU Architecture:', os.arch());
console.log('CPUs:', os.cpus().length);
console.log('Total Memory:', Math.round(os.totalmem() / 1024 / 1024 / 1024), 'GB');
console.log('Free Memory:', Math.round(os.freemem() / 1024 / 1024 / 1024), 'GB');
console.log('Home Directory:', os.homedir());
console.log('Hostname:', os.hostname());
console.log('Uptime:', Math.round(os.uptime() / 60), 'minutes');
```

#### 📖 Asynchronous Patterns

**1. Callbacks (Traditional):**
```javascript
const fs = require('fs');

fs.readFile('file1.txt', 'utf8', (err, data1) => {
    if (err) {
        console.error(err);
        return;
    }
    
    fs.readFile('file2.txt', 'utf8', (err, data2) => {
        if (err) {
            console.error(err);
            return;
        }
        
        const combined = data1 + data2;
        fs.writeFile('combined.txt', combined, (err) => {
            if (err) {
                console.error(err);
                return;
            }
            console.log('Files combined!');
        });
    });
});
```

**2. Promises (Better):**
```javascript
const fs = require('fs').promises;

fs.readFile('file1.txt', 'utf8')
    .then(data1 => {
        return fs.readFile('file2.txt', 'utf8')
            .then(data2 => data1 + data2);
    })
    .then(combined => {
        return fs.writeFile('combined.txt', combined);
    })
    .then(() => {
        console.log('Files combined!');
    })
    .catch(err => {
        console.error('Error:', err);
    });
```

**3. Async/Await (Best):**
```javascript
const fs = require('fs').promises;

async function combineFiles() {
    try {
        const data1 = await fs.readFile('file1.txt', 'utf8');
        const data2 = await fs.readFile('file2.txt', 'utf8');
        const combined = data1 + data2;
        await fs.writeFile('combined.txt', combined);
        console.log('Files combined!');
    } catch (err) {
        console.error('Error:', err);
    }
}

combineFiles();
```

#### 💡 Complete File Manager Example

**file-manager.js:**
```javascript
const fs = require('fs').promises;
const path = require('path');

class FileManager {
    constructor(baseDir = './files') {
        this.baseDir = baseDir;
    }
    
    // Ensure base directory exists
    async init() {
        try {
            await fs.mkdir(this.baseDir, { recursive: true });
            console.log('✓ File manager initialized');
        } catch (err) {
            console.error('✗ Init error:', err.message);
        }
    }
    
    // Create or overwrite file
    async createFile(filename, content) {
        try {
            const filePath = path.join(this.baseDir, filename);
            await fs.writeFile(filePath, content, 'utf8');
            console.log(`✓ Created: ${filename}`);
            return true;
        } catch (err) {
            console.error(`✗ Error creating ${filename}:`, err.message);
            return false;
        }
    }
    
    // Read file
    async readFile(filename) {
        try {
            const filePath = path.join(this.baseDir, filename);
            const content = await fs.readFile(filePath, 'utf8');
            console.log(`✓ Read: ${filename}`);
            return content;
        } catch (err) {
            console.error(`✗ Error reading ${filename}:`, err.message);
            return null;
        }
    }
    
    // Append to file
    async appendFile(filename, content) {
        try {
            const filePath = path.join(this.baseDir, filename);
            await fs.appendFile(filePath, content, 'utf8');
            console.log(`✓ Appended to: ${filename}`);
            return true;
        } catch (err) {
            console.error(`✗ Error appending to ${filename}:`, err.message);
            return false;
        }
    }
    
    // Delete file
    async deleteFile(filename) {
        try {
            const filePath = path.join(this.baseDir, filename);
            await fs.unlink(filePath);
            console.log(`✓ Deleted: ${filename}`);
            return true;
        } catch (err) {
            console.error(`✗ Error deleting ${filename}:`, err.message);
            return false;
        }
    }
    
    // List all files
    async listFiles() {
        try {
            const files = await fs.readdir(this.baseDir);
            console.log('✓ Files in directory:');
            files.forEach((file, index) => {
                console.log(`  ${index + 1}. ${file}`);
            });
            return files;
        } catch (err) {
            console.error('✗ Error listing files:', err.message);
            return [];
        }
    }
    
    // Get file info
    async getFileInfo(filename) {
        try {
            const filePath = path.join(this.baseDir, filename);
            const stats = await fs.stat(filePath);
            const info = {
                name: filename,
                size: `${stats.size} bytes`,
                created: stats.birthtime,
                modified: stats.mtime,
                isFile: stats.isFile(),
                isDirectory: stats.isDirectory()
            };
            console.log('✓ File info:', info);
            return info;
        } catch (err) {
            console.error(`✗ Error getting info for ${filename}:`, err.message);
            return null;
        }
    }
    
    // Copy file
    async copyFile(source, destination) {
        try {
            const sourcePath = path.join(this.baseDir, source);
            const destPath = path.join(this.baseDir, destination);
            await fs.copyFile(sourcePath, destPath);
            console.log(`✓ Copied ${source} to ${destination}`);
            return true;
        } catch (err) {
            console.error(`✗ Error copying file:`, err.message);
            return false;
        }
    }
    
    // Rename file
    async renameFile(oldName, newName) {
        try {
            const oldPath = path.join(this.baseDir, oldName);
            const newPath = path.join(this.baseDir, newName);
            await fs.rename(oldPath, newPath);
            console.log(`✓ Renamed ${oldName} to ${newName}`);
            return true;
        } catch (err) {
            console.error(`✗ Error renaming file:`, err.message);
            return false;
        }
    }
}

// Demo Usage
async function demo() {
    const fm = new FileManager('./myFiles');
    
    // Initialize
    await fm.init();
    
    // Create files
    await fm.createFile('notes.txt', 'Hello, Node.js!\nThis is my first note.');
    await fm.createFile('todo.txt', '1. Learn Node.js\n2. Build projects\n3. Practice daily');
    
    // Read file
    const content = await fm.readFile('notes.txt');
    console.log('\nFile content:', content);
    
    // Append to file
    await fm.appendFile('notes.txt', '\nThis line was appended!');
    
    // List files
    console.log('\n');
    await fm.listFiles();
    
    // Get file info
    console.log('\n');
    await fm.getFileInfo('notes.txt');
    
    // Copy file
    await fm.copyFile('notes.txt', 'notes-backup.txt');
    
    // Rename file
    await fm.renameFile('todo.txt', 'my-todos.txt');
    
    // List files again
    console.log('\n');
    await fm.listFiles();
    
    // Read updated file
    const updated = await fm.readFile('notes.txt');
    console.log('\nUpdated content:', updated);
}

// Run demo
demo().catch(err => console.error('Demo error:', err));

// Export for use in other files
module.exports = FileManager;
```

**Run it:**
```bash
node file-manager.js
```

**Output:**
```
✓ File manager initialized
✓ Created: notes.txt
✓ Created: todo.txt
✓ Read: notes.txt

File content: Hello, Node.js!
This is my first note.
✓ Appended to: notes.txt

✓ Files in directory:
  1. notes.txt
  2. todo.txt

✓ File info: {
  name: 'notes.txt',
  size: '65 bytes',
  created: 2024-01-15T10:30:00.000Z,
  modified: 2024-01-15T10:30:05.000Z,
  isFile: true,
  isDirectory: false
}
✓ Copied notes.txt to notes-backup.txt
✓ Renamed todo.txt to my-todos.txt

✓ Files in directory:
  1. notes.txt
  2. notes-backup.txt
  3. my-todos.txt
✓ Read: notes.txt

Updated content: Hello, Node.js!
This is my first note.
This line was appended!
```

**Learning Resources:**
- [Node.js File System](https://nodejs.org/dist/latest-v20.x/docs/api/fs.html)
- [JavaScript Promises](https://nodejs.dev/en/learn/understanding-javascript-promises/)
- [Async/Await Guide](https://javascript.info/async-await)

**Hands-on Practice:**
- Build a file manager with all CRUD operations
- Create a logger that writes to log files with timestamps
- Build a JSON database using files
- Create a backup system that copies important files
- Practice converting callbacks to promises to async/await

**Interview Questions:**

1. **Difference between callbacks, promises, and async/await?**
   - **Answer:** Three ways to handle asynchronous operations in JavaScript.
   
   **Callbacks:**
   ```javascript
   fs.readFile('file.txt', (err, data) => {
       if (err) console.error(err);
       else console.log(data);
   });
   ```
   - Oldest approach
   - Can lead to "callback hell"
   - Error handling with if(err)
   
   **Promises:**
   ```javascript
   fs.promises.readFile('file.txt')
       .then(data => console.log(data))
       .catch(err => console.error(err));
   ```
   - Cleaner than callbacks
   - Chainable with .then()
   - Better error handling with .catch()
   
   **Async/Await:**
   ```javascript
   async function read() {
       try {
           const data = await fs.promises.readFile('file.txt');
           console.log(data);
       } catch (err) {
           console.error(err);
       }
   }
   ```
   - Looks synchronous, runs asynchronously
   - Cleanest syntax
   - Try/catch for error handling
   - Must be inside async function

2. **What is the difference between synchronous and asynchronous code?**
   - **Answer:**
   
   **Synchronous (Blocking):**
   ```javascript
   const data = fs.readFileSync('file.txt', 'utf8');
   console.log(data);
   console.log('This waits for file read');
   ```
   - Executes line by line
   - Blocks next operation until current completes
   - Simple but inefficient
   - Can freeze application
   
   **Asynchronous (Non-blocking):**
   ```javascript
   fs.readFile('file.txt', 'utf8', (err, data) => {
       console.log(data);
   });
   console.log('This runs immediately!');
   ```
   - Doesn't wait for operation to complete
   - Continues with next code
   - Uses callbacks/promises/async-await
   - Better performance, handles many operations
   
   | Synchronous | Asynchronous |
   |-------------|--------------|
   | Blocking | Non-blocking |
   | Wait for operation | Don't wait |
   | One task at a time | Multiple tasks |
   | Simple | More complex |
   | Less efficient | More efficient |

3. **How do you handle errors in async/await?**
   - **Answer:** Use try/catch blocks, similar to synchronous error handling.
   
   **Basic Error Handling:**
   ```javascript
   async function readFile() {
       try {
           const data = await fs.promises.readFile('file.txt', 'utf8');
           console.log(data);
       } catch (err) {
           console.error('Error:', err.message);
       }
   }
   ```
   
   **Multiple Operations:**
   ```javascript
   async function processFiles() {
       try {
           const data1 = await fs.promises.readFile('file1.txt', 'utf8');
           const data2 = await fs.promises.readFile('file2.txt', 'utf8');
           await fs.promises.writeFile('output.txt', data1 + data2);
           console.log('Success!');
       } catch (err) {
           console.error('Error:', err.message);
           // All errors caught here
       }
   }
   ```
   
   **With Finally:**
   ```javascript
   async function operation() {
       try {
           await doSomething();
       } catch (err) {
           console.error(err);
       } finally {
           // Always runs (cleanup, closing connections)
           console.log('Cleanup complete');
       }
   }
   ```
   
   **Multiple Catches:**
   ```javascript
   async function robustOperation() {
       try {
           const data = await riskyOperation();
           return data;
       } catch (err) {
           if (err.code === 'ENOENT') {
               console.log('File not found');
           } else if (err.code === 'EACCES') {
               console.log('Permission denied');
           } else {
               console.log('Unknown error:', err);
           }
           throw err; // Re-throw if needed
       }
   }
   ```

---

### Day 24: HTTP Module & Creating Servers

#### 📖 What is HTTP?
HTTP (HyperText Transfer Protocol) is how browsers talk to servers!

**Think of it like:**
- **Client (Browser)** = Person asking a question
- **Server** = Person answering
- **HTTP** = The language they use to communicate

**Request → Response cycle:**
```
Browser: "GET /about page please"
Server: "Here's the about page! (HTML)"
```

#### 📖 HTTP Status Codes
Status codes tell you what happened with the request.

**Common Status Codes:**
- **200** = OK (Success!)
- **201** = Created (New resource created)
- **204** = No Content (Success, but nothing to return)
- **301** = Moved Permanently (Resource moved to new URL)
- **304** = Not Modified (Use cached version)
- **400** = Bad Request (Client sent invalid data)
- **401** = Unauthorized (Need to log in)
- **403** = Forbidden (Logged in but no access)
- **404** = Not Found (Page doesn't exist)
- **500** = Internal Server Error (Server crashed)
- **503** = Service Unavailable (Server down)

**Remember with emoji:**
- 2xx = ✅ Success
- 3xx = ↪️ Redirect
- 4xx = 😕 Client Error
- 5xx = 💥 Server Error

#### 📖 Creating Your First HTTP Server

**simple-server.js:**
```javascript
const http = require('http');

// Create server
const server = http.createServer((req, res) => {
    // req = request from browser
    // res = response we send back
    
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from Node.js server!');
});

// Start server
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
```

**Run it:**
```bash
node simple-server.js
# Visit: http://localhost:3000
```

#### 📖 Sending HTML Response

**html-server.js:**
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    
    const html = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Node.js Server</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: #f0f0f0;
                }
                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 { color: #333; }
                p { color: #666; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Node.js Server! 🚀</h1>
                <p>Current time: ${new Date().toLocaleString()}</p>
                <p>This HTML was generated by Node.js!</p>
            </div>
        </body>
        </html>
    `;
    
    res.end(html);
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
});
```

#### 📖 Routing (Different Pages)

**router-server.js:**
```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    // Log the request
    console.log(`${req.method} ${req.url}`);
    
    // Set content type
    res.setHeader('Content-Type', 'text/html');
    
    // Handle different routes
    if (req.url === '/' || req.url === '/home') {
        res.writeHead(200);
        res.end(`
            <h1>Home Page</h1>
            <nav>
                <a href="/about">About</a> |
                <a href="/contact">Contact</a> |
                <a href="/api/users">API</a>
            </nav>
            <p>Welcome to the home page!</p>
        `);
    }
    else if (req.url === '/about') {
        res.writeHead(200);
        res.end(`
            <h1>About Page</h1>
            <p>This is a Node.js HTTP server.</p>
            <a href="/">Back to Home</a>
        `);
    }
    else if (req.url === '/contact') {
        res.writeHead(200);
        res.end(`
            <h1>Contact Page</h1>
            <p>Email: contact@example.com</p>
            <p>Phone: (555) 123-4567</p>
            <a href="/">Back to Home</a>
        `);
    }
    else if (req.url === '/api/users') {
        // Send JSON response
        res.setHeader('Content-Type', 'application/json');
        res.writeHead(200);
        
        const users = [
            { id: 1, name: 'John Doe', email: 'john@example.com' },
            { id: 2, name: 'Sarah Smith', email: 'sarah@example.com' },
            { id: 3, name: 'Mike Johnson', email: 'mike@example.com' }
        ];
        
        res.end(JSON.stringify(users, null, 2));
    }
    else {
        // 404 Not Found
        res.writeHead(404);
        res.end(`
            <h1>404 - Page Not Found</h1>
            <p>The page you're looking for doesn't exist.</p>
            <a href="/">Go to Home</a>
        `);
    }
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
    console.log('Try these URLs:');
    console.log('  http://localhost:3000/');
    console.log('  http://localhost:3000/about');
    console.log('  http://localhost:3000/contact');
    console.log('  http://localhost:3000/api/users');
});
```

#### 📖 Handling Different HTTP Methods

**methods-server.js:**
```javascript
const http = require('http');

let users = [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Sarah Smith' }
];

const server = http.createServer((req, res) => {
    const { method, url } = req;
    
    // Set CORS headers (for testing with frontend)
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    // GET - Retrieve data
    if (method === 'GET' && url === '/api/users') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(users));
    }
    // POST - Create new data
    else if (method === 'POST' && url === '/api/users') {
        let body = '';
        
        req.on('data', chunk => {
            body += chunk.toString();
        });
        
        req.on('end', () => {
            const newUser = JSON.parse(body);
            newUser.id = users.length + 1;
            users.push(newUser);
            
            res.writeHead(201, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify(newUser));
        });
    }
    // PUT - Update data
    else if (method === 'PUT' && url.startsWith('/api/users/')) {
        const id = parseInt(url.split('/')[3]);
        let body = '';
        
        req.on('data', chunk => {
            body += chunk.toString();
        });
        
        req.on('end', () => {
            const updatedData = JSON.parse(body);
            const index = users.findIndex(u => u.id === id);
            
            if (index !== -1) {
                users[index] = { ...users[index], ...updatedData };
                res.writeHead(200, { 'Content-Type': 'application/json' });
                res.end(JSON.stringify(users[index]));
            } else {
                res.writeHead(404);
                res.end(JSON.stringify({ error: 'User not found' }));
            }
        });
    }
    // DELETE - Remove data
    else if (method === 'DELETE' && url.startsWith('/api/users/')) {
        const id = parseInt(url.split('/')[3]);
        const index = users.findIndex(u => u.id === id);
        
        if (index !== -1) {
            users.splice(index, 1);
            res.writeHead(204); // No content
            res.end();
        } else {
            res.writeHead(404);
            res.end(JSON.stringify({ error: 'User not found' }));
        }
    }
    else {
        res.writeHead(404);
        res.end(JSON.stringify({ error: 'Route not found' }));
    }
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000/');
    console.log('API Endpoints:');
    console.log('  GET    /api/users       - Get all users');
    console.log('  POST   /api/users       - Create user');
    console.log('  PUT    /api/users/:id   - Update user');
    console.log('  DELETE /api/users/:id   - Delete user');
});
```

**Test with curl:**
```bash
# GET all users
curl http://localhost:3000/api/users

# POST new user
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Mike Johnson"}'

# PUT update user
curl -X PUT http://localhost:3000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Updated"}'

# DELETE user
curl -X DELETE http://localhost:3000/api/users/2
```

#### 💡 Complete REST API Server

**rest-api-server.js:**
```javascript
const http = require('http');
const url = require('url');

// In-memory database
let todos = [
    { id: 1, title: 'Learn Node.js', completed: false },
    { id: 2, title: 'Build REST API', completed: false },
    { id: 3, title: 'Practice daily', completed: true }
];

// Helper function to send JSON
function sendJSON(res, statusCode, data) {
    res.writeHead(statusCode, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(data, null, 2));
}

// Helper function to get request body
function getRequestBody(req) {
    return new Promise((resolve, reject) => {
        let body = '';
        req.on('data', chunk => body += chunk.toString());
        req.on('end', () => {
            try {
                resolve(JSON.parse(body));
            } catch (err) {
                reject(err);
            }
        });
    });
}

const server = http.createServer(async (req, res) => {
    const { method } = req;
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;
    const id = pathname.split('/')[3]; // For /api/todos/:id
    
    // Enable CORS
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    // Handle OPTIONS (preflight)
    if (method === 'OPTIONS') {
        res.writeHead(204);
        res.end();
        return;
    }
    
    console.log(`${method} ${pathname}`);
    
    try {
        // GET /api/todos - Get all todos
        if (method === 'GET' && pathname === '/api/todos') {
            sendJSON(res, 200, {
                success: true,
                count: todos.length,
                data: todos
            });
        }
        // GET /api/todos/:id - Get single todo
        else if (method === 'GET' && pathname.startsWith('/api/todos/')) {
            const todo = todos.find(t => t.id === parseInt(id));
            if (todo) {
                sendJSON(res, 200, { success: true, data: todo });
            } else {
                sendJSON(res, 404, { success: false, error: 'Todo not found' });
            }
        }
        // POST /api/todos - Create new todo
        else if (method === 'POST' && pathname === '/api/todos') {
            const body = await getRequestBody(req);
            
            if (!body.title) {
                sendJSON(res, 400, { success: false, error: 'Title is required' });
                return;
            }
            
            const newTodo = {
                id: todos.length + 1,
                title: body.title,
                completed: body.completed || false
            };
            
            todos.push(newTodo);
            sendJSON(res, 201, { success: true, data: newTodo });
        }
        // PUT /api/todos/:id - Update todo
        else if (method === 'PUT' && pathname.startsWith('/api/todos/')) {
            const body = await getRequestBody(req);
            const index = todos.findIndex(t => t.id === parseInt(id));
            
            if (index === -1) {
                sendJSON(res, 404, { success: false, error: 'Todo not found' });
                return;
            }
            
            todos[index] = {
                ...todos[index],
                title: body.title || todos[index].title,
                completed: body.completed !== undefined ? body.completed : todos[index].completed
            };
            
            sendJSON(res, 200, { success: true, data: todos[index] });
        }
        // DELETE /api/todos/:id - Delete todo
        else if (method === 'DELETE' && pathname.startsWith('/api/todos/')) {
            const index = todos.findIndex(t => t.id === parseInt(id));
            
            if (index === -1) {
                sendJSON(res, 404, { success: false, error: 'Todo not found' });
                return;
            }
            
            const deleted = todos.splice(index, 1)[0];
            sendJSON(res, 200, { success: true, data: deleted });
        }
        // GET / - API Documentation
        else if (method === 'GET' && pathname === '/') {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(`
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Todos REST API</title>
                    <style>
                        body { font-family: Arial; max-width: 800px; margin: 50px auto; }
                        h1 { color: #333; }
                        .endpoint { background: #f0f0f0; padding: 15px; margin: 10px 0; border-radius: 5px; }
                        .method { display: inline-block; padding: 5px 10px; border-radius: 3px; color: white; font-weight: bold; }
                        .get { background: #61affe; }
                        .post { background: #49cc90; }
                        .put { background: #fca130; }
                        .delete { background: #f93e3e; }
                    </style>
                </head>
                <body>
                    <h1>📝 Todos REST API</h1>
                    <p>Simple REST API for managing todos</p>
                    
                    <h2>Endpoints:</h2>
                    
                    <div class="endpoint">
                        <span class="method get">GET</span>
                        <strong>/api/todos</strong>
                        <p>Get all todos</p>
                    </div>
                    
                    <div class="endpoint">
                        <span class="method get">GET</span>
                        <strong>/api/todos/:id</strong>
                        <p>Get single todo by ID</p>
                    </div>
                    
                    <div class="endpoint">
                        <span class="method post">POST</span>
                        <strong>/api/todos</strong>
                        <p>Create new todo</p>
                        <pre>{ "title": "Todo title", "completed": false }</pre>
                    </div>
                    
                    <div class="endpoint">
                        <span class="method put">PUT</span>
                        <strong>/api/todos/:id</strong>
                        <p>Update todo</p>
                        <pre>{ "title": "Updated title", "completed": true }</pre>
                    </div>
                    
                    <div class="endpoint">
                        <span class="method delete">DELETE</span>
                        <strong>/api/todos/:id</strong>
                        <p>Delete todo</p>
                    </div>
                    
                    <h2>Current Todos:</h2>
                    <pre>${JSON.stringify(todos, null, 2)}</pre>
                </body>
                </html>
            `);
        }
        else {
            sendJSON(res, 404, { success: false, error: 'Route not found' });
        }
    } catch (err) {
        console.error('Server error:', err);
        sendJSON(res, 500, { success: false, error: 'Internal server error' });
    }
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`\n🚀 Server running at http://localhost:${PORT}/\n`);
    console.log('API Endpoints:');
    console.log('  GET    http://localhost:3000/api/todos');
    console.log('  GET    http://localhost:3000/api/todos/:id');
    console.log('  POST   http://localhost:3000/api/todos');
    console.log('  PUT    http://localhost:3000/api/todos/:id');
    console.log('  DELETE http://localhost:3000/api/todos/:id\n');
});
```

**Learning Resources:**
- [Node.js HTTP Module](https://nodejs.org/dist/latest-v20.x/docs/api/http.html)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [REST API Design](https://restfulapi.net/)

**Hands-on Practice:**
- Create an HTTP server with multiple routes
- Build a simple REST API for books or movies
- Implement all CRUD operations (Create, Read, Update, Delete)
- Add proper status codes and error handling
- Test your API with Postman or curl

**Interview Questions:**

1. **What is the HTTP module in Node.js?**
   - **Answer:** The HTTP module is a built-in Node.js module that allows you to create web servers and make HTTP requests.
   
   **Key Features:**
   - Create HTTP servers (`http.createServer()`)
   - Handle requests and responses
   - Set headers and status codes
   - Parse URLs and query parameters
   - Make HTTP requests to other servers
   
   **Example:**
   ```javascript
   const http = require('http');
   
   const server = http.createServer((req, res) => {
       res.writeHead(200, { 'Content-Type': 'text/plain' });
       res.end('Hello World!');
   });
   
   server.listen(3000);
   ```
   
   **Why use it:** Foundation for web frameworks like Express.js. Understanding HTTP module helps you understand how web servers work.

2. **Explain common HTTP status codes.**
   - **Answer:** HTTP status codes indicate the result of an HTTP request.
   
   **Categories:**
   - **1xx** - Informational (100 Continue)
   - **2xx** - Success (200 OK, 201 Created)
   - **3xx** - Redirection (301 Moved, 304 Not Modified)
   - **4xx** - Client Errors (400 Bad Request, 404 Not Found, 401 Unauthorized)
   - **5xx** - Server Errors (500 Internal Error, 503 Service Unavailable)
   
   **Common Codes:**
   ```javascript
   // 200 - Success
   res.writeHead(200);
   res.end(JSON.stringify(data));
   
   // 201 - Created
   res.writeHead(201);
   res.end(JSON.stringify(newItem));
   
   // 400 - Bad Request
   res.writeHead(400);
   res.end(JSON.stringify({ error: 'Invalid data' }));
   
   // 404 - Not Found
   res.writeHead(404);
   res.end(JSON.stringify({ error: 'Not found' }));
   
   // 500 - Server Error
   res.writeHead(500);
   res.end(JSON.stringify({ error: 'Server error' }));
   ```
   
   **When to use:**
   - 200/201: Successful operations
   - 400: Invalid client input
   - 401/403: Authentication/authorization issues
   - 404: Resource doesn't exist
   - 500: Something went wrong on server

3. **How do you handle different routes in Node.js?**
   - **Answer:** Check the `req.url` property and use conditional statements to route to different handlers.
   
   **Basic Routing:**
   ```javascript
   const server = http.createServer((req, res) => {
       if (req.url === '/') {
           res.end('Home Page');
       } else if (req.url === '/about') {
           res.end('About Page');
       } else if (req.url === '/api/users') {
           res.end(JSON.stringify(users));
       } else {
           res.writeHead(404);
           res.end('Not Found');
       }
   });
   ```
   
   **With HTTP Methods:**
   ```javascript
   const { method, url } = req;
   
   if (method === 'GET' && url === '/api/users') {
       // Get all users
   } else if (method === 'POST' && url === '/api/users') {
       // Create user
   } else if (method === 'DELETE' && url.startsWith('/api/users/')) {
       const id = url.split('/')[3];
       // Delete user
   }
   ```
   
   **With URL Parameters:**
   ```javascript
   const url = require('url');
   const parsedUrl = url.parse(req.url, true);
   
   if (parsedUrl.pathname === '/api/users') {
       const id = parsedUrl.query.id; // ?id=123
   }
   ```
   
   **Better approach:** Use Express.js framework for complex routing!

---

### Day 25: Environment Variables & Best Practices

#### 📖 What are Environment Variables?
Environment variables store configuration outside your code - like passwords, API keys, database URLs.

**Think of them like:**
- **Hardcoded** = Writing your password directly in code (❌ Bad!)
- **Environment Variables** = Keeping passwords in a secure place (✅ Good!)

**Why use them?**
- 🔒 **Security** - Keep secrets out of code
- 🔄 **Flexibility** - Different settings for dev/production
- 👥 **Team Work** - Everyone has their own local settings
- 🚀 **Deployment** - Easy to configure on different servers

#### 📖 Using Environment Variables in Node.js

**Built-in way (process.env):**
```javascript
// Access environment variables
const port = process.env.PORT || 3000;
const environment = process.env.NODE_ENV || 'development';
const apiKey = process.env.API_KEY;

console.log('Port:', port);
console.log('Environment:', environment);
console.log('API Key:', apiKey);
```

**Run with environment variables:**
```bash
# Mac/Linux
PORT=5000 NODE_ENV=production node server.js

# Windows (CMD)
set PORT=5000 && set NODE_ENV=production && node server.js

# Windows (PowerShell)
$env:PORT="5000"; $env:NODE_ENV="production"; node server.js
```

#### 📖 Using dotenv Package (Better Way)

**Install dotenv:**
```bash
npm install dotenv
```

**Create .env file:**
```bash
# .env
PORT=3000
NODE_ENV=development
DATABASE_URL=mongodb://localhost:27017/myapp
API_KEY=your_secret_api_key_here
JWT_SECRET=super_secret_jwt_key
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password
```

**Load in your app:**
```javascript
// At the very top of your main file
require('dotenv').config();

// Now use variables
const PORT = process.env.PORT || 3000;
const dbURL = process.env.DATABASE_URL;
const apiKey = process.env.API_KEY;

console.log('Server will run on port:', PORT);
console.log('Database URL:', dbURL);
```

**IMPORTANT: Add .env to .gitignore:**
```bash
# .gitignore
node_modules/
.env
*.log
```

#### 📖 Creating .env.example
Create an example file for your team (WITHOUT sensitive data):

**.env.example:**
```bash
# Server Configuration
PORT=3000
NODE_ENV=development

# Database
DATABASE_URL=mongodb://localhost:27017/myapp

# API Keys (get from: https://example.com/api-keys)
API_KEY=your_api_key_here
JWT_SECRET=your_jwt_secret_here

# Email Configuration
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_password_here
```

**Team members copy it:**
```bash
cp .env.example .env
# Then fill in their own values
```

#### 💡 Complete Server with Environment Variables

**config.js:**
```javascript
require('dotenv').config();

const config = {
    // Server
    port: process.env.PORT || 3000,
    environment: process.env.NODE_ENV || 'development',
    
    // Database
    database: {
        url: process.env.DATABASE_URL || 'mongodb://localhost:27017/myapp',
        options: {
            useNewUrlParser: true,
            useUnifiedTopology: true
        }
    },
    
    // Authentication
    jwt: {
        secret: process.env.JWT_SECRET || 'fallback_secret_key',
        expiresIn: '24h'
    },
    
    // API Keys
    apiKeys: {
        stripe: process.env.STRIPE_API_KEY,
        sendgrid: process.env.SENDGRID_API_KEY,
        aws: process.env.AWS_ACCESS_KEY
    },
    
    // Email
    email: {
        user: process.env.EMAIL_USER,
        password: process.env.EMAIL_PASS,
        host: 'smtp.gmail.com',
        port: 587
    },
    
    // Frontend URL (for CORS)
    frontendURL: process.env.FRONTEND_URL || 'http://localhost:4200'
};

// Validate required variables
function validateConfig() {
    const required = ['PORT', 'DATABASE_URL', 'JWT_SECRET'];
    const missing = required.filter(key => !process.env[key]);
    
    if (missing.length > 0) {
        console.error('❌ Missing required environment variables:', missing);
        process.exit(1);
    }
    
    console.log('✅ All required environment variables are set');
}

// Only validate in production
if (config.environment === 'production') {
    validateConfig();
}

module.exports = config;
```

**server.js:**
```javascript
const http = require('http');
const config = require('./config');

const server = http.createServer((req, res) => {
    const { method, url } = req;
    
    // Enable CORS
    res.setHeader('Access-Control-Allow-Origin', config.frontendURL);
    res.setHeader('Content-Type', 'application/json');
    
    // Root endpoint
    if (method === 'GET' && url === '/') {
        res.writeHead(200);
        res.end(JSON.stringify({
            message: 'API is running!',
            environment: config.environment,
            port: config.port,
            timestamp: new Date()
        }));
    }
    // Health check
    else if (method === 'GET' && url === '/health') {
        res.writeHead(200);
        res.end(JSON.stringify({
            status: 'healthy',
            database: config.database.url ? 'connected' : 'not configured',
            uptime: process.uptime()
        }));
    }
    // Config info (be careful in production!)
    else if (method === 'GET' && url === '/config') {
        if (config.environment === 'production') {
            res.writeHead(403);
            res.end(JSON.stringify({ error: 'Forbidden in production' }));
        } else {
            res.writeHead(200);
            res.end(JSON.stringify({
                environment: config.environment,
                port: config.port,
                database: config.database.url,
                // Never expose secrets!
                jwt: { configured: !!config.jwt.secret },
                apiKeys: {
                    stripe: config.apiKeys.stripe ? 'configured' : 'not set',
                    sendgrid: config.apiKeys.sendgrid ? 'configured' : 'not set'
                }
            }, null, 2));
        }
    }
    else {
        res.writeHead(404);
        res.end(JSON.stringify({ error: 'Route not found' }));
    }
});

// Start server
server.listen(config.port, () => {
    console.log('\n🚀 Server started successfully!\n');
    console.log(`Environment: ${config.environment}`);
    console.log(`Port: ${config.port}`);
    console.log(`Database: ${config.database.url}`);
    console.log(`Frontend URL: ${config.frontendURL}`);
    console.log(`\nServer running at http://localhost:${config.port}/\n`);
});

// Handle errors
server.on('error', (err) => {
    if (err.code === 'EADDRINUSE') {
        console.error(`❌ Port ${config.port} is already in use`);
        console.log('Try changing PORT in .env file');
    } else {
        console.error('❌ Server error:', err);
    }
    process.exit(1);
});
```

**.env:**
```bash
# Server
PORT=3000
NODE_ENV=development

# Database
DATABASE_URL=mongodb://localhost:27017/myapp

# Security
JWT_SECRET=my_super_secret_jwt_key_12345

# API Keys
STRIPE_API_KEY=sk_test_abc123
SENDGRID_API_KEY=SG.xyz789

# Frontend
FRONTEND_URL=http://localhost:4200
```

**.gitignore:**
```bash
# Dependencies
node_modules/

# Environment variables
.env
.env.local
.env.production

# Logs
*.log
npm-debug.log*

# OS
.DS_Store
Thumbs.db
```

#### 📖 Best Practices

**1. Never commit secrets:**
```bash
# ❌ BAD - Hardcoded secret
const apiKey = 'sk_live_abc123xyz789';

# ✅ GOOD - From environment
const apiKey = process.env.API_KEY;
```

**2. Always have defaults:**
```javascript
const port = process.env.PORT || 3000;
const env = process.env.NODE_ENV || 'development';
```

**3. Validate critical variables:**
```javascript
if (!process.env.DATABASE_URL) {
    throw new Error('DATABASE_URL is required!');
}
```

**4. Use different configs for different environments:**
```javascript
const config = {
    development: {
        database: 'mongodb://localhost:27017/dev',
        logLevel: 'debug'
    },
    production: {
        database: process.env.DATABASE_URL,
        logLevel: 'error'
    }
};

const currentConfig = config[process.env.NODE_ENV || 'development'];
```

**5. Document your .env file:**
```bash
# .env.example with comments
# Port for the server (default: 3000)
PORT=3000

# Environment: development, staging, production
NODE_ENV=development

# Database connection string
# Get from: https://cloud.mongodb.com
DATABASE_URL=mongodb://localhost:27017/myapp

# JWT secret for authentication
# Generate with: node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
JWT_SECRET=your_secret_here
```

**6. Generate secure secrets:**
```bash
# Generate random secret
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

#### 💡 Different Environments Example

**config/development.js:**
```javascript
module.exports = {
    database: 'mongodb://localhost:27017/myapp_dev',
    apiURL: 'http://localhost:3000',
    logLevel: 'debug',
    cache: false
};
```

**config/production.js:**
```javascript
module.exports = {
    database: process.env.DATABASE_URL,
    apiURL: process.env.API_URL,
    logLevel: 'error',
    cache: true
};
```

**config/index.js:**
```javascript
require('dotenv').config();

const env = process.env.NODE_ENV || 'development';
const config = require(`./${env}`);

module.exports = {
    ...config,
    environment: env,
    port: process.env.PORT || 3000
};
```

**Learning Resources:**
- [dotenv npm package](https://www.npmjs.com/package/dotenv)
- [The Twelve-Factor App](https://12factor.net/config)
- [Environment Variables Guide](https://www.freecodecamp.org/news/how-to-use-environment-variables-in-node-js/)

**Hands-on Practice:**
- Create a `.env` file with PORT, DATABASE_URL, API_KEY
- Load variables with dotenv
- Create a config.js file that exports all configuration
- Build a server that uses environment variables
- Add .env to .gitignore and create .env.example
- Generate a secure JWT secret using crypto

**Interview Questions:**

1. **Why are environment variables important?**
   - **Answer:** Environment variables keep sensitive data out of your codebase and allow different configurations for different environments.
   
   **Why important:**
   - **Security:** Passwords, API keys stay out of code
   - **Flexibility:** Different settings for dev/staging/production
   - **Team collaboration:** Each dev has their own local config
   - **Deployment:** Easy to configure on different servers
   - **Version control:** No secrets in Git history
   
   **Example:**
   ```javascript
   // ❌ Bad - Secret in code
   const apiKey = 'sk_live_1234567890';
   
   // ✅ Good - Secret in environment
   const apiKey = process.env.API_KEY;
   ```
   
   **What to store:**
   - Database URLs
   - API keys
   - JWT secrets
   - Email passwords
   - Port numbers
   - Environment names (dev/prod)

2. **How do you use environment variables in Node.js?**
   - **Answer:** Use `process.env` to access variables, and dotenv package to load them from a .env file.
   
   **Method 1: Direct access**
   ```javascript
   const port = process.env.PORT;
   ```
   
   **Method 2: With dotenv**
   ```javascript
   // Install: npm install dotenv
   require('dotenv').config();
   
   const config = {
       port: process.env.PORT || 3000,
       database: process.env.DATABASE_URL,
       apiKey: process.env.API_KEY
   };
   ```
   
   **.env file:**
   ```bash
   PORT=3000
   DATABASE_URL=mongodb://localhost:27017/myapp
   API_KEY=abc123
   ```
   
   **Best practices:**
   - Load dotenv at the very top
   - Provide default values with ||
   - Validate critical variables
   - Never commit .env file
   - Create .env.example for team

3. **What should never be committed to Git?**
   - **Answer:** Any sensitive data, secrets, or environment-specific files should never be in Git.
   
   **Never commit:**
   - `.env` - Environment variables
   - API keys and passwords
   - Database credentials
   - JWT secrets
   - OAuth client secrets
   - AWS/Cloud credentials
   - SSH private keys
   - `node_modules/` - Dependencies
   - Build artifacts
   - Log files
   - OS-specific files (.DS_Store)
   
   **.gitignore example:**
   ```bash
   # Environment
   .env
   .env.local
   .env.production
   
   # Dependencies
   node_modules/
   
   # Logs
   *.log
   logs/
   
   # Build
   dist/
   build/
   
   # OS
   .DS_Store
   Thumbs.db
   
   # IDE
   .vscode/
   .idea/
   ```
   
   **What to commit:**
   - `.env.example` - Template without secrets
   - `config/` - Configuration structure
   - Code and documentation
   - package.json and package-lock.json
   
   **If you accidentally commit secrets:**
   1. Change the compromised secrets immediately
   2. Remove from Git history (git filter-branch)
   3. Force push (dangerous!)
   4. Better: Use tools like BFG Repo-Cleaner

---

### Day 26: Mini Project - Node.js CLI Tool

#### 📖 What is a CLI Tool?
CLI (Command Line Interface) tools are programs you run in the terminal - like `npm`, `git`, `node`.

**Examples you already use:**
- `npm install` - NPM is a CLI tool
- `git commit` - Git is a CLI tool
- `node app.js` - Node is a CLI tool

**We'll build:** A Task Manager CLI tool!

#### 📖 CLI Tool Features
Our task manager will support:
```bash
node todo.js list                    # Show all tasks
node todo.js add "Buy groceries"     # Add new task
node todo.js complete 1              # Mark task as done
node todo.js delete 2                # Delete task
node todo.js filter --status=pending # Filter tasks
```

#### 💡 Complete CLI Task Manager

**Install dependencies:**
```bash
npm init -y
npm install chalk@4.1.2 commander
```

**tasks.json (data file):**
```json
[
  {
    "id": 1,
    "title": "Learn Node.js",
    "status": "completed",
    "createdAt": "2024-01-10T10:00:00.000Z"
  },
  {
    "id": 2,
    "title": "Build CLI tool",
    "status": "pending",
    "createdAt": "2024-01-11T14:30:00.000Z"
  },
  {
    "id": 3,
    "title": "Practice daily",
    "status": "pending",
    "createdAt": "2024-01-12T09:15:00.000Z"
  }
]
```

**todo.js (Complete CLI Tool):**
```javascript
#!/usr/bin/env node

const fs = require('fs').promises;
const path = require('path');
const chalk = require('chalk');
const { Command } = require('commander');

const program = new Command();
const TASKS_FILE = path.join(__dirname, 'tasks.json');

// Helper: Read tasks from file
async function loadTasks() {
    try {
        const data = await fs.readFile(TASKS_FILE, 'utf8');
        return JSON.parse(data);
    } catch (err) {
        if (err.code === 'ENOENT') {
            // File doesn't exist, create it
            await saveTasks([]);
            return [];
        }
        throw err;
    }
}

// Helper: Save tasks to file
async function saveTasks(tasks) {
    await fs.writeFile(TASKS_FILE, JSON.stringify(tasks, null, 2));
}

// Helper: Get next ID
function getNextId(tasks) {
    if (tasks.length === 0) return 1;
    return Math.max(...tasks.map(t => t.id)) + 1;
}

// Helper: Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}

// Command: List all tasks
async function listTasks(options) {
    try {
        let tasks = await loadTasks();
        
        // Filter by status if provided
        if (options.status) {
            tasks = tasks.filter(t => t.status === options.status);
        }
        
        if (tasks.length === 0) {
            console.log(chalk.yellow('📝 No tasks found!'));
            return;
        }
        
        console.log(chalk.blue.bold('\n📋 Your Tasks:\n'));
        
        tasks.forEach(task => {
            const icon = task.status === 'completed' ? '✅' : '⏳';
            const statusColor = task.status === 'completed' ? chalk.green : chalk.yellow;
            const idStr = chalk.gray(`[${task.id}]`);
            const title = task.status === 'completed' 
                ? chalk.strikethrough(task.title)
                : chalk.white(task.title);
            
            console.log(`${icon} ${idStr} ${title}`);
            console.log(chalk.gray(`   Status: ${statusColor(task.status)} | Created: ${formatDate(task.createdAt)}\n`));
        });
        
        const completed = tasks.filter(t => t.status === 'completed').length;
        const pending = tasks.filter(t => t.status === 'pending').length;
        
        console.log(chalk.cyan(`Total: ${tasks.length} | Completed: ${completed} | Pending: ${pending}\n`));
    } catch (err) {
        console.error(chalk.red('❌ Error loading tasks:', err.message));
    }
}

// Command: Add new task
async function addTask(title) {
    try {
        const tasks = await loadTasks();
        
        const newTask = {
            id: getNextId(tasks),
            title: title,
            status: 'pending',
            createdAt: new Date().toISOString()
        };
        
        tasks.push(newTask);
        await saveTasks(tasks);
        
        console.log(chalk.green('\n✅ Task added successfully!'));
        console.log(chalk.gray(`   ID: ${newTask.id}`));
        console.log(chalk.white(`   Title: ${newTask.title}\n`));
    } catch (err) {
        console.error(chalk.red('❌ Error adding task:', err.message));
    }
}

// Command: Complete task
async function completeTask(id) {
    try {
        const tasks = await loadTasks();
        const task = tasks.find(t => t.id === parseInt(id));
        
        if (!task) {
            console.log(chalk.red(`\n❌ Task with ID ${id} not found!\n`));
            return;
        }
        
        if (task.status === 'completed') {
            console.log(chalk.yellow(`\n⚠️  Task "${task.title}" is already completed!\n`));
            return;
        }
        
        task.status = 'completed';
        task.completedAt = new Date().toISOString();
        
        await saveTasks(tasks);
        
        console.log(chalk.green('\n✅ Task marked as completed!'));
        console.log(chalk.white(`   "${task.title}"\n`));
    } catch (err) {
        console.error(chalk.red('❌ Error completing task:', err.message));
    }
}

// Command: Delete task
async function deleteTask(id) {
    try {
        const tasks = await loadTasks();
        const index = tasks.findIndex(t => t.id === parseInt(id));
        
        if (index === -1) {
            console.log(chalk.red(`\n❌ Task with ID ${id} not found!\n`));
            return;
        }
        
        const deletedTask = tasks.splice(index, 1)[0];
        await saveTasks(tasks);
        
        console.log(chalk.green('\n✅ Task deleted successfully!'));
        console.log(chalk.gray(`   "${deletedTask.title}"\n`));
    } catch (err) {
        console.error(chalk.red('❌ Error deleting task:', err.message));
    }
}

// Command: Clear all completed tasks
async function clearCompleted() {
    try {
        const tasks = await loadTasks();
        const remaining = tasks.filter(t => t.status !== 'completed');
        const deletedCount = tasks.length - remaining.length;
        
        if (deletedCount === 0) {
            console.log(chalk.yellow('\n⚠️  No completed tasks to clear!\n'));
            return;
        }
        
        await saveTasks(remaining);
        
        console.log(chalk.green(`\n✅ Cleared ${deletedCount} completed task(s)!\n`));
    } catch (err) {
        console.error(chalk.red('❌ Error clearing tasks:', err.message));
    }
}

// Configure CLI
program
    .name('todo')
    .description(chalk.blue('📝 Simple Task Manager CLI'))
    .version('1.0.0');

// List command
program
    .command('list')
    .description('List all tasks')
    .option('-s, --status <status>', 'Filter by status (pending/completed)')
    .action(listTasks);

// Add command
program
    .command('add <title>')
    .description('Add a new task')
    .action(addTask);

// Complete command
program
    .command('complete <id>')
    .description('Mark a task as completed')
    .action(completeTask);

// Delete command
program
    .command('delete <id>')
    .description('Delete a task')
    .action(deleteTask);

// Clear command
program
    .command('clear')
    .description('Clear all completed tasks')
    .action(clearCompleted);

// Parse arguments
program.parse(process.argv);

// Show help if no command provided
if (!process.argv.slice(2).length) {
    program.outputHelp();
}
```

**Make it executable (optional):**
```bash
chmod +x todo.js
```

**Add to package.json:**
```json
{
  "name": "task-manager-cli",
  "version": "1.0.0",
  "description": "Simple CLI task manager",
  "main": "todo.js",
  "bin": {
    "todo": "./todo.js"
  },
  "scripts": {
    "start": "node todo.js"
  },
  "keywords": ["cli", "todo", "tasks"],
  "author": "Your Name",
  "license": "MIT",
  "dependencies": {
    "chalk": "^4.1.2",
    "commander": "^9.4.1"
  }
}
```

**Usage Examples:**
```bash
# List all tasks
node todo.js list

# List only pending tasks
node todo.js list --status pending

# Add new task
node todo.js add "Learn Express.js"
node todo.js add "Build REST API"

# Complete task
node todo.js complete 2

# Delete task
node todo.js delete 3

# Clear all completed
node todo.js clear

# Show help
node todo.js --help
```

**Expected Output:**
```
📋 Your Tasks:

⏳ [1] Learn Node.js
   Status: pending | Created: 1/10/2024, 10:00:00 AM

✅ [2] Build CLI tool
   Status: completed | Created: 1/11/2024, 2:30:00 PM

⏳ [3] Practice daily
   Status: pending | Created: 1/12/2024, 9:15:00 AM

Total: 3 | Completed: 1 | Pending: 2
```

**Key Learning Points:**
- ✅ Reading/writing JSON files
- ✅ Command-line argument parsing
- ✅ Colorful terminal output
- ✅ Error handling
- ✅ Async/await with file system
- ✅ Array methods (filter, find, map)

**Extensions to try:**
- Add task priority (low, medium, high)
- Add task categories/tags
- Add search functionality
- Export tasks to CSV
- Add task editing
- Add due dates and reminders

---

## Module 7: Express.js Framework (Days 27-30)

### Day 27: Introduction to Express.js

#### 📖 What is Express.js?
Express.js is a **web framework** for Node.js that makes building web servers and APIs much easier!

**Think of it like:**
- **Plain Node.js** = Building a house with raw materials (hard!)
- **Express.js** = Building with pre-made tools and blueprints (easy!)

**Why Express?**
- 🚀 **Fast & Minimalist** - Lightweight and flexible
- 🛣️ **Routing** - Easy URL routing
- 🔧 **Middleware** - Powerful plugin system
- 📦 **Popular** - Most used Node.js framework
- 🎯 **REST APIs** - Perfect for building APIs
- 🌐 **Full Stack** - Works with React, Angular, Vue

**Comparison:**
```javascript
// Plain Node.js (verbose)
const http = require('http');
const server = http.createServer((req, res) => {
    if (req.url === '/' && req.method === 'GET') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ message: 'Hello' }));
    }
});

// Express.js (clean!)
const express = require('express');
const app = express();
app.get('/', (req, res) => {
    res.json({ message: 'Hello' });
});
```

#### 📖 Installing Express

```bash
# Create project
mkdir my-express-app
cd my-express-app
npm init -y

# Install Express
npm install express

# Install nodemon (for development)
npm install --save-dev nodemon
```

**Update package.json scripts:**
```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  }
}
```

#### 📖 Your First Express Server

**server.js:**
```javascript
const express = require('express');

// Create Express app
const app = express();

// Define routes
app.get('/', (req, res) => {
    res.send('Hello from Express!');
});

app.get('/about', (req, res) => {
    res.send('About Page');
});

app.get('/api/users', (req, res) => {
    res.json([
        { id: 1, name: 'John' },
        { id: 2, name: 'Sarah' }
    ]);
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
```

**Run it:**
```bash
npm run dev
# Visit: http://localhost:3000
```

#### 📖 Express Routing

**Basic Routes:**
```javascript
const express = require('express');
const app = express();

// GET request
app.get('/', (req, res) => {
    res.send('GET request to homepage');
});

// POST request
app.post('/api/users', (req, res) => {
    res.send('POST request to create user');
});

// PUT request
app.put('/api/users/:id', (req, res) => {
    res.send('PUT request to update user');
});

// DELETE request
app.delete('/api/users/:id', (req, res) => {
    res.send('DELETE request to delete user');
});

// Handle all HTTP methods
app.all('/secret', (req, res) => {
    res.send('Access granted to secret area');
});
```

**Route Parameters:**
```javascript
// URL: /users/123
app.get('/users/:id', (req, res) => {
    const userId = req.params.id;
    res.json({ userId, message: `User ${userId}` });
});

// URL: /posts/hello-world/comments/5
app.get('/posts/:postId/comments/:commentId', (req, res) => {
    const { postId, commentId } = req.params;
    res.json({ postId, commentId });
});

// Optional parameter
app.get('/users/:id?', (req, res) => {
    if (req.params.id) {
        res.send(`User ${req.params.id}`);
    } else {
        res.send('All users');
    }
});
```

**Query Parameters:**
```javascript
// URL: /search?q=nodejs&page=2&limit=10
app.get('/search', (req, res) => {
    const { q, page, limit } = req.query;
    res.json({
        search: q,
        page: page || 1,
        limit: limit || 20
    });
});

// URL: /products?category=electronics&sort=price&order=asc
app.get('/products', (req, res) => {
    const { category, sort, order } = req.query;
    res.json({ category, sort, order });
});
```

**Response Methods:**
```javascript
app.get('/demo', (req, res) => {
    // Send string
    res.send('Hello World');
    
    // Send JSON
    res.json({ message: 'Success', data: [] });
    
    // Send status code
    res.status(404).send('Not Found');
    res.sendStatus(200); // Sends "OK"
    
    // Redirect
    res.redirect('/new-url');
    res.redirect(301, '/permanent-redirect');
    
    // Download file
    res.download('/path/to/file.pdf');
    
    // Render HTML (with template engine)
    res.render('index', { title: 'Home' });
});
```

#### 💡 Complete Express REST API Example

**server.js:**
```javascript
const express = require('express');
const app = express();

// Middleware to parse JSON
app.use(express.json());

// In-memory database
let users = [
    { id: 1, name: 'John Doe', email: 'john@example.com', age: 25 },
    { id: 2, name: 'Sarah Smith', email: 'sarah@example.com', age: 30 },
    { id: 3, name: 'Mike Johnson', email: 'mike@example.com', age: 28 }
];

// Helper function to get next ID
const getNextId = () => {
    return users.length > 0 ? Math.max(...users.map(u => u.id)) + 1 : 1;
};

// GET / - API Documentation
app.get('/', (req, res) => {
    res.json({
        message: 'Welcome to Users API',
        version: '1.0.0',
        endpoints: {
            'GET /api/users': 'Get all users',
            'GET /api/users/:id': 'Get user by ID',
            'POST /api/users': 'Create new user',
            'PUT /api/users/:id': 'Update user',
            'DELETE /api/users/:id': 'Delete user'
        }
    });
});

// GET /api/users - Get all users (with optional filtering)
app.get('/api/users', (req, res) => {
    const { age, name } = req.query;
    
    let filteredUsers = users;
    
    // Filter by age
    if (age) {
        filteredUsers = filteredUsers.filter(u => u.age === parseInt(age));
    }
    
    // Search by name
    if (name) {
        filteredUsers = filteredUsers.filter(u => 
            u.name.toLowerCase().includes(name.toLowerCase())
        );
    }
    
    res.json({
        success: true,
        count: filteredUsers.length,
        data: filteredUsers
    });
});

// GET /api/users/:id - Get single user
app.get('/api/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return res.status(404).json({
            success: false,
            error: 'User not found'
        });
    }
    
    res.json({
        success: true,
        data: user
    });
});

// POST /api/users - Create new user
app.post('/api/users', (req, res) => {
    const { name, email, age } = req.body;
    
    // Validation
    if (!name || !email) {
        return res.status(400).json({
            success: false,
            error: 'Name and email are required'
        });
    }
    
    // Check if email already exists
    const existingUser = users.find(u => u.email === email);
    if (existingUser) {
        return res.status(400).json({
            success: false,
            error: 'Email already exists'
        });
    }
    
    const newUser = {
        id: getNextId(),
        name,
        email,
        age: age || null
    };
    
    users.push(newUser);
    
    res.status(201).json({
        success: true,
        message: 'User created successfully',
        data: newUser
    });
});

// PUT /api/users/:id - Update user
app.put('/api/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return res.status(404).json({
            success: false,
            error: 'User not found'
        });
    }
    
    const { name, email, age } = req.body;
    
    // Update fields
    if (name) user.name = name;
    if (email) user.email = email;
    if (age !== undefined) user.age = age;
    
    res.json({
        success: true,
        message: 'User updated successfully',
        data: user
    });
});

// DELETE /api/users/:id - Delete user
app.delete('/api/users/:id', (req, res) => {
    const index = users.findIndex(u => u.id === parseInt(req.params.id));
    
    if (index === -1) {
        return res.status(404).json({
            success: false,
            error: 'User not found'
        });
    }
    
    const deletedUser = users.splice(index, 1)[0];
    
    res.json({
        success: true,
        message: 'User deleted successfully',
        data: deletedUser
    });
});

// 404 handler (must be last)
app.use((req, res) => {
    res.status(404).json({
        success: false,
        error: 'Route not found'
    });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`\n🚀 Server running at http://localhost:${PORT}/\n`);
    console.log('API Endpoints:');
    console.log('  GET    /api/users');
    console.log('  GET    /api/users/:id');
    console.log('  POST   /api/users');
    console.log('  PUT    /api/users/:id');
    console.log('  DELETE /api/users/:id\n');
});
```

**Test with curl or Postman:**
```bash
# Get all users
curl http://localhost:3000/api/users

# Get user by ID
curl http://localhost:3000/api/users/1

# Filter users by age
curl "http://localhost:3000/api/users?age=25"

# Create new user
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Emma Wilson","email":"emma@example.com","age":27}'

# Update user
curl -X PUT http://localhost:3000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"John Updated","age":26}'

# Delete user
curl -X DELETE http://localhost:3000/api/users/2
```

**Learning Resources:**
- [Express.js Official Docs](https://expressjs.com/)
- [Express.js Installation](https://expressjs.com/en/starter/installing.html)
- [Express Routing Guide](https://expressjs.com/en/guide/routing.html)

**Hands-on Practice:**
- Create an Express server with 5+ routes
- Build a REST API for products or movies
- Implement all CRUD operations
- Add query parameter filtering
- Test with Postman or curl

**Interview Questions:**

1. **What is Express.js?**
   - **Answer:** Express.js is a minimal and flexible Node.js web application framework that provides a robust set of features for building web and mobile applications.
   
   **Key Features:**
   - Simplifies server creation
   - Powerful routing system
   - Middleware support
   - Template engine integration
   - Easy REST API development
   - Error handling
   
   **Why use Express:**
   - Reduces boilerplate code
   - Large ecosystem of middleware
   - Industry standard (most popular Node framework)
   - Great documentation and community
   - Works well with databases, authentication, etc.
   
   **Example:**
   ```javascript
   const express = require('express');
   const app = express();
   
   app.get('/api/users', (req, res) => {
       res.json({ users: [] });
   });
   
   app.listen(3000);
   ```

2. **Difference between app.use() and app.get()?**
   - **Answer:** `app.use()` applies middleware to all routes (or specific paths), while `app.get()` handles only GET requests to a specific route.
   
   **app.use():**
   - Applies middleware
   - Works for all HTTP methods
   - Can match path prefixes
   - Order matters!
   
   ```javascript
   // Runs for ALL requests
   app.use(express.json());
   
   // Runs for all /api/* routes
   app.use('/api', apiRouter);
   
   // Custom middleware
   app.use((req, res, next) => {
       console.log('Request:', req.method, req.url);
       next();
   });
   ```
   
   **app.get():**
   - Handles GET requests only
   - Exact route matching
   - Route handler, not middleware
   
   ```javascript
   // Only GET /users
   app.get('/users', (req, res) => {
       res.json({ users: [] });
   });
   
   // Other methods won't work
   // POST /users → 404
   ```
   
   **When to use:**
   - `app.use()` - Middleware, parsing, logging, authentication
   - `app.get()` - Specific route handlers

3. **What are route parameters vs query parameters?**
   - **Answer:** Route parameters are part of the URL path, while query parameters are key-value pairs after `?` in the URL.
   
   **Route Parameters (Path Parameters):**
   ```javascript
   // URL: /users/123
   app.get('/users/:id', (req, res) => {
       const id = req.params.id; // "123"
       res.json({ id });
   });
   
   // URL: /posts/hello/comments/5
   app.get('/posts/:postId/comments/:commentId', (req, res) => {
       const { postId, commentId } = req.params;
       // postId: "hello", commentId: "5"
   });
   ```
   - Part of URL structure
   - Required (unless optional with `?`)
   - Used for identifying resources
   - Access with `req.params`
   
   **Query Parameters:**
   ```javascript
   // URL: /search?q=nodejs&page=2&limit=10
   app.get('/search', (req, res) => {
       const { q, page, limit } = req.query;
       // q: "nodejs", page: "2", limit: "10"
   });
   ```
   - After `?` in URL
   - Optional
   - Used for filtering, sorting, pagination
   - Access with `req.query`
   
   **When to use:**
   - Route params: `/users/:id` (specific resource)
   - Query params: `/users?age=25&role=admin` (filtering)

---

### Day 28: Middleware in Express

#### 📖 What is Middleware?
Middleware are functions that execute **during the request-response cycle**. They can:
- Execute code
- Modify request and response objects
- End the request-response cycle
- Call the next middleware function

**Think of middleware like:**
Security checkpoints at an airport - each checkpoint checks something different before you board the plane!

```
Request → Middleware 1 → Middleware 2 → Middleware 3 → Route Handler → Response
           (logging)      (authentication)   (validation)    (business logic)
```

#### 📖 Middleware Signature

```javascript
function middlewareName(req, res, next) {
    // Do something
    console.log('Middleware executed');
    
    // MUST call next() to pass control to next middleware
    next();
    
    // Or end the response
    // res.send('Done');
}
```

**Key points:**
- Three parameters: `req`, `res`, `next`
- Call `next()` to continue to next middleware
- Or call `res.send()` to end the cycle

#### 📖 Types of Middleware

**1. Application-level Middleware:**
```javascript
const express = require('express');
const app = express();

// Runs for ALL routes
app.use((req, res, next) => {
    console.log('Time:', Date.now());
    next();
});

// Runs for specific path
app.use('/api', (req, res, next) => {
    console.log('API route accessed');
    next();
});
```

**2. Router-level Middleware:**
```javascript
const router = express.Router();

router.use((req, res, next) => {
    console.log('Router middleware');
    next();
});

router.get('/users', (req, res) => {
    res.send('Users');
});
```

**3. Built-in Middleware:**
```javascript
// Parse JSON bodies
app.use(express.json());

// Parse URL-encoded bodies (form data)
app.use(express.urlencoded({ extended: true }));

// Serve static files
app.use(express.static('public'));
```

**4. Third-party Middleware:**
```javascript
const cors = require('cors');
const morgan = require('morgan');

// Enable CORS
app.use(cors());

// HTTP request logger
app.use(morgan('dev'));
```

**5. Error-handling Middleware:**
```javascript
// Must have 4 parameters!
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});
```

#### 📖 Custom Middleware Examples

**Logging Middleware:**
```javascript
const logger = (req, res, next) => {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${req.method} ${req.url}`);
    next();
};

app.use(logger);
```

**Authentication Middleware:**
```javascript
const authenticate = (req, res, next) => {
    const token = req.headers.authorization;
    
    if (!token) {
        return res.status(401).json({ error: 'No token provided' });
    }
    
    if (token === 'secret-token-123') {
        req.user = { id: 1, name: 'John' };
        next();
    } else {
        res.status(403).json({ error: 'Invalid token' });
    }
};

// Apply to specific routes
app.get('/api/protected', authenticate, (req, res) => {
    res.json({ message: 'Protected data', user: req.user });
});
```

**Validation Middleware:**
```javascript
const validateUser = (req, res, next) => {
    const { name, email } = req.body;
    
    if (!name || !email) {
        return res.status(400).json({ 
            error: 'Name and email are required' 
        });
    }
    
    if (!email.includes('@')) {
        return res.status(400).json({ 
            error: 'Invalid email format' 
        });
    }
    
    // Validation passed
    next();
};

app.post('/api/users', validateUser, (req, res) => {
    // Create user
    res.json({ message: 'User created', data: req.body });
});
```

**Request Time Middleware:**
```javascript
const requestTime = (req, res, next) => {
    req.requestTime = Date.now();
    next();
};

app.use(requestTime);

app.get('/', (req, res) => {
    const responseTime = Date.now() - req.requestTime;
    res.send(`Response time: ${responseTime}ms`);
});
```

#### 💡 Complete Express App with Multiple Middleware

**Install dependencies:**
```bash
npm install express morgan cors helmet dotenv
```

**server.js:**
```javascript
require('dotenv').config();
const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const helmet = require('helmet');

const app = express();

// ========== MIDDLEWARE ==========

// 1. Security middleware (helmet)
app.use(helmet());

// 2. CORS middleware
app.use(cors());

// 3. Built-in middleware
app.use(express.json()); // Parse JSON
app.use(express.urlencoded({ extended: true })); // Parse form data
app.use(express.static('public')); // Serve static files

// 4. Logging middleware (morgan)
app.use(morgan('dev')); // dev, combined, common, short, tiny

// 5. Custom logging middleware
const customLogger = (req, res, next) => {
    const timestamp = new Date().toISOString();
    console.log(`[${timestamp}] ${req.method} ${req.url}`);
    next();
};
app.use(customLogger);

// 6. Request timing middleware
app.use((req, res, next) => {
    req.startTime = Date.now();
    next();
});

// 7. Custom authentication middleware
const authenticate = (req, res, next) => {
    const token = req.headers['authorization'];
    
    if (!token) {
        return res.status(401).json({ 
            success: false,
            error: 'No token provided' 
        });
    }
    
    // Simple token check (in real app, verify JWT)
    if (token === 'Bearer secret-token-123') {
        req.user = { id: 1, name: 'John Doe', role: 'admin' };
        next();
    } else {
        res.status(403).json({ 
            success: false,
            error: 'Invalid or expired token' 
        });
    }
};

// 8. Role-based authorization middleware
const authorize = (...roles) => {
    return (req, res, next) => {
        if (!req.user) {
            return res.status(401).json({ 
                error: 'Not authenticated' 
            });
        }
        
        if (!roles.includes(req.user.role)) {
            return res.status(403).json({ 
                error: 'Insufficient permissions' 
            });
        }
        
        next();
    };
};

// 9. Validation middleware
const validateUser = (req, res, next) => {
    const { name, email } = req.body;
    const errors = [];
    
    if (!name || name.trim().length === 0) {
        errors.push('Name is required');
    }
    
    if (!email || !email.includes('@')) {
        errors.push('Valid email is required');
    }
    
    if (errors.length > 0) {
        return res.status(400).json({ 
            success: false,
            errors 
        });
    }
    
    next();
};

// ========== ROUTES ==========

// Public routes
app.get('/', (req, res) => {
    const responseTime = Date.now() - req.startTime;
    res.json({
        message: 'Welcome to API',
        version: '1.0.0',
        responseTime: `${responseTime}ms`
    });
});

app.get('/api/public', (req, res) => {
    res.json({
        message: 'This is public data',
        timestamp: new Date()
    });
});

// Protected routes (authentication required)
app.get('/api/protected', authenticate, (req, res) => {
    res.json({
        message: 'This is protected data',
        user: req.user
    });
});

// Admin only route (authentication + authorization)
app.get('/api/admin', authenticate, authorize('admin'), (req, res) => {
    res.json({
        message: 'Admin dashboard data',
        user: req.user
    });
});

// Route with validation
app.post('/api/users', validateUser, (req, res) => {
    const { name, email } = req.body;
    
    // Simulate user creation
    const newUser = {
        id: Date.now(),
        name,
        email,
        createdAt: new Date()
    };
    
    res.status(201).json({
        success: true,
        message: 'User created successfully',
        data: newUser
    });
});

// Multiple middleware on one route
app.post('/api/admin/users', 
    authenticate, 
    authorize('admin'), 
    validateUser, 
    (req, res) => {
        res.json({
            success: true,
            message: 'Admin created user',
            user: req.user,
            data: req.body
        });
    }
);

// ========== ERROR HANDLING ==========

// 404 handler (must be after all routes)
app.use((req, res) => {
    res.status(404).json({
        success: false,
        error: 'Route not found',
        requestedUrl: req.url
    });
});

// Error handler (must have 4 parameters)
app.use((err, req, res, next) => {
    console.error('Error:', err.stack);
    
    res.status(err.status || 500).json({
        success: false,
        error: err.message || 'Internal server error',
        ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
    });
});

// ========== START SERVER ==========

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`\n🚀 Server running at http://localhost:${PORT}/\n`);
    console.log('Endpoints:');
    console.log('  GET  / - Home');
    console.log('  GET  /api/public - Public data');
    console.log('  GET  /api/protected - Protected (needs token)');
    console.log('  GET  /api/admin - Admin only');
    console.log('  POST /api/users - Create user (validation)\n');
    console.log('Test protected route:');
    console.log('  curl -H "Authorization: Bearer secret-token-123" http://localhost:3000/api/protected\n');
});
```

**Test the middleware:**
```bash
# Public route (no auth)
curl http://localhost:3000/api/public

# Protected route (with token)
curl -H "Authorization: Bearer secret-token-123" \
     http://localhost:3000/api/protected

# Protected route (without token) - Should fail
curl http://localhost:3000/api/protected

# Validation test (missing email) - Should fail
curl -X POST http://localhost:3000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name":"John"}'

# Validation test (valid data)
curl -X POST http://localhost:3000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name":"John Doe","email":"john@example.com"}'
```

#### 📖 Middleware Order Matters!

```javascript
// ❌ WRONG ORDER - Won't work!
app.get('/api/data', (req, res) => {
    res.json(req.body); // req.body is undefined!
});
app.use(express.json()); // Too late!

// ✅ CORRECT ORDER
app.use(express.json()); // Parse JSON first
app.get('/api/data', (req, res) => {
    res.json(req.body); // Now req.body works!
});
```

**Best practice order:**
1. Security middleware (helmet, cors)
2. Logging middleware (morgan)
3. Body parsing (express.json, express.urlencoded)
4. Static files (express.static)
5. Custom middleware
6. Routes
7. 404 handler
8. Error handler (must be last!)

**Learning Resources:**
- [Express Middleware Guide](https://expressjs.com/en/guide/using-middleware.html)
- [Writing Middleware](https://expressjs.com/en/guide/writing-middleware.html)
- [Morgan Documentation](https://github.com/expressjs/morgan)
- [Helmet.js](https://helmetjs.github.io/)

**Hands-on Practice:**
- Create custom logging middleware that logs to a file
- Build authentication middleware that checks tokens
- Create validation middleware for form data
- Test middleware execution order
- Add error handling middleware
- Use morgan for HTTP request logging

**Interview Questions:**

1. **What is middleware in Express?**
   - **Answer:** Middleware are functions that have access to the request object (req), response object (res), and the next middleware function in the application's request-response cycle.
   
   **What middleware can do:**
   - Execute any code
   - Modify req and res objects
   - End request-response cycle
   - Call next middleware with `next()`
   
   **Types:**
   - Application-level: `app.use()`
   - Router-level: `router.use()`
   - Built-in: `express.json()`, `express.static()`
   - Third-party: `cors()`, `morgan()`
   - Error-handling: 4 parameters
   
   **Example:**
   ```javascript
   // Custom middleware
   app.use((req, res, next) => {
       console.log('Request:', req.method, req.url);
       next(); // Pass to next middleware
   });
   
   // Built-in middleware
   app.use(express.json());
   
   // Route handler (also middleware!)
   app.get('/users', (req, res) => {
       res.json({ users: [] });
   });
   ```

2. **Explain the middleware execution flow.**
   - **Answer:** Middleware executes in the order they are defined, forming a chain. Each middleware must call `next()` to pass control to the next one.
   
   **Flow:**
   ```
   Request
      ↓
   Middleware 1 → next() →
      ↓
   Middleware 2 → next() →
      ↓
   Route Handler → res.send()
      ↓
   Response
   ```
   
   **Example:**
   ```javascript
   // 1. First middleware
   app.use((req, res, next) => {
       console.log('1st');
       next();
   });
   
   // 2. Second middleware
   app.use((req, res, next) => {
       console.log('2nd');
       next();
   });
   
   // 3. Route handler
   app.get('/', (req, res) => {
       console.log('3rd');
       res.send('Done');
   });
   
   // Output: 1st → 2nd → 3rd
   ```
   
   **Important:**
   - If middleware doesn't call `next()` or send response, request hangs!
   - Order matters - middleware executes sequentially
   - Error middleware (4 params) only runs when error occurs

3. **What is the difference between app.use() and app.all()?**
   - **Answer:** `app.use()` applies middleware to all HTTP methods and can match path prefixes, while `app.all()` is a route method that matches all HTTP methods for an exact path.
   
   **app.use():**
   ```javascript
   // Matches ALL methods and ALL paths starting with /api
   app.use('/api', (req, res, next) => {
       console.log('API middleware');
       next();
   });
   // Matches: /api, /api/users, /api/posts/123
   
   // Global middleware
   app.use(express.json());
   ```
   - Used for middleware
   - Matches path prefixes
   - No specific HTTP method
   
   **app.all():**
   ```javascript
   // Matches ALL methods for EXACT path /api/users
   app.all('/api/users', (req, res, next) => {
       console.log('All methods handler');
       next();
   });
   // Matches: GET /api/users, POST /api/users, etc.
   // Doesn't match: /api/users/123
   ```
   - Used for route handlers
   - Exact path matching
   - Handles all HTTP methods (GET, POST, PUT, DELETE, etc.)
   
   **When to use:**
   - `app.use()` - Middleware (logging, parsing, auth for multiple routes)
   - `app.all()` - Route-specific logic for all methods

---

### Day 29: Static Files & Error Handling

#### 📖 Serving Static Files
Static files are files that don't change - like images, CSS, JavaScript, PDFs, etc.

**Examples of static files:**
- Images (logo.png, photo.jpg)
- CSS files (style.css)
- JavaScript files (app.js, script.js)
- PDFs, fonts, videos

#### 📖 Using express.static()

**Basic setup:**
```javascript
const express = require('express');
const path = require('path');
const app = express();

// Serve files from 'public' directory
app.use(express.static('public'));

// Now files in 'public/' are accessible:
// public/style.css → http://localhost:3000/style.css
// public/image.jpg → http://localhost:3000/image.jpg
// public/js/app.js → http://localhost:3000/js/app.js
```

**Project structure:**
```
my-app/
├── server.js
├── public/
│   ├── index.html
│   ├── about.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── images/
│       └── logo.png
```

**With virtual path prefix:**
```javascript
// Serve files with /static prefix
app.use('/static', express.static('public'));

// Now:
// public/style.css → http://localhost:3000/static/style.css
// public/logo.png → http://localhost:3000/static/logo.png
```

**Multiple static directories:**
```javascript
app.use(express.static('public'));
app.use(express.static('files'));
app.use(express.static('uploads'));

// Express looks in order: public → files → uploads
```

**Absolute path (recommended):**
```javascript
app.use(express.static(path.join(__dirname, 'public')));
```

#### 📖 Error Handling in Express

**Types of errors:**
1. **Synchronous errors** - Caught automatically
2. **Asynchronous errors** - Need explicit handling
3. **404 errors** - Route not found

**Synchronous error (caught automatically):**
```javascript
app.get('/error', (req, res) => {
    throw new Error('Something went wrong!');
    // Express catches this automatically
});
```

**Asynchronous error (must catch):**
```javascript
// ❌ Won't work - error not caught
app.get('/async-error', async (req, res) => {
    const data = await riskyAsyncOperation();
    res.json(data);
});

// ✅ Works - error caught
app.get('/async-error', async (req, res, next) => {
    try {
        const data = await riskyAsyncOperation();
        res.json(data);
    } catch (err) {
        next(err); // Pass error to error handler
    }
});
```

**Custom error class:**
```javascript
class AppError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.statusCode = statusCode;
        this.status = `${statusCode}`.startsWith('4') ? 'fail' : 'error';
        this.isOperational = true;
        
        Error.captureStackTrace(this, this.constructor);
    }
}

// Usage
app.get('/users/:id', (req, res, next) => {
    const user = users.find(u => u.id === req.params.id);
    
    if (!user) {
        return next(new AppError('User not found', 404));
    }
    
    res.json({ user });
});
```

**Error-handling middleware (4 parameters!):**
```javascript
// Must have 4 parameters: err, req, res, next
app.use((err, req, res, next) => {
    console.error('Error:', err.stack);
    
    const statusCode = err.statusCode || 500;
    const status = err.status || 'error';
    
    res.status(statusCode).json({
        status,
        message: err.message,
        ...(process.env.NODE_ENV === 'development' && { 
            stack: err.stack 
        })
    });
});
```

**404 handler (must be before error handler):**
```javascript
// Catch 404 - BEFORE error handler
app.use((req, res, next) => {
    res.status(404).json({
        status: 'fail',
        message: `Can't find ${req.originalUrl} on this server`
    });
});

// Error handler - AFTER 404 handler
app.use((err, req, res, next) => {
    // Handle errors
});
```

#### 💡 Complete Static + Error Handling Example

**server.js:**
```javascript
const express = require('express');
const path = require('path');
const app = express();

// ========== MIDDLEWARE ==========

// Parse JSON
app.use(express.json());

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Logging middleware
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// ========== CUSTOM ERROR CLASS ==========

class AppError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.statusCode = statusCode;
        this.isOperational = true;
    }
}

// ========== ROUTES ==========

// Home route (returns HTML)
app.get('/api', (req, res) => {
    res.json({
        message: 'API is running',
        version: '1.0.0',
        endpoints: {
            'GET /api/users': 'Get all users',
            'GET /api/users/:id': 'Get single user',
            'POST /api/users': 'Create user'
        }
    });
});

// Sample data
let users = [
    { id: 1, name: 'John Doe', email: 'john@example.com' },
    { id: 2, name: 'Sarah Smith', email: 'sarah@example.com' }
];

// Get all users
app.get('/api/users', (req, res) => {
    res.json({
        success: true,
        data: users
    });
});

// Get single user
app.get('/api/users/:id', (req, res, next) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return next(new AppError('User not found', 404));
    }
    
    res.json({
        success: true,
        data: user
    });
});

// Create user (with async error handling)
app.post('/api/users', async (req, res, next) => {
    try {
        const { name, email } = req.body;
        
        // Validation
        if (!name || !email) {
            throw new AppError('Name and email are required', 400);
        }
        
        if (!email.includes('@')) {
            throw new AppError('Invalid email format', 400);
        }
        
        // Simulate async operation
        await new Promise(resolve => setTimeout(resolve, 100));
        
        const newUser = {
            id: users.length + 1,
            name,
            email
        };
        
        users.push(newUser);
        
        res.status(201).json({
            success: true,
            message: 'User created successfully',
            data: newUser
        });
    } catch (err) {
        next(err);
    }
});

// Intentional error route (for testing)
app.get('/api/error', (req, res, next) => {
    next(new AppError('This is a test error', 500));
});

// Async error route (for testing)
app.get('/api/async-error', async (req, res, next) => {
    try {
        // Simulate async error
        await Promise.reject(new Error('Async operation failed'));
    } catch (err) {
        next(new AppError(err.message, 500));
    }
});

// ========== ERROR HANDLING ==========

// 404 handler (must be BEFORE error handler)
app.use((req, res, next) => {
    const error = new AppError(`Can't find ${req.originalUrl}`, 404);
    next(error);
});

// Global error handler (must be LAST)
app.use((err, req, res, next) => {
    err.statusCode = err.statusCode || 500;
    err.status = err.status || 'error';
    
    console.error('Error:', err.message);
    
    if (process.env.NODE_ENV === 'development') {
        // Development - detailed error
        res.status(err.statusCode).json({
            status: err.status,
            error: err,
            message: err.message,
            stack: err.stack
        });
    } else {
        // Production - hide details
        if (err.isOperational) {
            // Operational error - safe to send to client
            res.status(err.statusCode).json({
                status: err.status,
                message: err.message
            });
        } else {
            // Programming error - don't leak details
            console.error('Programming Error:', err);
            res.status(500).json({
                status: 'error',
                message: 'Something went wrong'
            });
        }
    }
});

// ========== START SERVER ==========

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`\n🚀 Server running at http://localhost:${PORT}/\n`);
    console.log('Static files served from /public');
    console.log('  http://localhost:3000/ (index.html)');
    console.log('  http://localhost:3000/css/style.css\n');
    console.log('API Endpoints:');
    console.log('  GET  /api/users');
    console.log('  GET  /api/users/:id');
    console.log('  POST /api/users');
    console.log('  GET  /api/error (test error)');
    console.log('  GET  /api/async-error (test async error)\n');
});
```

**public/index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Express Static Files Demo</title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <div class="container">
        <h1>Welcome to Express Server! 🚀</h1>
        <p>This HTML file is served as a static file from the <code>public/</code> directory.</p>
        
        <div class="card">
            <h2>Features</h2>
            <ul>
                <li>✅ Static file serving</li>
                <li>✅ Error handling</li>
                <li>✅ REST API</li>
                <li>✅ Custom error pages</li>
            </ul>
        </div>
        
        <div class="links">
            <a href="/about.html">About Page</a>
            <a href="/api">API Documentation</a>
        </div>
    </div>
    
    <script src="/js/app.js"></script>
</body>
</html>
```

**public/css/style.css:**
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    max-width: 600px;
    width: 100%;
}

h1 {
    color: #333;
    margin-bottom: 20px;
}

p {
    color: #666;
    line-height: 1.6;
    margin-bottom: 20px;
}

code {
    background: #f0f0f0;
    padding: 2px 8px;
    border-radius: 4px;
    font-family: 'Courier New', monospace;
}

.card {
    background: #f9f9f9;
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
}

.card h2 {
    color: #667eea;
    margin-bottom: 15px;
}

.card ul {
    list-style: none;
    padding-left: 0;
}

.card li {
    padding: 8px 0;
    color: #555;
}

.links {
    display: flex;
    gap: 15px;
    margin-top: 20px;
}

.links a {
    display: inline-block;
    padding: 10px 20px;
    background: #667eea;
    color: white;
    text-decoration: none;
    border-radius: 5px;
    transition: all 0.3s;
}

.links a:hover {
    background: #764ba2;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
```

**public/js/app.js:**
```javascript
console.log('App.js loaded from static files!');

// Fetch users from API
async function loadUsers() {
    try {
        const response = await fetch('/api/users');
        const data = await response.json();
        console.log('Users:', data);
    } catch (err) {
        console.error('Error loading users:', err);
    }
}

// Test error handling
async function testError() {
    try {
        const response = await fetch('/api/error');
        const data = await response.json();
        console.log('Error response:', data);
    } catch (err) {
        console.error('Fetch error:', err);
    }
}

// Run on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('Page loaded!');
    loadUsers();
});
```

**Learning Resources:**
- [Express Static Files](https://expressjs.com/en/starter/static-files.html)
- [Error Handling Guide](https://expressjs.com/en/guide/error-handling.html)
- [MDN HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

**Hands-on Practice:**
- Create a public folder with HTML, CSS, JS files
- Serve static files with express.static()
- Create custom 404 page
- Implement error handling middleware
- Test different error scenarios
- Add error logging to a file

**Interview Questions:**

1. **How do you serve static files in Express?**
   - **Answer:** Use the `express.static()` built-in middleware function.
   
   **Basic usage:**
   ```javascript
   app.use(express.static('public'));
   // Serves files from 'public' directory
   ```
   
   **With virtual path:**
   ```javascript
   app.use('/static', express.static('public'));
   // URL: /static/image.jpg → public/image.jpg
   ```
   
   **Multiple directories:**
   ```javascript
   app.use(express.static('public'));
   app.use(express.static('files'));
   // Checks public first, then files
   ```
   
   **Absolute path (recommended):**
   ```javascript
   const path = require('path');
   app.use(express.static(path.join(__dirname, 'public')));
   ```
   
   **What it does:**
   - Serves files directly (no routing needed)
   - Sets proper Content-Type headers
   - Supports index.html by default
   - Caching headers included

2. **What is error-handling middleware?**
   - **Answer:** Error-handling middleware is a special middleware with **4 parameters** (err, req, res, next) that handles errors in Express applications.
   
   **Signature (MUST have 4 parameters):**
   ```javascript
   app.use((err, req, res, next) => {
       console.error(err.stack);
       res.status(err.statusCode || 500).json({
           error: err.message
       });
   });
   ```
   
   **Key points:**
   - Must have 4 parameters (even if not using next)
   - Must be defined AFTER all routes
   - Catches errors from routes and middleware
   - Can have multiple error handlers
   
   **Triggering errors:**
   ```javascript
   // Synchronous
   app.get('/error', (req, res) => {
       throw new Error('Error!');
   });
   
   // Asynchronous
   app.get('/async-error', async (req, res, next) => {
       try {
           await someAsyncOperation();
       } catch (err) {
           next(err); // Pass to error handler
       }
   });
   ```

3. **How do you handle 404 errors in Express?**
   - **Answer:** Create a middleware that catches all unmatched routes and place it AFTER all other routes but BEFORE the error handler.
   
   **Method 1: Simple 404 handler**
   ```javascript
   // After all routes
   app.use((req, res) => {
       res.status(404).json({
           error: 'Route not found',
           requestedUrl: req.originalUrl
       });
   });
   ```
   
   **Method 2: Pass to error handler**
   ```javascript
   // After all routes
   app.use((req, res, next) => {
       const error = new Error('Not Found');
       error.status = 404;
       next(error);
   });
   
   // Error handler
   app.use((err, req, res, next) => {
       res.status(err.status || 500).json({
           error: err.message
       });
   });
   ```
   
   **Method 3: Custom 404 page**
   ```javascript
   app.use((req, res) => {
       res.status(404).sendFile(path.join(__dirname, 'public', '404.html'));
   });
   ```
   
   **Correct order:**
   ```javascript
   // 1. Routes
   app.get('/users', ...);
   app.post('/users', ...);
   
   // 2. 404 handler
   app.use((req, res, next) => { ... });
   
   // 3. Error handler
   app.use((err, req, res, next) => { ... });
   ```

---

### Day 30: Express Router & Project Structure

#### 📖 What is Express Router?
Express Router is a mini Express application that helps you organize routes into modules!

**Think of it like:**
- **Without Router** = All routes in one huge file (messy!)
- **With Router** = Routes organized by feature (clean!)

**Why use Router?**
- 🗂️ **Organization** - Separate routes by feature
- ♻️ **Reusability** - Share routes across projects
- 🧹 **Clean Code** - Easier to maintain
- 👥 **Team Work** - Different devs work on different routes

#### 📖 Basic Router Example

**Without Router (messy):**
```javascript
// server.js - Everything in one file!
app.get('/api/users', ...);
app.post('/api/users', ...);
app.get('/api/posts', ...);
app.post('/api/posts', ...);
// ... 50 more routes
```

**With Router (clean):**
```javascript
// routes/userRoutes.js
const router = express.Router();

router.get('/', ...);  // /api/users
router.post('/', ...); // /api/users

module.exports = router;

// server.js
const userRoutes = require('./routes/userRoutes');
app.use('/api/users', userRoutes);
```

#### 📖 Creating Routers

**routes/userRoutes.js:**
```javascript
const express = require('express');
const router = express.Router();

// Sample data
let users = [
    { id: 1, name: 'John', email: 'john@example.com' },
    { id: 2, name: 'Sarah', email: 'sarah@example.com' }
];

// GET /api/users
router.get('/', (req, res) => {
    res.json({ success: true, data: users });
});

// GET /api/users/:id
router.get('/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) {
        return res.status(404).json({ success: false, error: 'User not found' });
    }
    res.json({ success: true, data: user });
});

// POST /api/users
router.post('/', (req, res) => {
    const newUser = {
        id: users.length + 1,
        ...req.body
    };
    users.push(newUser);
    res.status(201).json({ success: true, data: newUser });
});

// PUT /api/users/:id
router.put('/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) {
        return res.status(404).json({ success: false, error: 'User not found' });
    }
    Object.assign(user, req.body);
    res.json({ success: true, data: user });
});

// DELETE /api/users/:id
router.delete('/:id', (req, res) => {
    const index = users.findIndex(u => u.id === parseInt(req.params.id));
    if (index === -1) {
        return res.status(404).json({ success: false, error: 'User not found' });
    }
    const deleted = users.splice(index, 1)[0];
    res.json({ success: true, data: deleted });
});

module.exports = router;
```

**routes/postRoutes.js:**
```javascript
const express = require('express');
const router = express.Router();

let posts = [
    { id: 1, title: 'First Post', content: 'Hello World', authorId: 1 },
    { id: 2, title: 'Second Post', content: 'Learning Express', authorId: 2 }
];

router.get('/', (req, res) => {
    res.json({ success: true, data: posts });
});

router.get('/:id', (req, res) => {
    const post = posts.find(p => p.id === parseInt(req.params.id));
    if (!post) {
        return res.status(404).json({ success: false, error: 'Post not found' });
    }
    res.json({ success: true, data: post });
});

router.post('/', (req, res) => {
    const newPost = {
        id: posts.length + 1,
        ...req.body
    };
    posts.push(newPost);
    res.status(201).json({ success: true, data: newPost });
});

module.exports = router;
```

**server.js (using routers):**
```javascript
const express = require('express');
const userRoutes = require('./routes/userRoutes');
const postRoutes = require('./routes/postRoutes');

const app = express();
app.use(express.json());

// Mount routers
app.use('/api/users', userRoutes);
app.use('/api/posts', postRoutes);

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
```

#### 📖 MVC Pattern (Model-View-Controller)

**Project structure:**
```
my-app/
├── server.js
├── routes/
│   ├── userRoutes.js
│   └── postRoutes.js
├── controllers/
│   ├── userController.js
│   └── postController.js
├── models/
│   ├── User.js
│   └── Post.js
├── middleware/
│   ├── auth.js
│   └── validation.js
└── config/
    └── database.js
```

**controllers/userController.js:**
```javascript
// Business logic separated from routes

exports.getAllUsers = (req, res) => {
    // Logic to get users
    const users = []; // From database
    res.json({ success: true, data: users });
};

exports.getUser = (req, res) => {
    const { id } = req.params;
    // Logic to get single user
    res.json({ success: true, data: user });
};

exports.createUser = (req, res) => {
    const userData = req.body;
    // Logic to create user
    res.status(201).json({ success: true, data: newUser });
};

exports.updateUser = (req, res) => {
    const { id } = req.params;
    const updates = req.body;
    // Logic to update user
    res.json({ success: true, data: updatedUser });
};

exports.deleteUser = (req, res) => {
    const { id } = req.params;
    // Logic to delete user
    res.json({ success: true, message: 'User deleted' });
};
```

**routes/userRoutes.js (with controllers):**
```javascript
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const { authenticate } = require('../middleware/auth');

router.get('/', userController.getAllUsers);
router.get('/:id', userController.getUser);
router.post('/', authenticate, userController.createUser);
router.put('/:id', authenticate, userController.updateUser);
router.delete('/:id', authenticate, userController.deleteUser);

module.exports = router;
```

#### 💡 Complete Modular Express Application

**Project structure:**
```
express-app/
├── server.js
├── package.json
├── .env
├── routes/
│   ├── userRoutes.js
│   ├── postRoutes.js
│   └── authRoutes.js
├── controllers/
│   ├── userController.js
│   ├── postController.js
│   └── authController.js
├── middleware/
│   ├── auth.js
│   ├── errorHandler.js
│   └── validation.js
├── models/
│   └── data.js
└── utils/
    └── helpers.js
```

**models/data.js:**
```javascript
// Mock database
let users = [
    { id: 1, name: 'John Doe', email: 'john@example.com', role: 'admin' },
    { id: 2, name: 'Sarah Smith', email: 'sarah@example.com', role: 'user' }
];

let posts = [
    { id: 1, title: 'First Post', content: 'Hello World', userId: 1, createdAt: new Date() },
    { id: 2, title: 'Express Tutorial', content: 'Learning Express', userId: 2, createdAt: new Date() }
];

module.exports = { users, posts };
```

**controllers/userController.js:**
```javascript
const { users } = require('../models/data');

// Get all users
exports.getUsers = (req, res) => {
    res.json({
        success: true,
        count: users.length,
        data: users
    });
};

// Get single user
exports.getUser = (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return res.status(404).json({
            success: false,
            error: 'User not found'
        });
    }
    
    res.json({ success: true, data: user });
};

// Create user
exports.createUser = (req, res) => {
    const { name, email, role } = req.body;
    
    const newUser = {
        id: users.length + 1,
        name,
        email,
        role: role || 'user',
        createdAt: new Date()
    };
    
    users.push(newUser);
    
    res.status(201).json({
        success: true,
        message: 'User created successfully',
        data: newUser
    });
};

// Update user
exports.updateUser = (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return res.status(404).json({
            success: false,
            error: 'User not found'
        });
    }
    
    Object.assign(user, req.body);
    user.updatedAt = new Date();
    
    res.json({
        success: true,
        message: 'User updated successfully',
        data: user
    });
};

// Delete user
exports.deleteUser = (req, res) => {
    const index = users.findIndex(u => u.id === parseInt(req.params.id));
    
    if (index === -1) {
        return res.status(404).json({
            success: false,
            error: 'User not found'
        });
    }
    
    const deleted = users.splice(index, 1)[0];
    
    res.json({
        success: true,
        message: 'User deleted successfully',
        data: deleted
    });
};
```

**middleware/auth.js:**
```javascript
exports.authenticate = (req, res, next) => {
    const token = req.headers['authorization'];
    
    if (!token) {
        return res.status(401).json({
            success: false,
            error: 'No token provided'
        });
    }
    
    // Simple token validation (use JWT in production)
    if (token === 'Bearer secret-token') {
        req.user = { id: 1, role: 'admin' };
        next();
    } else {
        res.status(403).json({
            success: false,
            error: 'Invalid token'
        });
    }
};

exports.authorize = (...roles) => {
    return (req, res, next) => {
        if (!req.user) {
            return res.status(401).json({
                error: 'Not authenticated'
            });
        }
        
        if (!roles.includes(req.user.role)) {
            return res.status(403).json({
                error: 'Insufficient permissions'
            });
        }
        
        next();
    };
};
```

**middleware/validation.js:**
```javascript
exports.validateUser = (req, res, next) => {
    const { name, email } = req.body;
    const errors = [];
    
    if (!name || name.trim().length === 0) {
        errors.push('Name is required');
    }
    
    if (!email || !email.includes('@')) {
        errors.push('Valid email is required');
    }
    
    if (errors.length > 0) {
        return res.status(400).json({
            success: false,
            errors
        });
    }
    
    next();
};
```

**middleware/errorHandler.js:**
```javascript
exports.notFound = (req, res, next) => {
    res.status(404).json({
        success: false,
        error: `Route not found: ${req.originalUrl}`
    });
};

exports.errorHandler = (err, req, res, next) => {
    console.error('Error:', err.stack);
    
    res.status(err.statusCode || 500).json({
        success: false,
        error: err.message || 'Internal server error',
        ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
    });
};
```

**routes/userRoutes.js:**
```javascript
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const { authenticate, authorize } = require('../middleware/auth');
const { validateUser } = require('../middleware/validation');

router.get('/', userController.getUsers);
router.get('/:id', userController.getUser);
router.post('/', authenticate, validateUser, userController.createUser);
router.put('/:id', authenticate, userController.updateUser);
router.delete('/:id', authenticate, authorize('admin'), userController.deleteUser);

module.exports = router;
```

**server.js:**
```javascript
require('dotenv').config();
const express = require('express');
const userRoutes = require('./routes/userRoutes');
const postRoutes = require('./routes/postRoutes');
const { notFound, errorHandler } = require('./middleware/errorHandler');

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Logging
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// Routes
app.get('/', (req, res) => {
    res.json({
        message: 'API is running',
        version: '1.0.0',
        endpoints: {
            users: '/api/users',
            posts: '/api/posts'
        }
    });
});

app.use('/api/users', userRoutes);
app.use('/api/posts', postRoutes);

// Error handling
app.use(notFound);
app.use(errorHandler);

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`\n🚀 Server running on port ${PORT}\n`);
    console.log('API Endpoints:');
    console.log('  GET    /api/users');
    console.log('  GET    /api/users/:id');
    console.log('  POST   /api/users');
    console.log('  PUT    /api/users/:id');
    console.log('  DELETE /api/users/:id\n');
});
```

**Learning Resources:**
- [Express Router](https://expressjs.com/en/guide/routing.html#express-router)
- [MVC Pattern](https://www.freecodecamp.org/news/the-model-view-controller-pattern-mvc-architecture-and-frameworks-explained/)
- [Project Structure Best Practices](https://github.com/goldbergyoni/nodebestpractices)

**Hands-on Practice:**
- Refactor a large server.js into separate route files
- Implement MVC pattern with controllers
- Create middleware folder with reusable middleware
- Build a complete REST API with proper structure
- Add validation and authentication middleware

**Interview Questions:**

1. **What is Express Router?**
   - **Answer:** Express Router is a class that creates modular, mountable route handlers. It's like a mini Express application that handles only routing.
   
   **Benefits:**
   - Organize routes by feature/resource
   - Reusable route modules
   - Cleaner code structure
   - Easier testing and maintenance
   
   **Example:**
   ```javascript
   // routes/users.js
   const router = express.Router();
   router.get('/', getAllUsers);
   router.post('/', createUser);
   module.exports = router;
   
   // server.js
   const userRoutes = require('./routes/users');
   app.use('/api/users', userRoutes);
   ```
   
   **When to use:**
   - Large applications with many routes
   - API versioning (`/api/v1`, `/api/v2`)
   - Different route groups (admin, public, authenticated)

2. **Why is code modularization important?**
   - **Answer:** Modularization breaks code into smaller, manageable, reusable pieces.
   
   **Benefits:**
   - **Maintainability** - Easier to update and fix
   - **Reusability** - Use code across projects
   - **Testability** - Test individual modules
   - **Team Collaboration** - Work on separate modules
   - **Scalability** - Add features without breaking others
   - **Readability** - Easier to understand
   
   **Example:**
   ```
   ❌ Bad - One large file:
   server.js (1000+ lines)
   
   ✅ Good - Modular:
   server.js (50 lines)
   routes/userRoutes.js
   routes/postRoutes.js
   controllers/userController.js
   middleware/auth.js
   ```
   
   **Modularization techniques:**
   - Separate routes from logic (controllers)
   - Extract middleware to separate files
   - Group related functionality
   - Use proper folder structure

3. **Explain the MVC pattern.**
   - **Answer:** MVC (Model-View-Controller) is a design pattern that separates application into three components.
   
   **Components:**
   - **Model** - Data and business logic
   - **View** - User interface (templates, frontend)
   - **Controller** - Handles requests, coordinates Model and View
   
   **Flow:**
   ```
   Request → Router → Controller → Model → Controller → View → Response
   ```
   
   **In Express:**
   ```javascript
   // Model (data layer)
   const User = {
       find: () => database.query('SELECT * FROM users'),
       create: (data) => database.insert(data)
   };
   
   // Controller (business logic)
   exports.getUsers = async (req, res) => {
       const users = await User.find();
       res.json({ users });
   };
   
   // View (response/template)
   res.render('users', { users }); // or res.json({ users })
   
   // Router (routes requests)
   router.get('/users', userController.getUsers);
   ```
   
   **Benefits:**
   - Separation of concerns
   - Easier to test each layer
   - Multiple views for same data
   - Team can work on different layers

---

**Summary: Days 27-30 Completed! ✅**

You've now learned:
- Day 26: Built a complete CLI Tool project
- Day 27: Express.js basics, routing, REST API
- Day 28: Middleware (built-in, custom, third-party, error-handling)
- Day 29: Static files and error handling patterns
- Day 30: Express Router, MVC pattern, project structure

Next steps would be:
- Database integration (MongoDB/PostgreSQL)
- Authentication with JWT
- TypeScript with Express
- Testing APIs
- Deployment

Great progress! 🎉

---

## Module 8: TypeScript Fundamentals

### Day 31: TypeScript Introduction

**📖 What is TypeScript?**

TypeScript is a **superset of JavaScript** developed by Microsoft. Think of it as JavaScript with superpowers - it adds **static typing** and other features while compiling down to regular JavaScript.

**Real-World Analogy:**
- JavaScript is like writing a recipe without measurements - it's flexible but can lead to mistakes
- TypeScript is like writing a recipe with exact measurements - it catches errors before you cook (before runtime)

**Why Use TypeScript?**
1. **Catch errors early** - Find bugs during development, not in production
2. **Better IDE support** - Autocomplete, refactoring, navigation
3. **Self-documenting code** - Types serve as inline documentation
4. **Easier refactoring** - Change code confidently
5. **Team collaboration** - Clear contracts between code modules

---

**📖 TypeScript vs JavaScript**

| Feature | JavaScript | TypeScript |
|---------|-----------|------------|
| **Typing** | Dynamic (runtime) | Static (compile-time) |
| **Error Detection** | At runtime | At compile-time |
| **Learning Curve** | Easier | Steeper initially |
| **IDE Support** | Good | Excellent |
| **Compilation** | Not needed | Compiles to JS |
| **File Extension** | `.js` | `.ts` |

---

**💡 Example: The Problem TypeScript Solves**

```javascript
// ❌ JavaScript - No error until runtime
function addNumbers(a, b) {
  return a + b;
}

console.log(addNumbers(5, 10));      // ✅ 15
console.log(addNumbers(5, "10"));    // ⚠️ "510" - Bug!
console.log(addNumbers(5));          // ⚠️ NaN - Bug!
```

```typescript
// ✅ TypeScript - Catches errors during development
function addNumbers(a: number, b: number): number {
  return a + b;
}

console.log(addNumbers(5, 10));      // ✅ 15
console.log(addNumbers(5, "10"));    // ❌ Compile error!
console.log(addNumbers(5));          // ❌ Compile error!
```

---

**💡 Complete Setup Guide**

**Step 1: Install TypeScript**

```bash
# Install TypeScript globally
npm install -g typescript

# Check version
tsc --version

# Or install locally in a project
npm install --save-dev typescript
```

**Step 2: Create Your First TypeScript File**

Create `app.ts`:

```typescript
// app.ts
function greet(name: string): string {
  return `Hello, ${name}!`;
}

const userName: string = "Sarah";
console.log(greet(userName));

// Try uncommenting - TypeScript will show error!
// console.log(greet(42));  // ❌ Error: Argument of type 'number' is not assignable to parameter of type 'string'
```

**Step 3: Compile TypeScript to JavaScript**

```bash
# Compile single file
tsc app.ts

# This creates app.js - the compiled JavaScript file
node app.js
```

**Step 4: Initialize TypeScript Configuration**

```bash
# Create tsconfig.json
tsc --init
```

This creates `tsconfig.json` with default settings:

```json
{
  "compilerOptions": {
    "target": "ES2020",                  // JavaScript version to compile to
    "module": "commonjs",                 // Module system
    "strict": true,                       // Enable all strict type checking
    "esModuleInterop": true,             // Better compatibility
    "skipLibCheck": true,                 // Skip type checking of declaration files
    "forceConsistentCasingInFileNames": true,  // Ensure correct file name casing
    "outDir": "./dist",                   // Output directory for compiled files
    "rootDir": "./src"                    // Input directory for TypeScript files
  },
  "include": ["src/**/*"],               // Files to compile
  "exclude": ["node_modules"]            // Files to ignore
}
```

---

**💡 Complete TypeScript Project Example**

**Project Structure:**
```
typescript-demo/
├── src/
│   ├── index.ts
│   ├── calculator.ts
│   └── user.ts
├── dist/          (generated)
├── package.json
└── tsconfig.json
```

**1. Create package.json:**

```bash
npm init -y
npm install --save-dev typescript @types/node
```

**2. Update package.json scripts:**

```json
{
  "name": "typescript-demo",
  "version": "1.0.0",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsc && node dist/index.js"
  },
  "devDependencies": {
    "typescript": "^5.3.0",
    "@types/node": "^20.0.0"
  }
}
```

**3. Create src/calculator.ts:**

```typescript
// src/calculator.ts

/**
 * Calculator class with type-safe operations
 */
export class Calculator {
  /**
   * Adds two numbers
   * @param a - First number
   * @param b - Second number
   * @returns Sum of a and b
   */
  add(a: number, b: number): number {
    return a + b;
  }

  /**
   * Subtracts b from a
   */
  subtract(a: number, b: number): number {
    return a - b;
  }

  /**
   * Multiplies two numbers
   */
  multiply(a: number, b: number): number {
    return a * b;
  }

  /**
   * Divides a by b
   * @throws Error if dividing by zero
   */
  divide(a: number, b: number): number {
    if (b === 0) {
      throw new Error("Cannot divide by zero");
    }
    return a / b;
  }

  /**
   * Calculates power
   */
  power(base: number, exponent: number): number {
    return Math.pow(base, exponent);
  }
}
```

**4. Create src/user.ts:**

```typescript
// src/user.ts

/**
 * User type definition
 */
export type UserRole = 'admin' | 'user' | 'guest';

export interface User {
  id: number;
  name: string;
  email: string;
  age: number;
  role: UserRole;
  isActive: boolean;
}

/**
 * User manager class
 */
export class UserManager {
  private users: User[] = [];
  private nextId: number = 1;

  /**
   * Create a new user
   */
  createUser(
    name: string,
    email: string,
    age: number,
    role: UserRole = 'user'
  ): User {
    const user: User = {
      id: this.nextId++,
      name,
      email,
      age,
      role,
      isActive: true
    };
    this.users.push(user);
    return user;
  }

  /**
   * Get user by ID
   */
  getUserById(id: number): User | undefined {
    return this.users.find(user => user.id === id);
  }

  /**
   * Get all users
   */
  getAllUsers(): User[] {
    return [...this.users];
  }

  /**
   * Get users by role
   */
  getUsersByRole(role: UserRole): User[] {
    return this.users.filter(user => user.role === role);
  }

  /**
   * Update user
   */
  updateUser(id: number, updates: Partial<User>): User | undefined {
    const user = this.getUserById(id);
    if (user) {
      Object.assign(user, updates);
    }
    return user;
  }

  /**
   * Delete user
   */
  deleteUser(id: number): boolean {
    const index = this.users.findIndex(user => user.id === id);
    if (index !== -1) {
      this.users.splice(index, 1);
      return true;
    }
    return false;
  }

  /**
   * Get active users count
   */
  getActiveUsersCount(): number {
    return this.users.filter(user => user.isActive).length;
  }
}
```

**5. Create src/index.ts (Main Application):**

```typescript
// src/index.ts

import { Calculator } from './calculator';
import { UserManager, User } from './user';

console.log('=== TypeScript Demo Application ===\n');

// 1. Calculator Demo
console.log('--- Calculator Demo ---');
const calc = new Calculator();

console.log('5 + 3 =', calc.add(5, 3));
console.log('10 - 4 =', calc.subtract(10, 4));
console.log('6 * 7 =', calc.multiply(6, 7));
console.log('20 / 4 =', calc.divide(20, 4));
console.log('2 ^ 8 =', calc.power(2, 8));

// TypeScript catches this error at compile time!
// calc.add("5", "3");  // ❌ Error: Argument of type 'string' is not assignable to parameter of type 'number'

try {
  calc.divide(10, 0);
} catch (error) {
  console.log('Error:', (error as Error).message);
}

console.log('\n--- User Manager Demo ---');

// 2. User Manager Demo
const userManager = new UserManager();

// Create users
const user1 = userManager.createUser('Alice Johnson', 'alice@example.com', 28, 'admin');
const user2 = userManager.createUser('Bob Smith', 'bob@example.com', 32, 'user');
const user3 = userManager.createUser('Charlie Brown', 'charlie@example.com', 25, 'user');
const user4 = userManager.createUser('Diana Prince', 'diana@example.com', 30, 'guest');

console.log('\n✅ Created users:');
userManager.getAllUsers().forEach(user => {
  console.log(`  ${user.id}. ${user.name} (${user.role}) - ${user.email}`);
});

// Get user by ID
console.log('\n🔍 Get user by ID (2):');
const foundUser = userManager.getUserById(2);
if (foundUser) {
  console.log(`  Found: ${foundUser.name} - ${foundUser.email}`);
}

// Get users by role
console.log('\n👥 Users with role "user":');
const regularUsers = userManager.getUsersByRole('user');
regularUsers.forEach(user => {
  console.log(`  - ${user.name}`);
});

// Update user
console.log('\n✏️  Update user (3):');
const updated = userManager.updateUser(3, { age: 26, role: 'admin' });
if (updated) {
  console.log(`  Updated: ${updated.name} is now ${updated.age} years old and role is ${updated.role}`);
}

// Active users count
console.log('\n📊 Active users count:', userManager.getActiveUsersCount());

// Deactivate a user
userManager.updateUser(4, { isActive: false });
console.log('📊 Active users count after deactivation:', userManager.getActiveUsersCount());

// Delete user
console.log('\n🗑️  Delete user (2):');
const deleted = userManager.deleteUser(2);
console.log(`  Deleted: ${deleted ? 'Success' : 'Failed'}`);

console.log('\n📋 Final user list:');
userManager.getAllUsers().forEach(user => {
  console.log(`  ${user.id}. ${user.name} (${user.role}) - Active: ${user.isActive}`);
});

// TypeScript type safety examples
console.log('\n--- Type Safety Examples ---');

// ✅ Type inference
let message = "Hello";  // TypeScript infers type as string
console.log('Type of message:', typeof message);

// ❌ This would cause compile error
// message = 42;  // Error: Type 'number' is not assignable to type 'string'

// ✅ Explicit typing
let count: number = 10;
let isActive: boolean = true;
let items: string[] = ['apple', 'banana', 'orange'];

console.log('Count:', count);
console.log('Is Active:', isActive);
console.log('Items:', items.join(', '));

// ✅ Function with type annotations
function calculateDiscount(price: number, discount: number): number {
  return price - (price * discount / 100);
}

console.log('Price after 20% discount:', calculateDiscount(100, 20));

// ❌ This would cause compile error
// calculateDiscount("100", 20);  // Error: Argument of type 'string' is not assignable to parameter of type 'number'

console.log('\n=== TypeScript Demo Complete ===');
```

**6. Build and Run:**

```bash
# Compile TypeScript to JavaScript
npm run build

# Run the compiled JavaScript
npm start

# Or do both in one command
npm run dev
```

**Expected Output:**
```
=== TypeScript Demo Application ===

--- Calculator Demo ---
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
20 / 4 = 5
2 ^ 8 = 256
Error: Cannot divide by zero

--- User Manager Demo ---

✅ Created users:
  1. Alice Johnson (admin) - alice@example.com
  2. Bob Smith (user) - bob@example.com
  3. Charlie Brown (user) - charlie@example.com
  4. Diana Prince (guest) - diana@example.com

🔍 Get user by ID (2):
  Found: Bob Smith - bob@example.com

👥 Users with role "user":
  - Bob Smith
  - Charlie Brown

✏️  Update user (3):
  Updated: Charlie Brown is now 26 years old and role is admin

📊 Active users count: 4
📊 Active users count after deactivation: 3

🗑️  Delete user (2):
  Deleted: Success

📋 Final user list:
  1. Alice Johnson (admin) - Active: true
  3. Charlie Brown (admin) - Active: true
  4. Diana Prince (guest) - Active: false

--- Type Safety Examples ---
Type of message: string
Count: 10
Is Active: true
Items: apple, banana, orange
Price after 20% discount: 80

=== TypeScript Demo Complete ===
```

---

**💡 Understanding tsconfig.json Options**

```json
{
  "compilerOptions": {
    // Language & Environment
    "target": "ES2020",              // JavaScript version (ES5, ES6, ES2020, etc.)
    "lib": ["ES2020"],               // Standard library to include
    "module": "commonjs",            // Module system (commonjs, es2015, esnext)
    
    // Strict Type Checking
    "strict": true,                  // Enable all strict options
    "noImplicitAny": true,          // Error on expressions with implied 'any'
    "strictNullChecks": true,       // Ensure null/undefined are handled
    "strictFunctionTypes": true,    // Strict function types
    
    // Module Resolution
    "esModuleInterop": true,        // Better ES module compatibility
    "moduleResolution": "node",     // Use Node.js module resolution
    "resolveJsonModule": true,      // Allow importing JSON files
    
    // Emit
    "outDir": "./dist",             // Output directory
    "rootDir": "./src",             // Input directory
    "sourceMap": true,              // Generate .map files for debugging
    "declaration": true,            // Generate .d.ts files
    "removeComments": true,         // Remove comments from output
    
    // Type Checking
    "skipLibCheck": true,           // Skip type checking of .d.ts files
    "forceConsistentCasingInFileNames": true,
    
    // Advanced
    "allowSyntheticDefaultImports": true,
    "experimentalDecorators": true,  // Enable decorators
    "emitDecoratorMetadata": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.spec.ts"]
}
```

---

**💡 TypeScript Compiler Commands**

```bash
# Compile a single file
tsc app.ts

# Compile with config file
tsc

# Watch mode (auto-compile on changes)
tsc --watch
tsc -w

# Compile specific files
tsc file1.ts file2.ts

# Output to specific directory
tsc --outDir dist

# Compile without emitting files (check for errors only)
tsc --noEmit

# Show compiler version
tsc --version

# Initialize tsconfig.json
tsc --init

# Compile with specific target
tsc --target ES2020 app.ts
```

---

**🎯 Hands-on Practice**

**Exercise 1: Convert JavaScript to TypeScript**

Convert this JavaScript function to TypeScript with proper types:

```javascript
// JavaScript version
function calculateTotalPrice(items) {
  let total = 0;
  for (let item of items) {
    total += item.price * item.quantity;
  }
  return total;
}
```

**Solution:**

```typescript
// TypeScript version
interface CartItem {
  name: string;
  price: number;
  quantity: number;
}

function calculateTotalPrice(items: CartItem[]): number {
  let total: number = 0;
  for (let item of items) {
    total += item.price * item.quantity;
  }
  return total;
}

// Usage
const cart: CartItem[] = [
  { name: 'Laptop', price: 999, quantity: 1 },
  { name: 'Mouse', price: 29, quantity: 2 }
];

console.log('Total:', calculateTotalPrice(cart));  // Total: 1057
```

**Exercise 2: Create a TypeScript Library Manager**

```typescript
// library.ts

interface Book {
  id: number;
  title: string;
  author: string;
  year: number;
  isAvailable: boolean;
}

class Library {
  private books: Book[] = [];
  private nextId: number = 1;

  addBook(title: string, author: string, year: number): Book {
    const book: Book = {
      id: this.nextId++,
      title,
      author,
      year,
      isAvailable: true
    };
    this.books.push(book);
    return book;
  }

  findBookById(id: number): Book | undefined {
    return this.books.find(book => book.id === id);
  }

  findBooksByAuthor(author: string): Book[] {
    return this.books.filter(book => 
      book.author.toLowerCase().includes(author.toLowerCase())
    );
  }

  borrowBook(id: number): boolean {
    const book = this.findBookById(id);
    if (book && book.isAvailable) {
      book.isAvailable = false;
      return true;
    }
    return false;
  }

  returnBook(id: number): boolean {
    const book = this.findBookById(id);
    if (book && !book.isAvailable) {
      book.isAvailable = true;
      return true;
    }
    return false;
  }

  getAvailableBooks(): Book[] {
    return this.books.filter(book => book.isAvailable);
  }
}

// Usage
const library = new Library();
library.addBook('1984', 'George Orwell', 1949);
library.addBook('To Kill a Mockingbird', 'Harper Lee', 1960);
library.addBook('The Great Gatsby', 'F. Scott Fitzgerald', 1925);

console.log('Available books:', library.getAvailableBooks());
library.borrowBook(1);
console.log('After borrowing book 1:', library.getAvailableBooks());
```

---

**📚 Interview Questions & Answers**

**Q1: What is TypeScript and why should we use it?**

**Answer:**
TypeScript is a superset of JavaScript that adds static typing and other features. We should use it because:

1. **Early Error Detection**: Catches errors during development, not in production
2. **Better IDE Support**: Autocomplete, refactoring, IntelliSense
3. **Self-Documenting**: Types serve as inline documentation
4. **Improved Maintainability**: Easier to refactor large codebases
5. **Team Collaboration**: Clear contracts between modules

**Example:**
```typescript
// Without TypeScript - bug only found at runtime
function getUser(id) {
  return users.find(u => u.id === id);
}
getUser("123");  // Bug: expects number but got string

// With TypeScript - caught immediately
function getUser(id: number): User | undefined {
  return users.find(u => u.id === id);
}
getUser("123");  // ❌ Compile error: string not assignable to number
```

**Q2: What are the benefits of static typing?**

**Answer:**
Static typing provides several benefits:

1. **Type Safety**: Prevents type-related errors
2. **Better Documentation**: Code is self-documenting
3. **Refactoring Confidence**: Change code without breaking things
4. **Early Error Detection**: Find bugs before runtime
5. **Better Tooling**: IDE can provide better suggestions

**Example:**
```typescript
// Static typing prevents bugs
interface User {
  name: string;
  age: number;
}

function greetUser(user: User): string {
  return `Hello, ${user.name}! You are ${user.age} years old.`;
}

// ✅ Correct usage
greetUser({ name: 'Alice', age: 25 });

// ❌ Compile errors
greetUser({ name: 'Bob' });              // Missing 'age'
greetUser({ name: 'Charlie', age: '25' }); // Wrong type for 'age'
greetUser({ firstName: 'Diana', age: 30 }); // Wrong property name
```

**Q3: Explain the TypeScript compilation process.**

**Answer:**
TypeScript compilation involves these steps:

1. **Parse**: TypeScript code is parsed into an Abstract Syntax Tree (AST)
2. **Type Check**: TypeScript compiler checks types for errors
3. **Transform**: TypeScript-specific syntax is removed
4. **Emit**: JavaScript code is generated

```typescript
// 1. TypeScript Source (app.ts)
function add(a: number, b: number): number {
  return a + b;
}

// 2. TypeScript Compiler runs type checking
// Validates that types are correct

// 3. Compiled JavaScript Output (app.js)
function add(a, b) {
  return a + b;
}
```

**The Process:**
- Input: `.ts` file with type annotations
- Process: `tsc` (TypeScript Compiler) validates types
- Output: `.js` file with types removed
- Result: Regular JavaScript that runs anywhere

**Q4: What is the difference between `tsc` and `ts-node`?**

**Answer:**

**tsc (TypeScript Compiler):**
- Compiles TypeScript to JavaScript files
- Creates `.js` files in the output directory
- Used for production builds
- Two-step process: compile then run

```bash
tsc app.ts        # Creates app.js
node app.js       # Run the JavaScript
```

**ts-node:**
- Runs TypeScript directly without creating `.js` files
- Used for development and testing
- One-step process: compile and run in memory

```bash
ts-node app.ts    # Compiles and runs directly
```

**Q5: What happens if you don't specify types in TypeScript?**

**Answer:**
TypeScript uses **type inference** to automatically determine types:

```typescript
// No explicit type, but TypeScript infers it
let message = "Hello";  // inferred as string
let count = 42;         // inferred as number
let isActive = true;    // inferred as boolean

// TypeScript still enforces types
message = 123;          // ❌ Error: Type 'number' is not assignable to type 'string'

// Functions with inference
function double(x: number) {
  return x * 2;         // Return type inferred as number
}

// If TypeScript can't infer, it defaults to 'any' (no type checking)
let something;          // type: any
something = "text";     // OK
something = 42;         // OK (dangerous!)
```

**Best Practice**: Always enable `strict` mode in `tsconfig.json` to catch cases where types can't be inferred.

---

**🔑 Key Takeaways**

1. ✅ TypeScript = JavaScript + Static Types + Better Tooling
2. ✅ Catches errors during development, not in production
3. ✅ Compiles to regular JavaScript - runs anywhere
4. ✅ `tsconfig.json` configures compiler options
5. ✅ Use `tsc` to compile, `tsc --watch` for development
6. ✅ Type inference works, but explicit types are clearer
7. ✅ Great for large projects and team collaboration

**Learning Resources:**
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript Playground](https://www.typescriptlang.org/play) - Try TypeScript online
- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/)
- [Execute Program - TypeScript Course](https://www.executeprogram.com/courses/typescript)

---

### Day 32: Types, Interfaces, Enums & Generics

**📖 TypeScript Basic Types**

TypeScript provides several built-in types to describe values:

**Primitive Types:**
```typescript
// String
let name: string = "Alice";
let message: string = `Hello, ${name}`;

// Number (integers and floats)
let age: number = 25;
let price: number = 19.99;
let hex: number = 0xff;

// Boolean
let isActive: boolean = true;
let hasPermission: boolean = false;

// Any (avoid when possible - defeats purpose of TypeScript)
let anything: any = "hello";
anything = 42;       // OK, but not type-safe
anything = true;     // OK, but dangerous

// Void (no return value)
function logMessage(msg: string): void {
  console.log(msg);
  // No return statement
}

// Null and Undefined
let nothing: null = null;
let notDefined: undefined = undefined;

// Never (function never returns)
function throwError(message: string): never {
  throw new Error(message);
}
```

---

**📖 Arrays and Tuples**

```typescript
// Arrays - two syntaxes
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["Alice", "Bob", "Charlie"];

// Mixed types array (not recommended)
let mixed: any[] = [1, "hello", true];

// Better: Use union types
let values: (string | number)[] = [1, "two", 3, "four"];

// Tuples - fixed-length arrays with specific types
let person: [string, number] = ["Alice", 25];
let coordinate: [number, number] = [10, 20];

// Tuple with optional and rest elements
let record: [string, number, boolean?] = ["data", 42];
let moreValues: [string, ...number[]] = ["first", 1, 2, 3, 4];

// Accessing tuple elements
console.log(person[0]);  // "Alice"
console.log(person[1]);  // 25
```

---

**📖 Interfaces**

Interfaces define the structure of objects. Think of them as contracts or blueprints.

```typescript
// Basic interface
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// Using the interface
const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
  age: 25
};

// Optional properties
interface Product {
  id: number;
  name: string;
  price: number;
  description?: string;  // Optional (can be undefined)
  category?: string;
}

const product: Product = {
  id: 101,
  name: "Laptop",
  price: 999
  // description and category are optional
};

// Readonly properties
interface Config {
  readonly apiKey: string;
  readonly baseUrl: string;
  timeout: number;  // Can be changed
}

const config: Config = {
  apiKey: "abc123",
  baseUrl: "https://api.example.com",
  timeout: 5000
};

// config.apiKey = "new key";  // ❌ Error: Cannot assign to 'apiKey' because it is a read-only property

// Extending interfaces
interface Person {
  name: string;
  age: number;
}

interface Employee extends Person {
  employeeId: number;
  department: string;
  salary: number;
}

const employee: Employee = {
  name: "Bob",
  age: 30,
  employeeId: 1001,
  department: "Engineering",
  salary: 80000
};

// Interface for functions
interface MathOperation {
  (a: number, b: number): number;
}

const add: MathOperation = (x, y) => x + y;
const multiply: MathOperation = (x, y) => x * y;

console.log(add(5, 3));       // 8
console.log(multiply(4, 7));   // 28
```

---

**📖 Type Aliases**

Type aliases create custom names for types.

```typescript
// Simple type alias
type ID = string | number;
type Status = "pending" | "approved" | "rejected";

let userId: ID = 123;
let orderId: ID = "ORD-456";
let orderStatus: Status = "pending";

// Object type alias
type Point = {
  x: number;
  y: number;
};

const point: Point = { x: 10, y: 20 };

// Function type alias
type GreetFunction = (name: string) => string;

const greet: GreetFunction = (name) => `Hello, ${name}!`;

// Complex type alias
type User = {
  id: number;
  name: string;
  email: string;
  role: "admin" | "user" | "guest";
  permissions: string[];
};
```

**Interface vs Type Alias:**

```typescript
// Both can describe object shapes
interface UserInterface {
  name: string;
  age: number;
}

type UserType = {
  name: string;
  age: number;
};

// Key differences:

// 1. Interfaces can be extended
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

// 2. Types can use union and intersection
type Shape = Circle | Square | Triangle;
type Employee = Person & HasSalary;

// 3. Interfaces can be re-opened (declaration merging)
interface Window {
  title: string;
}

interface Window {
  size: number;
}

// Window now has both title and size

// Best Practice: Use interface for objects, type for unions/intersections
```

---

**📖 Enums**

Enums define a set of named constants.

```typescript
// Numeric enum (default starts at 0)
enum Direction {
  Up,       // 0
  Down,     // 1
  Left,     // 2
  Right     // 3
}

let playerDirection: Direction = Direction.Up;
console.log(playerDirection);  // 0

// Numeric enum with custom start
enum Status {
  Pending = 1,
  Approved = 2,
  Rejected = 3
}

// String enum
enum Color {
  Red = "RED",
  Green = "GREEN",
  Blue = "BLUE"
}

let favoriteColor: Color = Color.Blue;
console.log(favoriteColor);  // "BLUE"

// Mixed enum (not recommended)
enum Mixed {
  Yes = 1,
  No = "NO"
}

// Enum in practice
enum UserRole {
  Admin = "ADMIN",
  User = "USER",
  Guest = "GUEST"
}

interface User {
  id: number;
  name: string;
  role: UserRole;
}

const admin: User = {
  id: 1,
  name: "Alice",
  role: UserRole.Admin
};

function checkPermission(role: UserRole): boolean {
  if (role === UserRole.Admin) {
    return true;
  }
  return false;
}
```

---

**📖 Union and Intersection Types**

**Union Types** (OR): A value can be one of several types.

```typescript
// Union type
type Result = string | number;

let value: Result;
value = "success";  // OK
value = 404;        // OK
// value = true;    // ❌ Error

// Union with literal types
type Status = "loading" | "success" | "error";

function handleStatus(status: Status) {
  if (status === "loading") {
    console.log("Loading...");
  } else if (status === "success") {
    console.log("Success!");
  } else {
    console.log("Error occurred");
  }
}

// Function with union parameter
function printId(id: string | number) {
  console.log(`ID: ${id}`);
}

printId(123);      // OK
printId("ABC");    // OK

// Type narrowing with unions
function format(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase();  // TypeScript knows it's string here
  } else {
    return value.toFixed(2);     // TypeScript knows it's number here
  }
}
```

**Intersection Types** (AND): Combines multiple types into one.

```typescript
// Intersection type
type Person = {
  name: string;
  age: number;
};

type Employee = {
  employeeId: number;
  department: string;
};

type EmployeePerson = Person & Employee;

const worker: EmployeePerson = {
  name: "Bob",
  age: 30,
  employeeId: 1001,
  department: "IT"
  // Must have all properties from both types
};

// Practical example
type Timestamped = {
  createdAt: Date;
  updatedAt: Date;
};

type User = {
  id: number;
  name: string;
  email: string;
};

type UserWithTimestamps = User & Timestamped;

const user: UserWithTimestamps = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
  createdAt: new Date(),
  updatedAt: new Date()
};
```

---

**📖 Type Assertions**

Type assertions tell TypeScript "trust me, I know what I'm doing."

```typescript
// Using 'as' syntax (preferred)
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;

// Angle-bracket syntax (not in JSX/TSX)
let value: any = "hello";
let length: number = (<string>value).length;

// Practical example
const input = document.getElementById("username") as HTMLInputElement;
input.value = "Alice";  // TypeScript knows it's an input element

// Non-null assertion operator (!)
function processValue(value: string | null) {
  // Use ! to tell TypeScript: "I guarantee this is not null"
  console.log(value!.toUpperCase());
}

// Be careful with assertions - you're overriding TypeScript's safety
```

---

**📖 Generics**

Generics create reusable components that work with multiple types.

**Real-World Analogy:** A generic is like a container that can hold any type of item - like a storage box that works for books, clothes, or electronics.

```typescript
// Simple generic function
function identity<T>(value: T): T {
  return value;
}

let num = identity<number>(42);        // T is number
let str = identity<string>("hello");   // T is string
let auto = identity(true);             // T inferred as boolean

// Generic array function
function getFirstElement<T>(arr: T[]): T | undefined {
  return arr[0];
}

console.log(getFirstElement([1, 2, 3]));        // 1
console.log(getFirstElement(["a", "b", "c"]));  // "a"

// Generic interface
interface Box<T> {
  value: T;
}

let numberBox: Box<number> = { value: 123 };
let stringBox: Box<string> = { value: "hello" };

// Generic class
class DataStorage<T> {
  private data: T[] = [];

  addItem(item: T): void {
    this.data.push(item);
  }

  removeItem(item: T): void {
    const index = this.data.indexOf(item);
    if (index !== -1) {
      this.data.splice(index, 1);
    }
  }

  getItems(): T[] {
    return [...this.data];
  }
}

const textStorage = new DataStorage<string>();
textStorage.addItem("Hello");
textStorage.addItem("World");
console.log(textStorage.getItems());  // ["Hello", "World"]

const numberStorage = new DataStorage<number>();
numberStorage.addItem(10);
numberStorage.addItem(20);
console.log(numberStorage.getItems());  // [10, 20]

// Generic constraints
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(item: T): void {
  console.log(`Length: ${item.length}`);
}

logLength("hello");        // OK - string has length
logLength([1, 2, 3]);      // OK - array has length
// logLength(123);         // ❌ Error - number doesn't have length

// Multiple type parameters
function pair<T, U>(first: T, second: U): [T, U] {
  return [first, second];
}

let result = pair<string, number>("age", 25);
console.log(result);  // ["age", 25]
```

---

**💡 Complete Example: E-Commerce Product System**

```typescript
// types.ts

// Enums
export enum ProductCategory {
  Electronics = "ELECTRONICS",
  Clothing = "CLOTHING",
  Books = "BOOKS",
  Food = "FOOD",
  Sports = "SPORTS"
}

export enum OrderStatus {
  Pending = "PENDING",
  Processing = "PROCESSING",
  Shipped = "SHIPPED",
  Delivered = "DELIVERED",
  Cancelled = "CANCELLED"
}

// Interfaces
export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  category: ProductCategory;
  stock: number;
  isAvailable: boolean;
}

export interface Customer {
  id: number;
  name: string;
  email: string;
  phone: string;
  address: Address;
}

export interface Address {
  street: string;
  city: string;
  state: string;
  zipCode: string;
  country: string;
}

export interface OrderItem {
  product: Product;
  quantity: number;
  price: number;
}

export interface Order {
  id: number;
  customer: Customer;
  items: OrderItem[];
  total: number;
  status: OrderStatus;
  createdAt: Date;
  updatedAt: Date;
}

// Type aliases
export type ProductId = number;
export type CustomerId = number;
export type OrderId = number;

// Union type
export type PaymentMethod = "credit-card" | "debit-card" | "paypal" | "cash";

// Generic type
export type ApiResponse<T> = {
  success: boolean;
  data?: T;
  error?: string;
  timestamp: Date;
};
```

```typescript
// product-manager.ts

import {
  Product,
  ProductCategory,
  Customer,
  Order,
  OrderItem,
  OrderStatus,
  PaymentMethod,
  ApiResponse,
  ProductId,
  CustomerId,
  OrderId
} from './types';

// Generic class for data management
class DataManager<T extends { id: number }> {
  protected items: T[] = [];
  protected nextId: number = 1;

  getAll(): T[] {
    return [...this.items];
  }

  getById(id: number): T | undefined {
    return this.items.find(item => item.id === id);
  }

  delete(id: number): boolean {
    const index = this.items.findIndex(item => item.id === id);
    if (index !== -1) {
      this.items.splice(index, 1);
      return true;
    }
    return false;
  }

  count(): number {
    return this.items.length;
  }
}

// Product Manager
export class ProductManager extends DataManager<Product> {
  addProduct(
    name: string,
    description: string,
    price: number,
    category: ProductCategory,
    stock: number
  ): Product {
    const product: Product = {
      id: this.nextId++,
      name,
      description,
      price,
      category,
      stock,
      isAvailable: stock > 0
    };
    this.items.push(product);
    return product;
  }

  updateStock(id: ProductId, quantity: number): ApiResponse<Product> {
    const product = this.getById(id);
    if (!product) {
      return {
        success: false,
        error: "Product not found",
        timestamp: new Date()
      };
    }

    product.stock += quantity;
    product.isAvailable = product.stock > 0;

    return {
      success: true,
      data: product,
      timestamp: new Date()
    };
  }

  getProductsByCategory(category: ProductCategory): Product[] {
    return this.items.filter(p => p.category === category);
  }

  getAvailableProducts(): Product[] {
    return this.items.filter(p => p.isAvailable);
  }

  searchProducts(query: string): Product[] {
    const lowerQuery = query.toLowerCase();
    return this.items.filter(p =>
      p.name.toLowerCase().includes(lowerQuery) ||
      p.description.toLowerCase().includes(lowerQuery)
    );
  }
}

// Customer Manager
export class CustomerManager extends DataManager<Customer> {
  addCustomer(
    name: string,
    email: string,
    phone: string,
    address: {
      street: string;
      city: string;
      state: string;
      zipCode: string;
      country: string;
    }
  ): Customer {
    const customer: Customer = {
      id: this.nextId++,
      name,
      email,
      phone,
      address
    };
    this.items.push(customer);
    return customer;
  }

  findByEmail(email: string): Customer | undefined {
    return this.items.find(c => c.email === email);
  }

  updateCustomer(id: CustomerId, updates: Partial<Customer>): ApiResponse<Customer> {
    const customer = this.getById(id);
    if (!customer) {
      return {
        success: false,
        error: "Customer not found",
        timestamp: new Date()
      };
    }

    Object.assign(customer, updates);

    return {
      success: true,
      data: customer,
      timestamp: new Date()
    };
  }
}

// Order Manager
export class OrderManager extends DataManager<Order> {
  constructor(
    private productManager: ProductManager,
    private customerManager: CustomerManager
  ) {
    super();
  }

  createOrder(
    customerId: CustomerId,
    items: Array<{ productId: ProductId; quantity: number }>,
    paymentMethod: PaymentMethod
  ): ApiResponse<Order> {
    const customer = this.customerManager.getById(customerId);
    if (!customer) {
      return {
        success: false,
        error: "Customer not found",
        timestamp: new Date()
      };
    }

    const orderItems: OrderItem[] = [];
    let total = 0;

    for (const item of items) {
      const product = this.productManager.getById(item.productId);
      if (!product) {
        return {
          success: false,
          error: `Product ${item.productId} not found`,
          timestamp: new Date()
        };
      }

      if (product.stock < item.quantity) {
        return {
          success: false,
          error: `Insufficient stock for ${product.name}`,
          timestamp: new Date()
        };
      }

      const orderItem: OrderItem = {
        product,
        quantity: item.quantity,
        price: product.price
      };

      orderItems.push(orderItem);
      total += product.price * item.quantity;

      // Update stock
      this.productManager.updateStock(product.id, -item.quantity);
    }

    const order: Order = {
      id: this.nextId++,
      customer,
      items: orderItems,
      total,
      status: OrderStatus.Pending,
      createdAt: new Date(),
      updatedAt: new Date()
    };

    this.items.push(order);

    return {
      success: true,
      data: order,
      timestamp: new Date()
    };
  }

  updateOrderStatus(orderId: OrderId, status: OrderStatus): ApiResponse<Order> {
    const order = this.getById(orderId);
    if (!order) {
      return {
        success: false,
        error: "Order not found",
        timestamp: new Date()
      };
    }

    order.status = status;
    order.updatedAt = new Date();

    return {
      success: true,
      data: order,
      timestamp: new Date()
    };
  }

  getOrdersByCustomer(customerId: CustomerId): Order[] {
    return this.items.filter(o => o.customer.id === customerId);
  }

  getOrdersByStatus(status: OrderStatus): Order[] {
    return this.items.filter(o => o.status === status);
  }

  cancelOrder(orderId: OrderId): ApiResponse<Order> {
    const order = this.getById(orderId);
    if (!order) {
      return {
        success: false,
        error: "Order not found",
        timestamp: new Date()
      };
    }

    if (order.status === OrderStatus.Delivered) {
      return {
        success: false,
        error: "Cannot cancel delivered order",
        timestamp: new Date()
      };
    }

    // Restore stock
    for (const item of order.items) {
      this.productManager.updateStock(item.product.id, item.quantity);
    }

    order.status = OrderStatus.Cancelled;
    order.updatedAt = new Date();

    return {
      success: true,
      data: order,
      timestamp: new Date()
    };
  }
}
```

```typescript
// main.ts - Demo Application

import { ProductManager, CustomerManager, OrderManager } from './product-manager';
import { ProductCategory, OrderStatus } from './types';

console.log('=== E-Commerce System Demo ===\n');

// Initialize managers
const productManager = new ProductManager();
const customerManager = new CustomerManager();
const orderManager = new OrderManager(productManager, customerManager);

// Add products
console.log('--- Adding Products ---');
const laptop = productManager.addProduct(
  'MacBook Pro',
  '16-inch laptop with M3 chip',
  2499,
  ProductCategory.Electronics,
  10
);
const phone = productManager.addProduct(
  'iPhone 15 Pro',
  'Latest smartphone',
  999,
  ProductCategory.Electronics,
  25
);
const book = productManager.addProduct(
  'TypeScript Handbook',
  'Complete guide to TypeScript',
  39.99,
  ProductCategory.Books,
  50
);

console.log(`✅ Added ${productManager.count()} products`);

// Add customers
console.log('\n--- Adding Customers ---');
const customer1 = customerManager.addCustomer(
  'Alice Johnson',
  'alice@example.com',
  '555-0101',
  {
    street: '123 Main St',
    city: 'San Francisco',
    state: 'CA',
    zipCode: '94102',
    country: 'USA'
  }
);

const customer2 = customerManager.addCustomer(
  'Bob Smith',
  'bob@example.com',
  '555-0102',
  {
    street: '456 Oak Ave',
    city: 'New York',
    state: 'NY',
    zipCode: '10001',
    country: 'USA'
  }
);

console.log(`✅ Added ${customerManager.count()} customers`);

// Create orders
console.log('\n--- Creating Orders ---');
const order1Result = orderManager.createOrder(
  customer1.id,
  [
    { productId: laptop.id, quantity: 1 },
    { productId: book.id, quantity: 2 }
  ],
  'credit-card'
);

if (order1Result.success && order1Result.data) {
  console.log(`✅ Order #${order1Result.data.id} created for ${customer1.name}`);
  console.log(`   Total: $${order1Result.data.total.toFixed(2)}`);
  console.log(`   Items: ${order1Result.data.items.length}`);
}

const order2Result = orderManager.createOrder(
  customer2.id,
  [
    { productId: phone.id, quantity: 2 }
  ],
  'paypal'
);

if (order2Result.success && order2Result.data) {
  console.log(`✅ Order #${order2Result.data.id} created for ${customer2.name}`);
  console.log(`   Total: $${order2Result.data.total.toFixed(2)}`);
}

// Update order status
console.log('\n--- Processing Orders ---');
if (order1Result.success && order1Result.data) {
  orderManager.updateOrderStatus(order1Result.data.id, OrderStatus.Processing);
  orderManager.updateOrderStatus(order1Result.data.id, OrderStatus.Shipped);
  console.log(`✅ Order #${order1Result.data.id} status: ${OrderStatus.Shipped}`);
}

// Search products
console.log('\n--- Product Search ---');
const electronicProducts = productManager.getProductsByCategory(ProductCategory.Electronics);
console.log(`📱 Electronics (${electronicProducts.length}):`);
electronicProducts.forEach(p => {
  console.log(`   - ${p.name}: $${p.price} (Stock: ${p.stock})`);
});

const searchResults = productManager.searchProducts('TypeScript');
console.log(`\n🔍 Search for "TypeScript" (${searchResults.length} results):`);
searchResults.forEach(p => {
  console.log(`   - ${p.name}: $${p.price}`);
});

// Customer orders
console.log('\n--- Customer Order History ---');
const aliceOrders = orderManager.getOrdersByCustomer(customer1.id);
console.log(`📦 ${customer1.name}'s Orders (${aliceOrders.length}):`);
aliceOrders.forEach(order => {
  console.log(`   Order #${order.id}:`);
  console.log(`     Status: ${order.status}`);
  console.log(`     Total: $${order.total.toFixed(2)}`);
  console.log(`     Date: ${order.createdAt.toLocaleDateString()}`);
});

// Current inventory
console.log('\n--- Current Inventory ---');
const allProducts = productManager.getAll();
console.log('📊 All Products:');
allProducts.forEach(p => {
  const availability = p.isAvailable ? '✅ Available' : '❌ Out of Stock';
  console.log(`   ${p.name}: ${p.stock} units - ${availability}`);
});

console.log('\n=== Demo Complete ===');
```

**Run the example:**

```bash
# Compile
tsc

# Run
node dist/main.js
```

---

**🎯 Hands-on Practice**

**Exercise 1: Generic Stack Implementation**

```typescript
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }

  size(): number {
    return this.items.length;
  }

  clear(): void {
    this.items = [];
  }

  toArray(): T[] {
    return [...this.items];
  }
}

// Usage
const numberStack = new Stack<number>();
numberStack.push(10);
numberStack.push(20);
numberStack.push(30);
console.log(numberStack.pop());  // 30
console.log(numberStack.peek()); // 20

const stringStack = new Stack<string>();
stringStack.push("hello");
stringStack.push("world");
console.log(stringStack.toArray());  // ["hello", "world"]
```

**Exercise 2: Type-Safe Event Emitter**

```typescript
type EventCallback<T = any> = (data: T) => void;

class EventEmitter<Events extends Record<string, any>> {
  private events: Map<keyof Events, EventCallback[]> = new Map();

  on<K extends keyof Events>(event: K, callback: EventCallback<Events[K]>): void {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    this.events.get(event)!.push(callback);
  }

  emit<K extends keyof Events>(event: K, data: Events[K]): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      callbacks.forEach(callback => callback(data));
    }
  }

  off<K extends keyof Events>(event: K, callback: EventCallback<Events[K]>): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      const index = callbacks.indexOf(callback);
      if (index !== -1) {
        callbacks.splice(index, 1);
      }
    }
  }
}

// Define events with types
interface MyEvents {
  userLogin: { userId: number; timestamp: Date };
  dataUpdate: { id: number; value: string };
  error: { message: string; code: number };
}

const emitter = new EventEmitter<MyEvents>();

emitter.on('userLogin', (data) => {
  // TypeScript knows data has userId and timestamp
  console.log(`User ${data.userId} logged in at ${data.timestamp}`);
});

emitter.on('error', (data) => {
  // TypeScript knows data has message and code
  console.error(`Error ${data.code}: ${data.message}`);
});

emitter.emit('userLogin', { userId: 123, timestamp: new Date() });
emitter.emit('error', { message: 'Connection failed', code: 500 });
```

---

**📚 Interview Questions & Answers**

**Q1: What is the difference between interface and type alias in TypeScript?**

**Answer:**

**Interface:**
- Can be extended using `extends`
- Supports declaration merging (can add properties later)
- Best for object shapes and class contracts
- Can be implemented by classes

**Type Alias:**
- Can represent any type (primitives, unions, intersections, tuples)
- Cannot be reopened to add properties
- More flexible for complex types
- Cannot be implemented by classes (but intersection types can simulate this)

```typescript
// Interface - can be extended
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

// Interface - declaration merging
interface Window {
  title: string;
}

interface Window {
  size: number;
}
// Window now has both properties

// Type - unions and complex types
type Status = "loading" | "success" | "error";
type Result = string | number | boolean;
type Point = [number, number];

// Type - intersection
type Person = { name: string };
type Employee = { employeeId: number };
type EmployeePerson = Person & Employee;

// Best practice: Use interface for objects, type for everything else
```

**Q2: What are enums in TypeScript and when should you use them?**

**Answer:**
Enums are a way to define a set of named constants. They make code more readable and maintainable.

**Use enums when:**
- You have a fixed set of related values
- Values have meaningful names
- You want type safety for specific values

```typescript
// Without enum - error-prone
function setStatus(status: string) {
  if (status === "pending") {  // Typo risk: "pendin", "Pending"
    // ...
  }
}

// With enum - type-safe
enum OrderStatus {
  Pending = "PENDING",
  Processing = "PROCESSING",
  Shipped = "SHIPPED",
  Delivered = "DELIVERED"
}

function setStatus(status: OrderStatus) {
  if (status === OrderStatus.Pending) {  // No typos possible!
    // ...
  }
}

setStatus(OrderStatus.Pending);      // ✅ OK
// setStatus("pending");             // ❌ Error
```

**Benefits:**
- Autocomplete in IDE
- Prevents typos
- Easy refactoring
- Self-documenting code

**Q3: Explain union types with examples.**

**Answer:**
Union types allow a value to be one of several types (OR relationship).

```typescript
// Basic union
type ID = string | number;

let userId: ID;
userId = 123;      // OK
userId = "ABC";    // OK
// userId = true;  // Error

// Union with literal types
type Status = "success" | "error" | "loading";

function showMessage(status: Status) {
  switch (status) {
    case "success":
      return "✅ Success!";
    case "error":
      return "❌ Error!";
    case "loading":
      return "⏳ Loading...";
  }
}

// Type narrowing
function processValue(value: string | number) {
  if (typeof value === "string") {
    // TypeScript knows it's string here
    return value.toUpperCase();
  } else {
    // TypeScript knows it's number here
    return value.toFixed(2);
  }
}

// Union of object types
interface Cat {
  type: "cat";
  meow(): void;
}

interface Dog {
  type: "dog";
  bark(): void;
}

type Pet = Cat | Dog;

function handlePet(pet: Pet) {
  if (pet.type === "cat") {
    pet.meow();  // TypeScript knows it's Cat
  } else {
    pet.bark();  // TypeScript knows it's Dog
  }
}
```

**Q4: What are generics and why are they useful?**

**Answer:**
Generics create reusable code components that work with multiple types while maintaining type safety.

**Why use generics:**
- Code reusability
- Type safety
- Avoid code duplication
- Flexible yet type-safe

```typescript
// Without generics - code duplication
function getFirstNumber(arr: number[]): number {
  return arr[0];
}

function getFirstString(arr: string[]): string {
  return arr[0];
}

// With generics - one function for all types
function getFirst<T>(arr: T[]): T {
  return arr[0];
}

const num = getFirst([1, 2, 3]);        // T is number
const str = getFirst(["a", "b", "c"]);  // T is string
const bool = getFirst([true, false]);   // T is boolean

// Generic class example
class Box<T> {
  constructor(private value: T) {}

  getValue(): T {
    return this.value;
  }

  setValue(value: T): void {
    this.value = value;
  }
}

const numberBox = new Box(123);
const stringBox = new Box("hello");

// Generic with constraints
interface HasLength {
  length: number;
}

function logLength<T extends HasLength>(item: T): void {
  console.log(item.length);
}

logLength("hello");      // OK - string has length
logLength([1, 2, 3]);    // OK - array has length
// logLength(123);       // Error - number doesn't have length
```

**Q5: What is type assertion and when should you use it?**

**Answer:**
Type assertion tells TypeScript to treat a value as a specific type. It's like a type cast but doesn't change the runtime value.

**Syntax:**
```typescript
// Method 1: 'as' syntax (preferred)
let value: any = "hello";
let length = (value as string).length;

// Method 2: angle-bracket syntax (not in JSX)
let value2: any = "world";
let length2 = (<string>value2).length;
```

**Common use cases:**

```typescript
// 1. DOM manipulation
const input = document.getElementById("username") as HTMLInputElement;
input.value = "Alice";  // TypeScript knows it's an input

// 2. Working with any type
function processData(data: any) {
  if (typeof data === "string") {
    return (data as string).toUpperCase();
  }
}

// 3. Non-null assertion (!)
function getValue(value: string | null) {
  // Use ! when you KNOW it's not null
  console.log(value!.length);
}

// 4. Type narrowing
interface Cat {
  meow(): void;
}

interface Dog {
  bark(): void;
}

function handleAnimal(animal: Cat | Dog) {
  if ('meow' in animal) {
    (animal as Cat).meow();
  } else {
    (animal as Dog).bark();
  }
}
```

**⚠️ Warning:** Use type assertions carefully! You're telling TypeScript to trust you, so make sure you're correct.

---

**🔑 Key Takeaways**

1. ✅ **Interfaces** - Define object shapes, can be extended
2. ✅ **Type Aliases** - More flexible, supports unions/intersections
3. ✅ **Enums** - Define named constants for better code readability
4. ✅ **Union Types** - Value can be one of several types (OR)
5. ✅ **Intersection Types** - Combine multiple types (AND)
6. ✅ **Generics** - Create reusable, type-safe components
7. ✅ **Type Assertions** - Override TypeScript's type inference (use carefully)
8. ✅ **Tuples** - Fixed-length arrays with specific types
9. ✅ **Literal Types** - Specific values as types

**Learning Resources:**
- [TypeScript Handbook - Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [TypeScript Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
- [TypeScript Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)
- [TypeScript Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)

---

## Module 9: Databases (Days 33-40)

### Day 33: Introduction to Databases

**📖 What is a Database?**

A database is an organized collection of data that can be easily accessed, managed, and updated. Think of it as a digital filing cabinet where you store and organize information systematically.

**Real-World Analogy:**
- **Without Database**: Like keeping papers scattered on your desk - hard to find, organize, and update
- **With Database**: Like having a well-organized filing system - easy to search, retrieve, and maintain

---

**📖 Types of Databases**

**1. SQL (Relational) Databases**
- Data stored in **tables** with rows and columns
- Uses **structured query language (SQL)**
- Data has predefined **schema** (structure)
- Examples: MySQL, PostgreSQL, SQLite, Microsoft SQL Server

**When to use SQL:**
- Complex queries with multiple tables
- Data with clear relationships
- Need ACID properties (Atomicity, Consistency, Isolation, Durability)
- Financial applications, banking systems

**2. NoSQL (Non-Relational) Databases**
- Data stored in flexible formats (documents, key-value, graphs)
- Schema-less or flexible schema
- Horizontally scalable
- Examples: MongoDB, Redis, Cassandra, DynamoDB

**When to use NoSQL:**
- Rapid development with changing requirements
- Unstructured or semi-structured data
- Need horizontal scaling
- Real-time web applications, social media, IoT

---

**📖 SQL vs NoSQL Comparison**

| Feature | SQL (PostgreSQL, MySQL) | NoSQL (MongoDB) |
|---------|------------------------|-----------------|
| **Data Structure** | Tables with rows/columns | Documents (JSON-like) |
| **Schema** | Fixed, predefined | Flexible, dynamic |
| **Scaling** | Vertical (more powerful server) | Horizontal (more servers) |
| **Queries** | SQL language | JavaScript-like queries |
| **Relationships** | JOINs between tables | Embedded documents or references |
| **ACID** | Full ACID compliance | Eventually consistent (BASE) |
| **Best For** | Complex queries, transactions | Rapid development, flexibility |

**Example - Same data in both:**

**SQL (PostgreSQL):**
```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  age INTEGER
);

-- Posts table
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200),
  content TEXT,
  user_id INTEGER REFERENCES users(id)
);

-- Query with JOIN
SELECT users.name, posts.title
FROM users
JOIN posts ON users.id = posts.user_id;
```

**NoSQL (MongoDB):**
```javascript
// Users collection
{
  _id: ObjectId("..."),
  name: "Alice Johnson",
  email: "alice@example.com",
  age: 28,
  posts: [
    {
      title: "My First Post",
      content: "Hello World!"
    },
    {
      title: "Second Post",
      content: "Another day..."
    }
  ]
}

// Query
db.users.find({ name: "Alice Johnson" })
```

---

**💡 Complete MongoDB Introduction**

**Installing MongoDB:**

```bash
# macOS
brew tap mongodb/brew
brew install mongodb-community

# Start MongoDB service
brew services start mongodb-community

# Or run manually
mongod --config /usr/local/etc/mongod.conf

# Verify installation
mongosh --version
```

**MongoDB Basics:**

```javascript
// Connect to MongoDB shell
mongosh

// Show all databases
show dbs

// Create/switch to database
use myapp

// Show current database
db

// Show collections (tables)
show collections

// Basic operations
// 1. Insert one document
db.users.insertOne({
  name: "Alice",
  email: "alice@example.com",
  age: 28
})

// 2. Insert multiple documents
db.users.insertMany([
  { name: "Bob", email: "bob@example.com", age: 32 },
  { name: "Charlie", email: "charlie@example.com", age: 25 }
])

// 3. Find all documents
db.users.find()

// 4. Find with filter
db.users.find({ age: { $gte: 30 } })  // age >= 30

// 5. Find one document
db.users.findOne({ name: "Alice" })

// 6. Update one document
db.users.updateOne(
  { name: "Alice" },
  { $set: { age: 29 } }
)

// 7. Update multiple documents
db.users.updateMany(
  { age: { $lt: 30 } },
  { $set: { category: "young" } }
)

// 8. Delete one document
db.users.deleteOne({ name: "Bob" })

// 9. Delete multiple documents
db.users.deleteMany({ age: { $gt: 50 } })

// 10. Count documents
db.users.countDocuments()
db.users.countDocuments({ age: { $gte: 30 } })
```

---

**💡 MongoDB with Node.js - Complete Example**

**Project Structure:**
```
mongodb-demo/
├── package.json
├── .env
├── src/
│   ├── config/
│   │   └── database.js
│   ├── models/
│   │   ├── User.js
│   │   └── Product.js
│   └── index.js
```

**Step 1: Install Dependencies**

```bash
npm init -y
npm install mongodb dotenv
```

**Step 2: Create .env**

```env
# .env
MONGODB_URI=mongodb://localhost:27017/myapp
DB_NAME=myapp
```

**Step 3: Database Configuration (src/config/database.js)**

```javascript
// src/config/database.js
const { MongoClient } = require('mongodb');
require('dotenv').config();

class Database {
  constructor() {
    this.client = null;
    this.db = null;
  }

  async connect() {
    try {
      this.client = new MongoClient(process.env.MONGODB_URI);
      await this.client.connect();
      this.db = this.client.db(process.env.DB_NAME);
      console.log('✅ Connected to MongoDB');
      return this.db;
    } catch (error) {
      console.error('❌ MongoDB connection error:', error);
      throw error;
    }
  }

  getDb() {
    if (!this.db) {
      throw new Error('Database not connected. Call connect() first.');
    }
    return this.db;
  }

  async close() {
    if (this.client) {
      await this.client.close();
      console.log('MongoDB connection closed');
    }
  }
}

module.exports = new Database();
```

**Step 4: User Model (src/models/User.js)**

```javascript
// src/models/User.js
const { ObjectId } = require('mongodb');

class User {
  constructor(db) {
    this.collection = db.collection('users');
  }

  /**
   * Create a new user
   */
  async create(userData) {
    try {
      const user = {
        name: userData.name,
        email: userData.email,
        age: userData.age,
        createdAt: new Date(),
        updatedAt: new Date()
      };

      const result = await this.collection.insertOne(user);
      return { ...user, _id: result.insertedId };
    } catch (error) {
      throw new Error(`Error creating user: ${error.message}`);
    }
  }

  /**
   * Find all users
   */
  async findAll(filter = {}) {
    try {
      return await this.collection.find(filter).toArray();
    } catch (error) {
      throw new Error(`Error finding users: ${error.message}`);
    }
  }

  /**
   * Find user by ID
   */
  async findById(id) {
    try {
      return await this.collection.findOne({ _id: new ObjectId(id) });
    } catch (error) {
      throw new Error(`Error finding user: ${error.message}`);
    }
  }

  /**
   * Find user by email
   */
  async findByEmail(email) {
    try {
      return await this.collection.findOne({ email });
    } catch (error) {
      throw new Error(`Error finding user: ${error.message}`);
    }
  }

  /**
   * Update user
   */
  async update(id, updates) {
    try {
      const result = await this.collection.updateOne(
        { _id: new ObjectId(id) },
        { 
          $set: {
            ...updates,
            updatedAt: new Date()
          }
        }
      );
      return result.modifiedCount > 0;
    } catch (error) {
      throw new Error(`Error updating user: ${error.message}`);
    }
  }

  /**
   * Delete user
   */
  async delete(id) {
    try {
      const result = await this.collection.deleteOne({ _id: new ObjectId(id) });
      return result.deletedCount > 0;
    } catch (error) {
      throw new Error(`Error deleting user: ${error.message}`);
    }
  }

  /**
   * Find users by age range
   */
  async findByAgeRange(minAge, maxAge) {
    try {
      return await this.collection.find({
        age: { $gte: minAge, $lte: maxAge }
      }).toArray();
    } catch (error) {
      throw new Error(`Error finding users by age: ${error.message}`);
    }
  }

  /**
   * Count users
   */
  async count(filter = {}) {
    try {
      return await this.collection.countDocuments(filter);
    } catch (error) {
      throw new Error(`Error counting users: ${error.message}`);
    }
  }

  /**
   * Create index on email field
   */
  async createIndexes() {
    try {
      await this.collection.createIndex({ email: 1 }, { unique: true });
      console.log('✅ Created unique index on email');
    } catch (error) {
      throw new Error(`Error creating indexes: ${error.message}`);
    }
  }
}

module.exports = User;
```

**Step 5: Product Model (src/models/Product.js)**

```javascript
// src/models/Product.js
const { ObjectId } = require('mongodb');

class Product {
  constructor(db) {
    this.collection = db.collection('products');
  }

  async create(productData) {
    try {
      const product = {
        name: productData.name,
        description: productData.description,
        price: productData.price,
        category: productData.category,
        stock: productData.stock || 0,
        isAvailable: productData.stock > 0,
        createdAt: new Date(),
        updatedAt: new Date()
      };

      const result = await this.collection.insertOne(product);
      return { ...product, _id: result.insertedId };
    } catch (error) {
      throw new Error(`Error creating product: ${error.message}`);
    }
  }

  async findAll(filter = {}) {
    try {
      return await this.collection.find(filter).toArray();
    } catch (error) {
      throw new Error(`Error finding products: ${error.message}`);
    }
  }

  async findById(id) {
    try {
      return await this.collection.findOne({ _id: new ObjectId(id) });
    } catch (error) {
      throw new Error(`Error finding product: ${error.message}`);
    }
  }

  async findByCategory(category) {
    try {
      return await this.collection.find({ category }).toArray();
    } catch (error) {
      throw new Error(`Error finding products: ${error.message}`);
    }
  }

  async update(id, updates) {
    try {
      const result = await this.collection.updateOne(
        { _id: new ObjectId(id) },
        { 
          $set: {
            ...updates,
            updatedAt: new Date()
          }
        }
      );
      return result.modifiedCount > 0;
    } catch (error) {
      throw new Error(`Error updating product: ${error.message}`);
    }
  }

  async updateStock(id, quantity) {
    try {
      const product = await this.findById(id);
      if (!product) return false;

      const newStock = product.stock + quantity;
      return await this.update(id, {
        stock: newStock,
        isAvailable: newStock > 0
      });
    } catch (error) {
      throw new Error(`Error updating stock: ${error.message}`);
    }
  }

  async delete(id) {
    try {
      const result = await this.collection.deleteOne({ _id: new ObjectId(id) });
      return result.deletedCount > 0;
    } catch (error) {
      throw new Error(`Error deleting product: ${error.message}`);
    }
  }

  async searchByName(searchTerm) {
    try {
      return await this.collection.find({
        name: { $regex: searchTerm, $options: 'i' }
      }).toArray();
    } catch (error) {
      throw new Error(`Error searching products: ${error.message}`);
    }
  }

  async findInPriceRange(minPrice, maxPrice) {
    try {
      return await this.collection.find({
        price: { $gte: minPrice, $lte: maxPrice }
      }).toArray();
    } catch (error) {
      throw new Error(`Error finding products: ${error.message}`);
    }
  }

  async createIndexes() {
    try {
      await this.collection.createIndex({ name: 1 });
      await this.collection.createIndex({ category: 1 });
      await this.collection.createIndex({ price: 1 });
      console.log('✅ Created indexes on products collection');
    } catch (error) {
      throw new Error(`Error creating indexes: ${error.message}`);
    }
  }
}

module.exports = Product;
```

**Step 6: Main Application (src/index.js)**

```javascript
// src/index.js
const database = require('./config/database');
const User = require('./models/User');
const Product = require('./models/Product');

async function main() {
  try {
    console.log('=== MongoDB Demo Application ===\n');

    // Connect to database
    const db = await database.connect();

    // Initialize models
    const userModel = new User(db);
    const productModel = new Product(db);

    // Create indexes
    await userModel.createIndexes();
    await productModel.createIndexes();

    // === USER OPERATIONS ===
    console.log('\n--- User Operations ---');

    // Create users
    console.log('\n1. Creating users...');
    const user1 = await userModel.create({
      name: 'Alice Johnson',
      email: 'alice@example.com',
      age: 28
    });
    console.log('✅ Created user:', user1.name);

    const user2 = await userModel.create({
      name: 'Bob Smith',
      email: 'bob@example.com',
      age: 35
    });
    console.log('✅ Created user:', user2.name);

    const user3 = await userModel.create({
      name: 'Charlie Brown',
      email: 'charlie@example.com',
      age: 22
    });
    console.log('✅ Created user:', user3.name);

    // Find all users
    console.log('\n2. Finding all users...');
    const allUsers = await userModel.findAll();
    console.log(`✅ Found ${allUsers.length} users:`);
    allUsers.forEach(u => {
      console.log(`   - ${u.name} (${u.email}) - Age: ${u.age}`);
    });

    // Find user by email
    console.log('\n3. Finding user by email...');
    const foundUser = await userModel.findByEmail('alice@example.com');
    if (foundUser) {
      console.log(`✅ Found: ${foundUser.name} - Age: ${foundUser.age}`);
    }

    // Update user
    console.log('\n4. Updating user...');
    const updated = await userModel.update(user1._id.toString(), { age: 29 });
    if (updated) {
      const updatedUser = await userModel.findById(user1._id.toString());
      console.log(`✅ Updated ${updatedUser.name}'s age to ${updatedUser.age}`);
    }

    // Find users by age range
    console.log('\n5. Finding users aged 25-30...');
    const youngUsers = await userModel.findByAgeRange(25, 30);
    console.log(`✅ Found ${youngUsers.length} users:`);
    youngUsers.forEach(u => console.log(`   - ${u.name} (${u.age})`));

    // === PRODUCT OPERATIONS ===
    console.log('\n--- Product Operations ---');

    // Create products
    console.log('\n1. Creating products...');
    const product1 = await productModel.create({
      name: 'Laptop',
      description: 'High-performance laptop',
      price: 1299.99,
      category: 'Electronics',
      stock: 15
    });
    console.log('✅ Created product:', product1.name);

    const product2 = await productModel.create({
      name: 'Wireless Mouse',
      description: 'Ergonomic wireless mouse',
      price: 29.99,
      category: 'Electronics',
      stock: 50
    });
    console.log('✅ Created product:', product2.name);

    const product3 = await productModel.create({
      name: 'Office Chair',
      description: 'Comfortable office chair',
      price: 199.99,
      category: 'Furniture',
      stock: 10
    });
    console.log('✅ Created product:', product3.name);

    // Find all products
    console.log('\n2. Finding all products...');
    const allProducts = await productModel.findAll();
    console.log(`✅ Found ${allProducts.length} products:`);
    allProducts.forEach(p => {
      console.log(`   - ${p.name}: $${p.price} (Stock: ${p.stock})`);
    });

    // Find products by category
    console.log('\n3. Finding Electronics...');
    const electronics = await productModel.findByCategory('Electronics');
    console.log(`✅ Found ${electronics.length} electronics:`);
    electronics.forEach(p => console.log(`   - ${p.name}: $${p.price}`));

    // Search products
    console.log('\n4. Searching for "mouse"...');
    const searchResults = await productModel.searchByName('mouse');
    console.log(`✅ Found ${searchResults.length} results:`);
    searchResults.forEach(p => console.log(`   - ${p.name}`));

    // Find products in price range
    console.log('\n5. Finding products between $20-$100...');
    const affordableProducts = await productModel.findInPriceRange(20, 100);
    console.log(`✅ Found ${affordableProducts.length} products:`);
    affordableProducts.forEach(p => {
      console.log(`   - ${p.name}: $${p.price}`);
    });

    // Update stock
    console.log('\n6. Updating product stock...');
    await productModel.updateStock(product2._id.toString(), -5);
    const updatedProduct = await productModel.findById(product2._id.toString());
    console.log(`✅ Updated ${updatedProduct.name} stock to ${updatedProduct.stock}`);

    // Count documents
    console.log('\n7. Counting documents...');
    const userCount = await userModel.count();
    const productCount = await productModel.count();
    console.log(`✅ Total users: ${userCount}`);
    console.log(`✅ Total products: ${productCount}`);

    // Delete operations (commented out to preserve data)
    /*
    console.log('\n8. Deleting a user...');
    const deleted = await userModel.delete(user3._id.toString());
    if (deleted) {
      console.log('✅ User deleted');
    }
    */

    console.log('\n=== Demo Complete ===');

  } catch (error) {
    console.error('❌ Error:', error.message);
  } finally {
    // Close database connection
    await database.close();
  }
}

// Run the application
main();
```

**Step 7: Update package.json**

```json
{
  "name": "mongodb-demo",
  "version": "1.0.0",
  "description": "MongoDB with Node.js demo",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js"
  },
  "keywords": ["mongodb", "nodejs", "database"],
  "dependencies": {
    "mongodb": "^6.3.0",
    "dotenv": "^16.3.1"
  }
}
```

**Step 8: Run the Application**

```bash
# Make sure MongoDB is running
brew services start mongodb-community

# Run the demo
npm start
```

**Expected Output:**
```
=== MongoDB Demo Application ===

✅ Connected to MongoDB
✅ Created unique index on email
✅ Created indexes on products collection

--- User Operations ---

1. Creating users...
✅ Created user: Alice Johnson
✅ Created user: Bob Smith
✅ Created user: Charlie Brown

2. Finding all users...
✅ Found 3 users:
   - Alice Johnson (alice@example.com) - Age: 28
   - Bob Smith (bob@example.com) - Age: 35
   - Charlie Brown (charlie@example.com) - Age: 22

3. Finding user by email...
✅ Found: Alice Johnson - Age: 28

4. Updating user...
✅ Updated Alice Johnson's age to 29

5. Finding users aged 25-30...
✅ Found 2 users:
   - Alice Johnson (29)
   - Charlie Brown (22)

--- Product Operations ---

1. Creating products...
✅ Created product: Laptop
✅ Created product: Wireless Mouse
✅ Created product: Office Chair

2. Finding all products...
✅ Found 3 products:
   - Laptop: $1299.99 (Stock: 15)
   - Wireless Mouse: $29.99 (Stock: 50)
   - Office Chair: $199.99 (Stock: 10)

3. Finding Electronics...
✅ Found 2 electronics:
   - Laptop: $1299.99
   - Wireless Mouse: $29.99

4. Searching for "mouse"...
✅ Found 1 results:
   - Wireless Mouse

5. Finding products between $20-$100...
✅ Found 1 products:
   - Wireless Mouse: $29.99

6. Updating product stock...
✅ Updated Wireless Mouse stock to 45

7. Counting documents...
✅ Total users: 3
✅ Total products: 3

=== Demo Complete ===
MongoDB connection closed
```

---

**📚 Interview Questions & Answers**

**Q1: What is the difference between SQL and NoSQL databases?**

**Answer:**

**SQL (Relational) Databases:**
- **Structure**: Fixed schema with tables, rows, and columns
- **Query Language**: SQL (Structured Query Language)
- **Relationships**: Use JOINs to connect related data
- **Scaling**: Vertical scaling (more powerful hardware)
- **Examples**: PostgreSQL, MySQL, Oracle
- **Best for**: Complex queries, transactions, financial systems

**NoSQL (Non-Relational) Databases:**
- **Structure**: Flexible schema (documents, key-value, graphs)
- **Query Language**: Varies (MongoDB uses JavaScript-like syntax)
- **Relationships**: Embedded documents or references
- **Scaling**: Horizontal scaling (add more servers)
- **Examples**: MongoDB, Redis, Cassandra
- **Best for**: Rapid development, unstructured data, real-time apps

**Example:**
```javascript
// SQL - Separate tables with relationships
users: { id, name, email }
posts: { id, title, content, user_id }

// NoSQL - Embedded documents
{
  _id: "user123",
  name: "Alice",
  email: "alice@example.com",
  posts: [
    { title: "First Post", content: "..." },
    { title: "Second Post", content: "..." }
  ]
}
```

**Q2: What is MongoDB and when should you use it?**

**Answer:**
MongoDB is a document-oriented NoSQL database that stores data in JSON-like documents (BSON format).

**Use MongoDB when:**
- Rapid development with changing requirements
- Working with unstructured or semi-structured data
- Need horizontal scalability
- Building real-time applications
- Prototyping and startups
- Content management systems
- IoT and time-series data

**Don't use MongoDB when:**
- Complex transactions across multiple documents
- Data has many relationships requiring complex JOINs
- Financial systems requiring strict ACID compliance
- Data structure is well-defined and won't change

**Example use case:**
```javascript
// Perfect for MongoDB - flexible blog post structure
{
  _id: ObjectId("..."),
  title: "My Blog Post",
  content: "...",
  author: {
    name: "Alice",
    email: "alice@example.com"
  },
  tags: ["tech", "programming", "mongodb"],
  comments: [
    {
      user: "Bob",
      text: "Great post!",
      date: ISODate("2024-01-15")
    }
  ],
  views: 1523,
  publishedAt: ISODate("2024-01-10")
}
```

**Q3: Explain CRUD operations in MongoDB.**

**Answer:**
CRUD stands for Create, Read, Update, Delete - the four basic database operations.

```javascript
// CREATE
// insertOne - add single document
db.users.insertOne({ name: "Alice", age: 28 })

// insertMany - add multiple documents
db.users.insertMany([
  { name: "Bob", age: 32 },
  { name: "Charlie", age: 25 }
])

// READ
// find - get all documents
db.users.find()

// find with filter
db.users.find({ age: { $gte: 30 } })  // age >= 30

// findOne - get single document
db.users.findOne({ name: "Alice" })

// UPDATE
// updateOne - update single document
db.users.updateOne(
  { name: "Alice" },           // filter
  { $set: { age: 29 } }        // update
)

// updateMany - update multiple documents
db.users.updateMany(
  { age: { $lt: 30 } },
  { $set: { category: "young" } }
)

// DELETE
// deleteOne - remove single document
db.users.deleteOne({ name: "Bob" })

// deleteMany - remove multiple documents
db.users.deleteMany({ age: { $gt: 50 } })
```

**Common Operators:**
- `$set` - Set field value
- `$inc` - Increment number
- `$push` - Add to array
- `$pull` - Remove from array
- `$gte` - Greater than or equal
- `$lt` - Less than
- `$in` - Value in array
- `$regex` - Regular expression match

**Q4: What is the difference between `_id` and a regular field in MongoDB?**

**Answer:**

**`_id` field:**
- **Unique identifier** for each document
- **Automatically created** if not provided
- Type: `ObjectId` (12-byte identifier)
- **Indexed by default** for fast lookups
- **Immutable** - cannot be changed after creation
- **Primary key** of the document

```javascript
// MongoDB auto-generates _id
db.users.insertOne({ name: "Alice" })
// Result: { _id: ObjectId("507f1f77bcf86cd799439011"), name: "Alice" }

// You can provide custom _id
db.users.insertOne({ _id: "user123", name: "Bob" })

// _id is indexed automatically
db.users.findOne({ _id: ObjectId("507f1f77bcf86cd799439011") })  // Very fast

// Regular fields
db.users.insertOne({ 
  name: "Charlie",           // Not indexed by default
  email: "charlie@email.com" // Not indexed by default
})

// Create index on regular field for faster queries
db.users.createIndex({ email: 1 })
```

**ObjectId structure:**
- 4 bytes: Timestamp
- 5 bytes: Random value
- 3 bytes: Counter

**Q5: How do you connect to MongoDB from Node.js?**

**Answer:**

**Two main approaches:**

**1. Native MongoDB Driver:**
```javascript
const { MongoClient } = require('mongodb');

const uri = 'mongodb://localhost:27017';
const client = new MongoClient(uri);

async function connect() {
  try {
    await client.connect();
    const db = client.db('myapp');
    console.log('Connected to MongoDB');
    return db;
  } catch (error) {
    console.error('Connection error:', error);
  }
}

// Usage
const db = await connect();
const users = db.collection('users');
await users.insertOne({ name: 'Alice' });
```

**2. Mongoose (ODM - Object Data Modeling):**
```javascript
const mongoose = require('mongoose');

// Connect
await mongoose.connect('mongodb://localhost:27017/myapp');

// Define schema
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  age: Number
});

// Create model
const User = mongoose.model('User', userSchema);

// Usage
const user = new User({ name: 'Alice', email: 'alice@example.com', age: 28 });
await user.save();
```

**Comparison:**
- **Native Driver**: More control, less abstraction, closer to MongoDB
- **Mongoose**: Schema validation, middleware, easier to use, more features

**Connection best practices:**
```javascript
// Connection pooling
const client = new MongoClient(uri, {
  maxPoolSize: 10,
  minPoolSize: 5
});

// Error handling
client.on('error', (error) => {
  console.error('MongoDB error:', error);
});

// Graceful shutdown
process.on('SIGINT', async () => {
  await client.close();
  process.exit(0);
});
```

---

**🔑 Key Takeaways**

1. ✅ **SQL** - Structured data with relationships, fixed schema
2. ✅ **NoSQL** - Flexible schema, document-oriented, horizontally scalable
3. ✅ **MongoDB** - Document database, JSON-like storage, great for rapid development
4. ✅ **CRUD** - Create (insert), Read (find), Update, Delete operations
5. ✅ **ObjectId** - Unique identifier automatically generated for each document
6. ✅ **Collections** - Like tables in SQL, but flexible schema
7. ✅ **Documents** - Individual records in JSON format
8. ✅ **Indexes** - Speed up queries, created on frequently queried fields

**Learning Resources:**
- [MongoDB University](https://university.mongodb.com/) - Free courses
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [MongoDB Node.js Driver](https://www.mongodb.com/docs/drivers/node/current/)

---

### Day 34: Mongoose - MongoDB ODM

**📖 What is Mongoose?**

Mongoose is an **Object Data Modeling (ODM)** library for MongoDB and Node.js. It provides a schema-based solution to model your application data.

**Real-World Analogy:**
- **Native MongoDB Driver**: Like using raw SQL - you have full control but need to handle everything manually
- **Mongoose**: Like using an ORM - provides structure, validation, and helpful methods built-in

**Why Use Mongoose?**
1. **Schema Definition** - Define structure for your data
2. **Validation** - Built-in and custom validators
3. **Middleware** - Pre and post hooks for operations
4. **Type Casting** - Automatic type conversion
5. **Query Building** - Chainable query methods
6. **Population** - Handle relationships easily
7. **Plugins** - Extend functionality

---

**💡 Installing and Setting Up Mongoose**

```bash
npm init -y
npm install mongoose dotenv
```

**Basic Connection:**

```javascript
// db.js
const mongoose = require('mongoose');
require('dotenv').config();

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI);
    console.log('✅ MongoDB connected with Mongoose');
  } catch (error) {
    console.error('❌ MongoDB connection error:', error);
    process.exit(1);
  }
};

module.exports = connectDB;
```

```.env
MONGODB_URI=mongodb://localhost:27017/mongoose_demo
```

---

**📖 Mongoose Schemas and Models**

**Schema** - Defines the structure of documents
**Model** - A class compiled from Schema, used to create and query documents

```javascript
// models/User.js
const mongoose = require('mongoose');

// Define Schema
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, 'Name is required'],
    trim: true,
    minlength: [2, 'Name must be at least 2 characters'],
    maxlength: [50, 'Name cannot exceed 50 characters']
  },
  email: {
    type: String,
    required: [true, 'Email is required'],
    unique: true,
    lowercase: true,
    trim: true,
    match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email']
  },
  age: {
    type: Number,
    min: [0, 'Age cannot be negative'],
    max: [120, 'Age cannot exceed 120']
  },
  role: {
    type: String,
    enum: ['user', 'admin', 'moderator'],
    default: 'user'
  },
  isActive: {
    type: Boolean,
    default: true
  },
  tags: {
    type: [String],
    default: []
  },
  profile: {
    bio: String,
    website: String,
    location: String
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
}, {
  timestamps: true  // Automatically adds createdAt and updatedAt
});

// Create Model
const User = mongoose.model('User', userSchema);

module.exports = User;
```

---

**📖 Mongoose Data Types**

```javascript
const schema = new mongoose.Schema({
  // String
  name: String,
  
  // Number
  age: Number,
  
  // Boolean
  isActive: Boolean,
  
  // Date
  birthDate: Date,
  
  // Array
  tags: [String],
  numbers: [Number],
  
  // Nested Object
  address: {
    street: String,
    city: String,
    zipCode: String
  },
  
  // ObjectId (reference to another document)
  userId: mongoose.Schema.Types.ObjectId,
  
  // Mixed (any type)
  metadata: mongoose.Schema.Types.Mixed,
  
  // Buffer
  image: Buffer,
  
  // Map
  socialLinks: {
    type: Map,
    of: String
  },
  
  // Decimal128 (for precise decimals like money)
  price: mongoose.Schema.Types.Decimal128
});
```

---

**💡 Complete Mongoose CRUD Example**

**Project Structure:**
```
mongoose-demo/
├── package.json
├── .env
├── models/
│   ├── User.js
│   ├── Product.js
│   └── Order.js
├── config/
│   └── database.js
└── index.js
```

**models/User.js:**

```javascript
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true
  },
  age: {
    type: Number,
    min: 0
  },
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user'
  },
  isActive: {
    type: Boolean,
    default: true
  }
}, {
  timestamps: true
});

// Instance methods
userSchema.methods.getPublicProfile = function() {
  return {
    id: this._id,
    name: this.name,
    email: this.email,
    role: this.role
  };
};

// Static methods
userSchema.statics.findByEmail = function(email) {
  return this.findOne({ email: email.toLowerCase() });
};

userSchema.statics.findAdmins = function() {
  return this.find({ role: 'admin' });
};

// Virtual properties (computed properties)
userSchema.virtual('nameUpper').get(function() {
  return this.name.toUpperCase();
});

// Middleware (Pre-save hook)
userSchema.pre('save', function(next) {
  console.log(`Saving user: ${this.name}`);
  this.updatedAt = Date.now();
  next();
});

// Post-save hook
userSchema.post('save', function(doc) {
  console.log(`✅ User saved: ${doc.name}`);
});

const User = mongoose.model('User', userSchema);

module.exports = User;
```

**models/Product.js:**

```javascript
const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true
  },
  description: {
    type: String,
    required: true
  },
  price: {
    type: Number,
    required: true,
    min: 0
  },
  category: {
    type: String,
    required: true,
    enum: ['Electronics', 'Clothing', 'Books', 'Food', 'Sports']
  },
  stock: {
    type: Number,
    default: 0,
    min: 0
  },
  isAvailable: {
    type: Boolean,
    default: true
  },
  tags: [String],
  ratings: {
    average: {
      type: Number,
      default: 0,
      min: 0,
      max: 5
    },
    count: {
      type: Number,
      default: 0
    }
  }
}, {
  timestamps: true
});

// Virtual for availability status
productSchema.virtual('availabilityStatus').get(function() {
  if (this.stock === 0) return 'Out of Stock';
  if (this.stock < 10) return 'Low Stock';
  return 'In Stock';
});

// Instance method
productSchema.methods.updateStock = function(quantity) {
  this.stock += quantity;
  this.isAvailable = this.stock > 0;
  return this.save();
};

// Static method
productSchema.statics.findByCategory = function(category) {
  return this.find({ category });
};

productSchema.statics.findInStock = function() {
  return this.find({ isAvailable: true, stock: { $gt: 0 } });
};

const Product = mongoose.model('Product', productSchema);

module.exports = Product;
```

**models/Order.js:**

```javascript
const mongoose = require('mongoose');

const orderItemSchema = new mongoose.Schema({
  product: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Product',  // Reference to Product model
    required: true
  },
  quantity: {
    type: Number,
    required: true,
    min: 1
  },
  price: {
    type: Number,
    required: true
  }
});

const orderSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',  // Reference to User model
    required: true
  },
  items: [orderItemSchema],
  total: {
    type: Number,
    required: true,
    min: 0
  },
  status: {
    type: String,
    enum: ['pending', 'processing', 'shipped', 'delivered', 'cancelled'],
    default: 'pending'
  },
  shippingAddress: {
    street: String,
    city: String,
    state: String,
    zipCode: String,
    country: String
  }
}, {
  timestamps: true
});

// Virtual for item count
orderSchema.virtual('itemCount').get(function() {
  return this.items.reduce((sum, item) => sum + item.quantity, 0);
});

// Instance method
orderSchema.methods.calculateTotal = function() {
  this.total = this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  return this.total;
};

// Pre-save middleware
orderSchema.pre('save', function(next) {
  if (this.isModified('items')) {
    this.calculateTotal();
  }
  next();
});

const Order = mongoose.model('Order', orderSchema);

module.exports = Order;
```

**config/database.js:**

```javascript
const mongoose = require('mongoose');
require('dotenv').config();

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI, {
      // These options are now default in Mongoose 6+
      // useNewUrlParser: true,
      // useUnifiedTopology: true
    });
    
    console.log('✅ MongoDB connected successfully');
    
    // Connection events
    mongoose.connection.on('error', (err) => {
      console.error('❌ MongoDB error:', err);
    });
    
    mongoose.connection.on('disconnected', () => {
      console.log('MongoDB disconnected');
    });
    
  } catch (error) {
    console.error('❌ MongoDB connection failed:', error.message);
    process.exit(1);
  }
};

module.exports = connectDB;
```

**index.js - Main Application:**

```javascript
const connectDB = require('./config/database');
const User = require('./models/User');
const Product = require('./models/Product');
const Order = require('./models/Order');

async function main() {
  try {
    console.log('=== Mongoose Demo Application ===\n');

    // Connect to database
    await connectDB();

    // Clear existing data for demo
    await User.deleteMany({});
    await Product.deleteMany({});
    await Order.deleteMany({});

    // === CREATE USERS ===
    console.log('\n--- Creating Users ---');

    const user1 = await User.create({
      name: 'Alice Johnson',
      email: 'alice@example.com',
      age: 28,
      role: 'admin'
    });
    console.log(`✅ Created: ${user1.name}`);

    const user2 = await User.create({
      name: 'Bob Smith',
      email: 'bob@example.com',
      age: 35
    });
    console.log(`✅ Created: ${user2.name}`);

    const user3 = new User({
      name: 'Charlie Brown',
      email: 'charlie@example.com',
      age: 22
    });
    await user3.save();
    console.log(`✅ Created: ${user3.name}`);

    // === READ USERS ===
    console.log('\n--- Reading Users ---');

    // Find all users
    const allUsers = await User.find();
    console.log(`\nFound ${allUsers.length} users:`);
    allUsers.forEach(u => {
      console.log(`  - ${u.name} (${u.email}) - Role: ${u.role}`);
    });

    // Find with filter
    const admins = await User.find({ role: 'admin' });
    console.log(`\nAdmins (${admins.length}):`);
    admins.forEach(u => console.log(`  - ${u.name}`));

    // Find one by email (using static method)
    const foundUser = await User.findByEmail('alice@example.com');
    console.log(`\n Found by email: ${foundUser.name}`);

    // Find by ID
    const userById = await User.findById(user1._id);
    console.log(`Found by ID: ${userById.name}`);

    // Query chaining
    const youngUsers = await User
      .find({ age: { $lt: 30 } })
      .select('name age')  // Select only name and age
      .sort({ age: 1 })    // Sort by age ascending
      .limit(10);          // Limit to 10 results

    console.log(`\nYoung users (<30):`);
    youngUsers.forEach(u => console.log(`  - ${u.name}, ${u.age}`));

    // === UPDATE USERS ===
    console.log('\n--- Updating Users ---');

    // Update one
    const updateResult = await User.updateOne(
      { email: 'bob@example.com' },
      { $set: { age: 36 } }
    );
    console.log(`Updated ${updateResult.modifiedCount} user(s)`);

    // Find and update
    const updatedUser = await User.findOneAndUpdate(
      { name: 'Charlie Brown' },
      { $set: { age: 23, role: 'admin' } },
      { new: true }  // Return updated document
    );
    console.log(`Updated: ${updatedUser.name} - Age: ${updatedUser.age}, Role: ${updatedUser.role}`);

    // Update by ID
    const updatedById = await User.findByIdAndUpdate(
      user1._id,
      { $set: { age: 29 } },
      { new: true }
    );
    console.log(`Updated by ID: ${updatedById.name} - Age: ${updatedById.age}`);

    // === CREATE PRODUCTS ===
    console.log('\n--- Creating Products ---');

    const products = await Product.create([
      {
        name: 'Laptop',
        description: 'High-performance laptop',
        price: 1299.99,
        category: 'Electronics',
        stock: 15,
        tags: ['computer', 'tech', 'portable']
      },
      {
        name: 'Wireless Mouse',
        description: 'Ergonomic wireless mouse',
        price: 29.99,
        category: 'Electronics',
        stock: 50,
        tags: ['accessory', 'wireless']
      },
      {
        name: 'JavaScript Book',
        description: 'Complete guide to JavaScript',
        price: 39.99,
        category: 'Books',
        stock: 25,
        tags: ['programming', 'education']
      }
    ]);

    console.log(`✅ Created ${products.length} products`);

    // === READ PRODUCTS ===
    console.log('\n--- Reading Products ---');

    const allProducts = await Product.find();
    console.log(`\nAll products (${allProducts.length}):`);
    allProducts.forEach(p => {
      console.log(`  - ${p.name}: $${p.price} - ${p.availabilityStatus}`);
    });

    // Find by category
    const electronics = await Product.findByCategory('Electronics');
    console.log(`\nElectronics (${electronics.length}):`);
    electronics.forEach(p => console.log(`  - ${p.name}: $${p.price}`));

    // Complex query
    const affordableProducts = await Product.find({
      price: { $lte: 50 },
      stock: { $gt: 0 }
    }).sort({ price: 1 });

    console.log(`\nAffordable products ($50 or less):`);
    affordableProducts.forEach(p => {
      console.log(`  - ${p.name}: $${p.price}`);
    });

    // === CREATE ORDER ===
    console.log('\n--- Creating Order ---');

    const order = await Order.create({
      user: user1._id,
      items: [
        {
          product: products[0]._id,  // Laptop
          quantity: 1,
          price: products[0].price
        },
        {
          product: products[1]._id,  // Mouse
          quantity: 2,
          price: products[1].price
        }
      ],
      shippingAddress: {
        street: '123 Main St',
        city: 'San Francisco',
        state: 'CA',
        zipCode: '94102',
        country: 'USA'
      }
    });

    console.log(`✅ Created order #${order._id}`);
    console.log(`   Total: $${order.total.toFixed(2)}`);
    console.log(`   Items: ${order.itemCount}`);

    // === POPULATE (JOIN) ===
    console.log('\n--- Populating Order Details ---');

    const orderWithDetails = await Order
      .findById(order._id)
      .populate('user', 'name email')  // Populate user with selected fields
      .populate('items.product', 'name price');  // Populate products

    console.log(`\nOrder Details:`);
    console.log(`  Customer: ${orderWithDetails.user.name}`);
    console.log(`  Email: ${orderWithDetails.user.email}`);
    console.log(`  Items:`);
    orderWithDetails.items.forEach(item => {
      console.log(`    - ${item.product.name} x${item.quantity} @ $${item.price}`);
    });
    console.log(`  Total: $${orderWithDetails.total.toFixed(2)}`);
    console.log(`  Status: ${orderWithDetails.status}`);

    // === UPDATE PRODUCT STOCK ===
    console.log('\n--- Updating Product Stock ---');

    await products[0].updateStock(-1);  // Sell one laptop
    console.log(`✅ Updated ${products[0].name} stock to ${products[0].stock}`);

    // === DELETE ===
    console.log('\n--- Delete Operations ---');

    // Delete one
    const deleteResult = await User.deleteOne({ email: 'charlie@example.com' });
    console.log(`Deleted ${deleteResult.deletedCount} user(s)`);

    // Find and delete
    const deletedUser = await User.findOneAndDelete({ email: 'bob@example.com' });
    if (deletedUser) {
      console.log(`Deleted user: ${deletedUser.name}`);
    }

    // Count remaining
    const userCount = await User.countDocuments();
    const productCount = await Product.countDocuments();
    const orderCount = await Order.countDocuments();

    console.log(`\nFinal counts:`);
    console.log(`  Users: ${userCount}`);
    console.log(`  Products: ${productCount}`);
    console.log(`  Orders: ${orderCount}`);

    console.log('\n=== Demo Complete ===');

  } catch (error) {
    console.error('❌ Error:', error.message);
  } finally {
    // Close connection
    await mongoose.connection.close();
    console.log('Database connection closed');
  }
}

// Run the application
main();
```

**package.json:**

```json
{
  "name": "mongoose-demo",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "mongoose": "^8.0.0",
    "dotenv": "^16.3.1"
  }
}
```

**Run the application:**

```bash
npm start
```

---

**📖 Mongoose Query Methods**

```javascript
// Find methods
Model.find()                    // Find all
Model.findOne()                 // Find first match
Model.findById()                // Find by _id

// Create methods
Model.create()                  // Create one or more documents
new Model().save()              // Create and save

// Update methods
Model.updateOne()               // Update first match
Model.updateMany()              // Update all matches
Model.findOneAndUpdate()        // Find, update, and return document
Model.findByIdAndUpdate()       // Find by ID, update, and return

// Delete methods
Model.deleteOne()               // Delete first match
Model.deleteMany()              // Delete all matches
Model.findOneAndDelete()        // Find, delete, and return document
Model.findByIdAndDelete()       // Find by ID, delete, and return

// Count
Model.countDocuments()          // Count matching documents

// Query chaining
Model.find()
  .where('age').gte(18).lte(65)  // Age between 18 and 65
  .where('role').equals('user')   // Role is 'user'
  .select('name email')           // Select only name and email
  .sort({ createdAt: -1 })        // Sort by createdAt descending
  .limit(10)                      // Limit to 10 results
  .skip(20)                       // Skip first 20 results
  .exec();                        // Execute query
```

---

**📖 Mongoose Validation**

```javascript
const userSchema = new mongoose.Schema({
  // Required
  name: {
    type: String,
    required: true  // or [true, 'Custom error message']
  },
  
  // String validators
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true,
    minlength: [5, 'Email must be at least 5 characters'],
    maxlength: [100, 'Email cannot exceed 100 characters'],
    match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email']
  },
  
  // Number validators
  age: {
    type: Number,
    min: [0, 'Age cannot be negative'],
    max: [120, 'Age cannot exceed 120']
  },
  
  // Enum validator
  role: {
    type: String,
    enum: {
      values: ['user', 'admin', 'moderator'],
      message: '{VALUE} is not a valid role'
    }
  },
  
  // Custom validator
  password: {
    type: String,
    validate: {
      validator: function(value) {
        return value.length >= 8;
      },
      message: 'Password must be at least 8 characters long'
    }
  },
  
  // Custom async validator
  username: {
    type: String,
    validate: {
      validator: async function(value) {
        const user = await mongoose.model('User').findOne({ username: value });
        return !user;  // Valid if username doesn't exist
      },
      message: 'Username already exists'
    }
  }
});
```

---

**📖 Mongoose Middleware (Hooks)**

```javascript
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  password: String
});

// Pre-save hook - runs before saving
userSchema.pre('save', async function(next) {
  console.log('About to save user...');
  
  // Hash password before saving
  if (this.isModified('password')) {
    // Hash password here (example placeholder)
    this.password = `hashed_${this.password}`;
  }
  
  next();
});

// Post-save hook - runs after saving
userSchema.post('save', function(doc) {
  console.log(`User ${doc.name} has been saved`);
});

// Pre-remove hook
userSchema.pre('remove', function(next) {
  console.log('About to remove user...');
  // Clean up related data
  next();
});

// Pre-find hook
userSchema.pre('find', function() {
  // Modify query
  this.where({ isActive: true });
});

// Post-find hook
userSchema.post('find', function(docs) {
  console.log(`Found ${docs.length} documents`);
});
```

---

**📚 Interview Questions & Answers**

**Q1: What is Mongoose and why use it over the native MongoDB driver?**

**Answer:**
Mongoose is an ODM (Object Data Modeling) library for MongoDB that provides:

**Advantages over native driver:**

1. **Schema Definition**: Define structure for your data
```javascript
// Without Mongoose - no structure
db.users.insertOne({ name: 'Alice', random: 'data' })

// With Mongoose - structured
const User = mongoose.model('User', {
  name: { type: String, required: true },
  age: { type: Number, min: 0 }
})
```

2. **Built-in Validation**: Automatic data validation
3. **Middleware**: Pre/post hooks for operations
4. **Type Casting**: Automatic type conversion
5. **Relationships**: Easy population (like JOINs)
6. **Query Building**: Chainable, readable queries

**When to use:**
- Large applications with complex data models
- Need data validation
- Want structured, maintainable code
- Working in teams

**When not to use:**
- Simple applications
- Need maximum flexibility
- Performance-critical applications (slight overhead)

**Q2: Explain Mongoose Schema and Model.**

**Answer:**

**Schema** = Blueprint that defines structure, types, and validation

```javascript
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true },
  age: Number
});
```

**Model** = Class created from Schema, used to create/query documents

```javascript
const User = mongoose.model('User', userSchema);

// Now you can use User to interact with database
const user = new User({ name: 'Alice', email: 'alice@example.com' });
await user.save();
```

**Relationship:**
```
Schema → defines structure
   ↓
Model → compiled from schema
   ↓
Document → instance of model (actual data)
```

**Example:**
```javascript
// 1. Define Schema
const productSchema = new mongoose.Schema({
  name: String,
  price: Number
});

// 2. Create Model
const Product = mongoose.model('Product', productSchema);

// 3. Create Document (instance)
const laptop = new Product({
  name: 'Laptop',
  price: 999
});

await laptop.save();  // Save to database
```

**Q3: What are Mongoose middleware and when would you use them?**

**Answer:**
Middleware (hooks) are functions that run at specific stages of document lifecycle.

**Types:**
- **Pre hooks**: Run before operation
- **Post hooks**: Run after operation

**Common use cases:**

```javascript
const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  email: String
});

// 1. Hash password before saving
userSchema.pre('save', async function(next) {
  if (this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  next();
});

// 2. Lowercase email before saving
userSchema.pre('save', function(next) {
  this.email = this.email.toLowerCase();
  next();
});

// 3. Log after saving
userSchema.post('save', function(doc) {
  console.log(`User ${doc.username} saved`);
});

// 4. Clean up related data before removing
userSchema.pre('remove', async function(next) {
  await Post.deleteMany({ author: this._id });
  next();
});

// 5. Update timestamp
userSchema.pre('save', function(next) {
  this.updatedAt = Date.now();
  next();
});
```

**Q4: Explain population in Mongoose.**

**Answer:**
Population automatically replaces ObjectId references with actual documents - like a JOIN in SQL.

**Without population:**
```javascript
const order = await Order.findById(orderId);
console.log(order.user);  // ObjectId("507f1f77bcf86cd799439011")
```

**With population:**
```javascript
const order = await Order.findById(orderId).populate('user');
console.log(order.user);  
// { _id: "507f...", name: "Alice", email: "alice@example.com" }
```

**Example:**
```javascript
// Schema with reference
const orderSchema = new mongoose.Schema({
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'  // Reference to User model
  },
  product: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Product'
  }
});

// Populate single field
const order = await Order.findById(id).populate('user');

// Populate multiple fields
const order = await Order.findById(id)
  .populate('user')
  .populate('product');

// Populate with field selection
const order = await Order.findById(id)
  .populate('user', 'name email')  // Only include name and email
  .populate('product', 'name price');

// Nested population
const order = await Order.findById(id)
  .populate({
    path: 'user',
    populate: {
      path: 'company'
    }
  });
```

**Q5: What is the difference between `save()` and `create()` in Mongoose?**

**Answer:**

**`save()` method:**
- Instance method
- Save a single document
- Returns the saved document
- Triggers middleware

```javascript
const user = new User({ name: 'Alice', email: 'alice@example.com' });
await user.save();

// Can modify before saving
user.age = 28;
await user.save();
```

**`create()` method:**
- Static method (called on Model)
- Can create one or multiple documents
- Shortcut for `new Model()` + `save()`
- Also triggers middleware

```javascript
// Create one
const user = await User.create({
  name: 'Alice',
  email: 'alice@example.com'
});

// Create multiple
const users = await User.create([
  { name: 'Alice', email: 'alice@example.com' },
  { name: 'Bob', email: 'bob@example.com' }
]);
```

**Key differences:**

| Feature | `save()` | `create()` |
|---------|----------|------------|
| Type | Instance method | Static method |
| Usage | `doc.save()` | `Model.create()` |
| Multiple docs | No | Yes |
| Modify before save | Yes | No |
| Performance | Same | Same |

**Both trigger middleware and validation!**

---

**🔑 Key Takeaways**

1. ✅ **Mongoose** - ODM library providing structure and validation for MongoDB
2. ✅ **Schema** - Defines document structure, types, and validation rules
3. ✅ **Model** - Class compiled from schema, used to create/query documents
4. ✅ **Validation** - Built-in validators (required, min, max, enum, custom)
5. ✅ **Middleware** - Pre/post hooks for save, remove, find operations
6. ✅ **Population** - Replace ObjectId references with actual documents (like JOINs)
7. ✅ **Query Chaining** - Readable, chainable query methods
8. ✅ **Virtuals** - Computed properties not stored in database

**Learning Resources:**
- [Mongoose Documentation](https://mongoosejs.com/docs/guide.html)
- [Mongoose Queries](https://mongoosejs.com/docs/queries.html)
- [Mongoose Validation](https://mongoosejs.com/docs/validation.html)
- [Mongoose Middleware](https://mongoosejs.com/docs/middleware.html)

---

### Day 35: Introduction to SQL & PostgreSQL

**📖 What is SQL?**

SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. Think of it as the universal language that databases understand.

**Real-World Analogy:**
- **SQL Database**: Like a spreadsheet with multiple sheets (tables) connected by relationships
- **Tables**: Individual sheets with columns (fields) and rows (records)
- **Relationships**: Links between sheets using IDs (like VLOOKUP)

---

**📖 Popular SQL Databases**

| Database | Best For | Key Features |
|----------|----------|--------------|
| **PostgreSQL** | Complex queries, data integrity | Advanced features, JSON support, extensions |
| **MySQL** | Web applications, read-heavy | Fast, simple, widely used |
| **SQLite** | Mobile apps, prototypes | Serverless, lightweight, file-based |
| **Microsoft SQL Server** | Enterprise, Windows | .NET integration, business intelligence |
| **Oracle** | Large enterprises | Powerful, expensive, enterprise features |

**We'll focus on PostgreSQL** - it's powerful, open-source, and widely used in modern applications.

---

**📖 SQL vs NoSQL - When to Use SQL**

**Use SQL (PostgreSQL) when:**
- ✅ Data has clear relationships (users → orders → products)
- ✅ Need complex queries with JOINs
- ✅ Require ACID transactions (banking, e-commerce)
- ✅ Schema is well-defined and stable
- ✅ Data integrity is critical

**Use NoSQL (MongoDB) when:**
- ✅ Rapid development, changing requirements
- ✅ Unstructured or flexible data
- ✅ Need horizontal scaling
- ✅ Document-based data (blogs, catalogs)

---

**💡 Installing PostgreSQL**

**macOS:**
```bash
# Install PostgreSQL
brew install postgresql@15

# Start PostgreSQL service
brew services start postgresql@15

# Verify installation
psql --version

# Access PostgreSQL shell
psql postgres
```

**Create a Database:**
```bash
# In terminal
createdb myapp_db

# Or in psql shell
CREATE DATABASE myapp_db;

# Connect to database
\c myapp_db

# List all databases
\l

# List all tables
\dt

# Quit psql
\q
```

---

**📖 SQL Basics - DDL (Data Definition Language)**

**Creating Tables:**

```sql
-- Create users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,           -- Auto-incrementing ID
  name VARCHAR(100) NOT NULL,      -- String, required
  email VARCHAR(100) UNIQUE NOT NULL,
  age INTEGER CHECK (age >= 0),    -- Must be positive
  role VARCHAR(20) DEFAULT 'user', -- Default value
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  description TEXT,
  price NUMERIC(10, 2) NOT NULL,   -- 10 digits, 2 decimal places
  category VARCHAR(50),
  stock INTEGER DEFAULT 0,
  is_available BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create orders table with foreign keys
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  total NUMERIC(10, 2) NOT NULL,
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  -- Foreign key constraint
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create order_items table (many-to-many relationship)
CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  price NUMERIC(10, 2) NOT NULL,
  
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);
```

**Modifying Tables:**

```sql
-- Add a column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Modify a column
ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(150);

-- Drop a column
ALTER TABLE users DROP COLUMN phone;

-- Add constraint
ALTER TABLE users ADD CONSTRAINT email_format CHECK (email LIKE '%@%');

-- Drop table
DROP TABLE IF EXISTS table_name;
```

---

**📖 SQL Basics - DML (Data Manipulation Language)**

**INSERT - Adding Data:**

```sql
-- Insert single row
INSERT INTO users (name, email, age, role)
VALUES ('Alice Johnson', 'alice@example.com', 28, 'admin');

-- Insert multiple rows
INSERT INTO users (name, email, age) VALUES
  ('Bob Smith', 'bob@example.com', 35),
  ('Charlie Brown', 'charlie@example.com', 22),
  ('Diana Prince', 'diana@example.com', 30);

-- Insert and return the inserted row
INSERT INTO users (name, email, age)
VALUES ('Eve Wilson', 'eve@example.com', 26)
RETURNING *;

-- Insert products
INSERT INTO products (name, description, price, category, stock) VALUES
  ('Laptop', 'High-performance laptop', 1299.99, 'Electronics', 15),
  ('Mouse', 'Wireless mouse', 29.99, 'Electronics', 50),
  ('Desk Chair', 'Ergonomic chair', 199.99, 'Furniture', 10);
```

**SELECT - Reading Data:**

```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT name, email, age FROM users;

-- With WHERE clause (filter)
SELECT * FROM users WHERE age >= 25;

-- Multiple conditions
SELECT * FROM users WHERE age >= 25 AND role = 'admin';

-- OR condition
SELECT * FROM users WHERE role = 'admin' OR age > 30;

-- LIKE (pattern matching)
SELECT * FROM users WHERE email LIKE '%@example.com';

-- IN (multiple values)
SELECT * FROM products WHERE category IN ('Electronics', 'Furniture');

-- BETWEEN (range)
SELECT * FROM products WHERE price BETWEEN 20 AND 100;

-- IS NULL / IS NOT NULL
SELECT * FROM users WHERE phone IS NULL;

-- ORDER BY (sorting)
SELECT * FROM users ORDER BY age DESC;
SELECT * FROM products ORDER BY price ASC;

-- LIMIT (pagination)
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;  -- Skip first 20

-- DISTINCT (unique values)
SELECT DISTINCT category FROM products;

-- COUNT, SUM, AVG, MIN, MAX
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users;
SELECT SUM(stock) FROM products;
SELECT MIN(price), MAX(price) FROM products;

-- GROUP BY
SELECT category, COUNT(*) as product_count
FROM products
GROUP BY category;

SELECT role, AVG(age) as average_age
FROM users
GROUP BY role;

-- HAVING (filter groups)
SELECT category, COUNT(*) as count
FROM products
GROUP BY category
HAVING COUNT(*) > 5;
```

**UPDATE - Modifying Data:**

```sql
-- Update single row
UPDATE users
SET age = 29
WHERE email = 'alice@example.com';

-- Update multiple columns
UPDATE users
SET age = 36, role = 'admin'
WHERE name = 'Bob Smith';

-- Update multiple rows
UPDATE products
SET is_available = false
WHERE stock = 0;

-- Update with calculation
UPDATE products
SET price = price * 1.1
WHERE category = 'Electronics';

-- Update and return
UPDATE users
SET is_active = true
WHERE id = 5
RETURNING *;
```

**DELETE - Removing Data:**

```sql
-- Delete specific row
DELETE FROM users WHERE email = 'charlie@example.com';

-- Delete multiple rows
DELETE FROM products WHERE stock = 0;

-- Delete with condition
DELETE FROM users WHERE created_at < '2023-01-01';

-- Delete all rows (be careful!)
DELETE FROM users;

-- Delete and return
DELETE FROM users WHERE id = 10 RETURNING *;
```

---

**📖 SQL JOINS - Combining Tables**

```sql
-- Sample data for joins
INSERT INTO orders (user_id, total, status) VALUES
  (1, 1329.98, 'completed'),
  (2, 29.99, 'pending'),
  (1, 199.99, 'shipped');

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
  (1, 1, 1, 1299.99),
  (1, 2, 1, 29.99),
  (2, 2, 1, 29.99),
  (3, 3, 1, 199.99);

-- INNER JOIN - Returns matching rows from both tables
SELECT 
  users.name,
  orders.id as order_id,
  orders.total,
  orders.status
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN - Returns all rows from left table, matching rows from right
SELECT 
  users.name,
  orders.id as order_id,
  orders.total
FROM users
LEFT JOIN orders ON users.id = orders.user_id;

-- Multiple JOINS
SELECT 
  users.name as customer,
  orders.id as order_id,
  products.name as product,
  order_items.quantity,
  order_items.price
FROM orders
INNER JOIN users ON orders.user_id = users.id
INNER JOIN order_items ON orders.id = order_items.order_id
INNER JOIN products ON order_items.product_id = products.id;

-- Aggregation with JOIN
SELECT 
  users.name,
  COUNT(orders.id) as total_orders,
  SUM(orders.total) as total_spent
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY total_spent DESC;
```

---

**💡 PostgreSQL with Node.js - Complete Example**

**Install pg (PostgreSQL client):**

```bash
npm init -y
npm install pg dotenv
```

**Project Structure:**
```
postgres-demo/
├── package.json
├── .env
├── config/
│   └── database.js
├── models/
│   ├── User.js
│   └── Product.js
├── migrations/
│   └── setup.sql
└── index.js
```

**migrations/setup.sql:**

```sql
-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  age INTEGER CHECK (age >= 0),
  role VARCHAR(20) DEFAULT 'user',
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  description TEXT,
  price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
  category VARCHAR(50),
  stock INTEGER DEFAULT 0 CHECK (stock >= 0),
  is_available BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create orders table
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  total NUMERIC(10, 2) NOT NULL,
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create order_items table
CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  price NUMERIC(10, 2) NOT NULL
);

-- Create indexes for better performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

**.env:**

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp_db
DB_USER=your_username
DB_PASSWORD=your_password
```

**config/database.js:**

```javascript
const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  max: 20,  // Maximum number of connections
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000,
});

// Test connection
pool.on('connect', () => {
  console.log('✅ Connected to PostgreSQL');
});

pool.on('error', (err) => {
  console.error('❌ PostgreSQL error:', err);
});

module.exports = pool;
```

**models/User.js:**

```javascript
const pool = require('../config/database');

class User {
  /**
   * Create a new user
   */
  static async create(userData) {
    const { name, email, age, role = 'user' } = userData;
    
    const query = `
      INSERT INTO users (name, email, age, role)
      VALUES ($1, $2, $3, $4)
      RETURNING *
    `;
    
    try {
      const result = await pool.query(query, [name, email, age, role]);
      return result.rows[0];
    } catch (error) {
      if (error.code === '23505') {  // Unique violation
        throw new Error('Email already exists');
      }
      throw error;
    }
  }

  /**
   * Find all users
   */
  static async findAll(filters = {}) {
    let query = 'SELECT * FROM users WHERE 1=1';
    const params = [];
    let paramCount = 1;

    if (filters.role) {
      query += ` AND role = $${paramCount}`;
      params.push(filters.role);
      paramCount++;
    }

    if (filters.isActive !== undefined) {
      query += ` AND is_active = $${paramCount}`;
      params.push(filters.isActive);
      paramCount++;
    }

    query += ' ORDER BY created_at DESC';

    const result = await pool.query(query, params);
    return result.rows;
  }

  /**
   * Find user by ID
   */
  static async findById(id) {
    const query = 'SELECT * FROM users WHERE id = $1';
    const result = await pool.query(query, [id]);
    return result.rows[0];
  }

  /**
   * Find user by email
   */
  static async findByEmail(email) {
    const query = 'SELECT * FROM users WHERE email = $1';
    const result = await pool.query(query, [email]);
    return result.rows[0];
  }

  /**
   * Update user
   */
  static async update(id, updates) {
    const fields = [];
    const values = [];
    let paramCount = 1;

    Object.keys(updates).forEach(key => {
      fields.push(`${key} = $${paramCount}`);
      values.push(updates[key]);
      paramCount++;
    });

    fields.push(`updated_at = CURRENT_TIMESTAMP`);
    values.push(id);

    const query = `
      UPDATE users
      SET ${fields.join(', ')}
      WHERE id = $${paramCount}
      RETURNING *
    `;

    const result = await pool.query(query, values);
    return result.rows[0];
  }

  /**
   * Delete user
   */
  static async delete(id) {
    const query = 'DELETE FROM users WHERE id = $1 RETURNING *';
    const result = await pool.query(query, [id]);
    return result.rows[0];
  }

  /**
   * Count users
   */
  static async count(filters = {}) {
    let query = 'SELECT COUNT(*) FROM users WHERE 1=1';
    const params = [];
    let paramCount = 1;

    if (filters.role) {
      query += ` AND role = $${paramCount}`;
      params.push(filters.role);
      paramCount++;
    }

    const result = await pool.query(query, params);
    return parseInt(result.rows[0].count);
  }

  /**
   * Find users with pagination
   */
  static async findPaginated(page = 1, limit = 10) {
    const offset = (page - 1) * limit;
    
    const query = `
      SELECT * FROM users
      ORDER BY created_at DESC
      LIMIT $1 OFFSET $2
    `;
    
    const result = await pool.query(query, [limit, offset]);
    const total = await this.count();
    
    return {
      users: result.rows,
      pagination: {
        page,
        limit,
        total,
        totalPages: Math.ceil(total / limit)
      }
    };
  }

  /**
   * Get user with their orders
   */
  static async findWithOrders(userId) {
    const query = `
      SELECT 
        users.*,
        json_agg(
          json_build_object(
            'id', orders.id,
            'total', orders.total,
            'status', orders.status,
            'created_at', orders.created_at
          )
        ) FILTER (WHERE orders.id IS NOT NULL) as orders
      FROM users
      LEFT JOIN orders ON users.id = orders.user_id
      WHERE users.id = $1
      GROUP BY users.id
    `;

    const result = await pool.query(query, [userId]);
    return result.rows[0];
  }
}

module.exports = User;
```

**models/Product.js:**

```javascript
const pool = require('../config/database');

class Product {
  static async create(productData) {
    const { name, description, price, category, stock = 0 } = productData;
    
    const query = `
      INSERT INTO products (name, description, price, category, stock, is_available)
      VALUES ($1, $2, $3, $4, $5, $6)
      RETURNING *
    `;
    
    const isAvailable = stock > 0;
    const result = await pool.query(query, [
      name, description, price, category, stock, isAvailable
    ]);
    
    return result.rows[0];
  }

  static async findAll(filters = {}) {
    let query = 'SELECT * FROM products WHERE 1=1';
    const params = [];
    let paramCount = 1;

    if (filters.category) {
      query += ` AND category = $${paramCount}`;
      params.push(filters.category);
      paramCount++;
    }

    if (filters.isAvailable !== undefined) {
      query += ` AND is_available = $${paramCount}`;
      params.push(filters.isAvailable);
      paramCount++;
    }

    if (filters.minPrice) {
      query += ` AND price >= $${paramCount}`;
      params.push(filters.minPrice);
      paramCount++;
    }

    if (filters.maxPrice) {
      query += ` AND price <= $${paramCount}`;
      params.push(filters.maxPrice);
      paramCount++;
    }

    query += ' ORDER BY created_at DESC';

    const result = await pool.query(query, params);
    return result.rows;
  }

  static async findById(id) {
    const query = 'SELECT * FROM products WHERE id = $1';
    const result = await pool.query(query, [id]);
    return result.rows[0];
  }

  static async findByCategory(category) {
    const query = 'SELECT * FROM products WHERE category = $1';
    const result = await pool.query(query, [category]);
    return result.rows;
  }

  static async search(searchTerm) {
    const query = `
      SELECT * FROM products
      WHERE name ILIKE $1 OR description ILIKE $1
      ORDER BY name
    `;
    const result = await pool.query(query, [`%${searchTerm}%`]);
    return result.rows;
  }

  static async update(id, updates) {
    const fields = [];
    const values = [];
    let paramCount = 1;

    Object.keys(updates).forEach(key => {
      fields.push(`${key} = $${paramCount}`);
      values.push(updates[key]);
      paramCount++;
    });

    values.push(id);

    const query = `
      UPDATE products
      SET ${fields.join(', ')}
      WHERE id = $${paramCount}
      RETURNING *
    `;

    const result = await pool.query(query, values);
    return result.rows[0];
  }

  static async updateStock(id, quantity) {
    const query = `
      UPDATE products
      SET stock = stock + $1,
          is_available = (stock + $1) > 0
      WHERE id = $2
      RETURNING *
    `;
    const result = await pool.query(query, [quantity, id]);
    return result.rows[0];
  }

  static async delete(id) {
    const query = 'DELETE FROM products WHERE id = $1 RETURNING *';
    const result = await pool.query(query, [id]);
    return result.rows[0];
  }

  static async getStats() {
    const query = `
      SELECT 
        COUNT(*) as total_products,
        SUM(stock) as total_stock,
        AVG(price) as average_price,
        MIN(price) as min_price,
        MAX(price) as max_price,
        COUNT(*) FILTER (WHERE is_available = true) as available_count
      FROM products
    `;
    const result = await pool.query(query);
    return result.rows[0];
  }

  static async getByCategory() {
    const query = `
      SELECT 
        category,
        COUNT(*) as count,
        SUM(stock) as total_stock,
        AVG(price) as avg_price
      FROM products
      GROUP BY category
      ORDER BY count DESC
    `;
    const result = await pool.query(query);
    return result.rows;
  }
}

module.exports = Product;
```

**index.js - Main Application:**

```javascript
const pool = require('./config/database');
const User = require('./models/User');
const Product = require('./models/Product');
const fs = require('fs').promises;
const path = require('path');

async function setupDatabase() {
  try {
    console.log('Setting up database...');
    const sql = await fs.readFile(
      path.join(__dirname, 'migrations', 'setup.sql'),
      'utf8'
    );
    await pool.query(sql);
    console.log('✅ Database setup complete\n');
  } catch (error) {
    console.error('❌ Database setup error:', error.message);
    throw error;
  }
}

async function main() {
  try {
    console.log('=== PostgreSQL Demo Application ===\n');

    // Setup database
    await setupDatabase();

    // === CREATE USERS ===
    console.log('--- Creating Users ---');

    const user1 = await User.create({
      name: 'Alice Johnson',
      email: 'alice@example.com',
      age: 28,
      role: 'admin'
    });
    console.log(`✅ Created: ${user1.name}`);

    const user2 = await User.create({
      name: 'Bob Smith',
      email: 'bob@example.com',
      age: 35
    });
    console.log(`✅ Created: ${user2.name}`);

    const user3 = await User.create({
      name: 'Charlie Brown',
      email: 'charlie@example.com',
      age: 22
    });
    console.log(`✅ Created: ${user3.name}`);

    // === READ USERS ===
    console.log('\n--- Reading Users ---');

    const allUsers = await User.findAll();
    console.log(`\nFound ${allUsers.length} users:`);
    allUsers.forEach(u => {
      console.log(`  - ${u.name} (${u.email}) - Age: ${u.age}, Role: ${u.role}`);
    });

    // Find by email
    const foundUser = await User.findByEmail('alice@example.com');
    console.log(`\nFound by email: ${foundUser.name}`);

    // Find admins
    const admins = await User.findAll({ role: 'admin' });
    console.log(`\nAdmins (${admins.length}):`);
    admins.forEach(u => console.log(`  - ${u.name}`));

    // === UPDATE USER ===
    console.log('\n--- Updating User ---');

    const updated = await User.update(user2.id, { age: 36, role: 'admin' });
    console.log(`✅ Updated: ${updated.name} - Age: ${updated.age}, Role: ${updated.role}`);

    // === CREATE PRODUCTS ===
    console.log('\n--- Creating Products ---');

    const product1 = await Product.create({
      name: 'Laptop',
      description: 'High-performance laptop',
      price: 1299.99,
      category: 'Electronics',
      stock: 15
    });
    console.log(`✅ Created: ${product1.name}`);

    const product2 = await Product.create({
      name: 'Wireless Mouse',
      description: 'Ergonomic wireless mouse',
      price: 29.99,
      category: 'Electronics',
      stock: 50
    });
    console.log(`✅ Created: ${product2.name}`);

    const product3 = await Product.create({
      name: 'Office Chair',
      description: 'Comfortable ergonomic chair',
      price: 199.99,
      category: 'Furniture',
      stock: 10
    });
    console.log(`✅ Created: ${product3.name}`);

    // === READ PRODUCTS ===
    console.log('\n--- Reading Products ---');

    const allProducts = await Product.findAll();
    console.log(`\nAll products (${allProducts.length}):`);
    allProducts.forEach(p => {
      console.log(`  - ${p.name}: $${p.price} - Stock: ${p.stock}`);
    });

    // Find by category
    const electronics = await Product.findByCategory('Electronics');
    console.log(`\nElectronics (${electronics.length}):`);
    electronics.forEach(p => console.log(`  - ${p.name}: $${p.price}`));

    // Search products
    const searchResults = await Product.search('mouse');
    console.log(`\nSearch "mouse" (${searchResults.length}):`);
    searchResults.forEach(p => console.log(`  - ${p.name}`));

    // Products in price range
    const affordable = await Product.findAll({ minPrice: 20, maxPrice: 100 });
    console.log(`\nAffordable products ($20-$100):`);
    affordable.forEach(p => console.log(`  - ${p.name}: $${p.price}`));

    // === PRODUCT STATS ===
    console.log('\n--- Product Statistics ---');

    const stats = await Product.getStats();
    console.log(`\nOverall Stats:`);
    console.log(`  Total Products: ${stats.total_products}`);
    console.log(`  Total Stock: ${stats.total_stock}`);
    console.log(`  Average Price: $${parseFloat(stats.average_price).toFixed(2)}`);
    console.log(`  Price Range: $${stats.min_price} - $${stats.max_price}`);
    console.log(`  Available: ${stats.available_count}`);

    const categoryStats = await Product.getByCategory();
    console.log(`\nBy Category:`);
    categoryStats.forEach(cat => {
      console.log(`  ${cat.category}:`);
      console.log(`    Products: ${cat.count}`);
      console.log(`    Stock: ${cat.total_stock}`);
      console.log(`    Avg Price: $${parseFloat(cat.avg_price).toFixed(2)}`);
    });

    // === UPDATE PRODUCT STOCK ===
    console.log('\n--- Updating Stock ---');

    await Product.updateStock(product2.id, -5);
    const updatedProduct = await Product.findById(product2.id);
    console.log(`✅ Updated ${updatedProduct.name} stock to ${updatedProduct.stock}`);

    // === PAGINATION ===
    console.log('\n--- Pagination Example ---');

    const page1 = await User.findPaginated(1, 2);
    console.log(`\nPage 1 (${page1.users.length} users):`);
    page1.users.forEach(u => console.log(`  - ${u.name}`));
    console.log(`Total Pages: ${page1.pagination.totalPages}`);

    // === CREATE ORDER ===
    console.log('\n--- Creating Order ---');

    const orderQuery = `
      INSERT INTO orders (user_id, total, status)
      VALUES ($1, $2, $3)
      RETURNING *
    `;
    const order = await pool.query(orderQuery, [
      user1.id,
      1329.98,
      'completed'
    ]);
    console.log(`✅ Created order #${order.rows[0].id}`);

    // Add order items
    const itemsQuery = `
      INSERT INTO order_items (order_id, product_id, quantity, price)
      VALUES ($1, $2, $3, $4)
    `;
    await pool.query(itemsQuery, [order.rows[0].id, product1.id, 1, product1.price]);
    await pool.query(itemsQuery, [order.rows[0].id, product2.id, 1, product2.price]);
    console.log('✅ Added order items');

    // === JOIN QUERY ===
    console.log('\n--- Order Details (with JOINs) ---');

    const orderDetails = await pool.query(`
      SELECT 
        users.name as customer,
        orders.id as order_id,
        orders.total,
        orders.status,
        json_agg(
          json_build_object(
            'product', products.name,
            'quantity', order_items.quantity,
            'price', order_items.price
          )
        ) as items
      FROM orders
      INNER JOIN users ON orders.user_id = users.id
      INNER JOIN order_items ON orders.id = order_items.order_id
      INNER JOIN products ON order_items.product_id = products.id
      WHERE orders.id = $1
      GROUP BY users.name, orders.id, orders.total, orders.status
    `, [order.rows[0].id]);

    const orderInfo = orderDetails.rows[0];
    console.log(`\nOrder #${orderInfo.order_id}:`);
    console.log(`  Customer: ${orderInfo.customer}`);
    console.log(`  Status: ${orderInfo.status}`);
    console.log(`  Total: $${orderInfo.total}`);
    console.log(`  Items:`);
    orderInfo.items.forEach(item => {
      console.log(`    - ${item.product} x${item.quantity} @ $${item.price}`);
    });

    // === USER WITH ORDERS ===
    console.log('\n--- User with Orders ---');

    const userWithOrders = await User.findWithOrders(user1.id);
    console.log(`\n${userWithOrders.name}'s Orders:`);
    if (userWithOrders.orders) {
      userWithOrders.orders.forEach(o => {
        console.log(`  Order #${o.id}: $${o.total} - ${o.status}`);
      });
    }

    // === DELETE ===
    console.log('\n--- Delete Operations ---');

    const deleted = await User.delete(user3.id);
    console.log(`✅ Deleted user: ${deleted.name}`);

    // === FINAL COUNTS ===
    console.log('\n--- Final Counts ---');

    const userCount = await User.count();
    const productCount = await (await pool.query('SELECT COUNT(*) FROM products')).rows[0].count;
    console.log(`  Users: ${userCount}`);
    console.log(`  Products: ${productCount}`);

    console.log('\n=== Demo Complete ===');

  } catch (error) {
    console.error('❌ Error:', error.message);
  } finally {
    await pool.end();
    console.log('Database connection closed');
  }
}

// Run the application
main();
```

**package.json:**

```json
{
  "name": "postgres-demo",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "pg": "^8.11.0",
    "dotenv": "^16.3.1"
  }
}
```

**Run the application:**

```bash
# Create database
createdb myapp_db

# Run the demo
npm start
```

---

**📚 Interview Questions & Answers**

**Q1: What is the difference between SQL and NoSQL databases?**

**Answer:**
Already covered in Day 33, but here's a SQL-focused perspective:

**SQL (Relational):**
- Fixed schema with tables, rows, columns
- ACID transactions (Atomicity, Consistency, Isolation, Durability)
- Relationships through foreign keys and JOINs
- Best for: Complex queries, data integrity, financial systems

**Example:**
```sql
-- SQL enforces relationships
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id)  -- Must exist in users table
);

-- JOIN to get related data
SELECT users.name, orders.total
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

**Q2: Explain the different types of JOINs in SQL.**

**Answer:**

**1. INNER JOIN** - Returns only matching rows from both tables
```sql
SELECT users.name, orders.total
FROM users
INNER JOIN orders ON users.id = orders.user_id;
-- Only users who have orders
```

**2. LEFT JOIN** - Returns all rows from left table, matching from right
```sql
SELECT users.name, orders.total
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
-- All users, even those without orders (orders.total will be NULL)
```

**3. RIGHT JOIN** - Returns all rows from right table, matching from left
```sql
SELECT users.name, orders.total
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
-- All orders, even if user was deleted
```

**4. FULL OUTER JOIN** - Returns all rows from both tables
```sql
SELECT users.name, orders.total
FROM users
FULL OUTER JOIN orders ON users.id = orders.user_id;
-- All users and all orders, with NULLs where no match
```

**Visual Example:**
```
Table A (users):     Table B (orders):
id | name           user_id | total
1  | Alice          1       | 100
2  | Bob            1       | 200
3  | Charlie        2       | 150

INNER JOIN: Alice-100, Alice-200, Bob-150
LEFT JOIN:  Alice-100, Alice-200, Bob-150, Charlie-NULL
RIGHT JOIN: Alice-100, Alice-200, Bob-150
```

**Q3: What are SQL injection attacks and how do you prevent them?**

**Answer:**

**SQL Injection** - Malicious SQL code inserted through user input.

**Vulnerable code:**
```javascript
// ❌ NEVER DO THIS - vulnerable to SQL injection
const email = req.body.email;  // User input: "'; DROP TABLE users; --"
const query = `SELECT * FROM users WHERE email = '${email}'`;
await pool.query(query);

// This becomes:
// SELECT * FROM users WHERE email = ''; DROP TABLE users; --'
// Deletes your entire users table!
```

**Safe code - Use parameterized queries:**
```javascript
// ✅ SAFE - uses parameterized query
const email = req.body.email;
const query = 'SELECT * FROM users WHERE email = $1';
await pool.query(query, [email]);

// PostgreSQL treats the input as data, not code
// Even if input is "'; DROP TABLE users; --", it will just search for that exact string
```

**Prevention methods:**
1. **Parameterized queries** (prepared statements) - ALWAYS use this
2. **Input validation** - Validate and sanitize user input
3. **Least privilege** - Database user should have minimal permissions
4. **ORM/Query builder** - Use libraries that handle escaping

**Q4: What is a primary key and foreign key?**

**Answer:**

**Primary Key:**
- Uniquely identifies each row in a table
- Cannot be NULL
- Must be unique
- Usually auto-incrementing integer

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,  -- Primary key
  email VARCHAR(100) UNIQUE,
  name VARCHAR(100)
);
```

**Foreign Key:**
- References primary key in another table
- Enforces referential integrity
- Creates relationships between tables

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,  -- Foreign key
  total NUMERIC(10, 2),
  
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**Benefits:**
- **Data integrity**: Can't create order for non-existent user
- **CASCADE operations**: When user is deleted, their orders can be deleted too
- **Relationships**: Defines how tables relate to each other

**Example with CASCADE:**
```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
  -- When user is deleted, all their orders are automatically deleted
);
```

**Q5: Explain ACID properties in databases.**

**Answer:**

**ACID** ensures reliable database transactions:

**A - Atomicity:**
- Transaction is all-or-nothing
- Either all operations succeed or all fail

```sql
BEGIN;  -- Start transaction
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
  UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;  -- Both succeed or both fail
```

**C - Consistency:**
- Database moves from one valid state to another
- All constraints are enforced

```sql
-- Constraint: balance >= 0
UPDATE accounts SET balance = -50 WHERE id = 1;
-- Transaction fails - violates constraint
```

**I - Isolation:**
- Concurrent transactions don't interfere
- Each transaction appears to run alone

```sql
-- Transaction 1:
BEGIN;
  SELECT balance FROM accounts WHERE id = 1;  -- Reads 1000
  -- Transaction 2 updates to 500 here
  UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;  -- Result depends on isolation level
```

**D - Durability:**
- Completed transactions are permanent
- Survive system failures

```sql
COMMIT;  -- Once committed, data is safe even if power fails
```

**Real-world example - Money transfer:**
```javascript
const client = await pool.connect();
try {
  await client.query('BEGIN');
  
  // Withdraw from account 1
  await client.query(
    'UPDATE accounts SET balance = balance - $1 WHERE id = $2',
    [amount, fromAccount]
  );
  
  // Deposit to account 2
  await client.query(
    'UPDATE accounts SET balance = balance + $1 WHERE id = $2',
    [amount, toAccount]
  );
  
  await client.query('COMMIT');
} catch (error) {
  await client.query('ROLLBACK');  // Undo everything
  throw error;
} finally {
  client.release();
}
```

---

**🔑 Key Takeaways**

1. ✅ **SQL** - Structured Query Language for relational databases
2. ✅ **PostgreSQL** - Powerful, open-source SQL database
3. ✅ **Tables** - Store data in rows and columns with defined schema
4. ✅ **Primary Key** - Unique identifier for each row
5. ✅ **Foreign Key** - Creates relationships between tables
6. ✅ **JOINs** - Combine data from multiple tables
7. ✅ **Transactions** - ACID properties ensure data integrity
8. ✅ **Parameterized Queries** - Prevent SQL injection attacks
9. ✅ **Indexes** - Speed up queries on frequently accessed columns

**Learning Resources:**
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQL Zoo](https://sqlzoo.net/) - Interactive SQL tutorials
- [Node-postgres Documentation](https://node-postgres.com/)

---

### Day 36: Database Design & Relationships

**📖 Database Design Principles**

Good database design is crucial for:
- Data integrity
- Performance
- Scalability
- Maintainability

**Real-World Analogy:**
- **Bad Design**: Like throwing all your clothes in one pile - hard to find anything
- **Good Design**: Like organizing clothes by type, season, color - easy to find and maintain

---

**📖 Normalization**

Normalization is the process of organizing data to reduce redundancy and improve integrity.

**1st Normal Form (1NF):**
- Each column contains atomic (indivisible) values
- Each column contains values of a single type
- Each column has a unique name
- No repeating groups

**❌ Not 1NF:**
```
users
| id | name  | phones                    |
|----|-------|---------------------------|
| 1  | Alice | 555-1234, 555-5678       |
| 2  | Bob   | 555-9999                  |
```

**✅ 1NF:**
```
users                    user_phones
| id | name  |          | user_id | phone    |
|----|-------|          |---------|----------|
| 1  | Alice |          | 1       | 555-1234 |
| 2  | Bob   |          | 1       | 555-5678 |
                        | 2       | 555-9999 |
```

**2nd Normal Form (2NF):**
- Must be in 1NF
- No partial dependencies (non-key columns depend on entire primary key)

**❌ Not 2NF:**
```
order_items
| order_id | product_id | product_name | quantity | price |
|----------|------------|--------------|----------|-------|
| 1        | 101        | Laptop       | 1        | 999   |
| 1        | 102        | Mouse        | 2        | 29    |
```
*product_name depends only on product_id, not the full key (order_id + product_id)*

**✅ 2NF:**
```
products                    order_items
| id  | name   | price |    | order_id | product_id | quantity |
|-----|--------|-------|    |----------|------------|----------|
| 101 | Laptop | 999   |    | 1        | 101        | 1        |
| 102 | Mouse  | 29    |    | 1        | 102        | 2        |
```

**3rd Normal Form (3NF):**
- Must be in 2NF
- No transitive dependencies (non-key columns depend only on primary key)

**❌ Not 3NF:**
```
employees
| id | name  | department | dept_location |
|----|-------|------------|---------------|
| 1  | Alice | IT         | Building A    |
| 2  | Bob   | IT         | Building A    |
```
*dept_location depends on department, not directly on id*

**✅ 3NF:**
```
employees                  departments
| id | name  | dept_id |   | id | name | location   |
|----|-------|---------|   |----|------|------------|
| 1  | Alice | 1       |   | 1  | IT   | Building A |
| 2  | Bob   | 1       |   | 2  | HR   | Building B |
```

---

**📖 Types of Relationships**

**1. One-to-One (1:1)**
- One record in Table A relates to one record in Table B
- Example: User ↔ Profile

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE user_profiles (
  id SERIAL PRIMARY KEY,
  user_id INTEGER UNIQUE NOT NULL,  -- UNIQUE ensures 1:1
  bio TEXT,
  avatar_url VARCHAR(255),
  date_of_birth DATE,
  
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

**2. One-to-Many (1:N)**
- One record in Table A relates to many records in Table B
- Example: User → Posts (one user has many posts)

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,  -- Many posts can have same user_id
  title VARCHAR(200) NOT NULL,
  content TEXT,
  
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

**3. Many-to-Many (M:N)**
- Many records in Table A relate to many records in Table B
- Requires a **junction table** (join table)
- Example: Students ↔ Courses

```sql
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

-- Junction table
CREATE TABLE student_courses (
  id SERIAL PRIMARY KEY,
  student_id INTEGER NOT NULL,
  course_id INTEGER NOT NULL,
  enrollment_date DATE DEFAULT CURRENT_DATE,
  grade VARCHAR(2),
  
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  
  -- Prevent duplicate enrollments
  UNIQUE(student_id, course_id)
);
```

---

**💡 Complete E-Commerce Database Design**

```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  role VARCHAR(20) DEFAULT 'customer',
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User addresses (1:Many)
CREATE TABLE addresses (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  address_line1 VARCHAR(255) NOT NULL,
  address_line2 VARCHAR(255),
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  is_default BOOLEAN DEFAULT false,
  
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Categories table
CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) UNIQUE NOT NULL,
  description TEXT,
  parent_id INTEGER,  -- For nested categories
  
  FOREIGN KEY (parent_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Products table
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  category_id INTEGER,
  name VARCHAR(200) NOT NULL,
  description TEXT,
  price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
  compare_price NUMERIC(10, 2),  -- Original price for discounts
  cost NUMERIC(10, 2),  -- Cost to business
  sku VARCHAR(100) UNIQUE,  -- Stock Keeping Unit
  barcode VARCHAR(100),
  stock_quantity INTEGER DEFAULT 0 CHECK (stock_quantity >= 0),
  is_active BOOLEAN DEFAULT true,
  weight NUMERIC(10, 2),  -- in kg
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Product images (1:Many)
CREATE TABLE product_images (
  id SERIAL PRIMARY KEY,
  product_id INTEGER NOT NULL,
  url VARCHAR(255) NOT NULL,
  alt_text VARCHAR(255),
  is_primary BOOLEAN DEFAULT false,
  display_order INTEGER DEFAULT 0,
  
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Product tags (Many:Many)
CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE product_tags (
  product_id INTEGER NOT NULL,
  tag_id INTEGER NOT NULL,
  
  PRIMARY KEY (product_id, tag_id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

-- Shopping cart (1:Many)
CREATE TABLE cart_items (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  
  UNIQUE(user_id, product_id)  -- One product per user in cart
);

-- Orders table
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  order_number VARCHAR(50) UNIQUE NOT NULL,
  status VARCHAR(20) DEFAULT 'pending',
  
  subtotal NUMERIC(10, 2) NOT NULL,
  tax NUMERIC(10, 2) DEFAULT 0,
  shipping_cost NUMERIC(10, 2) DEFAULT 0,
  discount NUMERIC(10, 2) DEFAULT 0,
  total NUMERIC(10, 2) NOT NULL,
  
  shipping_address_id INTEGER,
  billing_address_id INTEGER,
  
  payment_method VARCHAR(50),
  payment_status VARCHAR(20) DEFAULT 'pending',
  
  notes TEXT,
  
  ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  shipped_at TIMESTAMP,
  delivered_at TIMESTAMP,
  
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT,
  FOREIGN KEY (shipping_address_id) REFERENCES addresses(id),
  FOREIGN KEY (billing_address_id) REFERENCES addresses(id)
);

-- Order items (1:Many)
CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  unit_price NUMERIC(10, 2) NOT NULL,
  total_price NUMERIC(10, 2) NOT NULL,
  
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

-- Product reviews (1:Many)
CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  product_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  order_id INTEGER,  -- Optional: link to verified purchase
  rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
  title VARCHAR(200),
  comment TEXT,
  is_verified_purchase BOOLEAN DEFAULT false,
  helpful_count INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE SET NULL,
  
  -- One review per user per product
  UNIQUE(product_id, user_id)
);

-- Wishlist (Many:Many)
CREATE TABLE wishlists (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  
  UNIQUE(user_id, product_id)
);

-- Create indexes for better performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_sku ON products(sku);
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_reviews_product ON reviews(product_id);
CREATE INDEX idx_cart_items_user ON cart_items(user_id);
```

---

**💡 Sample Queries for E-Commerce**

```sql
-- 1. Get product with category and images
SELECT 
  p.id,
  p.name,
  p.price,
  p.stock_quantity,
  c.name as category,
  json_agg(
    json_build_object(
      'url', pi.url,
      'is_primary', pi.is_primary
    ) ORDER BY pi.display_order
  ) FILTER (WHERE pi.id IS NOT NULL) as images
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
LEFT JOIN product_images pi ON p.id = pi.product_id
WHERE p.id = 1
GROUP BY p.id, c.name;

-- 2. Get user's cart with product details
SELECT 
  ci.id,
  ci.quantity,
  p.name,
  p.price,
  (ci.quantity * p.price) as subtotal
FROM cart_items ci
INNER JOIN products p ON ci.product_id = p.id
WHERE ci.user_id = 1;

-- 3. Create order from cart
BEGIN;
  -- Insert order
  INSERT INTO orders (
    user_id, order_number, subtotal, tax, shipping_cost, total, status
  ) VALUES (
    1, 'ORD-2024-0001', 1000, 80, 20, 1100, 'pending'
  ) RETURNING id;
  
  -- Insert order items from cart
  INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price)
  SELECT 
    1,  -- order_id from above
    ci.product_id,
    ci.quantity,
    p.price,
    (ci.quantity * p.price)
  FROM cart_items ci
  INNER JOIN products p ON ci.product_id = p.id
  WHERE ci.user_id = 1;
  
  -- Update product stock
  UPDATE products p
  SET stock_quantity = stock_quantity - ci.quantity
  FROM cart_items ci
  WHERE p.id = ci.product_id AND ci.user_id = 1;
  
  -- Clear cart
  DELETE FROM cart_items WHERE user_id = 1;
COMMIT;

-- 4. Get order details with items
SELECT 
  o.order_number,
  o.total,
  o.status,
  o.ordered_at,
  u.first_name || ' ' || u.last_name as customer,
  json_agg(
    json_build_object(
      'product', p.name,
      'quantity', oi.quantity,
      'price', oi.unit_price
    )
  ) as items
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.id = 1
GROUP BY o.id, u.first_name, u.last_name;

-- 5. Get product with average rating
SELECT 
  p.id,
  p.name,
  p.price,
  COALESCE(AVG(r.rating), 0) as avg_rating,
  COUNT(r.id) as review_count
FROM products p
LEFT JOIN reviews r ON p.id = r.product_id
WHERE p.id = 1
GROUP BY p.id;

-- 6. Get top selling products
SELECT 
  p.name,
  SUM(oi.quantity) as total_sold,
  SUM(oi.total_price) as total_revenue
FROM products p
INNER JOIN order_items oi ON p.id = oi.product_id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'delivered'
GROUP BY p.id, p.name
ORDER BY total_sold DESC
LIMIT 10;

-- 7. Get customer order history
SELECT 
  o.order_number,
  o.total,
  o.status,
  o.ordered_at,
  COUNT(oi.id) as item_count
FROM orders o
LEFT JOIN order_items oi ON o.id = oi.order_id
WHERE o.user_id = 1
GROUP BY o.id
ORDER BY o.ordered_at DESC;

-- 8. Search products by name or tag
SELECT DISTINCT p.*
FROM products p
LEFT JOIN product_tags pt ON p.id = pt.product_id
LEFT JOIN tags t ON pt.tag_id = t.id
WHERE 
  p.name ILIKE '%laptop%'
  OR p.description ILIKE '%laptop%'
  OR t.name ILIKE '%laptop%';

-- 9. Get products in user's wishlist
SELECT 
  p.*,
  w.added_at
FROM wishlists w
INNER JOIN products p ON w.product_id = p.id
WHERE w.user_id = 1
ORDER BY w.added_at DESC;

-- 10. Get low stock products
SELECT 
  id,
  name,
  stock_quantity,
  sku
FROM products
WHERE stock_quantity < 10 AND is_active = true
ORDER BY stock_quantity ASC;
```

---

**📖 Database Constraints**

```sql
-- NOT NULL - Column must have a value
CREATE TABLE users (
  email VARCHAR(100) NOT NULL  -- Cannot be empty
);

-- UNIQUE - No duplicate values
CREATE TABLE users (
  email VARCHAR(100) UNIQUE  -- Each email must be unique
);

-- PRIMARY KEY - Unique identifier (NOT NULL + UNIQUE)
CREATE TABLE users (
  id SERIAL PRIMARY KEY  -- Auto-increment unique ID
);

-- FOREIGN KEY - Reference to another table
CREATE TABLE orders (
  user_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- CHECK - Custom validation
CREATE TABLE products (
  price NUMERIC(10, 2) CHECK (price >= 0),  -- Price must be positive
  stock INTEGER CHECK (stock >= 0 AND stock <= 10000)
);

-- DEFAULT - Default value if not specified
CREATE TABLE users (
  role VARCHAR(20) DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- CASCADE options for foreign keys
CREATE TABLE orders (
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users(id) 
    ON DELETE CASCADE      -- Delete orders when user deleted
    ON UPDATE CASCADE      -- Update orders when user ID changes
);

-- Other CASCADE options:
-- ON DELETE RESTRICT  - Prevent deletion if referenced
-- ON DELETE SET NULL  - Set to NULL when parent deleted
-- ON DELETE SET DEFAULT - Set to default value
```

---

**📚 Interview Questions & Answers**

**Q1: Explain database normalization and its benefits.**

**Answer:**
Normalization is organizing data to reduce redundancy and improve integrity.

**Benefits:**
1. **Eliminate redundancy** - Store each fact once
2. **Prevent anomalies** - Avoid update/delete/insert issues
3. **Save storage** - Less duplicate data
4. **Improve integrity** - Maintain consistency

**Example:**

**❌ Unnormalized (redundant):**
```
orders
| id | customer_name | customer_email    | product  | price |
|----|---------------|-------------------|----------|-------|
| 1  | Alice         | alice@example.com | Laptop   | 999   |
| 2  | Alice         | alice@example.com | Mouse    | 29    |
```
*Alice's email stored twice - if she changes email, must update multiple rows*

**✅ Normalized:**
```
customers                orders
| id | name  | email  |   | id | customer_id | product_id |
|----|-------|--------|   |----|-------------|------------|
| 1  | Alice | a@e.c  |   | 1  | 1           | 1          |
                          | 2  | 1           | 2          |

products
| id | name   | price |
|----|--------|-------|
| 1  | Laptop | 999   |
| 2  | Mouse  | 29    |
```
*Each fact stored once - email change only needs one update*

**Q2: What are the different types of relationships in databases?**

**Answer:**

**1. One-to-One (1:1):**
- One record relates to exactly one record
- Example: User ↔ Profile

```sql
users: { id, email }
profiles: { id, user_id UNIQUE, bio }
```

**2. One-to-Many (1:N):**
- One record relates to many records
- Most common relationship
- Example: User → Orders

```sql
users: { id, name }
orders: { id, user_id, total }  -- Many orders per user
```

**3. Many-to-Many (M:N):**
- Many records relate to many records
- Requires junction table
- Example: Students ↔ Courses

```sql
students: { id, name }
courses: { id, name }
enrollments: { student_id, course_id }  -- Junction table
```

**Visual:**
```
1:1   User ━━━━ Profile
1:N   User ━━┳━ Order 1
          ┣━ Order 2
          ┗━ Order 3
M:N   Student 1 ━┳━ Enrollment ━━ Course A
      Student 2 ━╋━ Enrollment ━━ Course B
                 ┗━ Enrollment ━━ Course C
```

**Q3: What is the difference between DELETE CASCADE and DELETE RESTRICT?**

**Answer:**

**DELETE CASCADE:**
- Automatically deletes related records
- Use when child records are meaningless without parent

```sql
CREATE TABLE orders (
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users(id) 
    ON DELETE CASCADE
);

-- When user deleted, all their orders are automatically deleted
DELETE FROM users WHERE id = 1;
-- Orders for user 1 are also deleted
```

**DELETE RESTRICT:**
- Prevents deletion if related records exist
- Use when you want to protect data

```sql
CREATE TABLE order_items (
  product_id INTEGER,
  FOREIGN KEY (product_id) REFERENCES products(id)
    ON DELETE RESTRICT
);

-- Cannot delete product if it's in any orders
DELETE FROM products WHERE id = 1;
-- ERROR: Cannot delete - product is referenced in order_items
```

**Other options:**
```sql
ON DELETE SET NULL     -- Set foreign key to NULL
ON DELETE SET DEFAULT  -- Set to default value
```

**Q4: What are indexes and when should you use them?**

**Answer:**
Indexes speed up data retrieval but slow down writes.

**When to use indexes:**
✅ Columns in WHERE clauses
✅ Columns in JOIN conditions
✅ Columns in ORDER BY
✅ Foreign keys
✅ Frequently searched columns

**When NOT to use:**
❌ Small tables
❌ Columns with many NULL values
❌ Columns that change frequently
❌ Columns with low cardinality (few unique values)

**Example:**
```sql
-- Without index - slow (scans entire table)
SELECT * FROM users WHERE email = 'alice@example.com';

-- Create index
CREATE INDEX idx_users_email ON users(email);

-- With index - fast (direct lookup)
SELECT * FROM users WHERE email = 'alice@example.com';

-- Composite index (multiple columns)
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Useful for queries like:
SELECT * FROM orders WHERE user_id = 1 AND status = 'pending';
```

**Trade-offs:**
- **Faster reads** (queries are faster)
- **Slower writes** (inserts/updates/deletes take longer)
- **More storage** (indexes take disk space)

**Q5: Explain ACID properties with a practical example.**

**Answer:**
ACID ensures reliable transactions (covered in Day 35), but here's a practical shopping cart example:

**Scenario: User checkout process**

```javascript
// ✅ ACID Transaction
const client = await pool.connect();
try {
  await client.query('BEGIN');
  
  // 1. Create order
  const order = await client.query(`
    INSERT INTO orders (user_id, total)
    VALUES ($1, $2) RETURNING id
  `, [userId, total]);
  
  // 2. Move cart items to order
  await client.query(`
    INSERT INTO order_items (order_id, product_id, quantity, price)
    SELECT $1, product_id, quantity, price
    FROM cart_items WHERE user_id = $2
  `, [order.rows[0].id, userId]);
  
  // 3. Update product stock
  await client.query(`
    UPDATE products p
    SET stock_quantity = stock_quantity - c.quantity
    FROM cart_items c
    WHERE p.id = c.product_id AND c.user_id = $1
  `, [userId]);
  
  // 4. Clear cart
  await client.query(`
    DELETE FROM cart_items WHERE user_id = $1
  `, [userId]);
  
  await client.query('COMMIT');
  // ✅ All or nothing - either everything succeeds or nothing changes
  
} catch (error) {
  await client.query('ROLLBACK');
  // ❌ Error occurred - undo everything
  throw error;
} finally {
  client.release();
}
```

**ACID breakdown:**
- **Atomic**: All 4 steps succeed or none do
- **Consistent**: Database stays valid (stock never negative)
- **Isolated**: Other users don't see partial state
- **Durable**: Once committed, order is permanent

---

**🔑 Key Takeaways**

1. ✅ **Normalization** - Organize data to reduce redundancy
2. ✅ **Relationships** - 1:1, 1:N, M:N with foreign keys
3. ✅ **Constraints** - Enforce data integrity (NOT NULL, UNIQUE, CHECK)
4. ✅ **Indexes** - Speed up queries on frequently accessed columns
5. ✅ **CASCADE** - Automatic actions when parent records change
6. ✅ **Junction Tables** - Handle many-to-many relationships
7. ✅ **Transactions** - Group operations for ACID compliance

**Learning Resources:**
- [Database Design Tutorial](https://www.lucidchart.com/pages/database-diagram/database-design)
- [Normalization Explained](https://www.essentialsql.com/get-ready-to-learn-sql-database-normalization-explained-in-simple-english/)
- [PostgreSQL Indexes](https://www.postgresql.org/docs/current/indexes.html)

---

## Module 10: Authentication & Security (Days 49-54)

### Day 49: Authentication vs Authorization

**📖 What is Authentication?**

**Authentication** = Verifying WHO you are (proving identity)

**Real-World Analogy:**
- Showing your ID card at airport security - you prove you are who you claim to be

**Examples:**
- Login with username/password
- Fingerprint scan
- Face recognition
- Two-factor authentication (2FA)

---

**📖 What is Authorization?**

**Authorization** = Verifying WHAT you can do (checking permissions)

**Real-World Analogy:**
- Your airplane ticket says which seat you can access - you're authorized for seat 12A, not 12B

**Examples:**
- Admin can delete users, regular users cannot
- Premium users can download files, free users cannot
- Manager can approve expenses, employees cannot

---

**📖 Authentication vs Authorization**

| Feature | Authentication | Authorization |
|---------|----------------|---------------|
| **Question** | Who are you? | What can you do? |
| **Process** | Verify identity | Check permissions |
| **When** | Happens first | Happens after authentication |
| **Example** | Login with password | Access admin dashboard |
| **HTTP Status** | 401 Unauthorized | 403 Forbidden |
| **Data** | Username, password, biometrics | Roles, permissions, scopes |

**Complete Example:**
```javascript
// 1. AUTHENTICATION - Who are you?
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  
  // Verify identity
  const user = await User.findByEmail(email);
  if (!user || !await bcrypt.compare(password, user.password)) {
    return res.status(401).json({ error: 'Invalid credentials' });  // 401
  }
  
  // Generate token
  const token = jwt.sign({ userId: user.id, role: user.role }, SECRET);
  res.json({ token });
});

// 2. AUTHORIZATION - What can you do?
app.delete('/users/:id', authenticateToken, authorize('admin'), async (req, res) => {
  // Only admins can delete users
  await User.delete(req.params.id);
  res.json({ message: 'User deleted' });
});

// If non-admin tries: 403 Forbidden
```

---

**📖 Common Authentication Methods**

**1. Session-Based Authentication (Traditional)**
- Server stores session data
- Client gets session ID in cookie
- Stateful (server remembers who is logged in)

```
Client                     Server
  |----Login (credentials)--->|
  |<---Set-Cookie: sessionId--|
  |                            | [Store session in memory/DB]
  |----Request + Cookie------->|
  |                            | [Lookup session]
  |<---Response----------------|
```

**2. Token-Based Authentication (Modern)**
- Server creates signed token (JWT)
- Client stores token
- Stateless (server doesn't store sessions)

```
Client                     Server
  |----Login (credentials)--->|
  |<---JWT Token--------------|
  |                            | [No storage needed]
  |----Request + JWT---------->|
  |                            | [Verify signature]
  |<---Response----------------|
```

**3. OAuth 2.0 (Third-Party)**
- Login with Google, Facebook, GitHub
- User authorizes app to access their data
- No password handling

**4. Multi-Factor Authentication (MFA)**
- Something you know (password)
- Something you have (phone, token)
- Something you are (fingerprint, face)

---

**💡 Session-Based Authentication Example**

```javascript
const express = require('express');
const session = require('express-session');
const bcrypt = require('bcrypt');

const app = express();

// Configure session
app.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: false,  // true in production with HTTPS
    httpOnly: true,  // Prevent JavaScript access
    maxAge: 1000 * 60 * 60 * 24  // 24 hours
  }
}));

app.use(express.json());

// In-memory user storage (use database in production)
const users = [];

// Register
app.post('/register', async (req, res) => {
  const { email, password } = req.body;
  
  // Check if user exists
  if (users.find(u => u.email === email)) {
    return res.status(400).json({ error: 'Email already exists' });
  }
  
  // Hash password
  const hashedPassword = await bcrypt.hash(password, 10);
  
  // Save user
  const user = {
    id: users.length + 1,
    email,
    password: hashedPassword
  };
  users.push(user);
  
  res.status(201).json({ message: 'User created', userId: user.id });
});

// Login
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  
  // Find user
  const user = users.find(u => u.email === email);
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Verify password
  const isValid = await bcrypt.compare(password, user.password);
  if (!isValid) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  
  // Create session
  req.session.userId = user.id;
  req.session.email = user.email;
  
  res.json({ message: 'Logged in successfully', user: { id: user.id, email: user.email } });
});

// Middleware to check authentication
const requireAuth = (req, res, next) => {
  if (!req.session.userId) {
    return res.status(401).json({ error: 'Not authenticated' });
  }
  next();
};

// Protected route
app.get('/profile', requireAuth, (req, res) => {
  const user = users.find(u => u.id === req.session.userId);
  res.json({ user: { id: user.id, email: user.email } });
});

// Logout
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({ error: 'Logout failed' });
    }
    res.clearCookie('connect.sid');  // Session cookie name
    res.json({ message: 'Logged out successfully' });
  });
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

---

**📚 Interview Questions & Answers**

**Q1: What is the difference between authentication and authorization?**

**Answer:**
- **Authentication** verifies WHO you are (identity verification)
- **Authorization** verifies WHAT you can access (permission checking)

**Example:**
```javascript
// Authentication: Login
POST /login { email, password }
→ Returns token if credentials valid

// Authorization: Access control
GET /admin/users
→ Checks if user has 'admin' role
→ 401 if not authenticated
→ 403 if authenticated but not admin
```

**Real-world:**
- **Authentication**: Hotel checks your ID when you check in
- **Authorization**: Your room key only opens your room, not others

**Q2: What is session-based authentication?**

**Answer:**
Session-based authentication stores user session data on the server.

**How it works:**
1. User logs in with credentials
2. Server creates session and stores it (memory/database)
3. Server sends session ID to client as cookie
4. Client sends cookie with each request
5. Server looks up session to verify user

**Pros:**
- ✅ Server controls sessions (can revoke anytime)
- ✅ More secure (sensitive data on server)
- ✅ Easy to implement

**Cons:**
- ❌ Stateful (server must store sessions)
- ❌ Doesn't scale well (load balancer issues)
- ❌ Memory/database overhead

**Example:**
```javascript
// Server stores sessions
sessions = {
  'abc123': { userId: 1, email: 'alice@example.com' }
}

// Client sends cookie
Cookie: sessionId=abc123

// Server looks up session
const session = sessions['abc123'];  // { userId: 1, ... }
```

**Q3: What are common authentication methods?**

**Answer:**

**1. Password-based:**
- Username + password
- Most common, but vulnerable to attacks
- Requires hashing (bcrypt, argon2)

**2. Token-based (JWT):**
- Stateless, scalable
- Token contains user info
- Good for APIs and microservices

**3. OAuth/Social Login:**
- Login with Google, Facebook, GitHub
- No password management
- Uses OAuth 2.0 protocol

**4. Multi-Factor Authentication (MFA):**
- Password + SMS code
- Password + authenticator app
- Password + biometric

**5. Biometric:**
- Fingerprint, Face ID, iris scan
- Secure but requires special hardware

**6. Certificate-based:**
- SSL/TLS certificates
- Used in enterprise, SSH keys

**Security ranking:**
```
Least Secure                          Most Secure
    ↓                                     ↓
Password → Password+2FA → Biometric → Certificate+2FA
```

---

### Day 50: JWT (JSON Web Tokens) Authentication

**📖 What is JWT?**

JWT (JSON Web Token) is a compact, self-contained way to securely transmit information between parties as a JSON object.

**Real-World Analogy:**
- JWT is like a signed passport - it contains your information and is signed by a trusted authority. Anyone can read it, but only the authority can create/verify it.

**Why Use JWT?**
1. **Stateless** - Server doesn't store sessions
2. **Scalable** - Works across multiple servers
3. **Mobile-friendly** - Easy to use in mobile apps
4. **Cross-domain** - Works across different domains

---

**📖 JWT Structure**

A JWT consists of three parts separated by dots (`.`):

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEsImlhdCI6MTYxNjI0ODAwMH0.5mhBHqs5_DTLdINd9p5m7ZJ6XD0Xc55kIaCRY5r6HRA

HEADER.PAYLOAD.SIGNATURE
```

**1. Header** (Red):
```json
{
  "alg": "HS256",      // Algorithm
  "typ": "JWT"         // Type
}
```

**2. Payload** (Purple):
```json
{
  "userId": 1,
  "email": "alice@example.com",
  "role": "admin",
  "iat": 1616248000,   // Issued at
  "exp": 1616334400    // Expires at
}
```

**3. Signature** (Blue):
```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

---

**💡 Complete JWT Authentication System**

**Project Structure:**
```
jwt-auth/
├── package.json
├── .env
├── config/
│   └── database.js
├── models/
│   └── User.js
├── middleware/
│   ├── auth.js
│   └── authorize.js
├── routes/
│   ├── auth.js
│   └── users.js
└── server.js
```

**Install Dependencies:**
```bash
npm init -y
npm install express pg bcrypt jsonwebtoken dotenv
```

**.env:**
```env
PORT=3000
DB_HOST=localhost
DB_PORT=5432
DB_NAME=auth_db
DB_USER=postgres
DB_PASSWORD=yourpassword

JWT_SECRET=your-super-secret-key-change-in-production
JWT_EXPIRE=7d
```

**Database Schema:**
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  role VARCHAR(20) DEFAULT 'user',
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
```

**config/database.js:**
```javascript
const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD
});

pool.on('connect', () => {
  console.log('✅ Connected to PostgreSQL');
});

module.exports = pool;
```

**models/User.js:**
```javascript
const pool = require('../config/database');
const bcrypt = require('bcrypt');

class User {
  static async create(userData) {
    const { email, password, firstName, lastName, role = 'user' } = userData;
    
    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);
    
    const query = `
      INSERT INTO users (email, password, first_name, last_name, role)
      VALUES ($1, $2, $3, $4, $5)
      RETURNING id, email, first_name, last_name, role, created_at
    `;
    
    try {
      const result = await pool.query(query, [
        email,
        hashedPassword,
        firstName,
        lastName,
        role
      ]);
      return result.rows[0];
    } catch (error) {
      if (error.code === '23505') {  // Unique violation
        throw new Error('Email already exists');
      }
      throw error;
    }
  }

  static async findByEmail(email) {
    const query = 'SELECT * FROM users WHERE email = $1';
    const result = await pool.query(query, [email]);
    return result.rows[0];
  }

  static async findById(id) {
    const query = 'SELECT id, email, first_name, last_name, role, is_active, created_at FROM users WHERE id = $1';
    const result = await pool.query(query, [id]);
    return result.rows[0];
  }

  static async findAll() {
    const query = 'SELECT id, email, first_name, last_name, role, is_active, created_at FROM users ORDER BY created_at DESC';
    const result = await pool.query(query);
    return result.rows;
  }

  static async update(id, updates) {
    const fields = [];
    const values = [];
    let paramCount = 1;

    Object.keys(updates).forEach(key => {
      if (key !== 'id' && key !== 'password') {  // Don't update these directly
        fields.push(`${key} = $${paramCount}`);
        values.push(updates[key]);
        paramCount++;
      }
    });

    if (fields.length === 0) {
      throw new Error('No valid fields to update');
    }

    fields.push('updated_at = CURRENT_TIMESTAMP');
    values.push(id);

    const query = `
      UPDATE users
      SET ${fields.join(', ')}
      WHERE id = $${paramCount}
      RETURNING id, email, first_name, last_name, role, updated_at
    `;

    const result = await pool.query(query, values);
    return result.rows[0];
  }

  static async delete(id) {
    const query = 'DELETE FROM users WHERE id = $1 RETURNING id, email';
    const result = await pool.query(query, [id]);
    return result.rows[0];
  }

  static async verifyPassword(plainPassword, hashedPassword) {
    return await bcrypt.compare(plainPassword, hashedPassword);
  }
}

module.exports = User;
```

**middleware/auth.js:**
```javascript
const jwt = require('jsonwebtoken');
const User = require('../models/User');

const authenticateToken = async (req, res, next) => {
  try {
    // Get token from header
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];  // Bearer TOKEN

    if (!token) {
      return res.status(401).json({
        success: false,
        error: 'Access token required'
      });
    }

    // Verify token
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    // Get user from database
    const user = await User.findById(decoded.userId);

    if (!user) {
      return res.status(401).json({
        success: false,
        error: 'User not found'
      });
    }

    if (!user.is_active) {
      return res.status(401).json({
        success: false,
        error: 'Account is deactivated'
      });
    }

    // Attach user to request
    req.user = user;
    next();
  } catch (error) {
    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({
        success: false,
        error: 'Invalid token'
      });
    }
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({
        success: false,
        error: 'Token expired'
      });
    }
    res.status(500).json({
      success: false,
      error: 'Authentication failed'
    });
  }
};

module.exports = { authenticateToken };
```

**middleware/authorize.js:**
```javascript
const authorize = (...roles) => {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({
        success: false,
        error: 'Not authenticated'
      });
    }

    if (!roles.includes(req.user.role)) {
      return res.status(403).json({
        success: false,
        error: `Access denied. Requires one of: ${roles.join(', ')}`
      });
    }

    next();
  };
};

module.exports = { authorize };
```

**routes/auth.js:**
```javascript
const express = require('express');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const { authenticateToken } = require('../middleware/auth');

const router = express.Router();

// Generate JWT token
const generateToken = (userId) => {
  return jwt.sign(
    { userId },
    process.env.JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRE }
  );
};

// Register
router.post('/register', async (req, res) => {
  try {
    const { email, password, firstName, lastName } = req.body;

    // Validation
    if (!email || !password || !firstName || !lastName) {
      return res.status(400).json({
        success: false,
        error: 'Please provide all required fields'
      });
    }

    if (password.length < 6) {
      return res.status(400).json({
        success: false,
        error: 'Password must be at least 6 characters'
      });
    }

    // Create user
    const user = await User.create({ email, password, firstName, lastName });

    // Generate token
    const token = generateToken(user.id);

    res.status(201).json({
      success: true,
      data: {
        user: {
          id: user.id,
          email: user.email,
          firstName: user.first_name,
          lastName: user.last_name,
          role: user.role
        },
        token
      }
    });
  } catch (error) {
    res.status(400).json({
      success: false,
      error: error.message
    });
  }
});

// Login
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validation
    if (!email || !password) {
      return res.status(400).json({
        success: false,
        error: 'Please provide email and password'
      });
    }

    // Find user
    const user = await User.findByEmail(email);
    if (!user) {
      return res.status(401).json({
        success: false,
        error: 'Invalid credentials'
      });
    }

    // Verify password
    const isValidPassword = await User.verifyPassword(password, user.password);
    if (!isValidPassword) {
      return res.status(401).json({
        success: false,
        error: 'Invalid credentials'
      });
    }

    // Check if account is active
    if (!user.is_active) {
      return res.status(401).json({
        success: false,
        error: 'Account is deactivated'
      });
    }

    // Generate token
    const token = generateToken(user.id);

    res.json({
      success: true,
      data: {
        user: {
          id: user.id,
          email: user.email,
          firstName: user.first_name,
          lastName: user.last_name,
          role: user.role
        },
        token
      }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Login failed'
    });
  }
});

// Get current user
router.get('/me', authenticateToken, async (req, res) => {
  res.json({
    success: true,
    data: {
      user: {
        id: req.user.id,
        email: req.user.email,
        firstName: req.user.first_name,
        lastName: req.user.last_name,
        role: req.user.role,
        createdAt: req.user.created_at
      }
    }
  });
});

module.exports = router;
```

**routes/users.js:**
```javascript
const express = require('express');
const User = require('../models/User');
const { authenticateToken } = require('../middleware/auth');
const { authorize } = require('../middleware/authorize');

const router = express.Router();

// Get all users (admin only)
router.get('/', authenticateToken, authorize('admin'), async (req, res) => {
  try {
    const users = await User.findAll();
    res.json({
      success: true,
      data: { users }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to fetch users'
    });
  }
});

// Get user by ID (admin only)
router.get('/:id', authenticateToken, authorize('admin'), async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    
    if (!user) {
      return res.status(404).json({
        success: false,
        error: 'User not found'
      });
    }

    res.json({
      success: true,
      data: { user }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to fetch user'
    });
  }
});

// Update user (admin only)
router.put('/:id', authenticateToken, authorize('admin'), async (req, res) => {
  try {
    const { firstName, lastName, role, isActive } = req.body;
    
    const updates = {};
    if (firstName) updates.first_name = firstName;
    if (lastName) updates.last_name = lastName;
    if (role) updates.role = role;
    if (isActive !== undefined) updates.is_active = isActive;

    const user = await User.update(req.params.id, updates);

    res.json({
      success: true,
      data: { user }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to update user'
    });
  }
});

// Delete user (admin only)
router.delete('/:id', authenticateToken, authorize('admin'), async (req, res) => {
  try {
    const user = await User.delete(req.params.id);
    
    if (!user) {
      return res.status(404).json({
        success: false,
        error: 'User not found'
      });
    }

    res.json({
      success: true,
      data: { user }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to delete user'
    });
  }
});

module.exports = router;
```

**server.js:**
```javascript
const express = require('express');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const userRoutes = require('./routes/users');

const app = express();

// Middleware
app.use(express.json());

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/users', userRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    success: false,
    error: 'Something went wrong!'
  });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});
```

**Testing with curl/Postman:**

```bash
# 1. Register
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@example.com",
    "password": "password123",
    "firstName": "Alice",
    "lastName": "Johnson"
  }'

# Response:
# {
#   "success": true,
#   "data": {
#     "user": { "id": 1, "email": "alice@example.com", ... },
#     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
#   }
# }

# 2. Login
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "alice@example.com",
    "password": "password123"
  }'

# 3. Get current user (protected)
curl -X GET http://localhost:3000/api/auth/me \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

# 4. Get all users (admin only)
curl -X GET http://localhost:3000/api/users \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

---

**📖 JWT Best Practices**

**1. Token Storage:**
```javascript
// ✅ GOOD - Store in memory or secure httpOnly cookie
localStorage is vulnerable to XSS attacks

// Better options:
// 1. Memory (lost on refresh - needs refresh token)
let accessToken = null;

// 2. HttpOnly cookie (server-side only)
res.cookie('token', token, {
  httpOnly: true,  // JavaScript cannot access
  secure: true,    // HTTPS only
  sameSite: 'strict',
  maxAge: 7 * 24 * 60 * 60 * 1000  // 7 days
});
```

**2. Short Expiration:**
```javascript
// Access token: Short-lived (15 minutes - 1 hour)
const accessToken = jwt.sign({ userId }, SECRET, { expiresIn: '15m' });

// Refresh token: Long-lived (7-30 days)
const refreshToken = jwt.sign({ userId }, REFRESH_SECRET, { expiresIn: '7d' });
```

**3. Include Minimal Data:**
```javascript
// ✅ GOOD - Only necessary info
const token = jwt.sign({ userId: user.id, role: user.role }, SECRET);

// ❌ BAD - Too much sensitive data
const token = jwt.sign({ userId, email, password, ssn }, SECRET);
```

**4. Use Strong Secret:**
```javascript
// ❌ BAD
JWT_SECRET=secret

// ✅ GOOD
JWT_SECRET=8f7d6c5b4a3e2d1c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c
```

**5. Verify on Every Request:**
```javascript
// Always verify token before processing request
const authenticateToken = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
};
```

---

**📚 Interview Questions & Answers**

**Q1: What is JWT and how does it work?**

**Answer:**
JWT (JSON Web Token) is a compact, self-contained way to securely transmit information as a JSON object.

**Structure:**
```
HEADER.PAYLOAD.SIGNATURE

eyJhbGc...  .  eyJ1c2Vy...  .  5mhBHqs5...
```

**How it works:**
1. User logs in with credentials
2. Server verifies and creates JWT
3. Server signs JWT with secret key
4. Client receives and stores JWT
5. Client sends JWT with each request
6. Server verifies signature and processes request

**Key features:**
- **Stateless**: Server doesn't store tokens
- **Signed**: Prevents tampering
- **Base64 encoded**: Not encrypted (anyone can read payload)

**Example:**
```javascript
// Create token
const token = jwt.sign(
  { userId: 1, role: 'admin' },  // Payload
  'secret-key',                   // Secret
  { expiresIn: '1h' }            // Options
);

// Verify token
const decoded = jwt.verify(token, 'secret-key');
// { userId: 1, role: 'admin', iat: ..., exp: ... }
```

**Q2: Where should JWT tokens be stored?**

**Answer:**

**Options:**

**1. LocalStorage**
- ❌ Vulnerable to XSS attacks
- JavaScript can access and steal token
- Simple but not secure

**2. SessionStorage**
- ❌ Same XSS vulnerability as localStorage
- Lost when tab closes

**3. HttpOnly Cookie (RECOMMENDED)**
- ✅ JavaScript cannot access
- ✅ Protected from XSS
- ✅ Can set secure, sameSite flags
- ❌ Vulnerable to CSRF (use CSRF tokens)

**4. Memory (JavaScript variable)**
- ✅ Most secure (lost on refresh)
- ✅ No XSS or CSRF risk
- ❌ Lost on page refresh
- ❌ Needs refresh token mechanism

**Best practice:**
```javascript
// Store in httpOnly cookie
res.cookie('token', jwt, {
  httpOnly: true,     // Prevent JavaScript access
  secure: true,       // HTTPS only
  sameSite: 'strict', // CSRF protection
  maxAge: 3600000     // 1 hour
});
```

**Q3: What is the difference between access token and refresh token?**

**Answer:**

**Access Token:**
- Short-lived (15 min - 1 hour)
- Used to access protected resources
- Sent with every API request
- If stolen, limited damage (expires soon)

**Refresh Token:**
- Long-lived (7-30 days)
- Used to get new access tokens
- Stored securely (httpOnly cookie or database)
- Can be revoked on server

**Flow:**
```
1. Login → Get access + refresh tokens
2. API request → Use access token
3. Access token expires → Use refresh token to get new access token
4. Repeat until refresh token expires
5. User must login again
```

**Implementation:**
```javascript
// Login - return both tokens
app.post('/login', async (req, res) => {
  const user = await authenticate(req.body);
  
  const accessToken = jwt.sign(
    { userId: user.id },
    ACCESS_SECRET,
    { expiresIn: '15m' }
  );
  
  const refreshToken = jwt.sign(
    { userId: user.id },
    REFRESH_SECRET,
    { expiresIn: '7d' }
  );
  
  // Store refresh token in database
  await saveRefreshToken(user.id, refreshToken);
  
  res.json({ accessToken, refreshToken });
});

// Refresh endpoint
app.post('/refresh', async (req, res) => {
  const { refreshToken } = req.body;
  
  // Verify refresh token
  const decoded = jwt.verify(refreshToken, REFRESH_SECRET);
  
  // Check if token exists in database
  const isValid = await checkRefreshToken(decoded.userId, refreshToken);
  if (!isValid) {
    return res.status(403).json({ error: 'Invalid refresh token' });
  }
  
  // Generate new access token
  const accessToken = jwt.sign(
    { userId: decoded.userId },
    ACCESS_SECRET,
    { expiresIn: '15m' }
  );
  
  res.json({ accessToken });
});
```

**Q4: How do you secure JWT tokens?**

**Answer:**

**1. Use HTTPS** - Always transmit over encrypted connection
```javascript
// Enforce HTTPS
app.use((req, res, next) => {
  if (!req.secure && process.env.NODE_ENV === 'production') {
    return res.redirect('https://' + req.headers.host + req.url);
  }
  next();
});
```

**2. Strong Secret Key**
```bash
# Generate strong secret
node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"
```

**3. Short Expiration**
```javascript
jwt.sign(payload, secret, { expiresIn: '15m' });
```

**4. HttpOnly Cookies**
```javascript
res.cookie('token', jwt, { httpOnly: true, secure: true, sameSite: 'strict' });
```

**5. Validate Every Request**
```javascript
const auth = (req, res, next) => {
  try {
    const token = req.headers.authorization?.split(' ')[1];
    const decoded = jwt.verify(token, SECRET);
    
    // Additional checks
    if (decoded.exp < Date.now() / 1000) {
      throw new Error('Token expired');
    }
    
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Unauthorized' });
  }
};
```

**6. Token Blacklisting** (for logout)
```javascript
// Store invalidated tokens in Redis/database
const blacklist = new Set();

app.post('/logout', (req, res) => {
  const token = req.headers.authorization.split(' ')[1];
  blacklist.add(token);
  res.json({ message: 'Logged out' });
});

// Check blacklist in auth middleware
if (blacklist.has(token)) {
  return res.status(401).json({ error: 'Token revoked' });
}
```

**7. Include Claims**
```javascript
const token = jwt.sign({
  userId: user.id,
  role: user.role,
  iat: Math.floor(Date.now() / 1000),  // Issued at
  exp: Math.floor(Date.now() / 1000) + 3600,  // Expires
  iss: 'myapp.com',  // Issuer
  aud: 'myapp-users'  // Audience
}, SECRET);
```

---

**🔑 Key Takeaways**

1. ✅ **Authentication** - Who you are (identity)
2. ✅ **Authorization** - What you can access (permissions)
3. ✅ **JWT** - Stateless, scalable token-based authentication
4. ✅ **Token Storage** - HttpOnly cookies are most secure
5. ✅ **Access + Refresh** - Short-lived access, long-lived refresh
6. ✅ **Bcrypt** - Hash passwords before storing
7. ✅ **Middleware** - Protect routes with authentication checks
8. ✅ **HTTPS** - Always use encrypted connections

**Learning Resources:**
- [JWT.io](https://jwt.io/) - Decode and test JWTs
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Node.js JWT Best Practices](https://github.com/goldbergyoni/nodebestpractices#6-security-best-practices)

---

### Day 51-53: Advanced Security Topics

**📖 Password Security with Bcrypt**

Bcrypt is a password-hashing function designed to be slow (computationally expensive) to prevent brute-force attacks.

**Key Features:**
- **Salt** - Random data added to password before hashing
- **Cost factor** - Controls how slow hashing should be (higher = more secure but slower)
- **One-way** - Cannot reverse hash to get password

**Example:**
```javascript
const bcrypt = require('bcrypt');

// Hashing
const password = 'myPassword123';
const saltRounds = 10;  // Cost factor (2^10 iterations)
const hash = await bcrypt.hash(password, saltRounds);
// $2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy

// Verifying
const isMatch = await bcrypt.compare('myPassword123', hash);  // true
const isMatch2 = await bcrypt.compare('wrongPassword', hash);  // false
```

**📖 Environment Variables Security**

Never hardcode secrets in your code. Use environment variables.

**.env file:**
```env
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp_db
DB_USER=postgres
DB_PASSWORD=superSecretPassword123

# JWT
JWT_SECRET=8f7d6c5b4a3e2d1c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8e7d6c
JWT_EXPIRE=7d

# Server
PORT=3000
NODE_ENV=development
```

**.gitignore:**
```
node_modules/
.env
.env.local
.env.production
```

**Loading environment variables:**
```javascript
require('dotenv').config();

const dbConfig = {
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD
};
```

**📖 Input Validation & Sanitization**

Always validate and sanitize user input to prevent attacks.

```javascript
const validator = require('validator');

// Email validation
router.post('/register', async (req, res) => {
  const { email, password } = req.body;
  
  // Validate email
  if (!validator.isEmail(email)) {
    return res.status(400).json({ error: 'Invalid email format' });
  }
  
  // Validate password strength
  if (!validator.isStrongPassword(password, {
    minLength: 8,
    minLowercase: 1,
    minUppercase: 1,
    minNumbers: 1,
    minSymbols: 1
  })) {
    return res.status(400).json({
      error: 'Password must be at least 8 characters with uppercase, lowercase, number, and symbol'
    });
  }
  
  // Sanitize email
  const sanitizedEmail = validator.normalizeEmail(email);
  
  // Continue with registration...
});
```

**📖 Rate Limiting**

Prevent brute-force attacks by limiting request rates.

```javascript
const rateLimit = require('express-rate-limit');

// Limit login attempts
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 5,  // 5 requests per window
  message: 'Too many login attempts, please try again after 15 minutes'
});

app.post('/api/auth/login', loginLimiter, async (req, res) => {
  // Login logic
});
```

**📖 HTTPS & Security Headers**

```javascript
const helmet = require('helmet');
const express = require('express');

const app = express();

// Security headers
app.use(helmet());

// Force HTTPS in production
if (process.env.NODE_ENV === 'production') {
  app.use((req, res, next) => {
    if (req.header('x-forwarded-proto') !== 'https') {
      res.redirect(`https://${req.header('host')}${req.url}`);
    } else {
      next();
    }
  });
}
```

---

### Day 54: Complete Project - Secure Task Manager API

**💡 Full Implementation with Authentication & Authorization**

**Project Structure:**
```
task-manager-api/
├── .env
├── .gitignore
├── package.json
├── config/
│   └── database.js
├── models/
│   ├── User.js
│   └── Task.js
├── middleware/
│   ├── auth.js
│   ├── authorize.js
│   └── validation.js
├── routes/
│   ├── auth.js
│   └── tasks.js
└── server.js
```

**Database Schema:**
```sql
-- Users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  role VARCHAR(20) DEFAULT 'user',
  is_active BOOLEAN DEFAULT true,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tasks table
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  status VARCHAR(20) DEFAULT 'pending',
  priority VARCHAR(20) DEFAULT 'medium',
  due_date TIMESTAMP,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_status ON tasks(status);
```

**package.json:**
```json
{
  "name": "task-manager-api",
  "version": "1.0.0",
  "description": "Secure Task Manager API with JWT Authentication",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "pg": "^8.11.0",
    "bcrypt": "^5.1.0",
    "jsonwebtoken": "^9.0.0",
    "dotenv": "^16.0.3",
    "validator": "^13.9.0",
    "express-rate-limit": "^6.7.0",
    "helmet": "^7.0.0",
    "cors": "^2.8.5"
  },
  "devDependencies": {
    "nodemon": "^2.0.22"
  }
}
```

**.env:**
```env
PORT=3000
NODE_ENV=development

DB_HOST=localhost
DB_PORT=5432
DB_NAME=taskmanager_db
DB_USER=postgres
DB_PASSWORD=yourpassword

JWT_SECRET=your-super-secret-jwt-key-change-in-production
JWT_EXPIRE=7d
```

**models/Task.js:**
```javascript
const pool = require('../config/database');

class Task {
  static async create(taskData) {
    const { title, description, status, priority, dueDate, userId } = taskData;
    
    const query = `
      INSERT INTO tasks (title, description, status, priority, due_date, user_id)
      VALUES ($1, $2, $3, $4, $5, $6)
      RETURNING *
    `;
    
    const result = await pool.query(query, [
      title,
      description,
      status || 'pending',
      priority || 'medium',
      dueDate || null,
      userId
    ]);
    
    return result.rows[0];
  }

  static async findByUserId(userId, filters = {}) {
    let query = 'SELECT * FROM tasks WHERE user_id = $1';
    const params = [userId];
    let paramCount = 2;

    // Add filters
    if (filters.status) {
      query += ` AND status = $${paramCount}`;
      params.push(filters.status);
      paramCount++;
    }

    if (filters.priority) {
      query += ` AND priority = $${paramCount}`;
      params.push(filters.priority);
      paramCount++;
    }

    query += ' ORDER BY created_at DESC';

    const result = await pool.query(query, params);
    return result.rows;
  }

  static async findById(id, userId) {
    const query = 'SELECT * FROM tasks WHERE id = $1 AND user_id = $2';
    const result = await pool.query(query, [id, userId]);
    return result.rows[0];
  }

  static async update(id, userId, updates) {
    const fields = [];
    const values = [];
    let paramCount = 1;

    // Build dynamic update query
    Object.keys(updates).forEach(key => {
      if (['title', 'description', 'status', 'priority', 'due_date'].includes(key)) {
        fields.push(`${key} = $${paramCount}`);
        values.push(updates[key]);
        paramCount++;
      }
    });

    if (fields.length === 0) {
      throw new Error('No valid fields to update');
    }

    fields.push('updated_at = CURRENT_TIMESTAMP');
    values.push(id, userId);

    const query = `
      UPDATE tasks
      SET ${fields.join(', ')}
      WHERE id = $${paramCount} AND user_id = $${paramCount + 1}
      RETURNING *
    `;

    const result = await pool.query(query, values);
    return result.rows[0];
  }

  static async delete(id, userId) {
    const query = 'DELETE FROM tasks WHERE id = $1 AND user_id = $2 RETURNING *';
    const result = await pool.query(query, [id, userId]);
    return result.rows[0];
  }

  static async getStats(userId) {
    const query = `
      SELECT
        COUNT(*) as total,
        COUNT(*) FILTER (WHERE status = 'pending') as pending,
        COUNT(*) FILTER (WHERE status = 'in_progress') as in_progress,
        COUNT(*) FILTER (WHERE status = 'completed') as completed,
        COUNT(*) FILTER (WHERE priority = 'high') as high_priority,
        COUNT(*) FILTER (WHERE due_date < CURRENT_TIMESTAMP AND status != 'completed') as overdue
      FROM tasks
      WHERE user_id = $1
    `;
    
    const result = await pool.query(query, [userId]);
    return result.rows[0];
  }
}

module.exports = Task;
```

**middleware/validation.js:**
```javascript
const validator = require('validator');

const validateTask = (req, res, next) => {
  const { title, status, priority } = req.body;
  
  // Validate title
  if (!title || typeof title !== 'string' || title.trim().length === 0) {
    return res.status(400).json({
      success: false,
      error: 'Title is required'
    });
  }

  if (title.length > 200) {
    return res.status(400).json({
      success: false,
      error: 'Title must be less than 200 characters'
    });
  }

  // Validate status
  const validStatuses = ['pending', 'in_progress', 'completed'];
  if (status && !validStatuses.includes(status)) {
    return res.status(400).json({
      success: false,
      error: `Status must be one of: ${validStatuses.join(', ')}`
    });
  }

  // Validate priority
  const validPriorities = ['low', 'medium', 'high'];
  if (priority && !validPriorities.includes(priority)) {
    return res.status(400).json({
      success: false,
      error: `Priority must be one of: ${validPriorities.join(', ')}`
    });
  }

  next();
};

const validateRegistration = (req, res, next) => {
  const { email, password, firstName, lastName } = req.body;
  
  // Check required fields
  if (!email || !password || !firstName || !lastName) {
    return res.status(400).json({
      success: false,
      error: 'All fields are required'
    });
  }

  // Validate email
  if (!validator.isEmail(email)) {
    return res.status(400).json({
      success: false,
      error: 'Invalid email format'
    });
  }

  // Validate password
  if (password.length < 6) {
    return res.status(400).json({
      success: false,
      error: 'Password must be at least 6 characters'
    });
  }

  // Sanitize inputs
  req.body.email = validator.normalizeEmail(email);
  req.body.firstName = validator.escape(firstName.trim());
  req.body.lastName = validator.escape(lastName.trim());

  next();
};

module.exports = { validateTask, validateRegistration };
```

**routes/tasks.js:**
```javascript
const express = require('express');
const Task = require('../models/Task');
const { authenticateToken } = require('../middleware/auth');
const { validateTask } = require('../middleware/validation');

const router = express.Router();

// All routes require authentication
router.use(authenticateToken);

// Get all tasks for current user
router.get('/', async (req, res) => {
  try {
    const { status, priority } = req.query;
    const filters = {};
    
    if (status) filters.status = status;
    if (priority) filters.priority = priority;

    const tasks = await Task.findByUserId(req.user.id, filters);
    
    res.json({
      success: true,
      data: { tasks }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to fetch tasks'
    });
  }
});

// Get task statistics
router.get('/stats', async (req, res) => {
  try {
    const stats = await Task.getStats(req.user.id);
    
    res.json({
      success: true,
      data: { stats }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to fetch statistics'
    });
  }
});

// Get single task
router.get('/:id', async (req, res) => {
  try {
    const task = await Task.findById(req.params.id, req.user.id);
    
    if (!task) {
      return res.status(404).json({
        success: false,
        error: 'Task not found'
      });
    }

    res.json({
      success: true,
      data: { task }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to fetch task'
    });
  }
});

// Create new task
router.post('/', validateTask, async (req, res) => {
  try {
    const { title, description, status, priority, dueDate } = req.body;
    
    const task = await Task.create({
      title,
      description,
      status,
      priority,
      dueDate,
      userId: req.user.id
    });

    res.status(201).json({
      success: true,
      data: { task }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to create task'
    });
  }
});

// Update task
router.put('/:id', validateTask, async (req, res) => {
  try {
    const { title, description, status, priority, dueDate } = req.body;
    
    const updates = {};
    if (title !== undefined) updates.title = title;
    if (description !== undefined) updates.description = description;
    if (status !== undefined) updates.status = status;
    if (priority !== undefined) updates.priority = priority;
    if (dueDate !== undefined) updates.due_date = dueDate;

    const task = await Task.update(req.params.id, req.user.id, updates);

    if (!task) {
      return res.status(404).json({
        success: false,
        error: 'Task not found'
      });
    }

    res.json({
      success: true,
      data: { task }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to update task'
    });
  }
});

// Delete task
router.delete('/:id', async (req, res) => {
  try {
    const task = await Task.delete(req.params.id, req.user.id);

    if (!task) {
      return res.status(404).json({
        success: false,
        error: 'Task not found'
      });
    }

    res.json({
      success: true,
      data: { task }
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: 'Failed to delete task'
    });
  }
});

module.exports = router;
```

**server.js:**
```javascript
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const authRoutes = require('./routes/auth');
const taskRoutes = require('./routes/tasks');

const app = express();

// Security middleware
app.use(helmet());

// CORS
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:5173',
  credentials: true
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 100  // 100 requests per window
});
app.use(limiter);

// Body parser
app.use(express.json());

// Routes
app.use('/api/auth', authRoutes);
app.use('/api/tasks', taskRoutes);

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: 'Route not found'
  });
});

// Error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    success: false,
    error: 'Internal server error'
  });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`📝 Environment: ${process.env.NODE_ENV}`);
});
```

**Testing the API:**

```bash
# 1. Register a user
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123",
    "firstName": "John",
    "lastName": "Doe"
  }'

# Save the token from response

# 2. Login
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }'

# 3. Create a task (use token from login)
curl -X POST http://localhost:3000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README",
    "priority": "high",
    "status": "pending",
    "dueDate": "2024-12-31"
  }'

# 4. Get all tasks
curl -X GET http://localhost:3000/api/tasks \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

# 5. Get tasks by status
curl -X GET "http://localhost:3000/api/tasks?status=pending" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

# 6. Get task statistics
curl -X GET http://localhost:3000/api/tasks/stats \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

# 7. Update a task
curl -X PUT http://localhost:3000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "status": "completed"
  }'

# 8. Delete a task
curl -X DELETE http://localhost:3000/api/tasks/1 \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**📚 Interview Questions & Answers**

**Q1: How do you ensure tasks belong to the authenticated user?**

**Answer:**
Every task operation checks both task ID and user ID.

```javascript
// Instead of just checking task ID
const task = await Task.findById(req.params.id);

// We check both task ID AND user ID
const task = await Task.findById(req.params.id, req.user.id);

// SQL query
SELECT * FROM tasks WHERE id = $1 AND user_id = $2
```

This prevents:
- User A accessing User B's tasks
- User A modifying/deleting User B's tasks

**Q2: What security measures are implemented in this API?**

**Answer:**

**1. Authentication:**
- JWT-based authentication
- Password hashing with bcrypt
- Token expiration

**2. Authorization:**
- User can only access their own tasks
- Role-based access control (can be extended)

**3. Input Validation:**
- Email format validation
- Password strength requirements
- Task field validation
- SQL injection prevention (parameterized queries)

**4. Rate Limiting:**
- Prevents brute-force attacks
- Limits requests per time window

**5. Security Headers:**
- Helmet.js adds security headers
- CORS configuration
- HTTPS enforcement in production

**6. Environment Variables:**
- Secrets stored in .env file
- Not committed to version control

**Q3: How would you add pagination to the tasks endpoint?**

**Answer:**

```javascript
router.get('/', async (req, res) => {
  try {
    // Get pagination parameters
    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 10;
    const offset = (page - 1) * limit;

    // Get total count
    const countQuery = 'SELECT COUNT(*) FROM tasks WHERE user_id = $1';
    const countResult = await pool.query(countQuery, [req.user.id]);
    const total = parseInt(countResult.rows[0].count);

    // Get tasks with pagination
    const query = `
      SELECT * FROM tasks
      WHERE user_id = $1
      ORDER BY created_at DESC
      LIMIT $2 OFFSET $3
    `;
    const result = await pool.query(query, [req.user.id, limit, offset]);

    res.json({
      success: true,
      data: {
        tasks: result.rows,
        pagination: {
          page,
          limit,
          total,
          totalPages: Math.ceil(total / limit),
          hasMore: offset + limit < total
        }
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, error: 'Failed to fetch tasks' });
  }
});

// Usage:
// GET /api/tasks?page=1&limit=10
// GET /api/tasks?page=2&limit=20
```

---

**🔑 Key Takeaways - Authentication Module**

1. ✅ **Authentication** verifies identity (who you are)
2. ✅ **Authorization** verifies permissions (what you can do)
3. ✅ **JWT** enables stateless, scalable authentication
4. ✅ **Bcrypt** securely hashes passwords with salt
5. ✅ **Middleware** protects routes and enforces access control
6. ✅ **Validation** prevents invalid/malicious input
7. ✅ **Rate Limiting** prevents brute-force attacks
8. ✅ **HTTPS** encrypts data in transit
9. ✅ **Environment Variables** keep secrets secure
10. ✅ **Task Ownership** ensures users only access their own data

---

## Module 11: Full-Stack Integration (Days 55-60)

### Day 55: Full-Stack Project Structure & Organization

**📖 Monorepo vs Separate Repositories**

**Separate Repositories** (Most Common for Learning):
```
my-github-account/
├── task-manager-frontend/  (React/Vue app)
└── task-manager-backend/   (Express API)
```

**Pros:**
- ✅ Independent deployment
- ✅ Different team can work on each
- ✅ Separate version control
- ✅ Easier to understand for beginners

**Cons:**
- ❌ Code duplication (types, constants)
- ❌ Harder to keep in sync
- ❌ Two repositories to manage

**Monorepo** (Professional Projects):
```
task-manager/
├── frontend/    (React/Vue app)
├── backend/     (Express API)
├── shared/      (shared types, utilities)
└── package.json (root - manages both)
```

**Pros:**
- ✅ Single source of truth
- ✅ Share code between front/back
- ✅ Easier to refactor
- ✅ Atomic commits across full stack

**Cons:**
- ❌ More complex setup
- ❌ Larger repository size
- ❌ Requires monorepo tools (Turborepo, Nx, Lerna)

---

**💡 Complete Monorepo Structure**

```
fullstack-task-manager/
├── .gitignore
├── README.md
├── package.json (root workspace)
│
├── backend/
│   ├── .env
│   ├── .env.example
│   ├── package.json
│   ├── config/
│   │   └── database.js
│   ├── models/
│   │   ├── User.js
│   │   └── Task.js
│   ├── routes/
│   │   ├── auth.js
│   │   └── tasks.js
│   ├── middleware/
│   │   ├── auth.js
│   │   ├── authorize.js
│   │   └── validation.js
│   ├── utils/
│   │   └── tokenUtils.js
│   └── server.js
│
├── frontend/
│   ├── .env
│   ├── .env.example
│   ├── package.json
│   ├── index.html
│   ├── vite.config.js
│   ├── src/
│   │   ├── main.js
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── TaskList.jsx
│   │   │   ├── TaskItem.jsx
│   │   │   └── TaskForm.jsx
│   │   ├── pages/
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   └── NotFound.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   ├── authService.js
│   │   │   └── taskService.js
│   │   ├── context/
│   │   │   └── AuthContext.jsx
│   │   ├── hooks/
│   │   │   └── useAuth.js
│   │   └── styles/
│   │       └── App.css
│
└── shared/
    ├── package.json
    ├── types/
    │   ├── User.ts
    │   └── Task.ts
    └── constants/
        └── status.js
```

**.gitignore:**
```gitignore
# Dependencies
node_modules/
**/node_modules/

# Environment variables
.env
.env.local
.env.production
**/.env
**/.env.local

# Build outputs
dist/
build/
**/dist/
**/build/

# Logs
*.log
npm-debug.log*
logs/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Database
*.sqlite
*.db
```

**Root package.json (Monorepo):**
```json
{
  "name": "fullstack-task-manager",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "frontend",
    "backend",
    "shared"
  ],
  "scripts": {
    "dev": "concurrently \"npm run dev:backend\" \"npm run dev:frontend\"",
    "dev:backend": "npm run dev --workspace=backend",
    "dev:frontend": "npm run dev --workspace=frontend",
    "install:all": "npm install && npm install --workspace=backend && npm install --workspace=frontend",
    "build": "npm run build --workspace=frontend",
    "start": "npm run start --workspace=backend"
  },
  "devDependencies": {
    "concurrently": "^8.0.0"
  }
}
```

**README.md:**
```markdown
# Full-Stack Task Manager

A complete task management application with authentication, built with React and Express.

## Tech Stack

### Frontend
- React 18
- Vite
- React Router
- Axios

### Backend
- Node.js
- Express
- PostgreSQL
- JWT Authentication
- Bcrypt

## Project Structure

```
├── frontend/   # React frontend application
├── backend/    # Express API server
└── shared/     # Shared types and constants
```

## Getting Started

### Prerequisites
- Node.js 18+
- PostgreSQL 14+
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fullstack-task-manager.git
cd fullstack-task-manager
```

2. Install dependencies:
```bash
npm run install:all
```

3. Set up environment variables:

**Backend (.env):**
```env
PORT=3000
DB_HOST=localhost
DB_NAME=taskmanager_db
DB_USER=postgres
DB_PASSWORD=yourpassword
JWT_SECRET=your-secret-key
```

**Frontend (.env):**
```env
VITE_API_URL=http://localhost:3000/api
```

4. Create database:
```bash
createdb taskmanager_db
psql taskmanager_db < backend/database/schema.sql
```

5. Run development servers:
```bash
npm run dev
```

Frontend: http://localhost:5173
Backend: http://localhost:3000

## API Documentation

### Authentication
- POST `/api/auth/register` - Register new user
- POST `/api/auth/login` - Login user
- GET `/api/auth/me` - Get current user (protected)

### Tasks
- GET `/api/tasks` - Get all user tasks (protected)
- POST `/api/tasks` - Create task (protected)
- PUT `/api/tasks/:id` - Update task (protected)
- DELETE `/api/tasks/:id` - Delete task (protected)
- GET `/api/tasks/stats` - Get task statistics (protected)

## Deployment

### Backend (Render)
1. Create new Web Service
2. Connect GitHub repository
3. Set build command: `cd backend && npm install`
4. Set start command: `cd backend && npm start`
5. Add environment variables

### Frontend (Vercel)
1. Connect GitHub repository
2. Set root directory: `frontend`
3. Framework preset: Vite
4. Add environment variables

## Features

- ✅ User authentication (register/login)
- ✅ JWT-based authorization
- ✅ Password hashing with bcrypt
- ✅ Create, read, update, delete tasks
- ✅ Task filtering by status
- ✅ Task statistics dashboard
- ✅ Responsive design
- ✅ Protected routes
- ✅ Error handling

## License

MIT
```

---

### Day 56: Connecting Frontend to Backend

**📖 CORS (Cross-Origin Resource Sharing)**

CORS is a security feature that controls which websites can access your API.

**Problem:**
```
Frontend: http://localhost:5173 (React)
Backend:  http://localhost:3000 (Express)

Browser blocks requests due to different origins!
```

**Solution - Configure CORS in Express:**

```javascript
const cors = require('cors');

// Allow specific origin
app.use(cors({
  origin: 'http://localhost:5173',
  credentials: true
}));

// Allow multiple origins
app.use(cors({
  origin: ['http://localhost:5173', 'https://myapp.vercel.app'],
  credentials: true
}));

// Allow all origins (DEV ONLY - not secure for production)
app.use(cors());
```

---

**💡 Frontend API Service Layer**

**src/services/api.js:**
```javascript
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:3000/api';

// Create axios instance
const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Request interceptor - Add token to all requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor - Handle errors globally
api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response) {
      // Server responded with error
      const message = error.response.data?.error || 'Something went wrong';
      
      // Handle 401 (unauthorized) - redirect to login
      if (error.response.status === 401) {
        localStorage.removeItem('token');
        window.location.href = '/login';
      }
      
      return Promise.reject(new Error(message));
    } else if (error.request) {
      // Request made but no response
      return Promise.reject(new Error('No response from server'));
    } else {
      // Something else went wrong
      return Promise.reject(error);
    }
  }
);

export default api;
```

**src/services/authService.js:**
```javascript
import api from './api';

export const authService = {
  async register(userData) {
    const response = await api.post('/auth/register', userData);
    if (response.data.token) {
      localStorage.setItem('token', response.data.token);
    }
    return response.data;
  },

  async login(credentials) {
    const response = await api.post('/auth/login', credentials);
    if (response.data.token) {
      localStorage.setItem('token', response.data.token);
    }
    return response.data;
  },

  async getCurrentUser() {
    const response = await api.get('/auth/me');
    return response.data.user;
  },

  logout() {
    localStorage.removeItem('token');
    window.location.href = '/login';
  },

  getToken() {
    return localStorage.getItem('token');
  },

  isAuthenticated() {
    return !!this.getToken();
  }
};
```

**src/services/taskService.js:**
```javascript
import api from './api';

export const taskService = {
  async getAllTasks(filters = {}) {
    const params = new URLSearchParams(filters).toString();
    const response = await api.get(`/tasks?${params}`);
    return response.data.tasks;
  },

  async getTask(id) {
    const response = await api.get(`/tasks/${id}`);
    return response.data.task;
  },

  async createTask(taskData) {
    const response = await api.post('/tasks', taskData);
    return response.data.task;
  },

  async updateTask(id, updates) {
    const response = await api.put(`/tasks/${id}`, updates);
    return response.data.task;
  },

  async deleteTask(id) {
    const response = await api.delete(`/tasks/${id}`);
    return response.data.task;
  },

  async getStats() {
    const response = await api.get('/tasks/stats');
    return response.data.stats;
  }
};
```

---

**💡 React Components with API Integration**

**src/pages/Dashboard.jsx:**
```javascript
import { useState, useEffect } from 'react';
import { taskService } from '../services/taskService';
import TaskList from '../components/TaskList';
import TaskForm from '../components/TaskForm';

function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('all');

  useEffect(() => {
    fetchTasks();
    fetchStats();
  }, [filter]);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const filters = filter !== 'all' ? { status: filter } : {};
      const data = await taskService.getAllTasks(filters);
      
      setTasks(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const fetchStats = async () => {
    try {
      const data = await taskService.getStats();
      setStats(data);
    } catch (err) {
      console.error('Failed to fetch stats:', err);
    }
  };

  const handleCreateTask = async (taskData) => {
    try {
      await taskService.createTask(taskData);
      fetchTasks();
      fetchStats();
    } catch (err) {
      alert('Failed to create task: ' + err.message);
    }
  };

  const handleUpdateTask = async (id, updates) => {
    try {
      await taskService.updateTask(id, updates);
      fetchTasks();
      fetchStats();
    } catch (err) {
      alert('Failed to update task: ' + err.message);
    }
  };

  const handleDeleteTask = async (id) => {
    if (!confirm('Are you sure you want to delete this task?')) return;
    
    try {
      await taskService.deleteTask(id);
      fetchTasks();
      fetchStats();
    } catch (err) {
      alert('Failed to delete task: ' + err.message);
    }
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading tasks...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <p>Error: {error}</p>
        <button onClick={fetchTasks}>Retry</button>
      </div>
    );
  }

  return (
    <div className="dashboard">
      <h1>Task Dashboard</h1>

      {/* Statistics */}
      {stats && (
        <div className="stats-grid">
          <div className="stat-card">
            <h3>{stats.total}</h3>
            <p>Total Tasks</p>
          </div>
          <div className="stat-card">
            <h3>{stats.pending}</h3>
            <p>Pending</p>
          </div>
          <div className="stat-card">
            <h3>{stats.in_progress}</h3>
            <p>In Progress</p>
          </div>
          <div className="stat-card">
            <h3>{stats.completed}</h3>
            <p>Completed</p>
          </div>
          <div className="stat-card overdue">
            <h3>{stats.overdue}</h3>
            <p>Overdue</p>
          </div>
        </div>
      )}

      {/* Filter */}
      <div className="filter-bar">
        <button
          className={filter === 'all' ? 'active' : ''}
          onClick={() => setFilter('all')}
        >
          All
        </button>
        <button
          className={filter === 'pending' ? 'active' : ''}
          onClick={() => setFilter('pending')}
        >
          Pending
        </button>
        <button
          className={filter === 'in_progress' ? 'active' : ''}
          onClick={() => setFilter('in_progress')}
        >
          In Progress
        </button>
        <button
          className={filter === 'completed' ? 'active' : ''}
          onClick={() => setFilter('completed')}
        >
          Completed
        </button>
      </div>

      {/* Task Form */}
      <TaskForm onSubmit={handleCreateTask} />

      {/* Task List */}
      <TaskList
        tasks={tasks}
        onUpdate={handleUpdateTask}
        onDelete={handleDeleteTask}
      />
    </div>
  );
}

export default Dashboard;
```

**src/components/TaskList.jsx:**
```javascript
import TaskItem from './TaskItem';

function TaskList({ tasks, onUpdate, onDelete }) {
  if (tasks.length === 0) {
    return (
      <div className="empty-state">
        <p>No tasks found. Create your first task!</p>
      </div>
    );
  }

  return (
    <div className="task-list">
      {tasks.map(task => (
        <TaskItem
          key={task.id}
          task={task}
          onUpdate={onUpdate}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}

export default TaskList;
```

**src/components/TaskItem.jsx:**
```javascript
import { useState } from 'react';

function TaskItem({ task, onUpdate, onDelete }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editedTitle, setEditedTitle] = useState(task.title);
  const [editedDescription, setEditedDescription] = useState(task.description);

  const handleSave = () => {
    onUpdate(task.id, {
      title: editedTitle,
      description: editedDescription
    });
    setIsEditing(false);
  };

  const handleStatusChange = (newStatus) => {
    onUpdate(task.id, { status: newStatus });
  };

  if (isEditing) {
    return (
      <div className="task-item editing">
        <input
          type="text"
          value={editedTitle}
          onChange={(e) => setEditedTitle(e.target.value)}
        />
        <textarea
          value={editedDescription}
          onChange={(e) => setEditedDescription(e.target.value)}
        />
        <div className="task-actions">
          <button onClick={handleSave}>Save</button>
          <button onClick={() => setIsEditing(false)}>Cancel</button>
        </div>
      </div>
    );
  }

  return (
    <div className={`task-item ${task.status}`}>
      <div className="task-content">
        <h3>{task.title}</h3>
        <p>{task.description}</p>
        <div className="task-meta">
          <span className={`badge priority-${task.priority}`}>
            {task.priority}
          </span>
          <span className={`badge status-${task.status}`}>
            {task.status.replace('_', ' ')}
          </span>
        </div>
      </div>
      
      <div className="task-actions">
        <select
          value={task.status}
          onChange={(e) => handleStatusChange(e.target.value)}
        >
          <option value="pending">Pending</option>
          <option value="in_progress">In Progress</option>
          <option value="completed">Completed</option>
        </select>
        <button onClick={() => setIsEditing(true)}>Edit</button>
        <button onClick={() => onDelete(task.id)} className="delete">
          Delete
        </button>
      </div>
    </div>
  );
}

export default TaskItem;
```

---

**📚 Interview Questions & Answers**

**Q1: What is CORS and why is it important?**

**Answer:**
CORS (Cross-Origin Resource Sharing) is a security feature that controls which websites can access your API.

**Problem:**
By default, browsers block requests from one origin (domain) to another for security.

```
Frontend: http://localhost:5173
Backend:  http://localhost:3000
❌ Browser blocks this - different origins!
```

**Solution:**
Configure CORS on the backend:

```javascript
app.use(cors({
  origin: 'http://localhost:5173',  // Allow this origin
  credentials: true  // Allow cookies
}));
```

**Why important:**
- Prevents malicious websites from accessing your API
- Protects user data
- Required for frontend-backend communication

**Q2: Difference between Fetch and Axios?**

**Answer:**

**Fetch (Built-in):**
```javascript
// Fetch
fetch('http://localhost:3000/api/tasks', {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${token}`
  }
})
  .then(res => res.json())  // Must manually parse JSON
  .then(data => console.log(data))
  .catch(err => console.error(err));
```

**Axios (Library):**
```javascript
// Axios
axios.get('http://localhost:3000/api/tasks', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
})
  .then(res => console.log(res.data))  // Auto-parses JSON
  .catch(err => console.error(err));
```

**Comparison:**

| Feature | Fetch | Axios |
|---------|-------|-------|
| Built-in | ✅ Yes | ❌ No (needs install) |
| JSON parsing | Manual | Automatic |
| Interceptors | ❌ No | ✅ Yes |
| Timeout | ❌ No | ✅ Yes |
| Cancel requests | ❌ Complex | ✅ Easy |
| Error handling | Only network errors | All errors |
| Browser support | Modern only | IE11+ |

**Axios advantages:**
- Interceptors (add token automatically)
- Better error handling
- Request cancellation
- Timeout support

**Q3: How do you handle API errors in frontend?**

**Answer:**

**1. Try-Catch with Async/Await:**
```javascript
async function fetchTasks() {
  try {
    const response = await api.get('/tasks');
    setTasks(response.data.tasks);
    setError(null);
  } catch (error) {
    setError(error.message);
    console.error('Failed to fetch tasks:', error);
  }
}
```

**2. Loading States:**
```javascript
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);

try {
  setLoading(true);
  setError(null);
  const data = await api.get('/tasks');
  setTasks(data);
} catch (err) {
  setError(err.message);
} finally {
  setLoading(false);  // Always runs
}
```

**3. User-Friendly Messages:**
```javascript
// Display error to user
{error && (
  <div className="error-banner">
    <p>{error}</p>
    <button onClick={retry}>Retry</button>
  </div>
)}
```

**4. Global Error Handler (Axios Interceptor):**
```javascript
api.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401) {
      // Redirect to login
      window.location.href = '/login';
    } else if (error.response?.status === 500) {
      alert('Server error. Please try again later.');
    }
    return Promise.reject(error);
  }
);
```

**5. Toast Notifications:**
```javascript
import { toast } from 'react-toastify';

try {
  await api.post('/tasks', taskData);
  toast.success('Task created successfully!');
} catch (error) {
  toast.error(error.message);
}
```

---

**🔑 Key Takeaways - Full-Stack Integration**

1. ✅ **CORS** must be configured for frontend-backend communication
2. ✅ **Service Layer** centralizes all API calls
3. ✅ **Axios Interceptors** automatically add tokens to requests
4. ✅ **Error Handling** provides user-friendly feedback
5. ✅ **Loading States** improve user experience
6. ✅ **Environment Variables** store API URLs
7. ✅ **Try-Catch** handles async errors gracefully

---

### Day 57: Authentication UI & Protected Routes

**📖 Authentication Context (React)**

Create a central authentication state accessible to all components.

**src/context/AuthContext.jsx:**
```javascript
import { createContext, useState, useEffect, useContext } from 'react';
import { authService } from '../services/authService';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      if (authService.isAuthenticated()) {
        const userData = await authService.getCurrentUser();
        setUser(userData);
      }
    } catch (err) {
      console.error('Auth check failed:', err);
      authService.logout();
    } finally {
      setLoading(false);
    }
  };

  const login = async (credentials) => {
    try {
      setError(null);
      const response = await authService.login(credentials);
      setUser(response.user);
      return response;
    } catch (err) {
      setError(err.message);
      throw err;
    }
  };

  const register = async (userData) => {
    try {
      setError(null);
      const response = await authService.register(userData);
      setUser(response.user);
      return response;
    } catch (err) {
      setError(err.message);
      throw err;
    }
  };

  const logout = () => {
    authService.logout();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout, loading, error }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};
```

**src/main.jsx:**
```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import App from './App';
import './styles/App.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
```

---

**💡 Login & Register Pages**

**src/pages/Login.jsx:**
```javascript
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function Login() {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await login(formData);
      navigate('/dashboard');  // Redirect after successful login
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2>Login</h2>
        
        {error && (
          <div className="error-banner">
            <p>{error}</p>
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              disabled={loading}
            />
          </div>

          <button type="submit" disabled={loading}>
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </form>

        <p className="auth-link">
          Don't have an account? <Link to="/register">Register here</Link>
        </p>
      </div>
    </div>
  );
}

export default Login;
```

**src/pages/Register.jsx:**
```javascript
import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function Register() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    firstName: '',
    lastName: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    // Validate passwords match
    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    // Validate password strength
    if (formData.password.length < 6) {
      setError('Password must be at least 6 characters');
      return;
    }

    setLoading(true);

    try {
      await register({
        email: formData.email,
        password: formData.password,
        firstName: formData.firstName,
        lastName: formData.lastName
      });
      navigate('/dashboard');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2>Register</h2>
        
        {error && (
          <div className="error-banner">
            <p>{error}</p>
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="firstName">First Name</label>
              <input
                type="text"
                id="firstName"
                name="firstName"
                value={formData.firstName}
                onChange={handleChange}
                required
                disabled={loading}
              />
            </div>

            <div className="form-group">
              <label htmlFor="lastName">Last Name</label>
              <input
                type="text"
                id="lastName"
                name="lastName"
                value={formData.lastName}
                onChange={handleChange}
                required
                disabled={loading}
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              disabled={loading}
              minLength="6"
            />
          </div>

          <div className="form-group">
            <label htmlFor="confirmPassword">Confirm Password</label>
            <input
              type="password"
              id="confirmPassword"
              name="confirmPassword"
              value={formData.confirmPassword}
              onChange={handleChange}
              required
              disabled={loading}
            />
          </div>

          <button type="submit" disabled={loading}>
            {loading ? 'Creating account...' : 'Register'}
          </button>
        </form>

        <p className="auth-link">
          Already have an account? <Link to="/login">Login here</Link>
        </p>
      </div>
    </div>
  );
}

export default Register;
```

---

**💡 Protected Routes**

**src/components/ProtectedRoute.jsx:**
```javascript
import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default ProtectedRoute;
```

**src/App.jsx:**
```javascript
import { Routes, Route, Navigate } from 'react-router-dom';
import { useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import NotFound from './pages/NotFound';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  return (
    <div className="app">
      {user && <Navbar />}
      
      <Routes>
        {/* Public routes */}
        <Route
          path="/login"
          element={user ? <Navigate to="/dashboard" /> : <Login />}
        />
        <Route
          path="/register"
          element={user ? <Navigate to="/dashboard" /> : <Register />}
        />

        {/* Protected routes */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />

        {/* Redirect root to dashboard or login */}
        <Route
          path="/"
          element={<Navigate to={user ? "/dashboard" : "/login"} />}
        />

        {/* 404 */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
```

**src/components/Navbar.jsx:**
```javascript
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav className="navbar">
      <div className="nav-brand">
        <Link to="/dashboard">Task Manager</Link>
      </div>

      <div className="nav-user">
        <span>Hello, {user?.first_name}!</span>
        <button onClick={logout} className="logout-btn">
          Logout
        </button>
      </div>
    </nav>
  );
}

export default Navbar;
```

---

**📚 Interview Questions & Answers**

**Q1: Where should you store JWT tokens in frontend?**

**Answer:**

**Options:**

**1. LocalStorage (Common but has security risk):**
```javascript
localStorage.setItem('token', token);
const token = localStorage.getItem('token');
localStorage.removeItem('token');
```

**Pros:** Simple, persists across tabs/refreshes
**Cons:** ❌ Vulnerable to XSS attacks (JavaScript can access)

**2. SessionStorage:**
```javascript
sessionStorage.setItem('token', token);
```

**Pros:** Cleared when tab closes
**Cons:** ❌ Same XSS vulnerability, doesn't persist

**3. HttpOnly Cookie (MOST SECURE):**
```javascript
// Server sets cookie
res.cookie('token', jwt, {
  httpOnly: true,  // JavaScript cannot access
  secure: true,    // HTTPS only
  sameSite: 'strict'
});
```

**Pros:** ✅ JavaScript cannot access, ✅ Secure
**Cons:** Requires CSRF protection

**4. Memory (JavaScript variable):**
```javascript
let token = null;  // Lost on refresh
```

**Pros:** ✅ Most secure (no persistence)
**Cons:** ❌ Lost on page refresh

**Best Practice:**
- Development: localStorage (simple)
- Production: HttpOnly cookie + refresh token

**Q2: How do you implement protected routes in React?**

**Answer:**

**Step 1: Create ProtectedRoute component**
```javascript
function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();

  if (loading) return <LoadingSpinner />;
  if (!user) return <Navigate to="/login" />;
  
  return children;
}
```

**Step 2: Wrap protected pages**
```javascript
<Routes>
  <Route path="/login" element={<Login />} />
  
  <Route
    path="/dashboard"
    element={
      <ProtectedRoute>
        <Dashboard />
      </ProtectedRoute>
    }
  />
</Routes>
```

**Step 3: Auth context provides user state**
```javascript
const AuthContext = createContext();

function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  
  // Check if user is logged in
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      fetchUser();  // Get user from backend
    }
  }, []);
  
  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
```

**Q3: What is token refresh and why is it needed?**

**Answer:**

**Problem:**
- Access tokens expire quickly (15 min - 1 hour) for security
- User would have to login again every hour ❌

**Solution: Refresh Token**
- Access token: Short-lived (15 min)
- Refresh token: Long-lived (7-30 days)
- When access token expires, use refresh token to get new one

**Flow:**
```
1. Login → Get access token (15 min) + refresh token (7 days)
2. Use access token for API calls
3. Access token expires after 15 min
4. Call /refresh endpoint with refresh token
5. Get new access token (15 min)
6. Continue making API calls
7. Repeat until refresh token expires (7 days)
8. User must login again
```

**Implementation:**
```javascript
// Backend: Refresh endpoint
app.post('/api/auth/refresh', async (req, res) => {
  const { refreshToken } = req.body;
  
  try {
    // Verify refresh token
    const decoded = jwt.verify(refreshToken, REFRESH_SECRET);
    
    // Check if refresh token is in database (not revoked)
    const isValid = await checkRefreshToken(decoded.userId, refreshToken);
    if (!isValid) {
      return res.status(403).json({ error: 'Invalid refresh token' });
    }
    
    // Generate new access token
    const accessToken = jwt.sign(
      { userId: decoded.userId },
      ACCESS_SECRET,
      { expiresIn: '15m' }
    );
    
    res.json({ accessToken });
  } catch (error) {
    res.status(403).json({ error: 'Invalid refresh token' });
  }
});

// Frontend: Axios interceptor for automatic refresh
api.interceptors.response.use(
  response => response,
  async (error) => {
    const originalRequest = error.config;
    
    // If access token expired
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        // Get new access token using refresh token
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await axios.post('/api/auth/refresh', { refreshToken });
        
        // Save new access token
        const newAccessToken = response.data.accessToken;
        localStorage.setItem('token', newAccessToken);
        
        // Retry original request with new token
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
        return api(originalRequest);
      } catch (refreshError) {
        // Refresh failed - redirect to login
        localStorage.clear();
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }
    
    return Promise.reject(error);
  }
);
```

---

### Day 58-59: Deployment

**📖 Backend Deployment (Render)**

**Step 1: Prepare for deployment**

**package.json:**
```json
{
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}
```

**.env.example:**
```env
PORT=3000
DB_HOST=your-db-host
DB_PORT=5432
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
JWT_SECRET=your-jwt-secret
NODE_ENV=production
```

**Step 2: Deploy to Render**

1. Create account at https://render.com
2. Click "New +" → "Web Service"
3. Connect GitHub repository
4. Configure:
   - **Name:** task-manager-api
   - **Region:** Choose nearest
   - **Branch:** main
   - **Root Directory:** (leave empty or specify `backend` if monorepo)
   - **Build Command:** `npm install`
   - **Start Command:** `npm start`
5. Add environment variables (from .env.example)
6. Click "Create Web Service"

**Step 3: Database (PostgreSQL on Render)**

1. Click "New +" → "PostgreSQL"
2. Configure database
3. Copy connection string
4. Add to backend environment variables:
   - `DB_HOST`
   - `DB_PORT`
   - `DB_NAME`
   - `DB_USER`
   - `DB_PASSWORD`

**Step 4: Run migrations**

```bash
# Connect to production database
psql <connection-string>

# Run schema
\i database/schema.sql
```

---

**📖 Frontend Deployment (Vercel)**

**Step 1: Prepare for deployment**

**.env.production:**
```env
VITE_API_URL=https://your-backend.onrender.com/api
```

**vite.config.js:**
```javascript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist'
  }
});
```

**Step 2: Deploy to Vercel**

1. Create account at https://vercel.com
2. Click "Add New" → "Project"
3. Import GitHub repository
4. Configure:
   - **Framework Preset:** Vite
   - **Root Directory:** (leave empty or specify `frontend` if monorepo)
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
5. Add environment variables:
   - `VITE_API_URL`: `https://your-backend.onrender.com/api`
6. Click "Deploy"

**Step 3: Update backend CORS**

```javascript
app.use(cors({
  origin: [
    'http://localhost:5173',  // Development
    'https://your-app.vercel.app'  // Production
  ],
  credentials: true
}));
```

---

**📚 Interview Questions & Answers**

**Q1: What are important considerations for production deployment?**

**Answer:**

**1. Environment Variables:**
- Never commit secrets to Git
- Use platform's environment variable system
- Different values for dev/staging/production

**2. Database:**
- Use production-grade database (not SQLite)
- Enable SSL connections
- Regular backups
- Connection pooling

**3. Security:**
- HTTPS only
- Security headers (helmet.js)
- Rate limiting
- Input validation
- CORS configuration

**4. Error Handling:**
- Don't expose stack traces in production
- Log errors to monitoring service
- User-friendly error messages

**5. Performance:**
- Enable gzip compression
- CDN for static assets
- Database indexing
- Caching where appropriate

**6. Monitoring:**
- Error tracking (Sentry)
- Performance monitoring
- Uptime monitoring
- Log aggregation

**Example production configuration:**
```javascript
const express = require('express');
const helmet = require('helmet');
const compression = require('compression');

const app = express();

// Security headers
app.use(helmet());

// Gzip compression
app.use(compression());

// Trust proxy (for rate limiting, IP detection)
app.set('trust proxy', 1);

// Error handler
app.use((err, req, res, next) => {
  // Log error
  console.error(err);
  
  // Don't expose error details in production
  res.status(500).json({
    error: process.env.NODE_ENV === 'production'
      ? 'Internal server error'
      : err.message
  });
});
```

**Q2: What is CI/CD?**

**Answer:**

**CI/CD** = Continuous Integration / Continuous Deployment

**Continuous Integration (CI):**
- Automatically test code when pushed to Git
- Ensures code works before merging
- Runs tests, linters, type checking

**Continuous Deployment (CD):**
- Automatically deploy code after tests pass
- No manual deployment steps
- Fast, reliable releases

**Example workflow (GitHub Actions):**

**.github/workflows/deploy.yml:**
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Vercel
        run: vercel --prod
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
```

**Benefits:**
- ✅ Catch bugs early
- ✅ Faster deployments
- ✅ Consistent process
- ✅ Less human error

---

### Day 60: Final Full-Stack Project Summary

**🎯 Complete Task Manager Application**

You've now built a complete full-stack application with:

**Backend (Express + PostgreSQL):**
- ✅ RESTful API design
- ✅ JWT authentication
- ✅ Password hashing (bcrypt)
- ✅ User registration & login
- ✅ Protected routes
- ✅ CRUD operations
- ✅ Input validation
- ✅ Error handling
- ✅ Security best practices
- ✅ Database relationships
- ✅ Deployed to production

**Frontend (React):**
- ✅ React components & hooks
- ✅ React Router navigation
- ✅ Authentication context
- ✅ Protected routes
- ✅ Login/Register forms
- ✅ Task CRUD interface
- ✅ Loading states
- ✅ Error handling
- ✅ Responsive design
- ✅ API integration
- ✅ Deployed to production

**Skills Demonstrated:**
1. **Frontend:** React, routing, state management, API calls, form handling
2. **Backend:** Express, authentication, database, security, REST APIs
3. **Database:** PostgreSQL, relationships, queries, indexes
4. **Security:** JWT, bcrypt, input validation, CORS, rate limiting
5. **DevOps:** Environment variables, deployment, CI/CD concepts
6. **Full-Stack:** Complete application from database to UI

---

**🔑 Key Takeaways - Complete Full-Stack Module**

1. ✅ **Monorepo** organizes frontend + backend in one repository
2. ✅ **CORS** enables frontend-backend communication
3. ✅ **Service Layer** centralizes API calls
4. ✅ **Auth Context** manages authentication state globally
5. ✅ **Protected Routes** restrict access to authenticated users
6. ✅ **Token Refresh** keeps users logged in securely
7. ✅ **Environment Variables** separate config from code
8. ✅ **Deployment** makes your app accessible to the world
9. ✅ **CI/CD** automates testing and deployment
10. ✅ **Error Handling** provides great user experience

---

## 🚀 Bootcamp Projects

### Project 1: Responsive Portfolio Website
**Skills:** HTML, CSS, Flexbox, Grid, Media Queries, Tailwind/Bootstrap

**Requirements:**
- Responsive for desktop, tablet, mobile
- Navigation bar with section links
- Hero section with CTA
- About section
- Project gallery (CSS Grid/Flexbox)
- Contact form with validation
- Accessibility features
- Smooth scrolling
- Animations (optional)
- Dark mode toggle (stretch goal)

---

### Project 2: To-Do List App
**Skills:** JavaScript, DOM Manipulation, Arrays, Objects, Events

**Requirements:**
- Add tasks dynamically
- Mark tasks as complete/incomplete
- Delete tasks
- Edit tasks
- Filter tasks (all, completed, pending)
- Persist in localStorage
- Search functionality
- Due dates (stretch goal)

---

### Project 3: Weather App
**Skills:** Fetch API, Async/Await, JavaScript, CSS, TypeScript (optional)

**Requirements:**
- Search weather by city
- Display current weather:
  - Temperature
  - Humidity
  - Wind speed
  - Weather icon
  - Conditions
- Convert Celsius ↔ Fahrenheit
- 5-day forecast (stretch goal)
- Geolocation (stretch goal)
- TypeScript implementation (bonus)

**API:** OpenWeatherMap API or WeatherAPI

---

### Project 4: Blog Application
**Skills:** Node.js, Express, EJS/Handlebars, Routing, Middleware

**Requirements:**
- Dynamic routes for posts
- Modular routing (Express Router)
- Serve static files
- EJS templating with layouts
- View all posts
- View single post
- Add new post (admin form)
- Edit and delete posts
- Error handling (404 pages)
- Search functionality (stretch goal)

---

### Project 5: Full-Stack Task Manager
**Skills:** Node.js, Express, REST API, JWT, Fetch API, Deployment

**Requirements:**

**Backend:**
- RESTful API with Express
- JWT authentication
- CRUD operations for tasks
- bcrypt password hashing
- User-specific tasks
- Input validation
- Error handling
- Deployed on Render/Railway

**Frontend:**
- Login/Signup UI
- Task dashboard
- Add/Edit/Delete tasks
- Mark complete/incomplete
- Filter and search
- Responsive design
- localStorage for token
- Deployed on Vercel/Netlify

**Stretch Goals:**
- Real-time updates (WebSockets)
- Role-based access control
- Task categories/tags
- Due dates and reminders
- File attachments

---

## 📝 Interview Preparation Guide

### HTML Interview Questions

**Basic:**
1. What is the difference between HTML and XHTML?
2. What are meta tags and their uses?
3. What is the difference between `<span>` and `<div>`?
4. Explain semantic HTML with examples.
5. What is the purpose of the DOCTYPE declaration?

**Intermediate:**
1. How do HTML5 form validations work?
2. What are data attributes?
3. Explain the difference between SVG and Canvas.
4. What is the purpose of the `<picture>` element?
5. How do you optimize images for the web?

**Advanced:**
1. Explain Web Components.
2. What is Shadow DOM?
3. How does the browser render HTML?
4. Explain Critical Rendering Path.
5. What are Progressive Web Apps (PWA)?

---

### CSS Interview Questions

**Basic:**
1. What is the box model?
2. Difference between margin and padding?
3. What are CSS selectors? List different types.
4. Explain specificity in CSS.
5. What is the cascade in CSS?

**Intermediate:**
1. Difference between absolute, relative, fixed, and sticky positioning?
2. What are pseudo-classes and pseudo-elements?
3. Explain Flexbox vs Grid.
4. What are CSS variables (custom properties)?
5. How do you create responsive designs?

**Advanced:**
1. What is CSS-in-JS?
2. Explain CSS architecture (BEM, SMACSS, OOCSS).
3. What are CSS preprocessors (SASS, LESS)?
4. How do you optimize CSS performance?
5. Explain CSS animations vs transitions.

---

### JavaScript Interview Questions

**Basic:**
1. What are the primitive data types in JavaScript?
2. Difference between `==` and `===`?
3. What is hoisting?
4. Explain closures.
5. What is the event loop?

**Intermediate:**
1. Difference between `var`, `let`, and `const`?
2. What are arrow functions and their differences?
3. Explain promises and async/await.
4. What is destructuring?
5. What are higher-order functions?

**Advanced:**
1. Explain prototypal inheritance.
2. What is the JavaScript execution context?
3. What are generators and iterators?
4. Explain event delegation.
5. What is memoization?

---

### Node.js Interview Questions

**Basic:**
1. What is Node.js?
2. What is the event-driven architecture?
3. What is NPM?
4. Explain the require() function.
5. What is package.json?

**Intermediate:**
1. What is the difference between Node.js and browser JavaScript?
2. Explain callbacks, promises, and async/await.
3. What is middleware in Express?
4. How do you handle errors in Node.js?
5. What is the event emitter?

**Advanced:**
1. Explain the Node.js event loop.
2. What is clustering in Node.js?
3. How do you prevent callback hell?
4. What are streams in Node.js?
5. Explain memory leaks and how to prevent them.

---

### Express.js Interview Questions

1. What is Express.js?
2. Difference between app.use() and app.get()?
3. What is middleware?
4. How do you handle errors in Express?
5. What is Express Router?
6. Explain template engines.
7. How do you serve static files?
8. What is CORS and how do you enable it?
9. Explain request and response objects.
10. How do you implement authentication in Express?

---

### TypeScript Interview Questions

1. What is TypeScript?
2. Advantages of TypeScript over JavaScript?
3. What are interfaces?
4. Difference between interface and type?
5. What are generics?
6. What is type inference?
7. Explain enums.
8. What are decorators?
9. What is the difference between any and unknown?
10. How do you configure TypeScript?

---

### Authentication & Security Questions

1. What is authentication vs authorization?
2. What is JWT?
3. How does JWT work?
4. Where should you store tokens?
5. What is bcrypt?
6. Explain password hashing and salting.
7. What is HTTPS and SSL/TLS?
8. What is CSRF?
9. What is XSS?
10. What are security best practices?

---

### API & REST Questions

1. What is a RESTful API?
2. What are HTTP methods (GET, POST, PUT, DELETE, PATCH)?
3. What are status codes? List common ones.
4. What is the difference between PUT and PATCH?
5. What is API versioning?
6. What is rate limiting?
7. How do you handle CORS?
8. What is API documentation (Swagger/OpenAPI)?
9. What are webhooks?
10. GraphQL vs REST?

---

### Deployment & DevOps Questions

1. What is CI/CD?
2. What is Docker?
3. What is containerization?
4. What are environment variables?
5. How do you deploy a Node.js app?
6. What is load balancing?
7. What is caching?
8. What is CDN?
9. What are microservices?
10. What is serverless architecture?

---

## 🎯 Tips for Success

### Learning Tips:
1. **Practice Daily** - Code every day, even if just for 30 minutes
2. **Build Projects** - Apply concepts immediately in real projects
3. **Debug Actively** - Don't just copy-paste, understand why code works
4. **Read Documentation** - MDN, official docs are your best friends
5. **Join Communities** - Stack Overflow, Reddit, Discord servers

### Interview Preparation:
1. **Master Fundamentals** - Strong basics are crucial
2. **Practice Coding** - LeetCode, HackerRank for algorithms
3. **Build Portfolio** - Showcase 3-5 solid projects
4. **Contribute to Open Source** - Shows collaboration skills
5. **Mock Interviews** - Practice with friends or platforms like Pramp

### Project Best Practices:
1. **Version Control** - Use Git from day one
2. **Clean Code** - Follow naming conventions and best practices
3. **Documentation** - README, code comments
4. **Testing** - Write tests for critical functionality
5. **Responsive Design** - Mobile-first approach

---

## 📚 Additional Resources

### Documentation:
- [MDN Web Docs](https://developer.mozilla.org/)
- [Node.js Documentation](https://nodejs.org/docs/)
- [Express.js Guide](https://expressjs.com/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

### Learning Platforms:
- [freeCodeCamp](https://www.freecodecamp.org/)
- [The Odin Project](https://www.theodinproject.com/)
- [JavaScript.info](https://javascript.info/)
- [Node School](https://nodeschool.io/)

### YouTube Channels:
- Traversy Media
- Web Dev Simplified
- Fireship
- The Net Ninja
- Academind

### Practice Platforms:
- [Frontend Mentor](https://www.frontendmentor.io/)
- [LeetCode](https://leetcode.com/)
- [CodeWars](https://www.codewars.com/)
- [HackerRank](https://www.hackerrank.com/)

---

## ✅ Checklist for Full-Stack Readiness

### Frontend:
- [ ] HTML5 semantic markup
- [ ] CSS Grid and Flexbox
- [ ] Responsive design
- [ ] JavaScript ES6+
- [ ] DOM manipulation
- [ ] Fetch API / Axios
- [ ] Local storage
- [ ] Form validation
- [ ] Accessibility (a11y)

### Backend:
- [ ] Node.js fundamentals
- [ ] Express.js
- [ ] RESTful API design
- [ ] Middleware
- [ ] Authentication (JWT)
- [ ] Password hashing (bcrypt)
- [ ] Error handling
- [ ] File operations
- [ ] Environment variables

### Database (Optional):
- [ ] MongoDB or PostgreSQL
- [ ] CRUD operations
- [ ] Schema design
- [ ] Queries and aggregation

### DevOps:
- [ ] Git and GitHub
- [ ] Deploy backend (Render/Railway)
- [ ] Deploy frontend (Vercel/Netlify)
- [ ] Environment configuration
- [ ] Basic CI/CD

### Soft Skills:
- [ ] Problem-solving
- [ ] Debugging skills
- [ ] Code organization
- [ ] Documentation
- [ ] Communication

---

**Good luck with your Full-Stack Developer journey! 🚀**

Remember: Consistency is key. Code every day, build projects, and never stop learning!

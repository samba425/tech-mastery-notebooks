# 🚀 Tech Mastery Platform - Web Application

A beautiful, modern web application to browse and search all your technical learning guides in one place, inspired by platforms like MissionCompile.

## ✨ Features

- **📚 Organized Navigation** - All guides categorized by topic (Programming, AI/ML, DevOps, etc.)
- **🔍 Full-Text Search** - Search across all documentation
- **🎨 Modern UI** - Clean, responsive design with dark mode support
- **💻 Code Highlighting** - Syntax highlighting for all programming languages
- **📱 Mobile Friendly** - Works perfectly on all devices
- **⚡ Fast & Responsive** - Built with Next.js for optimal performance

## 🛠️ Tech Stack

- **Framework:** Next.js 14 (React)
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Markdown:** react-markdown with GitHub Flavored Markdown
- **Syntax Highlighting:** highlight.js
- **Icons:** Lucide React

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ installed
- npm or yarn

### Installation

1. **Navigate to the web-app directory:**
   ```bash
   cd web-app
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

That's it! You should now see your Tech Mastery Platform running locally.

## 📖 Usage

### Navigation
- Click on any category in the sidebar to expand it
- Click on a guide to view its content
- Use the search bar to find specific topics

### Search
- Type in the search bar at the top
- Results will filter in real-time in the sidebar

### Reading
- All markdown is beautifully rendered
- Code blocks have syntax highlighting
- Tables, lists, and images are properly formatted

## 🏗️ Project Structure

```
web-app/
├── app/
│   ├── api/
│   │   └── content/
│   │       └── route.ts          # API endpoint for content
│   ├── layout.tsx                # Root layout
│   ├── page.tsx                  # Home page
│   └── globals.css              # Global styles
├── components/
│   ├── Header.tsx               # Top navigation bar
│   ├── Sidebar.tsx              # Side navigation
│   └── ContentViewer.tsx        # Markdown renderer
├── lib/
│   └── contentLoader.ts         # Content loading logic
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.js
```

## 🎨 Customization

### Adding New Content

All content is automatically loaded from the parent directories. To add new guides:

1. Add your markdown file to the appropriate directory (e.g., `guides/`, `guides/ai_ml/`)
2. Update `lib/contentLoader.ts` to include the new file in the content structure
3. The guide will automatically appear in the sidebar!

### Changing Colors

Edit `tailwind.config.ts` to customize the color scheme:

```typescript
colors: {
  primary: {
    // Your custom colors here
  }
}
```

### Modifying Layout

- **Header:** Edit `components/Header.tsx`
- **Sidebar:** Edit `components/Sidebar.tsx`
- **Content Area:** Edit `components/ContentViewer.tsx`

## 📦 Building for Production

```bash
# Build the application
npm run build

# Start the production server
npm start
```

## 🚀 Deployment Options

### Vercel (Recommended)

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Deploy with one click!

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

### Netlify

```bash
npm run build
# Deploy the .next folder
```

### Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

### Static Export (Optional)

For static hosting:

1. Update `next.config.js`:
   ```javascript
   output: 'export'
   ```
2. Run `npm run build`
3. Deploy the `out` folder to any static host

## 🔧 Configuration

### Content Structure

Edit `lib/contentLoader.ts` to modify:
- Content organization
- Categories
- Badges
- Read time estimates
- File paths

### Markdown Features

Supports:
- ✅ Headers (H1-H6)
- ✅ Bold, italic, strikethrough
- ✅ Code blocks with syntax highlighting
- ✅ Tables
- ✅ Lists (ordered & unordered)
- ✅ Links and images
- ✅ Blockquotes
- ✅ GitHub Flavored Markdown

## 🐛 Troubleshooting

### Port 3000 already in use?

```bash
# Use a different port
PORT=3001 npm run dev
```

### Content not loading?

Check that the file paths in `lib/contentLoader.ts` are correct relative to the `web-app` directory.

### Styling issues?

```bash
# Clear Next.js cache
rm -rf .next
npm run dev
```

## 📝 License

This project is part of the Tech Mastery Notebooks repository.

## 🤝 Contributing

Feel free to:
- Add new features
- Improve the UI
- Fix bugs
- Add more content categories

## 📧 Support

If you encounter any issues, please check:
1. Node.js version (18+)
2. All dependencies installed (`npm install`)
3. File paths in `contentLoader.ts`

## 🎯 Roadmap

- [ ] Add bookmark/favorites functionality
- [ ] Progress tracking
- [ ] Code playground integration
- [ ] PDF export
- [ ] Multi-language support
- [ ] Interactive quizzes

---

**Built with ❤️ for learning and knowledge sharing**

Happy Learning! 🚀

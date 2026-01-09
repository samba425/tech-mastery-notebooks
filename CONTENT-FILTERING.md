# Content Filtering Feature

## Overview
The web app now supports URL-based content filtering to control which sections appear in the left sidebar navigation.

## How It Works

### Default View (Hidden Sections)
When you visit: `https://samba425.github.io/tech-mastery-notebooks`

**The following sections are HIDDEN by default:**
- ☁️ DevOps & Infrastructure
- 🏗️ Infrastructure Notebooks
- 🎯 System Design
- 💪 Programming Challenges
- 💼 Career Development
- 🎓 Python Teaching Curriculum
- 📚 Additional Resources

**Visible sections include:**
- 🏠 Welcome & Getting Started
- 🚀 Quick Start Guide
- 💻 Programming Languages
- 📊 Data Structures & Algorithms
- 🤖 AI/ML & Data Science

### Show All Sections
To view ALL content sections, use either:
1. `https://samba425.github.io/tech-mastery-notebooks?all=true`
2. `https://samba425.github.io/tech-mastery-notebooks/all` (if route configured)

### User Interface
When sections are hidden, users will see a helpful button in the sidebar:
- **"Show All Sections"** button
- Clicking it adds `?all=true` to the URL
- This reveals all hidden sections

## Implementation Details

### Files Modified
1. **`web-app/app/page.tsx`**
   - Added `useSearchParams()` to detect URL parameters
   - Added `HIDDEN_SECTION_IDS` array to define hidden sections
   - Wrapped component in `Suspense` boundary (Next.js requirement)
   - Filters `contentStructure` based on URL parameter

2. **`web-app/components/Sidebar.tsx`**
   - Added `showAllSectionsHint` prop
   - Displays UI hint when sections are hidden
   - Button to enable "show all" mode

### Configuration
To modify which sections are hidden, edit the `HIDDEN_SECTION_IDS` array in `web-app/app/page.tsx`:

```typescript
const HIDDEN_SECTION_IDS = [
  'devops',
  'infrastructure-notebooks', 
  'system-design',
  'programming-challenges',
  'career',
  'teaching',
  'extras'
]
```

## Benefits
- ✅ Cleaner default view for new users
- ✅ Easy access to all content via URL parameter
- ✅ Better user experience with progressive disclosure
- ✅ Maintains full content accessibility
- ✅ No content is permanently hidden

## Testing
1. **Default view**: Visit base URL - should show limited sections
2. **All view**: Add `?all=true` - should show all sections
3. **Button**: Click "Show All Sections" - URL should update

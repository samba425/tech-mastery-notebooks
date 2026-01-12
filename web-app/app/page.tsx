'use client'

import { useState, useEffect, Suspense } from 'react'
import Sidebar from '@/components/Sidebar'
import Header from '@/components/Header'
import ContentViewer from '@/components/ContentViewer'
import { getContentStructure, type ContentItem } from '@/lib/contentLoader'

function HomeContent() {
  const [selectedContent, setSelectedContent] = useState<ContentItem | null>(null)
  const [contentStructure, setContentStructure] = useState<any[]>([])
  const [searchQuery, setSearchQuery] = useState('')
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [loading, setLoading] = useState(false)

  // IDs to hide by default (shown only when /all is in URL)
  const HIDDEN_SECTION_IDS = [
    // Core Categories
    'devops',
    'infrastructure-notebooks', 
    'system-design',
    'programming-challenges',
    'career',
    'teaching',
    'extras',
    
    // New Professional Categories (hidden by default, shown in /all)
    'fundamentals',
    'cloud-platforms',
    'backend-development',
    'frontend-development',
    'databases',
    'architecture-design',
    'big-data-analytics',
    'devops-infrastructure-advanced',
    'performance-engineering',
    'security-testing'
  ]

  useEffect(() => {
    const structure = getContentStructure()
    
    // Check if pathname contains '/all'
    const showAll = typeof window !== 'undefined' && window.location.pathname.includes('/all')
    
    // Filter content structure based on showAll flag
    const filteredStructure = showAll 
      ? structure 
      : structure.filter(item => !HIDDEN_SECTION_IDS.includes(item.id))
    
    setContentStructure(filteredStructure)
    
    // Set default content to README
    const readme = filteredStructure.find((item: any) => item.id === 'readme')
    if (readme) {
      loadContent(readme)
    }
  }, [])

  const loadContent = async (item: ContentItem) => {
    if (!item.path) {
      setSelectedContent(item)
      return
    }

    setLoading(true)
    try {
      // Load from pre-generated JSON files
      // Use window.location to detect if we're on GitHub Pages
      const isGitHubPages = typeof window !== 'undefined' && window.location.hostname === 'samba425.github.io'
      const basePath = isGitHubPages ? '/tech-mastery-notebooks' : ''
      const response = await fetch(`${basePath}/content/${item.id}.json`)
      
      console.log('Loading content:', `${basePath}/content/${item.id}.json`, 'Response:', response.status)
      
      if (!response.ok) {
        throw new Error(`Failed to load content: ${response.status}`)
      }
      const data = await response.json()
      setSelectedContent(data)
      
      // Scroll to top when new content loads
      setTimeout(() => {
        const mainElement = document.querySelector('main')
        if (mainElement) {
          mainElement.scrollTo({ top: 0, behavior: 'smooth' })
        }
      }, 100)
    } catch (error) {
      console.error('Error loading content:', error)
      // Show a friendly error message
      setSelectedContent({
        ...item,
        content: `# Welcome to Tech Mastery Platform! 🚀\n\n## Content Loading\n\nYour learning platform is being set up. The content files are being generated.\n\n### What's Included:\n\n- **System Design** - 7,500+ lines (Architecture, HLD, LLD)\n- **AI/ML Guides** - 19,384 lines\n- **Programming Languages** - Python, JavaScript, TypeScript\n- **DevOps & Infrastructure** - Docker, Kubernetes, Terraform\n- **Career Development** - Interview guides, roadmaps\n\n### Total Value: $35,000+ in Educational Content! 🎓\n\nPlease check back in a few minutes, or run the platform locally with:\n\n\`\`\`bash\ncd web-app\nnpm install\nnpm run dev\n\`\`\`\n\nThen visit: http://localhost:3000`
      })
    } finally {
      setLoading(false)
    }
  }

  const handleContentSelect = (content: ContentItem) => {
    loadContent(content)
  }

  // Get flat list of all content items for navigation
  const getFlatContentList = (): ContentItem[] => {
    const flatList: ContentItem[] = []
    
    const flatten = (items: ContentItem[]) => {
      items.forEach(item => {
        if (item.children) {
          flatten(item.children)
        } else if (item.path) {
          flatList.push(item)
        }
      })
    }
    
    flatten(contentStructure)
    return flatList
  }

  // Get previous and next content items
  const getNavigation = () => {
    if (!selectedContent) return { prev: null, next: null }
    
    const flatList = getFlatContentList()
    const currentIndex = flatList.findIndex(item => item.id === selectedContent.id)
    
    return {
      prev: currentIndex > 0 ? flatList[currentIndex - 1] : null,
      next: currentIndex < flatList.length - 1 ? flatList[currentIndex + 1] : null
    }
  }

  const navigation = getNavigation()

  return (
    <div className="flex flex-col h-screen bg-gray-50 dark:bg-slate-900">
      <Header 
        onSearch={setSearchQuery}
        onMenuToggle={() => setSidebarOpen(!sidebarOpen)}
      />
      
      <div className="flex flex-1 overflow-hidden">
        <Sidebar
          contentStructure={contentStructure}
          selectedContent={selectedContent}
          onSelectContent={handleContentSelect}
          searchQuery={searchQuery}
          isOpen={sidebarOpen}
        />
        
        <main className="flex-1 overflow-auto scroll-smooth">
          <ContentViewer 
            content={selectedContent} 
            loading={loading}
            onNavigate={handleContentSelect}
            prevContent={navigation.prev}
            nextContent={navigation.next}
          />
        </main>
      </div>
    </div>
  )
}

export default function Home() {
  return (
    <Suspense fallback={
      <div className="flex items-center justify-center h-screen bg-gray-50 dark:bg-slate-900">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto mb-4"></div>
          <p className="text-gray-600 dark:text-gray-400">Loading...</p>
        </div>
      </div>
    }>
      <HomeContent />
    </Suspense>
  )
}

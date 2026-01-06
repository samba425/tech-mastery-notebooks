'use client'

import { useState, useEffect } from 'react'
import Sidebar from '@/components/Sidebar'
import Header from '@/components/Header'
import ContentViewer from '@/components/ContentViewer'
import { getContentStructure, type ContentItem } from '@/lib/contentLoader'

export default function Home() {
  const [selectedContent, setSelectedContent] = useState<ContentItem | null>(null)
  const [contentStructure, setContentStructure] = useState<any[]>([])
  const [searchQuery, setSearchQuery] = useState('')
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const structure = getContentStructure()
    setContentStructure(structure)
    
    // Set default content to README
    const readme = structure.find((item: any) => item.id === 'readme')
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
      const response = await fetch(`/api/content?id=${item.id}`)
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
      setSelectedContent({
        ...item,
        content: '# Error\n\nFailed to load content. Please try again.'
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

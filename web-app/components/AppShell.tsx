'use client'

import { useState, useEffect, useCallback } from 'react'
import { PanelLeft } from 'lucide-react'
import Sidebar from '@/components/Sidebar'
import Header from '@/components/Header'
import ContentViewer from '@/components/ContentViewer'
import { getContentStructure, type ContentItem } from '@/lib/contentLoader'
import {
  loadSidebarOpen,
  saveSidebarOpen,
  loadReadingWidth,
  saveReadingWidth,
  loadFontScale,
  saveFontScale,
  type ReadingWidth,
} from '@/lib/uiPreferences'

interface PdfIndexItem {
  id: string
  title: string
  fileName: string
}

const HIDDEN_SECTION_IDS = [
  'devops',
  'infrastructure-notebooks',
  'system-design',
  'programming-challenges',
  'career',
  'extras',
  'fundamentals',
  'cloud-platforms',
  'backend-development',
  'frontend-development',
  'databases',
  'architecture-design',
  'big-data-analytics',
  'devops-infrastructure-advanced',
  'performance-engineering',
  'security-testing',
]

interface AppShellProps {
  showAllSections?: boolean
}

export default function AppShell({ showAllSections = false }: AppShellProps) {
  const [selectedContent, setSelectedContent] = useState<ContentItem | null>(null)
  const [contentStructure, setContentStructure] = useState<ContentItem[]>([])
  const [searchQuery, setSearchQuery] = useState('')
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [mobileDrawerOpen, setMobileDrawerOpen] = useState(false)
  const [readingWidth, setReadingWidth] = useState<ReadingWidth>('comfortable')
  const [fontScale, setFontScale] = useState(100)
  const [loading, setLoading] = useState(false)
  const [prefsReady, setPrefsReady] = useState(false)

  useEffect(() => {
    setSidebarOpen(loadSidebarOpen())
    setReadingWidth(loadReadingWidth())
    setFontScale(loadFontScale())
    setPrefsReady(true)
  }, [])

  const getBasePath = () =>
    typeof window !== 'undefined' && window.location.hostname === 'samba425.github.io'
      ? '/tech-mastery-notebooks'
      : ''

  const appendPdfLibrary = async (structure: ContentItem[]) => {
    try {
      const response = await fetch(`${getBasePath()}/content/pdf-index.json`)
      if (!response.ok) return structure
      const pdfIndex: PdfIndexItem[] = await response.json()
      if (!Array.isArray(pdfIndex) || pdfIndex.length === 0) return structure
      const pdfChildren: ContentItem[] = pdfIndex.map((pdf) => ({
        id: pdf.id,
        title: `📄 ${pdf.title}`,
        path: `../filesLearn/${pdf.fileName}`,
        category: 'pdf-library',
        badge: 'PDF',
        description: `Read ${pdf.fileName} in the in-app PDF viewer`,
      }))
      const filtered = structure.filter((item) => item.id !== 'pdf-library')
      return [
        ...filtered,
        { id: 'pdf-library', title: '📚 PDF Library', children: pdfChildren },
      ]
    } catch {
      return structure
    }
  }

  useEffect(() => {
    const initializeContent = async () => {
      const structure = await appendPdfLibrary(getContentStructure() as ContentItem[])
      const showAll =
        showAllSections ||
        (typeof window !== 'undefined' && window.location.pathname.includes('/all'))
      const filtered = showAll
        ? structure
        : structure.filter((item) => !HIDDEN_SECTION_IDS.includes(item.id))
      setContentStructure(filtered)
      const defaultItem =
        filtered.find((item) => item.id === 'start-here') ||
        filtered.find((item) => item.id === 'readme')
      if (defaultItem) loadContent(defaultItem)
    }
    initializeContent()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [showAllSections])

  const loadContent = async (item: ContentItem) => {
    if (!item.path) {
      setSelectedContent(item)
      return
    }
    setLoading(true)
    try {
      const response = await fetch(`${getBasePath()}/content/${item.id}.json`)
      if (!response.ok) throw new Error(`Failed to load: ${response.status}`)
      const data = await response.json()
      setSelectedContent(data)
      setMobileDrawerOpen(false)
      setTimeout(() => {
        document.querySelector('main')?.scrollTo({ top: 0, behavior: 'smooth' })
      }, 80)
    } catch {
      setSelectedContent({
        ...item,
        content: `# Content unavailable\n\nRun \`node generate-content.js\` in \`web-app\` and rebuild.`,
      })
    } finally {
      setLoading(false)
    }
  }

  const toggleSidebar = useCallback(() => {
    setSidebarOpen((prev) => {
      const next = !prev
      saveSidebarOpen(next)
      return next
    })
  }, [])

  const handleMenuToggle = () => {
    if (typeof window !== 'undefined' && window.innerWidth < 1024) {
      setMobileDrawerOpen((o) => !o)
    } else {
      toggleSidebar()
    }
  }

  const getFlatContentList = (): ContentItem[] => {
    const flat: ContentItem[] = []
    const flatten = (items: ContentItem[]) => {
      items.forEach((item) => {
        if (item.children) flatten(item.children)
        else if (item.path) flat.push(item)
      })
    }
    flatten(contentStructure)
    return flat
  }

  const navigation = (() => {
    if (!selectedContent) return { prev: null, next: null }
    const flat = getFlatContentList()
    const i = flat.findIndex((item) => item.id === selectedContent.id)
    return {
      prev: i > 0 ? flat[i - 1] : null,
      next: i < flat.length - 1 ? flat[i + 1] : null,
    }
  })()

  const sidebarVisible = sidebarOpen || mobileDrawerOpen

  return (
    <div className="flex flex-col h-screen bg-slate-100/80 dark:bg-slate-950">
      <Header
        onSearch={setSearchQuery}
        onMenuToggle={handleMenuToggle}
        sidebarOpen={sidebarOpen}
      />

      <div className="flex flex-1 min-h-0 relative">
        <Sidebar
          contentStructure={contentStructure}
          selectedContent={selectedContent}
          onSelectContent={loadContent}
          searchQuery={searchQuery}
          isOpen={sidebarVisible}
          isCollapsed={!sidebarOpen && !mobileDrawerOpen}
          onClose={() => setMobileDrawerOpen(false)}
        />

        {!sidebarOpen && (
          <button
            type="button"
            onClick={toggleSidebar}
            className="hidden lg:flex fixed left-3 top-[4.25rem] z-30 items-center justify-center w-9 h-9 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 shadow-md text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors"
            aria-label="Show navigation panel"
            title="Show navigation"
          >
            <PanelLeft className="w-4 h-4" />
          </button>
        )}

        <main className="flex-1 min-w-0 overflow-auto scroll-smooth bg-slate-50 dark:bg-slate-900/50">
          <ContentViewer
            content={selectedContent}
            loading={loading || !prefsReady}
            onNavigate={loadContent}
            prevContent={navigation.prev}
            nextContent={navigation.next}
            sidebarOpen={sidebarOpen}
            onToggleSidebar={toggleSidebar}
            readingWidth={readingWidth}
            onReadingWidthChange={(w) => {
              setReadingWidth(w)
              saveReadingWidth(w)
            }}
            fontScale={fontScale}
            onFontScaleChange={(s) => {
              setFontScale(s)
              saveFontScale(s)
            }}
          />
        </main>
      </div>
    </div>
  )
}

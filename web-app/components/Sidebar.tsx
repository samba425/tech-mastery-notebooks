'use client'

import { ChevronRight, ChevronDown, FileText, Folder } from 'lucide-react'
import { useState } from 'react'
import type { ContentItem } from '@/lib/contentLoader'

interface SidebarProps {
  contentStructure: any[]
  selectedContent: ContentItem | null
  onSelectContent: (content: ContentItem) => void
  searchQuery: string
  isOpen: boolean
}

export default function Sidebar({
  contentStructure,
  selectedContent,
  onSelectContent,
  searchQuery,
  isOpen,
}: SidebarProps) {
  const [expandedFolders, setExpandedFolders] = useState<Set<string>>(
    new Set([
      'programming', 
      'ai-ml', 
      'devops', 
      'infrastructure-notebooks',
      'system-design',
      'programming-challenges',
      'career',
      'teaching'
    ])
  )

  const toggleFolder = (folderId: string) => {
    const newExpanded = new Set(expandedFolders)
    if (newExpanded.has(folderId)) {
      newExpanded.delete(folderId)
    } else {
      newExpanded.add(folderId)
    }
    setExpandedFolders(newExpanded)
  }

  const filterContent = (items: any[]): any[] => {
    if (!searchQuery) return items

    return items.filter(item => {
      if (item.children) {
        const filteredChildren = filterContent(item.children)
        if (filteredChildren.length > 0) {
          return true
        }
      }
      return item.title.toLowerCase().includes(searchQuery.toLowerCase())
    })
  }

  const renderItems = (items: any[], level: number = 0) => {
    return filterContent(items).map((item) => {
      const isExpanded = expandedFolders.has(item.id)
      const isSelected = selectedContent?.id === item.id
      const hasChildren = item.children && item.children.length > 0

      return (
        <div key={item.id}>
          <button
            onClick={() => {
              if (hasChildren) {
                toggleFolder(item.id)
              }
              if (item.path) {
                onSelectContent(item)
              }
            }}
            className={`w-full flex items-center gap-2 px-3 py-2 text-left rounded-lg transition-colors ${
              isSelected
                ? 'bg-primary-100 dark:bg-primary-900 text-primary-900 dark:text-primary-100'
                : 'hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-300'
            }`}
            style={{ paddingLeft: `${level * 16 + 12}px` }}
          >
            {hasChildren ? (
              isExpanded ? (
                <ChevronDown className="w-4 h-4 flex-shrink-0" />
              ) : (
                <ChevronRight className="w-4 h-4 flex-shrink-0" />
              )
            ) : (
              <FileText className="w-4 h-4 flex-shrink-0" />
            )}
            {hasChildren && <Folder className="w-4 h-4 flex-shrink-0" />}
            <span className="flex-1 text-sm font-medium truncate">{item.title}</span>
            {item.badge && (
              <span className="text-xs px-2 py-0.5 bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-100 rounded-full">
                {item.badge}
              </span>
            )}
          </button>

          {hasChildren && isExpanded && (
            <div className="mt-1">
              {renderItems(item.children, level + 1)}
            </div>
          )}
        </div>
      )
    })
  }

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
          onClick={() => {}}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`${
          isOpen ? 'translate-x-0' : '-translate-x-full'
        } lg:translate-x-0 fixed lg:relative z-40 w-80 bg-white dark:bg-slate-800 border-r border-gray-200 dark:border-gray-700 transition-transform duration-300 ease-in-out h-full overflow-y-auto`}
      >
        <div className="p-4">
          <div className="mb-4">
            <h2 className="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider px-3 mb-2">
              Learning Guides
            </h2>
          </div>

          <nav className="space-y-1">
            {renderItems(contentStructure)}
          </nav>

          <div className="mt-8 p-4 bg-gradient-to-br from-primary-50 to-primary-100 dark:from-primary-900 dark:to-primary-800 rounded-lg">
            <h3 className="font-semibold text-primary-900 dark:text-primary-100 mb-2">
              💡 Pro Tip
            </h3>
            <p className="text-sm text-primary-800 dark:text-primary-200">
              Use Ctrl+F to search within the current guide, or use the search bar above to search all guides.
            </p>
          </div>
        </div>
      </aside>
    </>
  )
}

'use client'

import { ChevronRight, ChevronDown, FileText, Folder, X } from 'lucide-react'
import { useState } from 'react'
import type { ContentItem } from '@/lib/contentLoader'

interface SidebarProps {
  contentStructure: ContentItem[]
  selectedContent: ContentItem | null
  onSelectContent: (content: ContentItem) => void
  searchQuery: string
  isOpen: boolean
  isCollapsed?: boolean
  onClose?: () => void
}

const badgeStyles: Record<string, string> = {
  'Start Here': 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-200',
  Start: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/50 dark:text-emerald-200',
  Reference: 'bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-200',
  New: 'bg-sky-100 text-sky-800 dark:bg-sky-900/50 dark:text-sky-200',
  default: 'bg-slate-100 text-slate-600 dark:bg-slate-700/80 dark:text-slate-300',
}

function badgeClass(badge?: string) {
  if (!badge) return ''
  return badgeStyles[badge] ?? badgeStyles.default
}

export default function Sidebar({
  contentStructure,
  selectedContent,
  onSelectContent,
  searchQuery,
  isOpen,
  isCollapsed = false,
  onClose,
}: SidebarProps) {
  const [expandedFolders, setExpandedFolders] = useState<Set<string>>(
    new Set([
      'python',
      'ai-ml',
      'ai-ml-phase-1-core',
      'ai-ml-phase-2-career',
      'devops',
      'infrastructure-notebooks',
      'system-design',
      'cloud-platforms',
      'cloud-phase-1-aws',
      'programming-challenges',
      'career',
    ])
  )

  const toggleFolder = (folderId: string) => {
    const next = new Set(expandedFolders)
    if (next.has(folderId)) next.delete(folderId)
    else next.add(folderId)
    setExpandedFolders(next)
  }

  const filterContent = (items: ContentItem[]): ContentItem[] => {
    if (!searchQuery) return items
    return items.filter((item) => {
      if (item.children) {
        const kids = filterContent(item.children)
        if (kids.length > 0) return true
      }
      return item.title.toLowerCase().includes(searchQuery.toLowerCase())
    })
  }

  const renderItems = (items: ContentItem[], level = 0) =>
    filterContent(items).map((item) => {
      const isExpanded = expandedFolders.has(item.id)
      const isSelected = selectedContent?.id === item.id
      const hasChildren = item.children && item.children.length > 0
      const isLeaf = Boolean(item.path)

      return (
        <div key={item.id}>
          <button
            type="button"
            onClick={() => {
              if (hasChildren) toggleFolder(item.id)
              if (item.path) onSelectContent(item)
            }}
            className={`group w-full flex items-start gap-2 py-2 pr-2 text-left rounded-lg transition-all duration-150 ${
              isSelected && isLeaf
                ? 'bg-primary-600/10 dark:bg-primary-500/15 text-primary-900 dark:text-primary-100 ring-1 ring-primary-500/30'
                : 'text-slate-700 dark:text-slate-300 hover:bg-slate-100/90 dark:hover:bg-slate-800/80'
            }`}
            style={{ paddingLeft: `${level * 14 + 10}px` }}
          >
            <span className="mt-0.5 flex-shrink-0 w-4 h-4 text-slate-400 dark:text-slate-500">
              {hasChildren ? (
                isExpanded ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />
              ) : (
                <FileText className="w-4 h-4" />
              )}
            </span>
            {hasChildren && !isLeaf && (
              <Folder className="w-4 h-4 flex-shrink-0 mt-0.5 text-slate-400" />
            )}
            <span className="flex-1 text-[13px] leading-snug font-medium line-clamp-2">{item.title}</span>
            {item.badge && (
              <span
                className={`flex-shrink-0 text-[10px] px-1.5 py-0.5 rounded font-medium ${badgeClass(item.badge)}`}
              >
                {item.badge}
              </span>
            )}
          </button>
          {hasChildren && isExpanded && (
            <div className="border-l border-slate-200/80 dark:border-slate-700/80 ml-4">
              {renderItems(item.children!, level + 1)}
            </div>
          )}
        </div>
      )
    })

  return (
    <>
      {isOpen && (
        <button
          type="button"
          className="fixed inset-0 bg-slate-900/40 backdrop-blur-[2px] z-40 lg:hidden"
          onClick={onClose}
          aria-label="Close navigation"
        />
      )}

      <aside
        className={`
          flex flex-col z-50 h-full
          bg-white dark:bg-slate-900
          border-r border-slate-200/90 dark:border-slate-800
          shadow-xl lg:shadow-none
          transition-[width,transform,opacity] duration-300 ease-out
          fixed lg:relative inset-y-0 left-0
          ${isOpen ? 'translate-x-0 opacity-100' : '-translate-x-full opacity-0 lg:opacity-100'}
          ${isCollapsed ? 'lg:w-0 lg:overflow-hidden lg:border-r-0' : 'w-[min(100vw,20rem)] lg:w-72'}
        `}
        aria-hidden={isCollapsed && !isOpen}
      >
        <div className="flex items-center justify-between px-4 py-3 border-b border-slate-100 dark:border-slate-800 flex-shrink-0">
          <div>
            <p className="text-[11px] font-semibold uppercase tracking-widest text-slate-400 dark:text-slate-500">
              Learning guides
            </p>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Navigate by path</p>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="lg:hidden p-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-500"
            aria-label="Close sidebar"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <nav className="flex-1 overflow-y-auto overflow-x-hidden px-2 py-3 scrollbar-thin">
          {renderItems(contentStructure)}
        </nav>

        <div className="flex-shrink-0 p-3 border-t border-slate-100 dark:border-slate-800">
          <div className="rounded-lg bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-800/50 dark:to-slate-800 p-3">
            <p className="text-xs font-semibold text-slate-700 dark:text-slate-200 mb-1">Reading tip</p>
            <p className="text-[11px] leading-relaxed text-slate-500 dark:text-slate-400">
              Hide the panel for focus mode. Use the toolbar to adjust text size and column width.
            </p>
          </div>
        </div>
      </aside>
    </>
  )
}

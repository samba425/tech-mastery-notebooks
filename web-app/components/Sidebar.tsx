'use client'

import { ChevronRight, ChevronDown, X, Lightbulb } from 'lucide-react'
import { useState, useEffect } from 'react'
import type { ContentItem } from '@/lib/contentLoader'
import { stripEmojis, NavIconBox } from '@/lib/navIcons'

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
  'Start Here':
    'bg-emerald-100/80 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-400 border border-emerald-200/80 dark:border-emerald-800/80',
  Start:
    'bg-emerald-100/80 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-400 border border-emerald-200/80 dark:border-emerald-800/80',
  Reference:
    'bg-slate-200/60 text-slate-700 dark:bg-slate-800 dark:text-slate-300 border border-slate-300/50 dark:border-slate-600',
  New:
    'bg-sky-100/80 text-sky-800 dark:bg-sky-950 dark:text-sky-400 border border-sky-200/80 dark:border-sky-800/80',
  default:
    'bg-slate-200/60 text-slate-600 dark:bg-slate-800 dark:text-slate-400 border border-slate-300/50 dark:border-slate-600',
}

function badgeClass(badge?: string) {
  if (!badge) return badgeStyles.default
  return badgeStyles[badge] ?? badgeStyles.default
}

function findAncestorIds(items: ContentItem[], targetId: string, trail: string[] = []): string[] | null {
  for (const item of items) {
    if (item.id === targetId) return trail
    if (item.children?.length) {
      const found = findAncestorIds(item.children, targetId, [...trail, item.id])
      if (found) return found
    }
  }
  return null
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
  /** All sections collapsed by default — user expands what they need */
  const [expandedFolders, setExpandedFolders] = useState<Set<string>>(() => new Set())

  useEffect(() => {
    if (!selectedContent?.id) return
    const ancestors = findAncestorIds(contentStructure, selectedContent.id)
    if (!ancestors?.length) return
    setExpandedFolders((prev) => {
      const next = new Set(prev)
      ancestors.forEach((id) => next.add(id))
      return next
    })
  }, [selectedContent?.id, contentStructure])

  const toggleFolder = (folderId: string) => {
    const next = new Set(expandedFolders)
    if (next.has(folderId)) next.delete(folderId)
    else next.add(folderId)
    setExpandedFolders(next)
  }

  const filterContent = (items: ContentItem[]): ContentItem[] => {
    if (!searchQuery) return items
    const q = searchQuery.toLowerCase()
    return items.filter((item) => {
      if (item.children) {
        if (filterContent(item.children).length > 0) return true
      }
      return (
        item.title.toLowerCase().includes(q) ||
        stripEmojis(item.title).toLowerCase().includes(q)
      )
    })
  }

  const renderItems = (items: ContentItem[], level = 0) =>
    filterContent(items).map((item) => {
      const isExpanded = expandedFolders.has(item.id)
      const isSelected = selectedContent?.id === item.id
      const hasChildren = Boolean(item.children?.length)
      const isLeaf = Boolean(item.path)
      const label = stripEmojis(item.title)

      return (
        <div key={item.id}>
          <button
            type="button"
            onClick={() => {
              if (hasChildren) toggleFolder(item.id)
              if (item.path) onSelectContent(item)
            }}
            className={`group w-full flex items-center gap-2.5 py-2 pr-2 text-left rounded-lg transition-all duration-150 ${
              isSelected && isLeaf
                ? 'bg-slate-200/70 text-slate-900 ring-1 ring-primary-500/35 dark:bg-slate-800 dark:text-slate-100 dark:ring-primary-400/40'
                : 'text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800/80'
            }`}
            style={{ paddingLeft: `${level * 12 + 8}px` }}
          >
            {hasChildren ? (
              <span className="flex-shrink-0 w-4 h-4 text-slate-400 dark:text-slate-500">
                {isExpanded ? (
                  <ChevronDown className="w-4 h-4" />
                ) : (
                  <ChevronRight className="w-4 h-4" />
                )}
              </span>
            ) : (
              <span className="w-4 flex-shrink-0" aria-hidden />
            )}

            <NavIconBox
              id={item.id}
              category={item.category}
              hasChildren={hasChildren && !isLeaf}
              fileType={item.fileType}
              selected={Boolean(isSelected && isLeaf)}
            />

            <span className="flex-1 text-[13px] leading-snug font-medium line-clamp-2 min-w-0">
              {label}
            </span>

            {item.badge && (
              <span
                className={`flex-shrink-0 text-[10px] px-1.5 py-0.5 rounded font-medium ${badgeClass(item.badge)}`}
              >
                {item.badge}
              </span>
            )}
          </button>

          {hasChildren && isExpanded && (
            <div className="ml-3 border-l border-slate-200/90 dark:border-slate-700/90">
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
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Enterprise curriculum</p>
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
          <div className="rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-slate-800/60 p-3">
            <p className="text-xs font-semibold text-slate-700 dark:text-slate-200 mb-1 flex items-center gap-1.5">
              <Lightbulb className="w-3.5 h-3.5 text-amber-500" />
              Focus mode
            </p>
            <p className="text-[11px] leading-relaxed text-slate-500 dark:text-slate-400">
              Hide the panel for full-width reading. Theme and width controls stay in the toolbar.
            </p>
          </div>
        </div>
      </aside>
    </>
  )
}

'use client'

import { PanelLeft, PanelLeftClose, Maximize2, Minimize2, Type } from 'lucide-react'
import type { ReadingWidth } from '@/lib/uiPreferences'

interface ReadingToolbarProps {
  sidebarOpen: boolean
  onToggleSidebar: () => void
  readingWidth: ReadingWidth
  onReadingWidthChange: (w: ReadingWidth) => void
  fontScale: number
  onFontScaleChange: (scale: number) => void
  title?: string
}

export default function ReadingToolbar({
  sidebarOpen,
  onToggleSidebar,
  readingWidth,
  onReadingWidthChange,
  fontScale,
  onFontScaleChange,
  title,
}: ReadingToolbarProps) {
  const cycleFont = () => {
    const next = fontScale === 100 ? 110 : fontScale === 110 ? 125 : 100
    onFontScaleChange(next)
  }

  return (
    <div className="sticky top-0 z-20 -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 mb-6">
      <div className="flex flex-wrap items-center gap-2 py-2.5 px-3 rounded-xl border border-slate-200/80 dark:border-slate-700/80 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md shadow-sm">
        <button
          type="button"
          onClick={onToggleSidebar}
          className="inline-flex items-center gap-2 px-3 py-1.5 text-sm font-medium rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          title={sidebarOpen ? 'Hide navigation panel' : 'Show navigation panel'}
          aria-label={sidebarOpen ? 'Hide sidebar' : 'Show sidebar'}
        >
          {sidebarOpen ? (
            <PanelLeftClose className="w-4 h-4" />
          ) : (
            <PanelLeft className="w-4 h-4" />
          )}
          <span className="hidden sm:inline">{sidebarOpen ? 'Hide panel' : 'Show panel'}</span>
        </button>

        <span className="hidden md:inline w-px h-5 bg-slate-200 dark:bg-slate-700" aria-hidden />

        <button
          type="button"
          onClick={cycleFont}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          title="Cycle text size"
        >
          <Type className="w-4 h-4" />
          <span className="tabular-nums">{fontScale}%</span>
        </button>

        <button
          type="button"
          onClick={() =>
            onReadingWidthChange(readingWidth === 'comfortable' ? 'wide' : 'comfortable')
          }
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          title={readingWidth === 'comfortable' ? 'Wider reading column' : 'Comfortable width'}
        >
          {readingWidth === 'comfortable' ? (
            <Maximize2 className="w-4 h-4" />
          ) : (
            <Minimize2 className="w-4 h-4" />
          )}
          <span className="hidden sm:inline">
            {readingWidth === 'comfortable' ? 'Wide' : 'Comfort'}
          </span>
        </button>

        {title && (
          <>
            <span className="hidden lg:inline w-px h-5 bg-slate-200 dark:bg-slate-700 ml-auto" />
            <span className="hidden lg:block ml-auto text-xs text-slate-500 dark:text-slate-400 truncate max-w-[280px]">
              {title}
            </span>
          </>
        )}
      </div>
    </div>
  )
}

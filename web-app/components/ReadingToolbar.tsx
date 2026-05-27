'use client'

import {
  PanelLeft,
  PanelLeftClose,
  Maximize2,
  Minimize2,
  Type,
  Sun,
  Moon,
  Monitor,
} from 'lucide-react'
import type { ReadingWidth, ThemeMode } from '@/lib/uiPreferences'
import { useTheme } from '@/components/ThemeProvider'

interface ReadingToolbarProps {
  sidebarOpen: boolean
  onToggleSidebar: () => void
  readingWidth: ReadingWidth
  onReadingWidthChange: (w: ReadingWidth) => void
  fontScale: number
  onFontScaleChange: (scale: number) => void
  title?: string
}

const themeLabels: Record<ThemeMode, string> = {
  light: 'Light',
  dark: 'Dark',
  system: 'Auto',
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
  const { theme, cycleTheme } = useTheme()

  const cycleFont = () => {
    const next = fontScale === 100 ? 110 : fontScale === 110 ? 125 : 100
    onFontScaleChange(next)
  }

  const ThemeIcon = theme === 'dark' ? Moon : theme === 'light' ? Sun : Monitor

  return (
    <div className="sticky top-0 z-20 mb-4">
      <div className="flex flex-wrap items-center gap-2 py-2.5 px-3 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-100/95 dark:bg-slate-900/95 backdrop-blur-md shadow-sm dark:shadow-none">
        <button
          type="button"
          onClick={onToggleSidebar}
          className="inline-flex items-center gap-2 px-3 py-1.5 text-sm font-medium rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          title={sidebarOpen ? 'Hide navigation panel' : 'Show navigation panel'}
        >
          {sidebarOpen ? <PanelLeftClose className="w-4 h-4" /> : <PanelLeft className="w-4 h-4" />}
          <span className="hidden sm:inline">{sidebarOpen ? 'Hide panel' : 'Show panel'}</span>
        </button>

        <span className="hidden md:inline w-px h-5 bg-slate-200 dark:bg-slate-700" aria-hidden />

        <button
          type="button"
          onClick={cycleTheme}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          title="Theme: light → dark → system"
        >
          <ThemeIcon className="w-4 h-4" />
          <span className="hidden sm:inline">{themeLabels[theme]}</span>
        </button>

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
          onClick={() => onReadingWidthChange(readingWidth === 'full' ? 'narrow' : 'full')}
          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
          title={readingWidth === 'full' ? 'Narrow column' : 'Full width'}
        >
          {readingWidth === 'full' ? (
            <Minimize2 className="w-4 h-4" />
          ) : (
            <Maximize2 className="w-4 h-4" />
          )}
          <span className="hidden sm:inline">{readingWidth === 'full' ? 'Narrow' : 'Full width'}</span>
        </button>

        {title && (
          <>
            <span className="hidden lg:inline w-px h-5 bg-slate-200 dark:bg-slate-700 ml-auto" />
            <span className="hidden lg:block ml-auto text-xs text-slate-500 dark:text-slate-400 truncate max-w-[min(40vw,320px)]">
              {title}
            </span>
          </>
        )}
      </div>
    </div>
  )
}

'use client'

import Link from 'next/link'
import { Search, PanelLeft, Sun, Moon, Monitor, GraduationCap } from 'lucide-react'
import { useTheme } from '@/components/ThemeProvider'

interface HeaderProps {
  onSearch: (query: string) => void
  onMenuToggle: () => void
  sidebarOpen?: boolean
}

export default function Header({ onSearch, onMenuToggle, sidebarOpen = true }: HeaderProps) {
  const { theme, cycleTheme } = useTheme()
  const ThemeIcon = theme === 'dark' ? Moon : theme === 'light' ? Sun : Monitor

  return (
    <header className="flex-shrink-0 z-50 border-b border-slate-200/90 dark:border-slate-800 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md">
      <div className="flex items-center justify-between gap-4 px-4 h-14">
        <div className="flex items-center gap-2 min-w-0">
          <button
            type="button"
            onClick={onMenuToggle}
            className="p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
            aria-label={sidebarOpen ? 'Hide navigation panel' : 'Show navigation panel'}
            title={sidebarOpen ? 'Hide panel' : 'Show panel'}
          >
            <PanelLeft className="w-5 h-5" />
          </button>

          <Link href="/" className="flex items-center gap-2.5 min-w-0 group">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-slate-800 to-slate-950 dark:from-primary-600 dark:to-primary-800 flex items-center justify-center shadow-sm flex-shrink-0">
              <GraduationCap className="w-4 h-4 text-white" strokeWidth={2} />
            </div>
            <div className="hidden sm:block min-w-0">
              <h1 className="text-sm font-semibold text-slate-900 dark:text-white truncate group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors">
                Tech Mastery
              </h1>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 -mt-0.5">Learning platform</p>
            </div>
          </Link>
        </div>

        <div className="flex items-center gap-2 sm:gap-3">
          <Link
            href="/"
            className="hidden md:inline-flex text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-primary-600 dark:hover:text-primary-400 px-2 py-1 rounded-md"
          >
            Home
          </Link>
          <button
            type="button"
            onClick={cycleTheme}
            className="p-2 rounded-lg text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
            title="Toggle theme (light / dark / system)"
            aria-label="Toggle theme"
          >
            <ThemeIcon className="w-5 h-5" />
          </button>
          <Link
            href="/all"
            className="text-xs sm:text-sm font-medium px-2.5 sm:px-3 py-1.5 rounded-lg bg-primary-50 dark:bg-primary-950/50 text-primary-700 dark:text-primary-300 border border-primary-100 dark:border-primary-900/50 hover:bg-primary-100 dark:hover:bg-primary-900/40 transition-colors whitespace-nowrap"
          >
            All guides
          </Link>
          <div className="relative hidden sm:block">
            <Search className="absolute left-2.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400 pointer-events-none" />
            <input
              type="search"
              placeholder="Search…"
              onChange={(e) => onSearch(e.target.value)}
              className="w-36 sm:w-52 lg:w-64 pl-9 pr-3 py-1.5 text-sm bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500/40 focus:border-primary-400 text-slate-900 dark:text-white placeholder:text-slate-400"
            />
          </div>
        </div>
      </div>
    </header>
  )
}

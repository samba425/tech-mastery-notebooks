'use client'

import Link from 'next/link'
import { Search, Menu } from 'lucide-react'

interface HeaderProps {
  onSearch: (query: string) => void
  onMenuToggle: () => void
}

function getBasePath() {
  if (typeof window === 'undefined') return ''
  return window.location.hostname === 'samba425.github.io' ? '/tech-mastery-notebooks' : ''
}

export default function Header({ onSearch, onMenuToggle }: HeaderProps) {
  const basePath = getBasePath()

  return (
    <header className="bg-white dark:bg-slate-800 border-b border-gray-200 dark:border-gray-700 sticky top-0 z-50">
      <div className="flex items-center justify-between px-4 py-3">
        <div className="flex items-center gap-3">
          <button
            onClick={onMenuToggle}
            className="lg:hidden p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg"
            aria-label="Toggle menu"
          >
            <Menu className="w-5 h-5" />
          </button>
          
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-br from-primary-500 to-primary-700 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-lg">T</span>
            </div>
            <h1 className="text-xl font-bold text-gray-900 dark:text-white hidden sm:block">
              Tech Mastery Platform
            </h1>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <Link
            href={`${basePath}/`}
            className="hidden md:inline text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-primary-600 dark:hover:text-primary-400"
          >
            Home
          </Link>
          <Link
            href={`${basePath}/all`}
            className="hidden sm:inline text-sm font-medium px-3 py-1.5 rounded-lg bg-primary-50 dark:bg-primary-900/40 text-primary-700 dark:text-primary-300 hover:bg-primary-100 dark:hover:bg-primary-900/60"
          >
            All guides
          </Link>
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
            <input
              type="text"
              placeholder="Search guides..."
              onChange={(e) => onSearch(e.target.value)}
              className="pl-10 pr-4 py-2 w-64 bg-gray-100 dark:bg-gray-700 border border-gray-200 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 text-gray-900 dark:text-white placeholder-gray-500"
            />
          </div> 
        </div>
      </div>
    </header>
  )
}

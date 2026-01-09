'use client'

import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeHighlight from 'rehype-highlight'
import rehypeSlug from 'rehype-slug'
import remarkCustomHeadingId from '@/lib/remark-custom-heading-id'
import type { ContentItem } from '@/lib/contentLoader'
import { Book, Clock, Tag } from 'lucide-react'
import 'highlight.js/styles/github-dark.css'

interface ContentViewerProps {
  content: ContentItem | null
  loading?: boolean
  onNavigate?: (content: ContentItem) => void
  prevContent?: ContentItem | null
  nextContent?: ContentItem | null
}

export default function ContentViewer({ content, loading, onNavigate, prevContent, nextContent }: ContentViewerProps) {
  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <div className="w-16 h-16 mx-auto mb-4 border-4 border-primary-500 border-t-transparent rounded-full animate-spin"></div>
          <p className="text-gray-600 dark:text-gray-400">Loading content...</p>
        </div>
      </div>
    )
  }

  if (!content) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <Book className="w-16 h-16 mx-auto mb-4 text-gray-400" />
          <h2 className="text-2xl font-bold text-gray-700 dark:text-gray-300 mb-2">
            Welcome to Tech Mastery Platform
          </h2>
          <p className="text-gray-600 dark:text-gray-400">
            Select a guide from the sidebar to start learning
          </p>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-5xl mx-auto px-6 py-8">
      {/* Content header */}
      <div className="mb-8 pb-6 border-b border-gray-200 dark:border-gray-700">
        <div className="flex items-start justify-between mb-4">
          <div>
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-2">
              {content.title}
            </h1>
            {content.description && (
              <p className="text-lg text-gray-600 dark:text-gray-400">
                {content.description}
              </p>
            )}
          </div>
        </div>

        {/* Metadata */}
        <div className="flex flex-wrap gap-4 text-sm text-gray-600 dark:text-gray-400">
          {content.category && (
            <div className="flex items-center gap-2">
              <Tag className="w-4 h-4" />
              <span className="capitalize">{content.category}</span>
            </div>
          )}
          {content.readTime && (
            <div className="flex items-center gap-2">
              <Clock className="w-4 h-4" />
              <span>{content.readTime} min read</span>
            </div>
          )}
        </div>
      </div>

      {/* Markdown content */}
      <div className="markdown-content">
        <ReactMarkdown
          remarkPlugins={[remarkGfm, remarkCustomHeadingId]}
          rehypePlugins={[rehypeSlug, rehypeHighlight]}
          components={{
            // Make anchor links work with smooth scrolling
            a: ({ node, href, children, ...props }) => {
              // If it's an internal anchor link (starts with #)
              if (href && href.startsWith('#')) {
                return (
                  <a
                    href={href}
                    onClick={(e) => {
                      e.preventDefault()
                      const id = href.replace('#', '')
                      const element = document.getElementById(id)
                      if (element) {
                        // Scroll within the main content container
                        const container = element.closest('main')
                        if (container) {
                          const elementTop = element.offsetTop
                          const offset = 80 // Header offset
                          container.scrollTo({ top: elementTop - offset, behavior: 'smooth' })
                        } else {
                          // Fallback to window scroll
                          const yOffset = -80
                          const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset
                          window.scrollTo({ top: y, behavior: 'smooth' })
                        }
                      }
                    }}
                    className="text-primary-600 dark:text-primary-400 hover:underline cursor-pointer"
                    {...props}
                  >
                    {children}
                  </a>
                )
              }
              // External links
              return (
                <a href={href} target="_blank" rel="noopener noreferrer" {...props}>
                  {children}
                </a>
              )
            },
          }}
        >
          {content.content || ''}
        </ReactMarkdown>
      </div>

      {/* Footer navigation */}
      <div className="mt-12 pt-6 border-t border-gray-200 dark:border-gray-700">
        <div className="flex justify-between items-center gap-4">
          {prevContent ? (
            <button 
              onClick={() => onNavigate?.(prevContent)}
              className="group px-5 py-3 text-primary-600 dark:text-primary-400 hover:bg-primary-50 dark:hover:bg-primary-900 border border-gray-200 dark:border-gray-700 hover:border-primary-300 dark:hover:border-primary-600 rounded-lg transition-all flex items-center gap-3 max-w-xs"
            >
              <span className="text-xl group-hover:-translate-x-1 transition-transform">←</span>
              <div className="text-left overflow-hidden">
                <div className="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wide">Previous</div>
                <div className="font-medium truncate group-hover:text-primary-700 dark:group-hover:text-primary-300">
                  {prevContent.title}
                </div>
              </div>
            </button>
          ) : (
            <div></div>
          )}
          
          {nextContent ? (
            <button 
              onClick={() => onNavigate?.(nextContent)}
              className="group px-5 py-3 text-primary-600 dark:text-primary-400 hover:bg-primary-50 dark:hover:bg-primary-900 border border-gray-200 dark:border-gray-700 hover:border-primary-300 dark:hover:border-primary-600 rounded-lg transition-all flex items-center gap-3 max-w-xs"
            >
              <div className="text-right overflow-hidden">
                <div className="text-xs text-gray-500 dark:text-gray-400 uppercase tracking-wide">Next</div>
                <div className="font-medium truncate group-hover:text-primary-700 dark:group-hover:text-primary-300">
                  {nextContent.title}
                </div>
              </div>
              <span className="text-xl group-hover:translate-x-1 transition-transform">→</span>
            </button>
          ) : (
            <div></div>
          )}
        </div>
      </div>
    </div>
  )
}

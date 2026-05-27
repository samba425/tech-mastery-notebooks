'use client'

import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeHighlight from 'rehype-highlight'
import rehypeSlug from 'rehype-slug'
import remarkCustomHeadingId from '@/lib/remark-custom-heading-id'
import { enrichChildren, prepareMarkdownForDisplay } from '@/lib/sectionRefs'
import type { ContentItem } from '@/lib/contentLoader'
import type { ReadingWidth } from '@/lib/uiPreferences'
import ReadingToolbar from '@/components/ReadingToolbar'
import { Book, Clock, Tag, ChevronLeft, ChevronRight } from 'lucide-react'
import { stripEmojis, NavIconBox } from '@/lib/navIcons'
import 'highlight.js/styles/github-dark.css'

interface ContentViewerProps {
  content: ContentItem | null
  loading?: boolean
  onNavigate?: (content: ContentItem) => void
  prevContent?: ContentItem | null
  nextContent?: ContentItem | null
  sidebarOpen?: boolean
  onToggleSidebar?: () => void
  readingWidth?: ReadingWidth
  onReadingWidthChange?: (w: ReadingWidth) => void
  fontScale?: number
  onFontScaleChange?: (scale: number) => void
}

export default function ContentViewer({
  content,
  loading,
  onNavigate,
  prevContent,
  nextContent,
  sidebarOpen = true,
  onToggleSidebar,
  readingWidth = 'full',
  onReadingWidthChange,
  fontScale = 100,
  onFontScaleChange,
}: ContentViewerProps) {
  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="text-center">
          <div className="w-12 h-12 mx-auto mb-4 border-2 border-primary-500 border-t-transparent rounded-full animate-spin" />
          <p className="text-sm text-slate-500 dark:text-slate-400">Loading guide…</p>
        </div>
      </div>
    )
  }

  if (!content) {
    return (
      <div className="flex items-center justify-center min-h-[60vh] px-6">
        <div className="text-center max-w-md">
          <Book className="w-14 h-14 mx-auto mb-4 text-slate-300 dark:text-slate-600" />
          <h2 className="text-xl font-semibold text-slate-800 dark:text-slate-100 mb-2">
            Welcome to Tech Mastery
          </h2>
          <p className="text-slate-600 dark:text-slate-400 text-sm leading-relaxed">
            Open <strong>Start Here</strong> in the navigation panel, or use <strong>All guides</strong> in the
            header.
          </p>
        </div>
      </div>
    )
  }

  const isGitHubPages =
    typeof window !== 'undefined' && window.location.hostname === 'samba425.github.io'
  const basePath = isGitHubPages ? '/tech-mastery-notebooks' : ''
  const resolvedPdfUrl = content.pdfUrl
    ? content.pdfUrl.startsWith('http')
      ? content.pdfUrl
      : `${basePath}${content.pdfUrl}`
    : null

  const markdownBody = prepareMarkdownForDisplay(content.content || '')
  const containerClass =
    readingWidth === 'narrow'
      ? 'max-w-3xl mx-auto px-4 sm:px-6 lg:px-8'
      : 'w-full max-w-none px-4 sm:px-6 lg:px-10 xl:px-14 2xl:px-16'

  const withSectionRefs = (Tag: keyof JSX.IntrinsicElements) => {
    return ({ children, ...props }: React.HTMLAttributes<HTMLElement>) => {
      const Component = Tag as 'p'
      return <Component {...props}>{enrichChildren(children)}</Component>
    }
  }

  return (
    <div className={`py-5 lg:py-7 ${containerClass}`}>
      {onToggleSidebar && onReadingWidthChange && onFontScaleChange && (
        <ReadingToolbar
          sidebarOpen={sidebarOpen}
          onToggleSidebar={onToggleSidebar}
          readingWidth={readingWidth}
          onReadingWidthChange={onReadingWidthChange}
          fontScale={fontScale}
          onFontScaleChange={onFontScaleChange}
          title={stripEmojis(content.title)}
        />
      )}

      <article className="article-card rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 shadow-sm shadow-slate-200/40 dark:shadow-none overflow-hidden">
        <header className="px-6 sm:px-8 pt-8 pb-6 border-b border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900/80">
          <div className="flex items-start gap-4">
            <NavIconBox
              id={content.id}
              category={content.category}
              fileType={content.fileType}
              selected
            />
            <div className="min-w-0 flex-1">
          <h1 className="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white tracking-tight leading-tight">
            {stripEmojis(content.title)}
          </h1>
          {content.description && (
            <p className="mt-3 text-base text-slate-600 dark:text-slate-400 leading-relaxed">
              {content.description}
            </p>
          )}
          <div className="flex flex-wrap gap-3 mt-4 text-xs text-slate-500 dark:text-slate-400">
            {content.category && (
              <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-200/70 dark:bg-slate-800 capitalize">
                <Tag className="w-3.5 h-3.5" />
                {content.category}
              </span>
            )}
            {content.readTime && (
              <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-200/70 dark:bg-slate-800">
                <Clock className="w-3.5 h-3.5" />
                {content.readTime} min read
              </span>
            )}
            {content.badge && (
              <span className="inline-flex items-center px-2.5 py-1 rounded-full bg-slate-200/70 dark:bg-slate-800 text-slate-700 dark:text-primary-300 font-medium">
                {content.badge}
              </span>
            )}
          </div>
            </div>
          </div>
        </header>

        <div
          className="markdown-content px-6 sm:px-8 py-8"
          style={{ fontSize: `${fontScale}%` }}
        >
          {resolvedPdfUrl ? (
            <div className="space-y-4">
              <div className="flex flex-wrap gap-3">
                <a
                  href={resolvedPdfUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-4 py-2 text-sm font-medium bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
                >
                  Open PDF in new tab
                </a>
                <a
                  href={resolvedPdfUrl}
                  download
                  className="px-4 py-2 text-sm font-medium border border-slate-200 dark:border-slate-600 rounded-lg text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors"
                >
                  Download PDF
                </a>
              </div>
              <div className="w-full h-[75vh] border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                <iframe
                  src={`${resolvedPdfUrl}#toolbar=1&navpanes=1&scrollbar=1`}
                  title={content.title}
                  className="w-full h-full"
                />
              </div>
            </div>
          ) : (
            <ReactMarkdown
              remarkPlugins={[remarkGfm, remarkCustomHeadingId]}
              rehypePlugins={[rehypeSlug, rehypeHighlight]}
              components={{
                p: withSectionRefs('p'),
                li: withSectionRefs('li'),
                td: withSectionRefs('td'),
                th: withSectionRefs('th'),
                strong: withSectionRefs('strong'),
                em: withSectionRefs('em'),
                h1: withSectionRefs('h1'),
                h2: withSectionRefs('h2'),
                h3: withSectionRefs('h3'),
                h4: withSectionRefs('h4'),
                a: ({ href, children, ...props }) => {
                  if (href?.startsWith('#')) {
                    return (
                      <a
                        href={href}
                        onClick={(e) => {
                          e.preventDefault()
                          const id = href.replace('#', '')
                          const element = document.getElementById(id)
                          if (element) {
                            const container = element.closest('main')
                            const offset = 100
                            if (container) {
                              container.scrollTo({
                                top: element.offsetTop - offset,
                                behavior: 'smooth',
                              })
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
                  return (
                    <a href={href} target="_blank" rel="noopener noreferrer" {...props}>
                      {children}
                    </a>
                  )
                },
              }}
            >
              {markdownBody}
            </ReactMarkdown>
          )}
        </div>

        {(prevContent || nextContent) && (
          <footer className="px-6 sm:px-8 py-6 border-t border-slate-200 dark:border-slate-800 bg-slate-100 dark:bg-slate-900/50">
            <div className="grid sm:grid-cols-2 gap-3">
              {prevContent ? (
                <button
                  type="button"
                  onClick={() => onNavigate?.(prevContent)}
                  className="group flex items-center gap-3 p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 hover:border-primary-400 dark:hover:border-primary-600 hover:shadow-sm text-left transition-all"
                >
                  <ChevronLeft className="w-5 h-5 text-slate-400 group-hover:text-primary-500 flex-shrink-0" />
                  <div className="min-w-0">
                    <div className="text-[10px] font-semibold uppercase tracking-wider text-slate-400">
                      Previous
                    </div>
                    <div className="text-sm font-medium text-slate-800 dark:text-slate-100 truncate">
                      {stripEmojis(prevContent.title)}
                    </div>
                  </div>
                </button>
              ) : (
                <div />
              )}
              {nextContent ? (
                <button
                  type="button"
                  onClick={() => onNavigate?.(nextContent)}
                  className="group flex items-center justify-end gap-3 p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 hover:border-primary-300 dark:hover:border-primary-700 hover:shadow-sm text-right transition-all sm:col-start-2"
                >
                  <div className="min-w-0">
                    <div className="text-[10px] font-semibold uppercase tracking-wider text-slate-400">
                      Next
                    </div>
                    <div className="text-sm font-medium text-slate-800 dark:text-slate-100 truncate">
                      {stripEmojis(nextContent.title)}
                    </div>
                  </div>
                  <ChevronRight className="w-5 h-5 text-slate-400 group-hover:text-primary-500 flex-shrink-0" />
                </button>
              ) : null}
            </div>
          </footer>
        )}
      </article>
    </div>
  )
}

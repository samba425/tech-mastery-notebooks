export type ReadingWidth = 'comfortable' | 'wide'

const KEYS = {
  sidebar: 'tm-sidebar-open',
  readingWidth: 'tm-reading-width',
  fontScale: 'tm-font-scale',
} as const

export function loadSidebarOpen(): boolean {
  if (typeof window === 'undefined') return true
  const v = localStorage.getItem(KEYS.sidebar)
  return v === null ? true : v === 'true'
}

export function saveSidebarOpen(open: boolean) {
  if (typeof window === 'undefined') return
  localStorage.setItem(KEYS.sidebar, String(open))
}

export function loadReadingWidth(): ReadingWidth {
  if (typeof window === 'undefined') return 'comfortable'
  const v = localStorage.getItem(KEYS.readingWidth)
  return v === 'wide' ? 'wide' : 'comfortable'
}

export function saveReadingWidth(width: ReadingWidth) {
  if (typeof window === 'undefined') return
  localStorage.setItem(KEYS.readingWidth, width)
}

export function loadFontScale(): number {
  if (typeof window === 'undefined') return 100
  const n = Number(localStorage.getItem(KEYS.fontScale))
  return n === 110 || n === 125 ? n : 100
}

export function saveFontScale(scale: number) {
  if (typeof window === 'undefined') return
  localStorage.setItem(KEYS.fontScale, String(scale))
}

export type ReadingWidth = 'full' | 'narrow'

export type ThemeMode = 'light' | 'dark' | 'system'

const KEYS = {
  sidebar: 'tm-sidebar-open',
  readingWidth: 'tm-reading-width',
  fontScale: 'tm-font-scale',
  theme: 'tm-theme',
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
  if (typeof window === 'undefined') return 'full'
  const v = localStorage.getItem(KEYS.readingWidth)
  if (v === 'narrow' || v === 'comfortable') return 'narrow'
  if (v === 'full' || v === 'wide') return 'full'
  return 'full'
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

export function loadTheme(): ThemeMode {
  if (typeof window === 'undefined') return 'system'
  const v = localStorage.getItem(KEYS.theme)
  if (v === 'light' || v === 'dark' || v === 'system') return v
  return 'system'
}

export function saveTheme(theme: ThemeMode) {
  if (typeof window === 'undefined') return
  localStorage.setItem(KEYS.theme, theme)
}

export function resolveDark(theme: ThemeMode): boolean {
  if (theme === 'dark') return true
  if (theme === 'light') return false
  if (typeof window === 'undefined') return false
  return window.matchMedia('(prefers-color-scheme: dark)').matches
}

export function applyTheme(theme: ThemeMode) {
  if (typeof document === 'undefined') return
  const isDark = resolveDark(theme)
  document.documentElement.classList.toggle('dark', isDark)
}

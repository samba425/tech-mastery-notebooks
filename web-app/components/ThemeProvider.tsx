'use client'

import { createContext, useContext, useEffect, useState, useCallback } from 'react'
import {
  applyTheme,
  loadTheme,
  saveTheme,
  type ThemeMode,
} from '@/lib/uiPreferences'

interface ThemeContextValue {
  theme: ThemeMode
  setTheme: (mode: ThemeMode) => void
  cycleTheme: () => void
  isDark: boolean
}

const ThemeContext = createContext<ThemeContextValue | null>(null)

export function useTheme() {
  const ctx = useContext(ThemeContext)
  if (!ctx) throw new Error('useTheme must be used within ThemeProvider')
  return ctx
}

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setThemeState] = useState<ThemeMode>('system')
  const [isDark, setIsDark] = useState(false)
  const [mounted, setMounted] = useState(false)

  const setTheme = useCallback((mode: ThemeMode) => {
    setThemeState(mode)
    saveTheme(mode)
    applyTheme(mode)
    setIsDark(mode === 'dark' || (mode === 'system' && resolveDarkClient()))
  }, [])

  const cycleTheme = useCallback(() => {
    const order: ThemeMode[] = ['light', 'dark', 'system']
    const i = order.indexOf(theme)
    const next = order[(i + 1) % order.length]
    setTheme(next)
  }, [theme, setTheme])

  useEffect(() => {
    const initial = loadTheme()
    setThemeState(initial)
    applyTheme(initial)
    setIsDark(
      initial === 'dark' || (initial === 'system' && resolveDarkClient())
    )
    setMounted(true)

    const mq = window.matchMedia('(prefers-color-scheme: dark)')
    const onChange = () => {
      const current = loadTheme()
      if (current === 'system') {
        applyTheme('system')
        setIsDark(mq.matches)
      }
    }
    mq.addEventListener('change', onChange)
    return () => mq.removeEventListener('change', onChange)
  }, [])

  return (
    <ThemeContext.Provider value={{ theme, setTheme, cycleTheme, isDark: mounted ? isDark : false }}>
      {children}
    </ThemeContext.Provider>
  )
}

function resolveDarkClient() {
  return window.matchMedia('(prefers-color-scheme: dark)').matches
}

/** Inline in layout <head> to avoid flash of wrong theme */
export const themeInitScript = `
(function() {
  try {
    var t = localStorage.getItem('tm-theme');
    var dark = t === 'dark' || (t !== 'light' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    if (dark) document.documentElement.classList.add('dark');
    else document.documentElement.classList.remove('dark');
  } catch (e) {}
})();
`

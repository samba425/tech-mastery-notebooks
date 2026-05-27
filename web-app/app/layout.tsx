import './globals.css'
import type { Metadata } from 'next'
import { Inter, Source_Serif_4 } from 'next/font/google'
import { ThemeProvider, themeInitScript } from '@/components/ThemeProvider'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-sans',
  display: 'swap',
})

const sourceSerif = Source_Serif_4({
  subsets: ['latin'],
  variable: '--font-serif',
  display: 'swap',
})

export const metadata: Metadata = {
  title: 'Tech Mastery Platform - Complete Learning Hub',
  description: 'Comprehensive guides for Python, JavaScript, TypeScript, AI/ML, DevOps, and more',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning className={`${inter.variable} ${sourceSerif.variable}`}>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeInitScript }} />
      </head>
      <body className="font-sans antialiased bg-slate-100 dark:bg-slate-950 text-slate-900 dark:text-slate-100">
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  )
}

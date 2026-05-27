import './globals.css'
import type { Metadata } from 'next'
import { Inter, Source_Serif_4 } from 'next/font/google'

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
    <html lang="en" className={`${inter.variable} ${sourceSerif.variable}`}>
      <body className="font-sans antialiased">{children}</body>
    </html>
  )
}

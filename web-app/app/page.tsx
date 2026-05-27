'use client'

import { Suspense } from 'react'
import AppShell from '@/components/AppShell'

export default function Home() {
  return (
    <Suspense
      fallback={
        <div className="flex items-center justify-center h-screen bg-slate-50 dark:bg-slate-950">
          <div className="w-10 h-10 border-2 border-primary-500 border-t-transparent rounded-full animate-spin" />
        </div>
      }
    >
      <AppShell />
    </Suspense>
  )
}

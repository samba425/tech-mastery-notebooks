import { NextRequest, NextResponse } from 'next/server'
import { getContentStructure, type ContentItem } from '@/lib/contentLoader'
import { loadContentFromFile } from '@/lib/serverContentLoader'

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url)
  const id = searchParams.get('id')

  if (!id) {
    // Return structure
    const structure = getContentStructure()
    return NextResponse.json(structure)
  }

  // Find and return specific content
  const structure = getContentStructure()
  
  const findContent = (items: any[], targetId: string): ContentItem | null => {
    for (const item of items) {
      if (item.id === targetId) {
        // Load content from file if path exists
        if (item.path) {
          const content = loadContentFromFile(item.path)
          return {
            ...item,
            content
          }
        }
        return item
      }
      if (item.children) {
        const found = findContent(item.children, targetId)
        if (found) return found
      }
    }
    return null
  }

  const content = findContent(structure, id)

  if (!content) {
    return NextResponse.json({ error: 'Content not found' }, { status: 404 })
  }

  return NextResponse.json(content)
}

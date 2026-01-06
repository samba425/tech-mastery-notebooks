import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

// Load content from file - SERVER SIDE ONLY
export function loadContentFromFile(relativePath: string): string {
  try {
    const fullPath = path.join(process.cwd(), relativePath)
    
    // Check if file exists
    if (!fs.existsSync(fullPath)) {
      return `# Content Not Found\n\nThe file at \`${relativePath}\` could not be found.\n\nPath: ${fullPath}`
    }

    const fileContent = fs.readFileSync(fullPath, 'utf8')
    
    // Handle Jupyter Notebooks (.ipynb files)
    if (relativePath.endsWith('.ipynb')) {
      try {
        const notebook = JSON.parse(fileContent)
        let markdownContent = ''
        
        if (notebook.cells && Array.isArray(notebook.cells)) {
          notebook.cells.forEach((cell: any, index: number) => {
            if (cell.cell_type === 'markdown') {
              // Add markdown cells directly
              const cellContent = Array.isArray(cell.source) ? cell.source.join('') : cell.source
              markdownContent += cellContent + '\n\n'
            } else if (cell.cell_type === 'code') {
              // Add code cells with syntax highlighting
              const cellContent = Array.isArray(cell.source) ? cell.source.join('') : cell.source
              const language = cell.metadata?.language || notebook.metadata?.language_info?.name || 'python'
              markdownContent += `\`\`\`${language}\n${cellContent}\n\`\`\`\n\n`
              
              // Add output if available
              if (cell.outputs && cell.outputs.length > 0) {
                cell.outputs.forEach((output: any) => {
                  if (output.output_type === 'stream') {
                    const text = Array.isArray(output.text) ? output.text.join('') : output.text
                    markdownContent += `**Output:**\n\`\`\`\n${text}\n\`\`\`\n\n`
                  } else if (output.output_type === 'execute_result' || output.output_type === 'display_data') {
                    if (output.data && output.data['text/plain']) {
                      const text = Array.isArray(output.data['text/plain']) ? output.data['text/plain'].join('') : output.data['text/plain']
                      markdownContent += `**Result:**\n\`\`\`\n${text}\n\`\`\`\n\n`
                    }
                  }
                })
              }
            }
          })
        }
        
        return markdownContent || '# Empty Notebook\n\nThis notebook has no content yet.'
      } catch (error) {
        return `# Error Parsing Notebook\n\nFailed to parse Jupyter notebook: ${error}`
      }
    }
    
    // For Python/JS/TS files, wrap in code block
    if (relativePath.endsWith('.py') || relativePath.endsWith('.js') || relativePath.endsWith('.ts')) {
      const lang = relativePath.endsWith('.py') ? 'python' : relativePath.endsWith('.ts') ? 'typescript' : 'javascript'
      return `# Code Examples\n\n\`\`\`${lang}\n${fileContent}\n\`\`\``
    }
    
    // Try to parse front matter for markdown
    try {
      const { data, content } = matter(fileContent)
      return content
    } catch {
      return fileContent
    }
  } catch (error) {
    return `# Error Loading Content\n\nThere was an error loading the content: ${error}\n\nPath: ${relativePath}`
  }
}

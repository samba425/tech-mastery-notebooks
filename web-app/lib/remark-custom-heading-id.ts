import { visit } from 'unist-util-visit'
import type { Plugin } from 'unified'
import type { Root } from 'mdast'

/**
 * Remark plugin to extract custom heading IDs from {#id} syntax
 * Transforms: ## My Heading {#custom-id}
 * Into a heading with data.hProperties.id = 'custom-id'
 */
const remarkCustomHeadingId: Plugin<[], Root> = () => {
  return (tree) => {
    visit(tree, 'heading', (node: any) => {
      const lastChild = node.children[node.children.length - 1]
      
      if (lastChild && lastChild.type === 'text') {
        const text = lastChild.value as string
        const match = text.match(/\s*\{#([a-zA-Z0-9_-]+)\}\s*$/)
        
        if (match) {
          const id = match[1]
          
          // Remove the {#id} from the text
          lastChild.value = text.replace(/\s*\{#([a-zA-Z0-9_-]+)\}\s*$/, '')
          
          // Add the custom ID to the heading
          if (!node.data) {
            node.data = {}
          }
          if (!node.data.hProperties) {
            node.data.hProperties = {}
          }
          node.data.hProperties.id = id
        }
      }
    })
  }
}

export default remarkCustomHeadingId

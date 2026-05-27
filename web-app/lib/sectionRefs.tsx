import React from 'react'

const SECTION_REF_PATTERN = /§(\d+(?:\.\d+)?)/g

/** Render §N with a font stack that displays the section sign reliably. */
export function enrichTextWithSectionRefs(text: string): React.ReactNode[] {
  if (!text.includes('§')) {
    return [text]
  }

  const parts: React.ReactNode[] = []
  let lastIndex = 0
  let match: RegExpExecArray | null
  const re = new RegExp(SECTION_REF_PATTERN.source, 'g')

  while ((match = re.exec(text)) !== null) {
    if (match.index > lastIndex) {
      parts.push(text.slice(lastIndex, match.index))
    }
    parts.push(
      <span key={`sec-${match.index}`} className="section-ref" title={`Section ${match[1]}`}>
        §{match[1]}
      </span>
    )
    lastIndex = match.index + match[0].length
  }

  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex))
  }

  return parts.length > 0 ? parts : [text]
}

export function enrichChildren(children: React.ReactNode): React.ReactNode {
  return React.Children.map(children, (child) => {
    if (typeof child === 'string') {
      return enrichTextWithSectionRefs(child)
    }

    if (React.isValidElement(child)) {
      const childProps = child.props as { children?: React.ReactNode }
      if (childProps.children !== undefined) {
        return React.cloneElement(child, {
          ...childProps,
          children: enrichChildren(childProps.children),
        } as React.Attributes)
      }
    }

    return child
  })
}

/** Table cells starting with § often render blank — use Sec. N in tables only. */
export function prepareMarkdownForDisplay(markdown: string): string {
  return markdown.replace(/\| §(\d+(?:\.\d+)?)/g, '| Sec. $1')
}

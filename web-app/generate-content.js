const fs = require('fs');
const path = require('path');

// Import content structure directly (avoiding TS modules)
function getContentStructure() {
  // This is a simplified version - we'll copy the structure here
  return [
    {
      id: 'readme',
      title: '🏠 Welcome & Getting Started',
      path: '../README.md',
    },
    {
      id: 'start-here',
      title: '🚀 Quick Start Guide',
      path: '../START-HERE.md',
    },
    // Add more items as needed - for now let's just handle these two
  ];
}

function loadContentFromFile(relativePath) {
  try {
    const fullPath = path.join(__dirname, relativePath);
    
    if (!fs.existsSync(fullPath)) {
      return `# Content Not Found\n\nThe file at \`${relativePath}\` could not be found.`;
    }

    const fileContent = fs.readFileSync(fullPath, 'utf8');
    
    // Handle Jupyter Notebooks
    if (relativePath.endsWith('.ipynb')) {
      try {
        const notebook = JSON.parse(fileContent);
        let markdownContent = '';
        
        if (notebook.cells && Array.isArray(notebook.cells)) {
          notebook.cells.forEach((cell) => {
            if (cell.cell_type === 'markdown') {
              const cellContent = Array.isArray(cell.source) ? cell.source.join('') : cell.source;
              markdownContent += cellContent + '\n\n';
            } else if (cell.cell_type === 'code') {
              const cellContent = Array.isArray(cell.source) ? cell.source.join('') : cell.source;
              const language = cell.metadata?.language || notebook.metadata?.language_info?.name || 'python';
              markdownContent += `\`\`\`${language}\n${cellContent}\n\`\`\`\n\n`;
            }
          });
        }
        
        return markdownContent || '# Empty Notebook';
      } catch (error) {
        return `# Error Parsing Notebook\n\nFailed to parse: ${error.message}`;
      }
    }
    
    // For Python/JS/TS files, wrap in code block
    if (relativePath.endsWith('.py') || relativePath.endsWith('.js') || relativePath.endsWith('.ts')) {
      const lang = relativePath.endsWith('.py') ? 'python' : relativePath.endsWith('.ts') ? 'typescript' : 'javascript';
      return `# Code Examples\n\n\`\`\`${lang}\n${fileContent}\n\`\`\``;
    }
    
    return fileContent;
  } catch (error) {
    return `# Error Loading Content\n\nError: ${error.message}`;
  }
}

// Pre-generate simple welcome content
function generateStaticContent() {
  const outputDir = path.join(__dirname, 'public', 'content');
  
  // Create output directory
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  // Generate a simple welcome message
  const welcomeContent = {
    id: 'readme',
    title: '🏠 Welcome & Getting Started',
    content: `# 🎉 Tech Mastery Platform\n\nWelcome to your complete learning platform!\n\nThis platform contains 45,000+ lines of educational content including:\n\n- System Design (HLD/LLD)\n- AI/ML Guides\n- Programming Languages\n- DevOps & Infrastructure\n\nSelect a guide from the sidebar to start learning! 🚀`
  };
  
  const outputPath = path.join(outputDir, 'readme.json');
  fs.writeFileSync(outputPath, JSON.stringify(welcomeContent));
  console.log('✓ Generated welcome content');
}

generateStaticContent();

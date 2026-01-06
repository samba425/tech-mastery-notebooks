const fs = require('fs');
const path = require('path');

// Import content structure directly (avoiding TS modules)
function getContentStructure() {
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
    {
      id: 'python-guide',
      title: '🐍 Python Complete Guide',
      path: '../guides/Python-Complete-Guide.md',
    },
    {
      id: 'javascript-guide',
      title: '⚡ JavaScript Complete Guide',
      path: '../guides/JavaScript-Complete-Guide.md',
    },
    {
      id: 'typescript-guide',
      title: '📘 TypeScript Complete Guide',
      path: '../guides/TypeScript-Complete-Guide.md',
    },
    {
      id: 'docker-guide',
      title: '🐳 Docker Zero to Hero',
      path: '../guides/Docker-Zero-to-Hero.md',
    },
    {
      id: 'kubernetes-guide',
      title: '☸️ Kubernetes Zero to Hero',
      path: '../guides/Kubernetes-Zero-to-Hero.md',
    },
    {
      id: 'terraform-guide',
      title: '🏗️ Terraform Complete Mastery',
      path: '../guides/Terraform-Complete-Mastery-Guide.md',
    },
    {
      id: 'terraform-part2',
      title: '🏗️ Terraform Mastery Part 2',
      path: '../guides/Terraform-Complete-Mastery-Guide-Part2.md',
    },
    {
      id: 'terraform-zero-hero',
      title: '🏗️ Terraform Zero to Hero',
      path: '../guides/Terraform-Zero-to-Hero.md',
    },
    {
      id: 'ansible-guide',
      title: '📦 Ansible Zero to Hero',
      path: '../guides/Ansible-Zero-to-Hero.md',
    },
    {
      id: 'ai-agents',
      title: '🤖 AI Agents Complete Guide',
      path: '../guides/ai_ml/AI-Agents-Complete-Guide.md',
    },
    {
      id: 'build-models',
      title: '🔬 Build ML Models From Scratch',
      path: '../guides/ai_ml/Build-ML-Models-From-Scratch-Complete-Guide.md',
    },
    {
      id: 'computer-vision',
      title: '👁️ Computer Vision Complete Guide',
      path: '../guides/ai_ml/Computer-Vision-Complete-Guide.md',
    },
    {
      id: 'feature-engineering',
      title: '⚙️ Feature Engineering Complete Guide',
      path: '../guides/ai_ml/Feature-Engineering-Complete-Guide.md',
    },
    {
      id: 'mlops-guide',
      title: '🚀 MLOps Production Complete Guide',
      path: '../guides/ai_ml/MLOps-Production-Complete-Guide.md',
    },
    {
      id: 'nlp-guide',
      title: '📝 NLP Complete Guide',
      path: '../guides/ai_ml/NLP-Complete-Guide.md',
    },
    {
      id: 'master-roadmap',
      title: '🗺️ ML/DS Complete Roadmap',
      path: '../guides/ai_ml/MASTER-ML-DS-COMPLETE-ROADMAP.md',
    },
    {
      id: 'ml-quick-ref',
      title: '📋 ML/DS Quick Reference',
      path: '../guides/ai_ml/ML-DS-QUICK-REFERENCE-CHEATSHEET.md',
    },
    {
      id: 'llm-interview',
      title: '💬 LLM Interview Questions',
      path: '../guides/ai_ml/LLM-Interview-Questions-Complete.md',
    },
    {
      id: 'rag-interview',
      title: '� RAG Interview Questions',
      path: '../guides/ai_ml/RAG-Interview-Questions-Complete.md',
    },
    {
      id: 'learning-order',
      title: '📚 ML Learning Order Guide',
      path: '../guides/ai_ml/LEARNING-ORDER-GUIDE.md',
    },
    {
      id: 'complete-system-design',
      title: '📖 Complete System Design Guide',
      path: '../system-design/COMPLETE-SYSTEM-DESIGN-GUIDE.md',
    },
    {
      id: 'system-architecture',
      title: '🏛️ System Architecture Patterns',
      path: '../system-design/architecture/system-architecture-patterns.ipynb',
    },
    {
      id: 'system-hld',
      title: '🎯 High-Level Design (HLD)',
      path: '../system-design/hld/system-design-hld.ipynb',
    },
    {
      id: 'system-lld',
      title: '🔧 Low-Level Design (LLD)',
      path: '../system-design/lld/system-design-lld.ipynb',
    },
    {
      id: 'python-challenges',
      title: '🎯 Python Challenges',
      path: '../programming-challenges/python.challenges.ipynb',
    },
    {
      id: 'js-challenges',
      title: '🎯 JavaScript Challenges',
      path: '../programming-challenges/javascript.challenges.ipynb',
    },
    {
      id: 'ai-ml-systems',
      title: '🧠 AI/ML Systems',
      path: '../infrastructure/ai-ml-systems.ipynb',
    },
    {
      id: 'cloud-devops',
      title: '☁️ Cloud & DevOps',
      path: '../infrastructure/cloud-devops.ipynb',
    },
    {
      id: 'database-design',
      title: '💾 Database Design',
      path: '../infrastructure/database-design.ipynb',
    },
    {
      id: 'python-code',
      title: '🐍 Python Code Examples',
      path: '../code-examples/python-mastery-guide.py',
    },
    {
      id: 'javascript-code',
      title: '⚡ JavaScript Code Examples',
      path: '../code-examples/javascript-mastery-guide.js',
    },
    {
      id: 'typescript-code',
      title: '📘 TypeScript Code Examples',
      path: '../code-examples/typescript-mastery-guide.ts',
    },
    {
      id: 'career-roadmap',
      title: '🎯 Career Roadmap',
      path: '../docs/career-roadmap.md',
    },
    {
      id: 'interview-guide',
      title: '💼 Interview Guide',
      path: '../docs/interview-guide.md',
    },
    {
      id: 'fullstack-training',
      title: '🌐 Full Stack Developer Training',
      path: '../Full_Stack_Developer_Training_Notes.md',
    },
    {
      id: 'vedic-math',
      title: '🔢 Vedic Mathematics',
      path: '../vedic-mathematics-zero-to-hero.md',
    },
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

// Pre-generate content for all items
function generateStaticContent() {
  const outputDir = path.join(__dirname, 'public', 'content');
  
  // Create output directory
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const contentItems = getContentStructure();
  let successCount = 0;
  let errorCount = 0;
  
  console.log(`Generating content for ${contentItems.length} items...`);
  
  contentItems.forEach(item => {
    try {
      const content = loadContentFromFile(item.path);
      const contentData = {
        id: item.id,
        title: item.title,
        content: content
      };
      
      const outputPath = path.join(outputDir, `${item.id}.json`);
      fs.writeFileSync(outputPath, JSON.stringify(contentData));
      successCount++;
      console.log(`✓ Generated: ${item.id}`);
    } catch (error) {
      errorCount++;
      console.error(`✗ Failed to generate ${item.id}: ${error.message}`);
    }
  });
  
  console.log(`\n✓ Successfully generated ${successCount}/${contentItems.length} content files`);
  if (errorCount > 0) {
    console.log(`✗ Failed: ${errorCount} files`);
  }
}

generateStaticContent();

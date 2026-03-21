const fs = require('fs');
const path = require('path');

// Import content structure directly (avoiding TS modules)
function getContentStructure() {
  return [
    { id: 'readme', title: '🏠 Welcome & Getting Started', path: '../README.md' },
    { id: 'start-here', title: '🚀 Quick Start Guide', path: '../START-HERE.md' },
    { id: 'python-guide', title: '🐍 Python Complete Guide', path: '../guides/Python-Complete-Guide.md' },
    { id: 'javascript-guide', title: '⚡ JavaScript Complete Guide', path: '../guides/JavaScript-Complete-Guide.md' },
    { id: 'typescript-guide', title: '📘 TypeScript Complete Guide', path: '../guides/TypeScript-Complete-Guide.md' },
    { id: 'python-code', title: '🐍 Python Code Examples', path: '../code-examples/python-mastery-guide.py' },
    { id: 'javascript-code', title: '⚡ JavaScript Code Examples', path: '../code-examples/javascript-mastery-guide.js' },
    { id: 'typescript-code', title: '📘 TypeScript Code Examples', path: '../code-examples/typescript-mastery-guide.ts' },
    { id: 'docker-guide', title: '🐳 Docker Zero to Hero', path: '../guides/Docker-Zero-to-Hero.md' },
    { id: 'terraform-guide', title: '🏗️ Terraform Zero to Hero', path: '../guides/Terraform-Zero-to-Hero.md' },
    { id: 'terraform-complete', title: '🏗️ Terraform Complete Mastery', path: '../guides/Terraform-Complete-Mastery-Guide.md' },
    { id: 'terraform-part2', title: '🏗️ Terraform Mastery Part 2', path: '../guides/Terraform-Complete-Mastery-Guide-Part2.md' },
    { id: 'ansible-guide', title: '📦 Ansible Zero to Hero', path: '../guides/Ansible-Zero-to-Hero.md' },
    { id: 'master-roadmap', title: '🗺️ ML/DS Complete Roadmap', path: '../guides/ai_ml/MASTER-ML-DS-COMPLETE-ROADMAP.md' },
    { id: 'learning-order', title: '📚 ML Learning Order Guide', path: '../guides/ai_ml/LEARNING-ORDER-GUIDE.md' },
    { id: 'ml-quick-ref', title: '📋 ML/DS Quick Reference', path: '../guides/ai_ml/ML-DS-QUICK-REFERENCE-CHEATSHEET.md' },
    { id: 'build-models', title: '🔬 Build ML Models From Scratch', path: '../guides/ai_ml/Build-ML-Models-From-Scratch-Complete-Guide.md' },
    { id: 'feature-engineering', title: '⚙️ Feature Engineering Complete Guide', path: '../guides/ai_ml/Feature-Engineering-Complete-Guide.md' },
    { id: 'nlp-guide', title: '📝 NLP Complete Guide', path: '../guides/ai_ml/NLP-Complete-Guide.md' },
    { id: 'computer-vision', title: '👁️ Computer Vision Complete Guide', path: '../guides/ai_ml/Computer-Vision-Complete-Guide.md' },
    { id: 'mlops-guide', title: '🚀 MLOps Production Complete Guide', path: '../guides/ai_ml/MLOps-Production-Complete-Guide.md' },
    { id: 'ai-agents', title: '🤖 AI Agents Complete Guide', path: '../guides/ai_ml/AI-Agents-Complete-Guide.md' },
    { id: 'llm-interview', title: '💬 LLM Interview Questions', path: '../guides/ai_ml/LLM-Interview-Questions-Complete.md' },
    { id: 'rag-interview', title: '🔍 RAG Interview Questions', path: '../guides/ai_ml/RAG-Interview-Questions-Complete.md' },
    { id: 'ai-ml-systems', title: '🧠 AI/ML Systems', path: '../infrastructure/ai-ml-systems.ipynb' },
    { id: 'cloud-devops', title: '☁️ Cloud & DevOps', path: '../infrastructure/cloud-devops.ipynb' },
    { id: 'database-design', title: '💾 Database Design', path: '../infrastructure/database-design.ipynb' },
    { id: 'complete-system-design', title: '📖 Complete System Design Guide', path: '../system-design/COMPLETE-SYSTEM-DESIGN-GUIDE.md' },
    { id: 'system-architecture', title: '🏛️ System Architecture Patterns', path: '../system-design/architecture/system-architecture-patterns.ipynb' },
    { id: 'hld-guide', title: '🎯 High-Level Design (HLD)', path: '../system-design/hld/system-design-hld.ipynb' },
    { id: 'lld-guide', title: '🔧 Low-Level Design (LLD)', path: '../system-design/lld/system-design-lld.ipynb' },
    { id: 'python-challenges', title: '🎯 Python Challenges', path: '../programming-challenges/python.challenges.ipynb' },
    { id: 'javascript-challenges', title: '🎯 JavaScript Challenges', path: '../programming-challenges/javascript.challenges.ipynb' },
    { id: 'career-roadmap', title: '🎯 Career Roadmap', path: '../docs/career-roadmap.md' },
    { id: 'interview-guide', title: '💼 Interview Guide', path: '../docs/interview-guide.md' },
    { id: 'master-roadmap-career', title: '🗺️ ML/DS Career Complete Roadmap', path: '../guides/ai_ml/MASTER-ML-DS-COMPLETE-ROADMAP.md' },
    { id: 'llm-interview-career', title: '💬 LLM Interview Questions', path: '../guides/ai_ml/LLM-Interview-Questions-Complete.md' },
    { id: 'rag-interview-career', title: '🔍 RAG Interview Questions', path: '../guides/ai_ml/RAG-Interview-Questions-Complete.md' },
    { id: 'system-design-career', title: '📖 Complete System Design Guide', path: '../system-design/COMPLETE-SYSTEM-DESIGN-GUIDE.md' },
    { id: 'python-challenges-career', title: '🎯 Python Coding Challenges', path: '../programming-challenges/python.challenges.ipynb' },
    { id: 'javascript-challenges-career', title: '🎯 JavaScript Coding Challenges', path: '../programming-challenges/javascript.challenges.ipynb' },
    { id: 'teaching-plan', title: '🎓 Python Teaching Plan (12 Days)', path: '../pythonclass/Python_Teaching_Plan_12_Days.md' },
    { id: 'part1-fundamentals', title: '📘 Part 1: Python Fundamentals (Hours 1-10)', path: '../pythonclass/Part1_Python_Fundamentals_Hours_1-10.md' },
    { id: 'part2-backend', title: '🔧 Part 2: Backend Development (Hours 11-20)', path: '../pythonclass/Part2_Backend_Development_Hours_11-20.md' },
    { id: 'part3-frontend', title: '🎨 Part 3: Frontend Development (Hours 21-30)', path: '../pythonclass/Part3_Frontend_Development_Hours_21-30.md' },
    { id: 'part4-advanced', title: '🚀 Part 4: Advanced Backend (Hours 31-40)', path: '../pythonclass/Part4_Advanced_Backend_Hours_31-40.md' },
    { id: 'python-demos', title: '🎮 Python Full-Stack Live Demos (21 Projects)', path: '../pythonclass/demo-projects/PYTHON-DEMOS.md' },
    { id: 'vedic-math', title: '🔢 Vedic Mathematics', path: '../vedic-mathematics-zero-to-hero.md' },
    
    // Big Data & Analytics Category
    { id: 'data-engineering', title: '🗄️ Data Engineering Zero to Hero', path: '../guides/big-data-analytics/Data-Engineering-Zero-to-Hero.md' },
    
    // Architecture & Design Category
    { id: 'event-driven-arch', title: '🏗️ Event-Driven Architecture Zero to Hero', path: '../guides/architecture-design/Event-Driven-Architecture-Zero-to-Hero.md' },
    { id: 'microservices', title: '🔧 Microservices Architecture Complete Guide', path: '../guides/architecture-design/microservices-complete-guide.md' },
    { id: 'kafka-queues', title: '📨 Kafka & Message Queues Zero to Hero', path: '../guides/architecture-design/kafka-message-queues-zero-to-hero.md' },
    
    // DevOps & Infrastructure Category
    { id: 'kubernetes-guide', title: '☸️ Kubernetes Zero to Hero', path: '../guides/devops-infrastructure/Kubernetes-Zero-to-Hero.md' },
    { id: 'load-balancing-ha', title: '🚀 Load Balancing & High Availability Zero to Hero', path: '../guides/devops-infrastructure/Load-Balancing-High-Availability-Zero-to-Hero.md' },
    { id: 'cicd-guide', title: '🔄 CI/CD Zero to Hero', path: '../guides/devops-infrastructure/cicd-zero-to-hero.md' },
    
    // Performance Engineering Category
    { id: 'performance-optimization', title: '⚡ Performance Optimization Complete Guide', path: '../guides/performance-engineering/Performance-Optimization-Complete-Guide.md' },
    
    // Cloud Platforms Category
  { id: 'aws-cloud', title: '☁️ AWS Cloud Zero to Hero', path: '../guides/cloud-platforms/aws-cloud-zero-to-hero.md' },
  { id: 'aws-cert-index', title: '📚 AWS Certification Master Guide', path: '../guides/cloud-platforms/README-AWS-Certifications.md' },
  { id: 'aws-cloud-practitioner', title: '📖 AWS Cloud Practitioner (CLF-C02)', path: '../guides/cloud-platforms/AWS-Cloud-Practitioner-Complete-Guide.md' },
  { id: 'aws-solutions-architect', title: '🏗️ AWS Solutions Architect (SAA-C03)', path: '../guides/cloud-platforms/AWS-Solutions-Architect-Associate-Guide.md' },
  { id: 'aws-saa-c03-solutions', title: 'AWS SAA-C03 Solutions Guide', path: '../guides/cloud-platforms/AWS_SAA-C03_Solutions.md' },
  { id: 'aws-quick-reference', title: '⚡ AWS Exam Quick Reference', path: '../guides/cloud-platforms/AWS-Exam-Quick-Reference-Cheatsheet.md' },
  { id: 'aws-roadmap', title: '🗺️ AWS Certification Roadmap', path: '../docs/aws-certification-roadmap.md' },
  { id: 'azure-cloud', title: '☁️ Azure Cloud Zero to Hero', path: '../guides/cloud-platforms/azure-cloud-zero-to-hero.md' },
    
    // Backend Development Category
    { id: 'nodejs-express', title: '🟢 Node.js & Express Zero to Hero', path: '../guides/backend-development/nodejs-express-zero-to-hero.md' },
    { id: 'rest-api', title: '🌐 REST API Development Zero to Hero', path: '../guides/backend-development/rest-api-development-zero-to-hero.md' },
    
    // Frontend Development Category
    { id: 'react-frontend', title: '⚛️ React Frontend Zero to Hero', path: '../guides/frontend-development/react-frontend-zero-to-hero.md' },
    { id: 'nextjs', title: '▲ Next.js Zero to Hero', path: '../guides/frontend-development/nextjs-zero-to-hero.md' },
    { id: 'flutter-dart', title: '📱 Flutter & Dart Complete Guide', path: '../guides/frontend-development/Flutter-Dart-Complete-Guide.md' },
    { id: 'fullstack-notes', title: '🌐 Full Stack Developer Training', path: '../guides/frontend-development/Full_Stack_Developer_Training_Notes.md' },
    
    // Databases Category
    { id: 'mongodb', title: '🍃 MongoDB Zero to Hero', path: '../guides/databases/mongodb-zero-to-hero.md' },
    { id: 'sql-databases', title: '💾 SQL Databases Zero to Hero', path: '../guides/databases/sql-databases-zero-to-hero.md' },
    { id: 'redis-caching', title: '🔴 Redis & Caching Zero to Hero', path: '../guides/databases/redis-caching-zero-to-hero.md' },
    
    // Fundamentals Category
    { id: 'dsa-zero-to-hero', title: '📊 DSA Zero to Hero', path: '../guides/fundamentals/data-structures-algorithms-zero-to-hero.md' },
    { id: 'git-github', title: '🌿 Git & GitHub Zero to Hero', path: '../guides/fundamentals/git-github-zero-to-hero.md' },
    { id: 'linux-cli', title: '🐧 Linux Command Line Zero to Hero', path: '../guides/fundamentals/linux-command-line-zero-to-hero.md' },
    
    // Security & Testing Category
    { id: 'security-practices', title: '🔒 Security Best Practices Zero to Hero', path: '../guides/security-testing/security-best-practices-zero-to-hero.md' },
    { id: 'testing-tdd', title: '🧪 Testing & TDD Zero to Hero', path: '../guides/security-testing/testing-tdd-zero-to-hero.md' },
    
    // LeetCode & Coding Challenges
    { id: 'leetcode-solutions', title: '💻 LeetCode Solutions', path: '../code-examples/leetcode_solve.md' },
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

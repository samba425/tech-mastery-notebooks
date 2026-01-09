export interface ContentItem {
  id: string
  title: string
  description?: string
  path?: string
  content?: string
  category?: string
  readTime?: number
  badge?: string
  children?: ContentItem[]
}

// This is the content structure - manually defined for better organization
// Content will be loaded server-side via API routes
export function getContentStructure(): any[] {
  return [
    {
      id: 'readme',
      title: '🏠 Welcome & Getting Started',
      path: '../README.md',
      category: 'overview',
      badge: 'Start Here',
      description: 'Your complete guide to the Tech Mastery Platform'
    },
    {
      id: 'start-here',
      title: '🚀 Quick Start Guide',
      path: '../START-HERE.md',
      category: 'overview',
      badge: 'Essential',
      description: 'Your complete learning journey starts here'
    },
    {
      id: 'programming',
      title: '💻 Programming Languages',
      children: [
        {
          id: 'python-guide',
          title: 'Python Complete Guide',
          path: '../guides/Python-Complete-Guide.md',
          category: 'programming',
          readTime: 120,
          description: '2000+ lines of Python mastery'
        },
        {
          id: 'javascript-guide',
          title: 'JavaScript Complete Guide',
          path: '../guides/JavaScript-Complete-Guide.md',
          category: 'programming',
          readTime: 110,
          description: 'Modern JavaScript from basics to advanced'
        },
        {
          id: 'typescript-guide',
          title: 'TypeScript Complete Guide',
          path: '../guides/TypeScript-Complete-Guide.md',
          category: 'programming',
          readTime: 90,
          description: 'Type-safe JavaScript development'
        },
        {
          id: 'python-code',
          title: 'Python Code Examples',
          path: '../code-examples/python-mastery-guide.py',
          category: 'programming',
          readTime: 60,
          description: 'Executable Python examples'
        },
        {
          id: 'javascript-code',
          title: 'JavaScript Code Examples',
          path: '../code-examples/javascript-mastery-guide.js',
          category: 'programming',
          readTime: 50,
          description: 'Executable JavaScript examples'
        },
        {
          id: 'typescript-code',
          title: 'TypeScript Code Examples',
          path: '../code-examples/typescript-mastery-guide.ts',
          category: 'programming',
          readTime: 50,
          description: 'Executable TypeScript examples'
        }
      ]
    },
    {
      id: 'dsa',
      title: '📊 Data Structures & Algorithms',
      children: [
        {
          id: 'dsa-zero-to-hero',
          title: 'DSA Zero to Hero',
          path: '../data-structures-algorithms-zero-to-hero.md',
          category: 'dsa',
          badge: 'Essential',
          readTime: 180,
          description: 'Complete beginner to expert DSA guide with 7000+ lines'
        }
      ]
    },
    {
      id: 'ai-ml',
      title: '🤖 AI/ML & Data Science',
      children: [
        {
          id: 'master-roadmap',
          title: 'ML/DS Complete Roadmap',
          path: '../guides/ai_ml/MASTER-ML-DS-COMPLETE-ROADMAP.md',
          category: 'ai-ml',
          badge: 'Essential',
          readTime: 60,
          description: 'Your complete path from beginner to expert'
        },
        {
          id: 'learning-order',
          title: 'AI/ML Learning Order',
          path: '../guides/ai_ml/LEARNING-ORDER-GUIDE.md',
          category: 'ai-ml',
          badge: 'Start Here',
          readTime: 30,
          description: 'Step-by-step learning sequence'
        },
        {
          id: 'ml-quick-ref',
          title: 'ML/DS Quick Reference',
          path: '../guides/ai_ml/ML-DS-QUICK-REFERENCE-CHEATSHEET.md',
          category: 'ai-ml',
          readTime: 45,
          description: 'Essential concepts cheatsheet'
        },
        {
          id: 'build-models',
          title: 'Build ML Models From Scratch',
          path: '../guides/ai_ml/Build-ML-Models-From-Scratch-Complete-Guide.md',
          category: 'ai-ml',
          readTime: 150,
          description: 'Implement algorithms from first principles'
        },
        {
          id: 'feature-engineering',
          title: 'Feature Engineering Complete Guide',
          path: '../guides/ai_ml/Feature-Engineering-Complete-Guide.md',
          category: 'ai-ml',
          readTime: 90,
          description: 'Master data preparation and feature creation'
        },
        {
          id: 'nlp-guide',
          title: 'NLP Complete Guide',
          path: '../guides/ai_ml/NLP-Complete-Guide.md',
          category: 'ai-ml',
          readTime: 120,
          description: 'Natural Language Processing mastery'
        },
        {
          id: 'computer-vision',
          title: 'Computer Vision Complete Guide',
          path: '../guides/ai_ml/Computer-Vision-Complete-Guide.md',
          category: 'ai-ml',
          readTime: 120,
          description: 'Image processing and deep learning'
        },
        {
          id: 'mlops-guide',
          title: 'MLOps Production Complete Guide',
          path: '../guides/ai_ml/MLOps-Production-Complete-Guide.md',
          category: 'ai-ml',
          readTime: 100,
          description: 'Deploy and maintain ML systems'
        },
        {
          id: 'ai-agents',
          title: 'AI Agents Complete Guide',
          path: '../guides/ai_ml/AI-Agents-Complete-Guide.md',
          category: 'ai-ml',
          readTime: 80,
          description: 'Build intelligent autonomous agents'
        },
        {
          id: 'llm-interview',
          title: 'LLM Interview Questions',
          path: '../guides/ai_ml/LLM-Interview-Questions-Complete.md',
          category: 'ai-ml',
          readTime: 60,
          description: 'Complete LLM interview preparation'
        },
        {
          id: 'rag-interview',
          title: 'RAG Interview Questions',
          path: '../guides/ai_ml/RAG-Interview-Questions-Complete.md',
          category: 'ai-ml',
          readTime: 45,
          description: 'RAG systems interview prep'
        }
      ]
    },
    {
      id: 'devops',
      title: '☁️ DevOps & Infrastructure',
      children: [
        {
          id: 'docker-guide',
          title: 'Docker Zero to Hero',
          path: '../guides/Docker-Zero-to-Hero.md',
          category: 'devops',
          readTime: 90,
          description: 'Complete containerization mastery'
        },
        {
          id: 'kubernetes-guide',
          title: 'Kubernetes Zero to Hero',
          path: '../guides/Kubernetes-Zero-to-Hero.md',
          category: 'devops',
          readTime: 120,
          description: 'Container orchestration expertise'
        },
        {
          id: 'terraform-guide',
          title: 'Terraform Zero to Hero',
          path: '../guides/Terraform-Zero-to-Hero.md',
          category: 'devops',
          readTime: 80,
          description: 'Infrastructure as Code basics'
        },
        {
          id: 'terraform-complete',
          title: 'Terraform Complete Mastery',
          path: '../guides/Terraform-Complete-Mastery-Guide.md',
          category: 'devops',
          readTime: 150,
          description: 'Advanced Terraform techniques'
        },
        {
          id: 'terraform-part2',
          title: 'Terraform Mastery Part 2',
          path: '../guides/Terraform-Complete-Mastery-Guide-Part2.md',
          category: 'devops',
          readTime: 120,
          description: 'Advanced patterns and best practices'
        },
        {
          id: 'ansible-guide',
          title: 'Ansible Zero to Hero',
          path: '../guides/Ansible-Zero-to-Hero.md',
          category: 'devops',
          readTime: 80,
          description: 'Configuration management automation'
        }
      ]
    },
    {
      id: 'infrastructure-notebooks',
      title: '🏗️ Infrastructure Notebooks',
      children: [
        {
          id: 'ai-ml-systems',
          title: 'AI/ML Systems Infrastructure',
          path: '../infrastructure/ai-ml-systems.ipynb',
          category: 'infrastructure',
          readTime: 45,
          description: 'Building scalable AI/ML infrastructure'
        },
        {
          id: 'cloud-devops',
          title: 'Cloud & DevOps Practices',
          path: '../infrastructure/cloud-devops.ipynb',
          category: 'infrastructure',
          readTime: 40,
          description: 'Cloud infrastructure and DevOps workflows'
        },
        {
          id: 'database-design',
          title: 'Database Design & Architecture',
          path: '../infrastructure/database-design.ipynb',
          category: 'infrastructure',
          readTime: 50,
          description: 'Scalable database design patterns'
        }
      ]
    },
    {
      id: 'system-design',
      title: '🎯 System Design',
      children: [
        {
          id: 'complete-system-design',
          title: '📖 Complete System Design Guide',
          path: '../system-design/COMPLETE-SYSTEM-DESIGN-GUIDE.md',
          category: 'system-design',
          readTime: 180,
          badge: 'Must Read',
          description: 'Comprehensive guide with diagrams and real-world examples'
        },
        {
          id: 'system-architecture',
          title: 'System Architecture Patterns',
          path: '../system-design/architecture/system-architecture-patterns.ipynb',
          category: 'system-design',
          readTime: 60,
          badge: 'Important',
          description: 'Common architecture patterns and best practices'
        },
        {
          id: 'hld-guide',
          title: 'High-Level Design (HLD)',
          path: '../system-design/hld/system-design-hld.ipynb',
          category: 'system-design',
          readTime: 75,
          badge: 'Essential',
          description: 'High-level system design concepts'
        },
        {
          id: 'lld-guide',
          title: 'Low-Level Design (LLD)',
          path: '../system-design/lld/system-design-lld.ipynb',
          category: 'system-design',
          readTime: 70,
          badge: 'Essential',
          description: 'Low-level design and implementation details'
        }
      ]
    },
    {
      id: 'programming-challenges',
      title: '💪 Programming Challenges',
      children: [
        {
          id: 'python-challenges',
          title: 'Python Challenges Notebook',
          path: '../programming-challenges/python.challenges.ipynb',
          category: 'challenges',
          readTime: 90,
          description: 'Python coding challenges and solutions'
        },
        {
          id: 'javascript-challenges',
          title: 'JavaScript Challenges Notebook',
          path: '../programming-challenges/javascript.challenges.ipynb',
          category: 'challenges',
          readTime: 85,
          description: 'JavaScript coding challenges and solutions'
        }
      ]
    },
    {
      id: 'career',
      title: '💼 Career Development',
      children: [
        {
          id: 'career-roadmap',
          title: 'Career Roadmap',
          path: '../docs/career-roadmap.md',
          category: 'career',
          readTime: 30,
          description: 'Plan your tech career progression'
        },
        {
          id: 'interview-guide',
          title: 'Interview Guide',
          path: '../docs/interview-guide.md',
          category: 'career',
          readTime: 45,
          description: 'Ace your technical interviews'
        },
        {
          id: 'fullstack-notes',
          title: 'Full Stack Developer Training',
          path: '../Full_Stack_Developer_Training_Notes.md',
          category: 'career',
          readTime: 60,
          description: 'Complete full stack development path'
        }
      ]
    },
    {
      id: 'teaching',
      title: '🎓 Python Teaching Curriculum',
      children: [
        {
          id: 'teaching-plan',
          title: 'Python Teaching Plan (12 Days)',
          path: '../pythonclass/Python_Teaching_Plan_12_Days.md',
          category: 'teaching',
          readTime: 40,
          description: '12-day comprehensive Python course'
        },
        {
          id: 'part1-fundamentals',
          title: 'Part 1: Python Fundamentals (Hours 1-10)',
          path: '../pythonclass/Part1_Python_Fundamentals_Hours_1-10.md',
          category: 'teaching',
          readTime: 90,
          description: 'Python basics and core concepts'
        },
        {
          id: 'part2-backend',
          title: 'Part 2: Backend Development (Hours 11-20)',
          path: '../pythonclass/Part2_Backend_Development_Hours_11-20.md',
          category: 'teaching',
          readTime: 90,
          description: 'Flask, APIs, and databases'
        },
        {
          id: 'part3-frontend',
          title: 'Part 3: Frontend Development (Hours 21-30)',
          path: '../pythonclass/Part3_Frontend_Development_Hours_21-30.md',
          category: 'teaching',
          readTime: 90,
          description: 'HTML, CSS, JavaScript integration'
        },
        {
          id: 'part4-advanced',
          title: 'Part 4: Advanced Backend (Hours 31-40)',
          path: '../pythonclass/Part4_Advanced_Backend_Hours_31-40.md',
          category: 'teaching',
          readTime: 90,
          description: 'Advanced patterns and deployment'
        }
      ]
    },
    {
      id: 'extras',
      title: '📚 Additional Resources',
      children: [
        {
          id: 'vedic-math',
          title: 'Vedic Mathematics Zero to Hero',
          path: '../vedic-mathematics-zero-to-hero.md',
          category: 'extras',
          readTime: 60,
          description: 'Ancient mathematical techniques'
        }
      ]
    }
  ]
}


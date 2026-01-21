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
      id: 'fundamentals',
      title: '📊 Fundamentals',
      children: [
        {
          id: 'dsa-zero-to-hero',
          title: 'DSA Zero to Hero',
          path: '../guides/fundamentals/data-structures-algorithms-zero-to-hero.md',
          category: 'fundamentals',
          badge: 'Essential',
          readTime: 180,
          description: 'Complete beginner to expert DSA guide with 7000+ lines'
        },
        {
          id: 'git-github',
          title: 'Git & GitHub Zero to Hero',
          path: '../guides/fundamentals/git-github-zero-to-hero.md',
          category: 'fundamentals',
          readTime: 60,
          description: 'Version control and collaboration'
        },
        {
          id: 'linux-cli',
          title: 'Linux Command Line Zero to Hero',
          path: '../guides/fundamentals/linux-command-line-zero-to-hero.md',
          category: 'fundamentals',
          readTime: 75,
          description: 'Master the Linux terminal'
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
        },
        {
          id: 'leetcode-solutions',
          title: 'LeetCode Solutions',
          path: '../code-examples/leetcode_solve.md',
          category: 'challenges',
          badge: 'New',
          readTime: 45,
          description: 'Two Sum problem with 4 solution approaches - Python & JavaScript'
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
          id: 'master-roadmap-career',
          title: 'ML/DS Career Complete Roadmap',
          path: '../guides/ai_ml/MASTER-ML-DS-COMPLETE-ROADMAP.md',
          category: 'career',
          badge: 'Career Growth',
          readTime: 60,
          description: 'Complete ML/DS career path from junior to senior'
        },
        {
          id: 'llm-interview-career',
          title: 'LLM Interview Questions',
          path: '../guides/ai_ml/LLM-Interview-Questions-Complete.md',
          category: 'career',
          badge: 'Interview Prep',
          readTime: 60,
          description: 'Master LLM interviews for AI/ML roles'
        },
        {
          id: 'rag-interview-career',
          title: 'RAG Interview Questions',
          path: '../guides/ai_ml/RAG-Interview-Questions-Complete.md',
          category: 'career',
          badge: 'Interview Prep',
          readTime: 45,
          description: 'RAG systems interview preparation'
        },
        {
          id: 'system-design-career',
          title: 'Complete System Design Guide',
          path: '../system-design/COMPLETE-SYSTEM-DESIGN-GUIDE.md',
          category: 'career',
          badge: 'Must Read',
          readTime: 180,
          description: 'Master system design for senior+ interviews'
        },
        {
          id: 'python-challenges-career',
          title: 'Python Coding Challenges',
          path: '../programming-challenges/python.challenges.ipynb',
          category: 'career',
          badge: 'Practice',
          readTime: 90,
          description: 'Interview coding practice - Python'
        },
        {
          id: 'javascript-challenges-career',
          title: 'JavaScript Coding Challenges',
          path: '../programming-challenges/javascript.challenges.ipynb',
          category: 'career',
          badge: 'Practice',
          readTime: 85,
          description: 'Interview coding practice - JavaScript'
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
    },
    {
      id: 'cloud-platforms',
      title: '☁️ Cloud Platforms',
      children: [
        {
          id: 'aws-cloud',
          title: 'AWS Cloud Zero to Hero',
          path: '../guides/cloud-platforms/aws-cloud-zero-to-hero.md',
          category: 'cloud',
          readTime: 90,
          description: 'Complete AWS cloud services guide'
        },
        {
          id: 'aws-cert-index',
          title: 'AWS Certification Master Guide',
          path: '../guides/cloud-platforms/README-AWS-Certifications.md',
          category: 'cloud',
          badge: 'New',
          readTime: 15,
          description: 'Complete AWS certification roadmap and study plan'
        },
        {
          id: 'aws-cloud-practitioner',
          title: 'AWS Cloud Practitioner (CLF-C02)',
          path: '../guides/cloud-platforms/AWS-Cloud-Practitioner-Complete-Guide.md',
          category: 'cloud',
          badge: 'New',
          readTime: 180,
          description: '1500+ lines complete exam preparation with 40+ practice questions'
        },
        {
          id: 'aws-solutions-architect',
          title: 'AWS Solutions Architect (SAA-C03)',
          path: '../guides/cloud-platforms/AWS-Solutions-Architect-Associate-Guide.md',
          category: 'cloud',
          badge: 'New',
          readTime: 240,
          description: '3800+ lines advanced guide with architecture patterns and 40+ questions'
        },
        {
          id: 'aws-quick-reference',
          title: 'AWS Exam Quick Reference',
          path: '../guides/cloud-platforms/AWS-Exam-Quick-Reference-Cheatsheet.md',
          category: 'cloud',
          badge: 'New',
          readTime: 30,
          description: 'Last 24-hour exam review cheatsheet - print friendly'
        },
        {
          id: 'aws-roadmap',
          title: 'AWS Certification Roadmap',
          path: '../docs/aws-certification-roadmap.md',
          category: 'cloud',
          badge: 'New',
          readTime: 20,
          description: '12-week progressive study plan for both certifications'
        },
        {
          id: 'azure-cloud',
          title: 'Azure Cloud Zero to Hero',
          path: '../guides/cloud-platforms/azure-cloud-zero-to-hero.md',
          category: 'cloud',
          readTime: 95,
          badge: 'New',
          description: 'Microsoft Azure cloud platform - enterprise alternative to AWS'
        }
      ]
    },
    {
      id: 'backend-development',
      title: '🟢 Backend Development',
      children: [
        {
          id: 'nodejs-express',
          title: 'Node.js & Express Zero to Hero',
          path: '../guides/backend-development/nodejs-express-zero-to-hero.md',
          category: 'backend',
          readTime: 100,
          badge: 'New',
          description: 'Backend JavaScript development with Node.js and Express'
        },
        {
          id: 'rest-api',
          title: 'REST API Development Zero to Hero',
          path: '../guides/backend-development/rest-api-development-zero-to-hero.md',
          category: 'backend',
          readTime: 85,
          description: 'Build robust RESTful APIs'
        }
      ]
    },
    {
      id: 'frontend-development',
      title: '⚛️ Frontend Development',
      children: [
        {
          id: 'react-frontend',
          title: 'React Frontend Zero to Hero',
          path: '../guides/frontend-development/react-frontend-zero-to-hero.md',
          category: 'frontend',
          readTime: 100,
          description: 'Modern React development'
        },
        {
          id: 'nextjs',
          title: 'Next.js Zero to Hero',
          path: '../guides/frontend-development/nextjs-zero-to-hero.md',
          category: 'frontend',
          readTime: 85,
          badge: 'New',
          description: 'Modern React framework for production applications'
        },
        {
          id: 'fullstack-notes',
          title: 'Full Stack Developer Training',
          path: '../guides/frontend-development/Full_Stack_Developer_Training_Notes.md',
          category: 'frontend',
          readTime: 60,
          description: 'Complete full stack development path'
        }
      ]
    },
    {
      id: 'databases',
      title: '💾 Databases',
      children: [
        {
          id: 'mongodb',
          title: 'MongoDB Zero to Hero',
          path: '../guides/databases/mongodb-zero-to-hero.md',
          category: 'databases',
          readTime: 90,
          badge: 'New',
          description: 'NoSQL database mastery - from basics to production'
        },
        {
          id: 'sql-databases',
          title: 'SQL Databases Zero to Hero',
          path: '../guides/databases/sql-databases-zero-to-hero.md',
          category: 'databases',
          readTime: 95,
          description: 'Relational database mastery'
        },
        {
          id: 'redis-caching',
          title: 'Redis & Caching Zero to Hero',
          path: '../guides/databases/redis-caching-zero-to-hero.md',
          category: 'databases',
          readTime: 65,
          description: 'In-memory data store and caching'
        }
      ]
    },
    {
      id: 'architecture-design',
      title: '🏗️ Architecture & Design',
      children: [
        {
          id: 'microservices',
          title: 'Microservices Architecture Complete Guide',
          path: '../guides/architecture-design/microservices-complete-guide.md',
          category: 'architecture',
          readTime: 120,
          badge: 'New',
          description: 'Senior-level microservices patterns and best practices'
        },
        {
          id: 'kafka-queues',
          title: 'Kafka & Message Queues Zero to Hero',
          path: '../guides/architecture-design/kafka-message-queues-zero-to-hero.md',
          category: 'architecture',
          readTime: 80,
          description: 'Distributed messaging systems'
        },
        {
          id: 'event-driven-arch',
          title: 'Event-Driven Architecture Zero to Hero',
          path: '../guides/architecture-design/Event-Driven-Architecture-Zero-to-Hero.md',
          category: 'architecture',
          readTime: 100,
          badge: 'New',
          description: 'Build scalable event-driven systems'
        }
      ]
    },
    {
      id: 'big-data-analytics',
      title: '🗄️ Big Data & Analytics',
      children: [
        {
          id: 'data-engineering',
          title: 'Data Engineering Zero to Hero',
          path: '../guides/big-data-analytics/Data-Engineering-Zero-to-Hero.md',
          category: 'big-data',
          readTime: 180,
          badge: 'New',
          description: 'Complete data engineering pipeline mastery'
        }
      ]
    },
    {
      id: 'devops-infrastructure-advanced',
      title: '🚀 DevOps & Infrastructure (Advanced)',
      children: [
        {
          id: 'kubernetes-guide',
          title: 'Kubernetes Zero to Hero',
          path: '../guides/devops-infrastructure/Kubernetes-Zero-to-Hero.md',
          category: 'devops-advanced',
          readTime: 120,
          description: 'Container orchestration expertise'
        },
        {
          id: 'cicd-guide',
          title: 'CI/CD Zero to Hero',
          path: '../guides/devops-infrastructure/cicd-zero-to-hero.md',
          category: 'devops-advanced',
          readTime: 70,
          description: 'Continuous Integration & Deployment mastery'
        },
        {
          id: 'load-balancing-ha',
          title: 'Load Balancing & High Availability Zero to Hero',
          path: '../guides/devops-infrastructure/Load-Balancing-High-Availability-Zero-to-Hero.md',
          category: 'devops-advanced',
          readTime: 80,
          badge: 'New',
          description: 'Build highly available and scalable systems'
        }
      ]
    },
    {
      id: 'performance-engineering',
      title: '⚡ Performance Engineering',
      children: [
        {
          id: 'performance-optimization',
          title: 'Performance Optimization Complete Guide',
          path: '../guides/performance-engineering/Performance-Optimization-Complete-Guide.md',
          category: 'performance',
          readTime: 120,
          badge: 'New',
          description: 'Frontend, backend, and database performance optimization'
        }
      ]
    },
    {
      id: 'security-testing',
      title: '🔒 Security & Testing',
      children: [
        {
          id: 'security-practices',
          title: 'Security Best Practices Zero to Hero',
          path: '../guides/security-testing/security-best-practices-zero-to-hero.md',
          category: 'security',
          readTime: 90,
          description: 'Application security fundamentals'
        },
        {
          id: 'testing-tdd',
          title: 'Testing & TDD Zero to Hero',
          path: '../guides/security-testing/testing-tdd-zero-to-hero.md',
          category: 'testing',
          readTime: 70,
          description: 'Test-driven development practices'
        }
      ]
    }
  ]
}


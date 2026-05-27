export interface ContentItem {
  id: string
  title: string
  description?: string
  path?: string
  content?: string
  pdfUrl?: string
  fileType?: 'markdown' | 'code' | 'notebook' | 'pdf'
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
      id: 'start-here',
      title: '🚀 Start Here — Pick Your Path',
      path: '../START-HERE.md',
      category: 'overview',
      badge: 'Start Here',
      description: 'Choose AI/ML, full-stack, DevOps, or system design — then follow the plan'
    },
    {
      id: 'readme',
      title: '🏠 Repository Overview',
      path: '../README.md',
      category: 'overview',
      description: 'What is in this repo (guides, notebooks, career docs)'
    },
    {
      id: 'learning-checkpoints',
      title: '✅ Learning Checkpoints (All Folders)',
      path: '../LEARNING-CHECKPOINTS.md',
      category: 'overview',
      badge: 'Track Progress',
      description: 'Pass criteria for every major folder and career path'
    },
    {
      id: 'python',
      title: '🐍 Python Zero to Hero',
      children: [
        {
          id: 'python-zero-to-hero',
          title: 'Start Here (Python + AI/ML)',
          path: '../guides/PYTHON-ZERO-TO-HERO.md',
          category: 'python',
          badge: 'Start',
          readTime: 45,
          description: 'Full plan: Python + FastAPI + AI/ML 4 phases in one file'
        },
        {
          id: 'python-guide',
          title: 'Complete Guide (Theory + Code)',
          path: '../guides/Python-Complete-Guide.md',
          category: 'python',
          readTime: 120,
          badge: 'Main Book',
          description: 'Sec. 1–29: fundamentals, NumPy, Pandas, FastAPI, Docker'
        },
        {
          id: 'python-code',
          title: 'Code Examples',
          path: '../code-examples/python-mastery-guide.py',
          category: 'python',
          readTime: 60,
          description: 'Extra runnable Python scripts'
        },
        {
          id: 'python-challenges',
          title: 'Challenges Notebook',
          path: '../programming-challenges/python.challenges.ipynb',
          category: 'python',
          readTime: 90,
          description: 'Practice problems with solutions'
        },
        {
          id: 'teaching-plan',
          title: 'Teaching Plan (12 Days)',
          path: '../pythonclass/Python_Teaching_Plan_12_Days.md',
          category: 'python',
          readTime: 40,
          description: 'Structured 12-day Python course'
        },
        {
          id: 'part1-fundamentals',
          title: 'Part 1: Fundamentals (Hours 1–10)',
          path: '../pythonclass/Part1_Python_Fundamentals_Hours_1-10.md',
          category: 'python',
          readTime: 90,
          description: 'Python basics and core concepts'
        },
        {
          id: 'part2-backend',
          title: 'Part 2: Backend (Hours 11–20)',
          path: '../pythonclass/Part2_Backend_Development_Hours_11-20.md',
          category: 'python',
          readTime: 90,
          description: 'Flask, APIs, and databases'
        },
        {
          id: 'part3-frontend',
          title: 'Part 3: Frontend (Hours 21–30)',
          path: '../pythonclass/Part3_Frontend_Development_Hours_21-30.md',
          category: 'python',
          readTime: 90,
          description: 'HTML, CSS, JavaScript integration'
        },
        {
          id: 'part4-advanced',
          title: 'Part 4: Advanced Backend (Hours 31–40)',
          path: '../pythonclass/Part4_Advanced_Backend_Hours_31-40.md',
          category: 'python',
          readTime: 90,
          description: 'Advanced patterns and deployment'
        },
        {
          id: 'python-demos',
          title: 'Full-Stack Live Demos (21 Projects)',
          path: '../pythonclass/demo-projects/PYTHON-DEMOS.md',
          category: 'python',
          badge: 'Demos',
          readTime: 45,
          description: 'Interactive Python project showcase'
        }
      ]
    },
    {
      id: 'programming',
      title: '💻 JavaScript & TypeScript',
      children: [
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
          title: 'DSA Zero to Hero (complete)',
          path: '../system-design/DATA-STRUCTURES-ZERO-TO-HERO.md',
          category: 'fundamentals',
          badge: 'Complete',
          readTime: 180,
          description: 'All DSA theory, diagrams, and Python examples in one file'
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
      title: '🤖 AI/ML Zero to Hero',
      children: [
        {
          id: 'ai-ml-zero-to-hero',
          title: 'Start Here — Enterprise ML Path',
          path: '../guides/ai_ml/AI-ML-ZERO-TO-HERO.md',
          category: 'ai-ml',
          badge: 'Start',
          readTime: 35,
          description: 'Ordered phases: core ML → MLOps → specialization → interviews'
        },
        {
          id: 'llm-apps-zero-to-hero',
          title: 'LLM Apps — RAG & Agents (Examples)',
          path: '../guides/ai_ml/LLM-APPS-ZERO-TO-HERO.md',
          category: 'ai-ml',
          badge: 'RAG+Agents',
          readTime: 40,
          description:
            'End-to-end: RAG, LangChain, LangGraph, agents, Langfuse — simple runnable code'
        },
        {
          id: 'rag-production-guide',
          title: 'RAG in Production (chunking, RAGAS, vector DBs)',
          path: '../guides/ai_ml/RAG-PRODUCTION-GUIDE.md',
          category: 'ai-ml',
          badge: 'Production',
          readTime: 45,
          description: 'After LLM Apps: eval, Haystack/LlamaIndex, deployment checklist'
        },
        {
          id: 'ai-ml-phase-0-prereq',
          title: 'Prerequisite: Python Sec. 11',
          children: [
            {
              id: 'ai-ml-prereq-python',
              title: '↪ Python Zero to Hero (Sec. 11)',
              path: '../guides/PYTHON-ZERO-TO-HERO.md',
              category: 'ai-ml',
              badge: 'Required',
              readTime: 45,
              description: 'Finish NumPy/Pandas mini-project before ML Phase 1'
            }
          ]
        },
        {
          id: 'ai-ml-phase-1-core',
          title: 'Phase 1 — Core ML (Weeks 1–8)',
          children: [
            {
              id: 'statistics-for-ml',
              title: '0. Statistics for ML (read first)',
              path: '../guides/ai_ml/STATISTICS-FOR-ML.md',
              category: 'ai-ml',
              badge: 'Prerequisite',
              readTime: 35,
              description: 'Distributions, hypothesis tests, bias/variance'
            },
            {
              id: 'feature-engineering',
              title: '1. Feature Engineering',
              path: '../guides/ai_ml/Feature-Engineering-Complete-Guide.md',
              category: 'ai-ml',
              badge: 'Weeks 1–3',
              readTime: 90,
              description: 'Data cleaning, encoding, scaling, pipelines'
            },
            {
              id: 'build-models',
              title: '2. Build ML Models From Scratch',
              path: '../guides/ai_ml/Build-ML-Models-From-Scratch-Complete-Guide.md',
              category: 'ai-ml',
              badge: 'Weeks 4–8',
              readTime: 150,
              description: 'Algorithms, neural nets, training discipline'
            },
            {
              id: 'pytorch-zero-to-hero',
              title: '3. PyTorch Zero to Hero',
              path: '../guides/ai_ml/PYTORCH-ZERO-TO-HERO.md',
              category: 'ai-ml',
              badge: 'Weeks 7–8',
              readTime: 50,
              description: 'NumPy → tensors, training loops, CNNs, transfer learning'
            }
          ]
        },
        {
          id: 'ai-ml-phase-2-career',
          title: 'Phase 2 — Roadmap & MLOps (Weeks 9–14)',
          children: [
            {
              id: 'master-roadmap',
              title: '3. ML/DS Career Roadmap',
              path: '../guides/ai_ml/MASTER-ML-DS-COMPLETE-ROADMAP.md',
              category: 'ai-ml',
              badge: 'Weeks 9–10',
              readTime: 60,
              description: 'Portfolio, specialization choice, career planning'
            },
            {
              id: 'ml-quick-ref',
              title: '4. Quick Reference (keep open)',
              path: '../guides/ai_ml/ML-DS-QUICK-REFERENCE-CHEATSHEET.md',
              category: 'ai-ml',
              badge: 'Reference',
              readTime: 45,
              description: 'Formulas and patterns while you code'
            },
            {
              id: 'mlops-guide',
              title: '5. MLOps & Production',
              path: '../guides/ai_ml/MLOps-Production-Complete-Guide.md',
              category: 'ai-ml',
              badge: 'Weeks 11–14',
              readTime: 100,
              description: 'Docker, serving, MLflow, monitoring'
            }
          ]
        },
        {
          id: 'ai-ml-phase-3-specialize',
          title: 'Phase 3 — Pick ONE Track (Weeks 15–16)',
          children: [
            {
              id: 'nlp-guide',
              title: 'NLP & LLMs',
              path: '../guides/ai_ml/NLP-Complete-Guide.md',
              category: 'ai-ml',
              readTime: 120,
              description: 'Text, transformers, production NLP'
            },
            {
              id: 'computer-vision',
              title: 'Computer Vision',
              path: '../guides/ai_ml/Computer-Vision-Complete-Guide.md',
              category: 'ai-ml',
              readTime: 120,
              description: 'CNNs, detection, vision pipelines'
            },
            {
              id: 'ai-agents',
              title: 'AI Agents (full guide)',
              path: '../guides/ai_ml/AI-Agents-Complete-Guide.md',
              category: 'ai-ml',
              readTime: 80,
              description: 'After LLM Apps examples: LangChain, CrewAI, LangGraph depth'
            },
            {
              id: 'generative-ai-zero-to-hero',
              title: 'Generative AI (GANs, diffusion, LoRA)',
              path: '../guides/ai_ml/GENERATIVE-AI-ZERO-TO-HERO.md',
              category: 'ai-ml',
              badge: 'Images',
              readTime: 45,
              description: 'Beyond text LLMs: image generation and fine-tuning'
            }
          ]
        },
        {
          id: 'ai-ml-phase-4-interviews',
          title: 'Phase 4 — Interviews & Deep Schedules',
          children: [
            {
              id: 'llm-interview',
              title: 'LLM Interview Questions',
              path: '../guides/ai_ml/LLM-Interview-Questions-Complete.md',
              category: 'ai-ml',
              readTime: 60,
              description: 'LLM concepts and interview drills'
            },
            {
              id: 'rag-interview',
              title: 'RAG Interview Questions',
              path: '../guides/ai_ml/RAG-Interview-Questions-Complete.md',
              category: 'ai-ml',
              readTime: 45,
              description: 'Retrieval, chunking, evaluation'
            },
            {
              id: 'learning-order',
              title: 'Extended Learning Order (5 paths)',
              path: '../guides/ai_ml/LEARNING-ORDER-GUIDE.md',
              category: 'ai-ml',
              readTime: 30,
              description: 'Optional week-by-week detail for each career path'
            }
          ]
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
      title: '🎯 System Design & DSA',
      children: [
        {
          id: 'data-structures-zero-to-hero',
          title: 'DSA Zero to Hero (complete guide)',
          path: '../system-design/DATA-STRUCTURES-ZERO-TO-HERO.md',
          category: 'system-design',
          readTime: 180,
          badge: 'Start Here',
          description: 'All topics: theory, diagrams, Python examples, interviews — one file'
        },
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
        },
        {
          id: 'system-design-practice-track',
          title: 'System Design Practice Track',
          path: '../system-design/SYSTEM-DESIGN-PRACTICE-TRACK.md',
          category: 'system-design',
          readTime: 45,
          badge: 'Practice',
          description: 'Graded prompts L1–L4 with rubrics and 10-week plan'
        }
      ]
    },
    {
      id: 'programming-challenges',
      title: '💪 Programming Challenges',
      children: [
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
      title: '☁️ Cloud Zero to Hero',
      children: [
        {
          id: 'cloud-zero-to-hero',
          title: 'Start Here — Cloud Path (tri-cloud)',
          path: '../guides/cloud-platforms/CLOUD-ZERO-TO-HERO.md',
          category: 'cloud',
          badge: 'Start Here',
          readTime: 30,
          description: 'AWS → certs → Azure → ML on AWS → GCP → data engineering'
        },
        {
          id: 'cloud-phase-1-aws',
          title: 'Phase 1 — AWS Fundamentals (Weeks 1–3)',
          children: [
            {
              id: 'aws-cloud',
              title: 'AWS Cloud Zero to Hero',
              path: '../guides/cloud-platforms/aws-cloud-zero-to-hero.md',
              category: 'cloud',
              readTime: 90,
              description: 'IAM, EC2, S3, VPC, Lambda, RDS — complete service guide'
            }
          ]
        },
        {
          id: 'cloud-phase-2-certs',
          title: 'Phase 2 — AWS Certifications (Weeks 4–6)',
          children: [
            {
              id: 'aws-cert-index',
              title: 'AWS Certification Master Guide',
              path: '../guides/cloud-platforms/README-AWS-Certifications.md',
              category: 'cloud',
              badge: 'Roadmap',
              readTime: 15,
              description: 'Which cert, study order, resources'
            },
            {
              id: 'aws-roadmap',
              title: '12-Week Certification Roadmap',
              path: '../docs/aws-certification-roadmap.md',
              category: 'cloud',
              readTime: 20,
              description: 'Progressive CLF → SAA study plan'
            },
            {
              id: 'aws-cloud-practitioner',
              title: 'Cloud Practitioner (CLF-C02)',
              path: '../guides/cloud-platforms/AWS-Cloud-Practitioner-Complete-Guide.md',
              category: 'cloud',
              badge: 'CLF',
              readTime: 180,
              description: 'Foundational exam prep with practice questions'
            },
            {
              id: 'aws-solutions-architect',
              title: 'Solutions Architect (SAA-C03)',
              path: '../guides/cloud-platforms/AWS-Solutions-Architect-Associate-Guide.md',
              category: 'cloud',
              badge: 'SAA',
              readTime: 240,
              description: 'Architecture patterns and exam prep'
            },
            {
              id: 'aws-saa-c03-solutions',
              title: 'SAA-C03 Solutions Q&A',
              path: '../guides/cloud-platforms/AWS_SAA-C03_Solutions.md',
              category: 'cloud',
              readTime: 300,
              description: '634 Q&A for practice exams'
            },
            {
              id: 'aws-quick-reference',
              title: 'Exam Quick Reference (24h review)',
              path: '../guides/cloud-platforms/AWS-Exam-Quick-Reference-Cheatsheet.md',
              category: 'cloud',
              badge: 'Cheat',
              readTime: 30,
              description: 'Print-friendly last-day review'
            }
          ]
        },
        {
          id: 'cloud-phase-3-azure',
          title: 'Phase 3 — Azure (Weeks 7–8)',
          children: [
            {
              id: 'azure-cloud',
              title: 'Azure Cloud Zero to Hero',
              path: '../guides/cloud-platforms/azure-cloud-zero-to-hero.md',
              category: 'cloud',
              readTime: 95,
              description: 'VMs, Blob, Entra ID, Functions — AWS mapping included'
            }
          ]
        },
        {
          id: 'cloud-phase-4-ml-genai',
          title: 'Phase 4 — ML & GenAI on AWS (Weeks 9–10)',
          children: [
            {
              id: 'aws-ml-genai-zero-to-hero',
              title: 'AWS ML & GenAI (SageMaker + Bedrock)',
              path: '../guides/cloud-platforms/AWS-ML-GENAI-ZERO-TO-HERO.md',
              category: 'cloud',
              badge: 'ML',
              readTime: 40,
              description: 'S3, IAM, SageMaker train/deploy, Bedrock — for ML engineers'
            }
          ]
        },
        {
          id: 'cloud-phase-5-gcp',
          title: 'Phase 5 — GCP (Weeks 10–11)',
          children: [
            {
              id: 'gcp-cloud-zero-to-hero',
              title: 'GCP Cloud Zero to Hero',
              path: '../guides/cloud-platforms/GCP-CLOUD-ZERO-TO-HERO.md',
              category: 'cloud',
              badge: 'GCP',
              readTime: 35,
              description: 'GCE, GCS, BigQuery, Vertex AI intro'
            }
          ]
        },
        {
          id: 'cloud-phase-6-data',
          title: 'Phase 6 — Data Engineering (Weeks 11–12)',
          children: [
            {
              id: 'data-engineering-cloud',
              title: 'Data Engineering Zero to Hero',
              path: '../guides/big-data-analytics/Data-Engineering-Zero-to-Hero.md',
              category: 'cloud',
              readTime: 90,
              description: 'Pipelines, lakes, Spark — after cloud foundations'
            }
          ]
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
          id: 'flutter-dart',
          title: 'Flutter & Dart Complete Guide',
          path: '../guides/frontend-development/Flutter-Dart-Complete-Guide.md',
          category: 'frontend',
          readTime: 180,
          badge: 'New',
          description: '12-16 week comprehensive Flutter & Dart guide from beginner to expert'
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


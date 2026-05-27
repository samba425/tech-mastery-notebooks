import type { LucideIcon } from 'lucide-react'
import {
  Rocket,
  Home,
  CheckSquare,
  FileCode,
  Braces,
  BookOpen,
  Brain,
  Cloud,
  Container,
  Server,
  Network,
  Target,
  Briefcase,
  Calculator,
  Database,
  Layout,
  Layers,
  BarChart3,
  Shield,
  TestTube2,
  GitBranch,
  Terminal,
  MessageSquare,
  ScanEye,
  Bot,
  Sparkles,
  LineChart,
  Workflow,
  FileText,
  BookMarked,
  GraduationCap,
  Route,
  ClipboardList,
  Boxes,
  Cpu,
  CloudCog,
  HardDrive,
  Zap,
  Lock,
  Radio,
  FolderOpen,
  FolderTree,
  ChevronRight,
  Award,
  Map,
  FileType,
  ScrollText,
  Code2,
} from 'lucide-react'

/** Remove leading emoji / symbols from sidebar & page titles */
export function stripEmojis(title: string): string {
  return title
    .replace(/^[\s\p{Extended_Pictographic}\u2600-\u27BF\uFE0F]+/gu, '')
    .replace(/^[\s\-—]+/, '')
    .trim()
}

const ID_ICON: Record<string, LucideIcon> = {
  'start-here': Rocket,
  readme: Home,
  'learning-checkpoints': CheckSquare,
  python: FileCode,
  'python-zero-to-hero': Rocket,
  'python-guide': BookOpen,
  'python-code': FileCode,
  'python-challenges': Target,
  'teaching-plan': GraduationCap,
  'part1-fundamentals': BookOpen,
  'part2-backend': Server,
  'part3-frontend': Layout,
  'part4-advanced': Cpu,
  'python-demos': Boxes,
  programming: Braces,
  'javascript-guide': FileCode,
  'typescript-guide': FileCode,
  'javascript-code': FileCode,
  'typescript-code': FileCode,
  fundamentals: BookOpen,
  'dsa-zero-to-hero': Route,
  'dsa-complete-reference-fundamentals': BookMarked,
  'dsa-complete-reference': BookMarked,
  'git-github': GitBranch,
  'linux-cli': Terminal,
  'ai-ml': Brain,
  'ai-ml-zero-to-hero': Brain,
  'llm-apps-zero-to-hero': MessageSquare,
  'rag-production-guide': Workflow,
  'ai-ml-phase-0-prereq': BookOpen,
  'ai-ml-prereq-python': FileCode,
  'ai-ml-phase-1-core': LineChart,
  'statistics-for-ml': LineChart,
  'feature-engineering': Layers,
  'build-models': Cpu,
  'pytorch-zero-to-hero': Zap,
  'ai-ml-phase-2-career': Route,
  'master-roadmap': Map,
  'ml-quick-ref': ClipboardList,
  'mlops-guide': Workflow,
  'ai-ml-phase-3-specialize': Sparkles,
  'nlp-guide': MessageSquare,
  'computer-vision': ScanEye,
  'ai-agents': Bot,
  'generative-ai-zero-to-hero': Sparkles,
  'ai-ml-phase-4-interviews': Briefcase,
  'llm-interview': MessageSquare,
  'rag-interview': Workflow,
  'learning-order': Route,
  devops: Container,
  'docker-guide': Container,
  'terraform-guide': Layers,
  'terraform-complete': Layers,
  'terraform-part2': Layers,
  'ansible-guide': Workflow,
  'infrastructure-notebooks': Server,
  'ai-ml-systems': Brain,
  'cloud-devops': CloudCog,
  'database-design': Database,
  'system-design': Network,
  'data-structures-zero-to-hero': Route,
  'dsa-labs': FolderTree,
  'complete-system-design': Network,
  'system-architecture': Boxes,
  'hld-guide': Layers,
  'lld-guide': FileCode,
  'system-design-practice-track': Target,
  'programming-challenges': Target,
  'javascript-challenges': Target,
  'javascript-challenges-career': Target,
  'python-challenges-career': Target,
  'leetcode-solutions': Code2,
  career: Briefcase,
  'career-roadmap': Map,
  'interview-guide': Briefcase,
  'master-roadmap-career': Map,
  'llm-interview-career': MessageSquare,
  'rag-interview-career': Workflow,
  'system-design-career': Network,
  extras: Sparkles,
  'vedic-math': Calculator,
  'cloud-platforms': Cloud,
  'cloud-zero-to-hero': Cloud,
  'cloud-phase-1-aws': Cloud,
  'aws-cloud': Cloud,
  'cloud-phase-2-certs': Award,
  'aws-cert-index': Award,
  'aws-roadmap': Map,
  'aws-cloud-practitioner': Award,
  'aws-solutions-architect': Network,
  'aws-saa-c03-solutions': ClipboardList,
  'aws-quick-reference': ClipboardList,
  'cloud-phase-3-azure': Cloud,
  'azure-cloud': Cloud,
  'cloud-phase-4-ml-genai': Brain,
  'aws-ml-genai-zero-to-hero': Brain,
  'cloud-phase-5-gcp': Cloud,
  'gcp-cloud-zero-to-hero': Cloud,
  'cloud-phase-6-data': BarChart3,
  'data-engineering-cloud': BarChart3,
  'backend-development': Server,
  'nodejs-express': Server,
  'rest-api': Radio,
  'frontend-development': Layout,
  'react-frontend': Layout,
  nextjs: Layout,
  'flutter-dart': Layout,
  'fullstack-notes': Layers,
  databases: Database,
  mongodb: Database,
  'sql-databases': Database,
  'redis-caching': HardDrive,
  'architecture-design': Boxes,
  microservices: Boxes,
  'kafka-queues': Radio,
  'event-driven-arch': Workflow,
  'big-data-analytics': BarChart3,
  'data-engineering': BarChart3,
  'devops-infrastructure-advanced': CloudCog,
  'kubernetes-guide': Container,
  'cicd-guide': Workflow,
  'load-balancing-ha': Network,
  'performance-engineering': Zap,
  'performance-optimization': Zap,
  'security-testing': Shield,
  'security-practices': Lock,
  'testing-tdd': TestTube2,
  'pdf-library': FileType,
}

const CATEGORY_ICON: Record<string, LucideIcon> = {
  overview: Home,
  python: FileCode,
  javascript: Braces,
  typescript: Braces,
  fundamentals: BookOpen,
  'ai-ml': Brain,
  devops: Container,
  infrastructure: Server,
  'system-design': Network,
  cloud: Cloud,
  backend: Server,
  frontend: Layout,
  databases: Database,
  'pdf-library': FileType,
}

const PHASE_PREFIX_ICON: { prefix: string; icon: LucideIcon }[] = [
  { prefix: 'dsa-phase-', icon: FolderOpen },
  { prefix: 'dsa-lab-', icon: ScrollText },
  { prefix: 'cloud-phase-', icon: FolderOpen },
  { prefix: 'ai-ml-phase-', icon: FolderOpen },
]

export function getNavIcon(
  id: string,
  opts?: { category?: string; hasChildren?: boolean; fileType?: string }
): LucideIcon {
  if (ID_ICON[id]) return ID_ICON[id]

  for (const { prefix, icon } of PHASE_PREFIX_ICON) {
    if (id.startsWith(prefix)) return icon
  }

  if (id.startsWith('pdf-')) return FileType
  if (id.startsWith('dsa-lab-')) return ScrollText

  if (opts?.fileType === 'notebook') return ScrollText
  if (opts?.fileType === 'pdf') return FileType
  if (opts?.fileType === 'code') return FileCode

  if (opts?.hasChildren) return FolderOpen

  if (opts?.category && CATEGORY_ICON[opts.category]) {
    return CATEGORY_ICON[opts.category]
  }

  if (id.includes('interview')) return Briefcase
  if (id.includes('aws')) return Cloud
  if (id.includes('azure') || id.includes('gcp')) return Cloud
  if (id.includes('guide')) return BookOpen
  if (id.includes('roadmap')) return Map

  return FileText
}

export function NavIconBox({
  id,
  category,
  hasChildren,
  fileType,
  selected,
}: {
  id: string
  category?: string
  hasChildren?: boolean
  fileType?: string
  selected?: boolean
}) {
  const Icon = getNavIcon(id, { category, hasChildren, fileType })
  return (
    <span
      className={`flex-shrink-0 flex items-center justify-center w-7 h-7 rounded-md ${
        selected
          ? 'bg-slate-300/50 text-slate-800 dark:bg-slate-700 dark:text-primary-300'
          : 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400 group-hover:bg-slate-200/80 dark:group-hover:bg-slate-700'
      }`}
    >
      <Icon className="w-3.5 h-3.5" strokeWidth={2} />
    </span>
  )
}

export { ChevronRight }

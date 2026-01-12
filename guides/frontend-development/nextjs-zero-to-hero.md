# Next.js: Zero to Hero Guide
## Modern React Framework for Production

---

## 📚 Table of Contents

1. [Introduction to Next.js](#introduction)
2. [Installation & Setup](#setup)
3. [File-based Routing](#routing)
4. [App Router vs Pages Router](#routers)
5. [Server & Client Components](#components)
6. [Data Fetching](#data-fetching)
7. [API Routes](#api-routes)
8. [Static Site Generation (SSG)](#ssg)
9. [Server-Side Rendering (SSR)](#ssr)
10. [Dynamic Routes](#dynamic-routes)
11. [Image Optimization](#images)
12. [Metadata & SEO](#seo)
13. [Authentication](#auth)
14. [Database Integration](#database)
15. [Deployment](#deployment)
16. [Best Practices](#best-practices)
17. [Real-World Projects](#projects)

---

## 🎯 Introduction to Next.js {#introduction}

### What is Next.js?

**Next.js** is a React framework for building full-stack web applications with built-in routing, rendering strategies, and optimization.

```
┌─────────────────────────────────────┐
│     Plain React                     │
├─────────────────────────────────────┤
│  ❌ Manual routing setup            │
│  ❌ Client-side only                │
│  ❌ Manual SEO optimization         │
│  ❌ No built-in API routes          │
│  ❌ Manual code splitting           │
└─────────────────────────────────────┘
                 vs
┌─────────────────────────────────────┐
│     Next.js                         │
├─────────────────────────────────────┤
│  ✅ File-based routing              │
│  ✅ SSR + SSG + ISR                 │
│  ✅ Automatic SEO optimization      │
│  ✅ Built-in API routes             │
│  ✅ Automatic code splitting        │
│  ✅ Image optimization              │
│  ✅ TypeScript support              │
└─────────────────────────────────────┘
```

### Why Next.js?

- ✅ **Performance** - Automatic optimization
- ✅ **SEO-Friendly** - Server-side rendering
- ✅ **Developer Experience** - Hot reload, TypeScript, ESLint
- ✅ **Full-Stack** - Frontend + Backend in one project
- ✅ **Production-Ready** - Used by Vercel, Netflix, TikTok

---

## 🔧 Installation & Setup {#setup}

### Create New Project

```bash
# Create Next.js app
npx create-next-app@latest my-next-app

# Options
✔ Would you like to use TypeScript? › Yes
✔ Would you like to use ESLint? › Yes
✔ Would you like to use Tailwind CSS? › Yes
✔ Would you like to use `src/` directory? › Yes
✔ Would you like to use App Router? › Yes
✔ Would you like to customize the default import alias? › No

# Navigate to project
cd my-next-app

# Start development server
npm run dev
```

### Project Structure (App Router)

```
my-next-app/
├── src/
│   └── app/
│       ├── page.tsx          # Home page (/)
│       ├── layout.tsx        # Root layout
│       ├── globals.css       # Global styles
│       ├── about/
│       │   └── page.tsx      # About page (/about)
│       └── api/
│           └── hello/
│               └── route.ts  # API endpoint
├── public/
│   └── images/               # Static assets
├── next.config.js            # Next.js configuration
├── package.json
└── tsconfig.json
```

### Running Commands

```bash
# Development
npm run dev          # Start dev server (http://localhost:3000)

# Production
npm run build        # Build for production
npm run start        # Start production server

# Linting
npm run lint         # Run ESLint
```

---

## 🛣️ File-based Routing {#routing}

### Basic Routes

```
File Structure                    URL
──────────────────────────────────────────
app/page.tsx                  →   /
app/about/page.tsx            →   /about
app/blog/page.tsx             →   /blog
app/contact/page.tsx          →   /contact
app/dashboard/page.tsx        →   /dashboard
app/products/page.tsx         →   /products
```

**Example: Creating Pages**

```tsx
// app/page.tsx (Home Page)
export default function Home() {
  return (
    <main className="p-8">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
      <p>This is the home page</p>
    </main>
  )
}

// app/about/page.tsx
export default function About() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold">About Us</h1>
      <p>Learn more about our company</p>
    </div>
  )
}
```

### Nested Routes

```
File Structure                    URL
──────────────────────────────────────────
app/blog/page.tsx             →   /blog
app/blog/[slug]/page.tsx      →   /blog/my-post
app/dashboard/page.tsx        →   /dashboard
app/dashboard/settings/page.tsx →  /dashboard/settings
```

### Route Groups (Organization Only)

```
app/
├── (marketing)/
│   ├── about/page.tsx        →   /about
│   └── contact/page.tsx      →   /contact
├── (shop)/
│   ├── products/page.tsx     →   /products
│   └── cart/page.tsx         →   /cart
└── page.tsx                  →   /

Note: (marketing) and (shop) don't appear in URL
```

---

## ⚡ App Router vs Pages Router {#routers}

### App Router (New - Recommended)

```tsx
// app/page.tsx
export default function Page() {
  return <h1>App Router</h1>
}

Benefits:
✅ Server Components by default
✅ Layouts and nested routing
✅ Better data fetching
✅ Streaming and Suspense
```

### Pages Router (Legacy)

```tsx
// pages/index.tsx
export default function Page() {
  return <h1>Pages Router</h1>
}

When to use:
- Existing projects
- Need getServerSideProps
- Community plugins compatibility
```

**This guide focuses on App Router** (modern approach)

---

## 🧩 Server & Client Components {#components}

### Server Components (Default)

Components that render on the server.

```tsx
// app/products/page.tsx (Server Component)
async function getProducts() {
  const res = await fetch('https://api.example.com/products')
  return res.json()
}

export default async function ProductsPage() {
  const products = await getProducts()
  
  return (
    <div>
      <h1>Products</h1>
      {products.map(product => (
        <div key={product.id}>{product.name}</div>
      ))}
    </div>
  )
}
```

**Benefits:**
- ✅ Direct database access
- ✅ Server-only code (API keys safe)
- ✅ Smaller bundle size
- ✅ Better SEO

### Client Components

Components that need interactivity.

```tsx
'use client'  // ← Required for client components

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  )
}
```

**When to use Client Components:**
- useState, useEffect, other hooks
- Browser APIs (localStorage, window)
- Event handlers (onClick, onChange)
- Third-party libraries with browser dependencies

### Composition Pattern

```tsx
// app/page.tsx (Server Component)
import ClientCounter from '@/components/ClientCounter'

async function getData() {
  // Server-side data fetching
  const res = await fetch('https://api.example.com/data')
  return res.json()
}

export default async function Page() {
  const data = await getData()
  
  return (
    <div>
      <h1>Server Component</h1>
      <p>Data from server: {data.message}</p>
      
      {/* Embed Client Component */}
      <ClientCounter />
    </div>
  )
}
```

---

## 📊 Data Fetching {#data-fetching}

### Server Component (Async/Await)

```tsx
// app/posts/page.tsx
async function getPosts() {
  const res = await fetch('https://api.example.com/posts', {
    next: { revalidate: 60 } // Revalidate every 60 seconds
  })
  
  if (!res.ok) {
    throw new Error('Failed to fetch posts')
  }
  
  return res.json()
}

export default async function PostsPage() {
  const posts = await getPosts()
  
  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  )
}
```

### Caching & Revalidation

```tsx
// Static (cached forever)
fetch('https://api.example.com/data')

// Revalidate every hour
fetch('https://api.example.com/data', {
  next: { revalidate: 3600 }
})

// Never cache (always fresh)
fetch('https://api.example.com/data', {
  cache: 'no-store'
})

// Tag-based revalidation
fetch('https://api.example.com/data', {
  next: { tags: ['posts'] }
})
```

### Parallel Data Fetching

```tsx
async function getUser(id: string) {
  const res = await fetch(`https://api.example.com/users/${id}`)
  return res.json()
}

async function getPosts(userId: string) {
  const res = await fetch(`https://api.example.com/posts?userId=${userId}`)
  return res.json()
}

export default async function UserProfile({ params }: { params: { id: string } }) {
  // Fetch in parallel
  const [user, posts] = await Promise.all([
    getUser(params.id),
    getPosts(params.id)
  ])
  
  return (
    <div>
      <h1>{user.name}</h1>
      <div>
        {posts.map(post => (
          <article key={post.id}>{post.title}</article>
        ))}
      </div>
    </div>
  )
}
```

### Loading & Error States

```tsx
// app/posts/loading.tsx (Loading UI)
export default function Loading() {
  return <div>Loading posts...</div>
}

// app/posts/error.tsx (Error UI)
'use client'

export default function Error({
  error,
  reset
}: {
  error: Error
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <p>{error.message}</p>
      <button onClick={reset}>Try again</button>
    </div>
  )
}
```

---

## 🔌 API Routes {#api-routes}

### Creating API Routes

```tsx
// app/api/hello/route.ts
import { NextResponse } from 'next/server'

export async function GET() {
  return NextResponse.json({ message: 'Hello from API!' })
}
```

**URL:** `http://localhost:3000/api/hello`

### HTTP Methods

```tsx
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server'

// GET /api/users
export async function GET(request: NextRequest) {
  const users = [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Jane Smith' }
  ]
  
  return NextResponse.json(users)
}

// POST /api/users
export async function POST(request: NextRequest) {
  const body = await request.json()
  
  // Validate data
  if (!body.name || !body.email) {
    return NextResponse.json(
      { error: 'Name and email required' },
      { status: 400 }
    )
  }
  
  // Create user in database
  const user = { id: 3, name: body.name, email: body.email }
  
  return NextResponse.json(user, { status: 201 })
}

// PUT /api/users
export async function PUT(request: NextRequest) {
  const body = await request.json()
  // Update user logic
  return NextResponse.json({ updated: true })
}

// DELETE /api/users
export async function DELETE(request: NextRequest) {
  // Delete user logic
  return NextResponse.json({ deleted: true })
}
```

### Dynamic API Routes

```tsx
// app/api/users/[id]/route.ts
import { NextRequest, NextResponse } from 'next/server'

export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  const userId = params.id
  
  // Fetch user from database
  const user = { id: userId, name: 'John Doe' }
  
  return NextResponse.json(user)
}
```

**URL:** `GET /api/users/123`

### Query Parameters & Headers

```tsx
// app/api/search/route.ts
export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams
  const query = searchParams.get('q')
  const limit = searchParams.get('limit') || '10'
  
  // Get headers
  const authToken = request.headers.get('authorization')
  
  return NextResponse.json({
    query,
    limit,
    authenticated: !!authToken
  })
}
```

**URL:** `GET /api/search?q=nextjs&limit=20`

---

## 🏗️ Static Site Generation (SSG) {#ssg}

### Generate Static Page

```tsx
// app/posts/[slug]/page.tsx
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts').then(res => res.json())
  
  return posts.map((post: any) => ({
    slug: post.slug
  }))
}

export default async function Post({ params }: { params: { slug: string } }) {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`)
    .then(res => res.json())
  
  return (
    <article>
      <h1>{post.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
    </article>
  )
}
```

**At build time, Next.js generates:**
- `/posts/first-post`
- `/posts/second-post`
- `/posts/third-post`

### Incremental Static Regeneration (ISR)

```tsx
// Revalidate every 60 seconds
export const revalidate = 60

export default async function Page() {
  const data = await fetch('https://api.example.com/data')
  // Page regenerates every 60 seconds when visited
}
```

---

## 🚀 Server-Side Rendering (SSR) {#ssr}

### Always Fresh Data

```tsx
// app/dashboard/page.tsx
export const dynamic = 'force-dynamic' // Disable caching

export default async function Dashboard() {
  const data = await fetch('https://api.example.com/dashboard', {
    cache: 'no-store'
  }).then(res => res.json())
  
  return (
    <div>
      <h1>Dashboard</h1>
      <p>Last updated: {new Date().toLocaleString()}</p>
      <div>{JSON.stringify(data)}</div>
    </div>
  )
}
```

---

## 🔗 Dynamic Routes {#dynamic-routes}

### Single Dynamic Segment

```tsx
// app/products/[id]/page.tsx
export default function Product({ params }: { params: { id: string } }) {
  return <h1>Product ID: {params.id}</h1>
}
```

**URLs:** `/products/1`, `/products/abc`, `/products/xyz`

### Multiple Dynamic Segments

```tsx
// app/blog/[category]/[slug]/page.tsx
export default function BlogPost({
  params
}: {
  params: { category: string; slug: string }
}) {
  return (
    <div>
      <h1>Category: {params.category}</h1>
      <h2>Post: {params.slug}</h2>
    </div>
  )
}
```

**URL:** `/blog/tech/nextjs-guide`

### Catch-All Routes

```tsx
// app/docs/[...slug]/page.tsx
export default function Docs({ params }: { params: { slug: string[] } }) {
  return <h1>Docs: {params.slug.join('/')}</h1>
}
```

**URLs:**
- `/docs/getting-started` → `['getting-started']`
- `/docs/api/reference` → `['api', 'reference']`
- `/docs/guides/deployment/vercel` → `['guides', 'deployment', 'vercel']`

---

## 🖼️ Image Optimization {#images}

### Next.js Image Component

```tsx
import Image from 'next/image'

export default function Page() {
  return (
    <div>
      {/* Local image */}
      <Image
        src="/images/hero.jpg"
        alt="Hero"
        width={800}
        height={600}
        priority // Load immediately
      />
      
      {/* Remote image */}
      <Image
        src="https://example.com/photo.jpg"
        alt="Photo"
        width={400}
        height={300}
        loading="lazy" // Lazy load
      />
      
      {/* Responsive image */}
      <Image
        src="/images/banner.jpg"
        alt="Banner"
        fill
        style={{ objectFit: 'cover' }}
      />
    </div>
  )
}
```

**Benefits:**
- ✅ Automatic WebP/AVIF conversion
- ✅ Lazy loading
- ✅ Responsive images
- ✅ Blur placeholder
- ✅ Prevents layout shift

### Configure Remote Images

```javascript
// next.config.js
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        pathname: '/images/**'
      }
    ]
  }
}
```

---

## 🎯 Metadata & SEO {#seo}

### Static Metadata

```tsx
// app/about/page.tsx
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'About Us',
  description: 'Learn more about our company',
  openGraph: {
    title: 'About Us',
    description: 'Learn more about our company',
    images: ['/og-image.jpg']
  }
}

export default function About() {
  return <h1>About Page</h1>
}
```

### Dynamic Metadata

```tsx
// app/products/[id]/page.tsx
export async function generateMetadata({
  params
}: {
  params: { id: string }
}): Promise<Metadata> {
  const product = await fetch(`https://api.example.com/products/${params.id}`)
    .then(res => res.json())
  
  return {
    title: product.name,
    description: product.description,
    openGraph: {
      images: [product.image]
    }
  }
}
```

### Sitemap & Robots.txt

```tsx
// app/sitemap.ts
import { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://example.com',
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 1
    },
    {
      url: 'https://example.com/about',
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8
    }
  ]
}

// app/robots.ts
export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/admin/'
    },
    sitemap: 'https://example.com/sitemap.xml'
  }
}
```

---

## 🔐 Authentication {#auth}

### NextAuth.js Setup

```bash
npm install next-auth
```

```tsx
// app/api/auth/[...nextauth]/route.ts
import NextAuth from 'next-auth'
import GithubProvider from 'next-auth/providers/github'
import CredentialsProvider from 'next-auth/providers/credentials'

const handler = NextAuth({
  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_ID!,
      clientSecret: process.env.GITHUB_SECRET!
    }),
    CredentialsProvider({
      name: 'Credentials',
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        // Verify credentials
        const user = await verifyUser(credentials)
        return user || null
      }
    })
  ],
  pages: {
    signIn: '/login'
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.id = user.id
      }
      return token
    },
    async session({ session, token }) {
      session.user.id = token.id
      return session
    }
  }
})

export { handler as GET, handler as POST }
```

### Protected Routes

```tsx
// app/dashboard/page.tsx
import { getServerSession } from 'next-auth'
import { redirect } from 'next/navigation'

export default async function Dashboard() {
  const session = await getServerSession()
  
  if (!session) {
    redirect('/login')
  }
  
  return (
    <div>
      <h1>Welcome, {session.user?.name}</h1>
    </div>
  )
}
```

### Client-Side Auth

```tsx
'use client'

import { useSession, signIn, signOut } from 'next-auth/react'

export default function LoginButton() {
  const { data: session } = useSession()
  
  if (session) {
    return (
      <div>
        Signed in as {session.user?.email}
        <button onClick={() => signOut()}>Sign out</button>
      </div>
    )
  }
  
  return <button onClick={() => signIn()}>Sign in</button>
}
```

---

## 💾 Database Integration {#database}

### Prisma Setup

```bash
npm install prisma @prisma/client
npx prisma init
```

```prisma
// prisma/schema.prisma
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String?
  posts     Post[]
  createdAt DateTime @default(now())
}

model Post {
  id        String   @id @default(cuid())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User     @relation(fields: [authorId], references: [id])
  authorId  String
  createdAt DateTime @default(now())
}
```

```bash
# Generate Prisma Client
npx prisma generate

# Run migrations
npx prisma migrate dev
```

### Using Prisma

```tsx
// lib/prisma.ts
import { PrismaClient } from '@prisma/client'

const globalForPrisma = global as unknown as { prisma: PrismaClient }

export const prisma = globalForPrisma.prisma || new PrismaClient()

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma

// app/posts/page.tsx
import { prisma } from '@/lib/prisma'

export default async function Posts() {
  const posts = await prisma.post.findMany({
    where: { published: true },
    include: { author: true },
    orderBy: { createdAt: 'desc' }
  })
  
  return (
    <div>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>By {post.author.name}</p>
        </article>
      ))}
    </div>
  )
}

// app/api/posts/route.ts
import { prisma } from '@/lib/prisma'
import { NextResponse } from 'next/server'

export async function POST(request: Request) {
  const { title, content, authorId } = await request.json()
  
  const post = await prisma.post.create({
    data: {
      title,
      content,
      author: { connect: { id: authorId } }
    }
  })
  
  return NextResponse.json(post, { status: 201 })
}
```

---

## 🚀 Deployment {#deployment}

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Production deployment
vercel --prod
```

### Docker Deployment

```dockerfile
# Dockerfile
FROM node:18-alpine AS base

# Dependencies
FROM base AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

# Builder
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# Runner
FROM base AS runner
WORKDIR /app

ENV NODE_ENV production

COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static

EXPOSE 3000

CMD ["node", "server.js"]
```

### Environment Variables

```bash
# .env.local
DATABASE_URL="postgresql://..."
NEXTAUTH_SECRET="your-secret"
NEXTAUTH_URL="http://localhost:3000"
```

---

## ✅ Best Practices {#best-practices}

### 1. Use Server Components by Default

```tsx
// ✅ Good: Server Component
async function Page() {
  const data = await fetchData()
  return <div>{data}</div>
}

// ❌ Avoid: Unnecessary Client Component
'use client'
function Page() {
  // No hooks or browser APIs used
  return <div>Static content</div>
}
```

### 2. Optimize Images

```tsx
// ✅ Use Next.js Image
import Image from 'next/image'
<Image src="/photo.jpg" width={800} height={600} alt="Photo" />

// ❌ Avoid regular img
<img src="/photo.jpg" alt="Photo" />
```

### 3. Implement Metadata

```tsx
// ✅ Every page should have metadata
export const metadata = {
  title: 'Page Title',
  description: 'Page description'
}
```

### 4. Use Loading States

```tsx
// app/posts/loading.tsx
export default function Loading() {
  return <Skeleton />
}
```

---

## 🎯 Real-World Projects {#projects}

### Project 1: Blog Platform
- SSG for blog posts
- Admin dashboard with auth
- API routes for CRUD
- Image optimization
- SEO metadata

### Project 2: E-commerce Store
- Dynamic product pages
- Shopping cart (client component)
- Checkout with Stripe
- Order management
- Admin panel

### Project 3: SaaS Dashboard
- NextAuth authentication
- Protected routes
- Prisma + PostgreSQL
- Real-time updates
- Analytics dashboard

---

## 🏆 Congratulations!

You've mastered Next.js! You can now:

- ✅ Build full-stack applications
- ✅ Optimize for SEO and performance
- ✅ Implement authentication
- ✅ Work with databases
- ✅ Deploy to production

**Next Steps:**
- Build real projects
- Learn advanced patterns
- Explore Next.js 15 features
- Study server actions

Keep building! 🚀

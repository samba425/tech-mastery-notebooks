# Performance Optimization: Complete Guide
## Frontend, Backend, Database & Infrastructure Performance Mastery

---

## 📚 Table of Contents

1. [Introduction to Performance Optimization](#introduction)
2. [Performance Fundamentals](#fundamentals)
3. [Frontend Performance Optimization](#frontend)
4. [Backend Performance Optimization](#backend)
5. [Database Performance Tuning](#database)
6. [Caching Strategies](#caching)
7. [Load Testing & Monitoring](#testing)
8. [Network & Infrastructure Optimization](#network)
9. [Code-Level Optimizations](#code-level)
10. [Memory Management & Optimization](#memory)
11. [Security vs Performance Trade-offs](#security)
12. [Real-World Case Studies](#case-studies)
13. [Performance Best Practices](#best-practices)

---

## 🎯 Introduction to Performance Optimization {#introduction}

### What is Performance Optimization?

**Performance Optimization** is the process of making systems faster, more efficient, and capable of handling larger loads while maintaining reliability and user experience.

```
Before Optimization
┌─────────────────────────────────────┐
│  Slow Response Times (3-5 seconds)  │
│  High Resource Usage (80%+ CPU)     │
│  Poor User Experience              │
│  Limited Concurrent Users          │
│  Frequent Timeouts                 │
└─────────────────────────────────────┘

After Optimization  
┌─────────────────────────────────────┐
│  Fast Response Times (<200ms)       │
│  Optimized Resource Usage (40% CPU) │
│  Excellent User Experience         │
│  High Concurrent Users             │
│  Reliable Performance              │
└─────────────────────────────────────┘
```

### Performance Metrics That Matter

**Frontend Metrics**:
- **First Contentful Paint (FCP)**: < 1.8 seconds
- **Largest Contentful Paint (LCP)**: < 2.5 seconds  
- **First Input Delay (FID)**: < 100 milliseconds
- **Cumulative Layout Shift (CLS)**: < 0.1
- **Time to Interactive (TTI)**: < 3.8 seconds

**Backend Metrics**:
- **Response Time**: < 200ms for API calls
- **Throughput**: Requests handled per second
- **Error Rate**: < 0.1% for critical paths
- **CPU Usage**: < 70% under normal load
- **Memory Usage**: < 80% of available memory

**Database Metrics**:
- **Query Response Time**: < 100ms for simple queries
- **Connection Pool Usage**: < 80% of pool size
- **Cache Hit Ratio**: > 90% for frequently accessed data
- **Index Usage**: > 95% of queries use indexes
- **Lock Wait Time**: < 10ms average

### Performance Budget Framework

```javascript
// Performance budgets for different page types
const performanceBudgets = {
  'landing-page': {
    totalSize: '1.5MB',
    javascript: '300KB',
    css: '100KB', 
    images: '1MB',
    fonts: '100KB',
    firstLoad: '2s',
    repeatVisit: '1s'
  },
  'dashboard': {
    totalSize: '2MB',
    javascript: '500KB',
    css: '150KB',
    images: '1.2MB',
    fonts: '150KB',
    firstLoad: '3s',
    repeatVisit: '1.5s'
  },
  'mobile': {
    totalSize: '1MB',
    javascript: '200KB',
    css: '80KB',
    images: '600KB',
    fonts: '80KB',
    firstLoad: '1.5s',
    repeatVisit: '0.8s'
  }
}

// Budget monitoring function
function checkPerformanceBudget(pageType, actualMetrics) {
  const budget = performanceBudgets[pageType]
  const violations = []
  
  Object.keys(budget).forEach(metric => {
    const budgetValue = parseSize(budget[metric])
    const actualValue = actualMetrics[metric]
    
    if (actualValue > budgetValue) {
      violations.push({
        metric,
        budget: budget[metric],
        actual: actualValue,
        overBudget: actualValue - budgetValue
      })
    }
  })
  
  return violations
}

function parseSize(sizeString) {
  const units = { 'KB': 1024, 'MB': 1024 * 1024, 's': 1 }
  const match = sizeString.match(/^([\d.]+)([A-Za-z]+)$/)
  
  if (match) {
    const [, number, unit] = match
    return parseFloat(number) * (units[unit] || 1)
  }
  
  return parseFloat(sizeString)
}
```

---

## ⚡ Performance Fundamentals {#fundamentals}

### The Performance Optimization Process

```
1. Measure & Baseline
   ├─ Set up monitoring
   ├─ Collect baseline metrics
   └─ Identify bottlenecks

2. Analyze & Prioritize
   ├─ Profile application
   ├─ Find performance hotspots
   └─ Prioritize by impact

3. Optimize & Test
   ├─ Implement optimizations
   ├─ Measure improvements
   └─ Validate no regressions

4. Monitor & Iterate
   ├─ Continuous monitoring
   ├─ Performance alerts
   └─ Regular optimization cycles
```

### Performance Profiling Tools

```python
import time
import functools
import psutil
import tracemalloc
from memory_profiler import profile
import cProfile
import pstats
import io
from typing import Callable, Any, Dict
import logging
from contextlib import contextmanager

class PerformanceProfiler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.metrics = {}
    
    def timing_decorator(self, func_name: str = None):
        """Decorator to measure function execution time"""
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                name = func_name or func.__name__
                start_time = time.perf_counter()
                
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    end_time = time.perf_counter()
                    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                    
                    # Track timing metrics
                    if name not in self.metrics:
                        self.metrics[name] = []
                    self.metrics[name].append(execution_time)
                    
                    self.logger.info(f"Function {name} took {execution_time:.2f}ms")
            
            return wrapper
        return decorator
    
    @contextmanager
    def measure_block(self, block_name: str):
        """Context manager to measure code block performance"""
        start_time = time.perf_counter()
        start_memory = psutil.Process().memory_info().rss
        
        try:
            yield
        finally:
            end_time = time.perf_counter()
            end_memory = psutil.Process().memory_info().rss
            
            execution_time = (end_time - start_time) * 1000
            memory_delta = end_memory - start_memory
            
            self.logger.info(f"Block {block_name}: {execution_time:.2f}ms, "
                           f"Memory delta: {memory_delta / 1024 / 1024:.2f}MB")
    
    def profile_function(self, func: Callable, *args, **kwargs):
        """Profile function with cProfile"""
        pr = cProfile.Profile()
        pr.enable()
        
        try:
            result = func(*args, **kwargs)
        finally:
            pr.disable()
        
        # Get profile stats
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
        ps.print_stats(20)  # Top 20 functions
        
        profile_output = s.getvalue()
        self.logger.info(f"Profile for {func.__name__}:\n{profile_output}")
        
        return result
    
    def memory_profile_function(self, func: Callable, *args, **kwargs):
        """Profile function memory usage"""
        tracemalloc.start()
        
        try:
            result = func(*args, **kwargs)
        finally:
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            self.logger.info(f"Memory usage for {func.__name__}: "
                           f"Current: {current / 1024 / 1024:.2f}MB, "
                           f"Peak: {peak / 1024 / 1024:.2f}MB")
        
        return result
    
    def get_timing_statistics(self, func_name: str) -> Dict[str, float]:
        """Get timing statistics for a function"""
        if func_name not in self.metrics:
            return {}
        
        timings = self.metrics[func_name]
        
        return {
            'count': len(timings),
            'mean': sum(timings) / len(timings),
            'min': min(timings),
            'max': max(timings),
            'p50': sorted(timings)[len(timings) // 2],
            'p95': sorted(timings)[int(len(timings) * 0.95)],
            'p99': sorted(timings)[int(len(timings) * 0.99)]
        }

# System Resource Monitor
class SystemResourceMonitor:
    def __init__(self, interval_seconds: int = 1):
        self.interval_seconds = interval_seconds
        self.monitoring = False
        self.metrics_history = []
    
    def start_monitoring(self):
        """Start system resource monitoring"""
        self.monitoring = True
        
        import threading
        
        def monitor_loop():
            while self.monitoring:
                metrics = self.collect_system_metrics()
                self.metrics_history.append(metrics)
                time.sleep(self.interval_seconds)
        
        monitor_thread = threading.Thread(target=monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
    
    def stop_monitoring(self):
        """Stop system resource monitoring"""
        self.monitoring = False
    
    def collect_system_metrics(self) -> Dict[str, Any]:
        """Collect current system metrics"""
        process = psutil.Process()
        
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'cpu': {
                'process_percent': process.cpu_percent(),
                'system_percent': psutil.cpu_percent(interval=None),
                'core_count': psutil.cpu_count()
            },
            'memory': {
                'process_mb': process.memory_info().rss / 1024 / 1024,
                'process_percent': process.memory_percent(),
                'system_available_mb': psutil.virtual_memory().available / 1024 / 1024,
                'system_used_percent': psutil.virtual_memory().percent
            },
            'disk': {
                'io_read_mb': psutil.disk_io_counters().read_bytes / 1024 / 1024 if psutil.disk_io_counters() else 0,
                'io_write_mb': psutil.disk_io_counters().write_bytes / 1024 / 1024 if psutil.disk_io_counters() else 0,
                'usage_percent': psutil.disk_usage('/').percent
            },
            'network': {
                'bytes_sent': psutil.net_io_counters().bytes_sent if psutil.net_io_counters() else 0,
                'bytes_recv': psutil.net_io_counters().bytes_recv if psutil.net_io_counters() else 0,
                'packets_sent': psutil.net_io_counters().packets_sent if psutil.net_io_counters() else 0,
                'packets_recv': psutil.net_io_counters().packets_recv if psutil.net_io_counters() else 0
            }
        }
        
        return metrics
    
    def get_performance_summary(self, duration_minutes: int = 5) -> Dict[str, Any]:
        """Get performance summary for specified duration"""
        cutoff_time = datetime.now() - timedelta(minutes=duration_minutes)
        
        recent_metrics = [
            m for m in self.metrics_history 
            if datetime.fromisoformat(m['timestamp']) > cutoff_time
        ]
        
        if not recent_metrics:
            return {}
        
        # Calculate averages
        summary = {
            'period_minutes': duration_minutes,
            'sample_count': len(recent_metrics),
            'cpu': {
                'avg_process_percent': sum(m['cpu']['process_percent'] for m in recent_metrics) / len(recent_metrics),
                'max_process_percent': max(m['cpu']['process_percent'] for m in recent_metrics),
                'avg_system_percent': sum(m['cpu']['system_percent'] for m in recent_metrics) / len(recent_metrics)
            },
            'memory': {
                'avg_process_mb': sum(m['memory']['process_mb'] for m in recent_metrics) / len(recent_metrics),
                'max_process_mb': max(m['memory']['process_mb'] for m in recent_metrics),
                'avg_system_used_percent': sum(m['memory']['system_used_percent'] for m in recent_metrics) / len(recent_metrics)
            }
        }
        
        return summary

# Usage examples
if __name__ == "__main__":
    # Initialize profiler
    profiler = PerformanceProfiler()
    
    # Example function to profile
    @profiler.timing_decorator("slow_function")
    def slow_function(n):
        """Simulate slow function"""
        total = 0
        for i in range(n):
            total += i ** 2
        time.sleep(0.1)  # Simulate I/O
        return total
    
    # Run function multiple times
    for i in range(5):
        result = slow_function(10000)
    
    # Get timing statistics
    stats = profiler.get_timing_statistics("slow_function")
    print(f"Timing stats: {stats}")
    
    # Profile with context manager
    with profiler.measure_block("data_processing"):
        # Simulate data processing
        import pandas as pd
        df = pd.DataFrame({'x': range(10000), 'y': range(10000)})
        result = df.groupby('x').sum()
    
    # Start system monitoring
    monitor = SystemResourceMonitor(interval_seconds=1)
    monitor.start_monitoring()
    
    # Simulate workload
    time.sleep(5)
    
    # Stop monitoring and get summary
    monitor.stop_monitoring()
    summary = monitor.get_performance_summary(duration_minutes=1)
    print(f"System performance summary: {summary}")
```

---

## 🎨 Frontend Performance Optimization {#frontend}

### Critical Rendering Path Optimization

```html
<!-- Optimized HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Preconnect to external domains -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://api.example.com">
    
    <!-- DNS prefetch for third-party resources -->
    <link rel="dns-prefetch" href="https://analytics.google.com">
    
    <!-- Inline critical CSS -->
    <style>
        /* Critical above-the-fold CSS */
        body { font-family: Arial, sans-serif; margin: 0; }
        .header { background: #333; color: white; padding: 1rem; }
        .main-content { min-height: 400px; }
    </style>
    
    <!-- Preload critical resources -->
    <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/js/critical.js" as="script">
    
    <!-- Load non-critical CSS asynchronously -->
    <link rel="preload" href="/css/non-critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    <noscript><link rel="stylesheet" href="/css/non-critical.css"></noscript>
    
    <title>Performance Optimized Page</title>
</head>
<body>
    <!-- Critical above-the-fold content -->
    <header class="header">
        <h1>Fast Loading Site</h1>
    </header>
    
    <main class="main-content">
        <!-- Hero section - visible immediately -->
        <section class="hero">
            <h2>Welcome to our fast site!</h2>
            <!-- Optimized image with modern formats -->
            <picture>
                <source srcset="/images/hero.webp" type="image/webp">
                <source srcset="/images/hero.avif" type="image/avif">
                <img src="/images/hero.jpg" 
                     alt="Hero image" 
                     loading="eager"
                     width="800" 
                     height="400"
                     decoding="sync">
            </picture>
        </section>
        
        <!-- Below-the-fold content with lazy loading -->
        <section class="products">
            <h2>Our Products</h2>
            <div class="product-grid" id="product-grid">
                <!-- Products loaded dynamically -->
            </div>
        </section>
    </main>
    
    <!-- Critical JavaScript inline -->
    <script>
        // Critical functionality
        (function() {
            // Track performance
            window.performance.mark('contentLoaded');
            
            // Lazy load non-critical components
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        loadProductGrid();
                        observer.disconnect();
                    }
                });
            });
            
            observer.observe(document.getElementById('product-grid'));
        })();
    </script>
    
    <!-- Non-critical JavaScript loaded asynchronously -->
    <script src="/js/analytics.js" async></script>
    <script src="/js/non-critical.js" defer></script>
</body>
</html>
```

### JavaScript Performance Optimization

```javascript
// 1. Efficient DOM Manipulation
class DOMOptimizer {
    constructor() {
        this.batchedUpdates = [];
        this.updateScheduled = false;
    }
    
    // Batch DOM updates to avoid layout thrashing
    batchUpdate(element, property, value) {
        this.batchedUpdates.push({ element, property, value });
        
        if (!this.updateScheduled) {
            this.updateScheduled = true;
            requestAnimationFrame(() => this.flushUpdates());
        }
    }
    
    flushUpdates() {
        // Use document fragment for multiple DOM insertions
        const fragment = document.createDocumentFragment();
        
        this.batchedUpdates.forEach(({ element, property, value }) => {
            if (property === 'appendChild') {
                fragment.appendChild(value);
            } else {
                element[property] = value;
            }
        });
        
        // Single DOM update
        if (fragment.children.length > 0) {
            document.body.appendChild(fragment);
        }
        
        this.batchedUpdates = [];
        this.updateScheduled = false;
    }
    
    // Virtual scrolling for large lists
    createVirtualList(container, items, itemHeight, visibleCount) {
        const totalHeight = items.length * itemHeight;
        const viewport = document.createElement('div');
        viewport.style.height = `${visibleCount * itemHeight}px`;
        viewport.style.overflow = 'auto';
        
        const content = document.createElement('div');
        content.style.height = `${totalHeight}px`;
        content.style.position = 'relative';
        
        viewport.appendChild(content);
        container.appendChild(viewport);
        
        let startIndex = 0;
        
        const updateVisibleItems = () => {
            const scrollTop = viewport.scrollTop;
            const newStartIndex = Math.floor(scrollTop / itemHeight);
            
            if (newStartIndex !== startIndex) {
                startIndex = newStartIndex;
                const endIndex = Math.min(startIndex + visibleCount, items.length);
                
                // Clear existing items
                content.innerHTML = '';
                
                // Render visible items
                for (let i = startIndex; i < endIndex; i++) {
                    const itemElement = document.createElement('div');
                    itemElement.style.position = 'absolute';
                    itemElement.style.top = `${i * itemHeight}px`;
                    itemElement.style.height = `${itemHeight}px`;
                    itemElement.textContent = items[i];
                    content.appendChild(itemElement);
                }
            }
        };
        
        viewport.addEventListener('scroll', updateVisibleItems);
        updateVisibleItems(); // Initial render
    }
}

// 2. Efficient Event Handling
class EventOptimizer {
    constructor() {
        this.throttleTimers = new Map();
        this.debounceTimers = new Map();
    }
    
    // Throttle function execution
    throttle(func, delay, key = 'default') {
        if (!this.throttleTimers.has(key)) {
            this.throttleTimers.set(key, null);
        }
        
        if (!this.throttleTimers.get(key)) {
            func();
            this.throttleTimers.set(key, setTimeout(() => {
                this.throttleTimers.set(key, null);
            }, delay));
        }
    }
    
    // Debounce function execution
    debounce(func, delay, key = 'default') {
        if (this.debounceTimers.has(key)) {
            clearTimeout(this.debounceTimers.get(key));
        }
        
        this.debounceTimers.set(key, setTimeout(func, delay));
    }
    
    // Optimized scroll handling
    optimizeScrollEvents() {
        let ticking = false;
        
        function updateScrollPosition() {
            // Expensive scroll operations here
            console.log('Scroll position updated');
            ticking = false;
        }
        
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(updateScrollPosition);
                ticking = true;
            }
        });
    }
    
    // Event delegation for dynamic content
    setupEventDelegation(container, selector, eventType, handler) {
        container.addEventListener(eventType, (event) => {
            if (event.target.matches(selector)) {
                handler(event);
            }
        });
    }
}

// 3. Memory Management
class MemoryManager {
    constructor() {
        this.cache = new Map();
        this.maxCacheSize = 1000;
        this.observers = [];
    }
    
    // Object pooling for frequently created objects
    createObjectPool(createFn, resetFn, initialSize = 10) {
        const pool = [];
        
        // Pre-populate pool
        for (let i = 0; i < initialSize; i++) {
            pool.push(createFn());
        }
        
        return {
            acquire: () => {
                if (pool.length > 0) {
                    return pool.pop();
                } else {
                    return createFn();
                }
            },
            
            release: (obj) => {
                resetFn(obj);
                if (pool.length < initialSize * 2) {
                    pool.push(obj);
                }
            }
        };
    }
    
    // Efficient caching with LRU eviction
    set(key, value) {
        // Remove if exists to update position
        if (this.cache.has(key)) {
            this.cache.delete(key);
        }
        
        // Evict oldest if cache is full
        if (this.cache.size >= this.maxCacheSize) {
            const firstKey = this.cache.keys().next().value;
            this.cache.delete(firstKey);
        }
        
        this.cache.set(key, value);
    }
    
    get(key) {
        if (this.cache.has(key)) {
            // Move to end (most recently used)
            const value = this.cache.get(key);
            this.cache.delete(key);
            this.cache.set(key, value);
            return value;
        }
        return null;
    }
    
    // Cleanup unused observers
    cleanupObservers() {
        this.observers = this.observers.filter(observer => {
            if (observer.element && !document.contains(observer.element)) {
                // Element no longer in DOM, cleanup observer
                if (observer.disconnect) {
                    observer.disconnect();
                }
                return false;
            }
            return true;
        });
    }
}

// 4. Image Optimization
class ImageOptimizer {
    constructor() {
        this.loadedImages = new Set();
        this.imageCache = new Map();
    }
    
    // Lazy loading with Intersection Observer
    setupLazyLoading() {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    this.loadImage(img);
                    imageObserver.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px'  // Start loading 50px before entering viewport
        });
        
        // Observe all images with data-src
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    loadImage(img) {
        const src = img.dataset.src;
        
        if (this.loadedImages.has(src)) {
            img.src = src;
            return;
        }
        
        // Show loading placeholder
        img.classList.add('loading');
        
        const imageLoader = new Image();
        imageLoader.onload = () => {
            img.src = src;
            img.classList.remove('loading');
            img.classList.add('loaded');
            this.loadedImages.add(src);
        };
        
        imageLoader.onerror = () => {
            img.classList.remove('loading');
            img.classList.add('error');
            img.src = '/images/placeholder.jpg'; // Fallback image
        };
        
        imageLoader.src = src;
    }
    
    // Responsive image loading
    loadResponsiveImage(img) {
        const sizes = [480, 768, 1024, 1200, 1600];
        const devicePixelRatio = window.devicePixelRatio || 1;
        const screenWidth = window.screen.width * devicePixelRatio;
        
        // Find appropriate size
        const targetSize = sizes.find(size => size >= screenWidth) || sizes[sizes.length - 1];
        
        const baseUrl = img.dataset.baseUrl;
        const format = this.supportsWebP() ? 'webp' : 'jpg';
        const optimizedSrc = `${baseUrl}?w=${targetSize}&f=${format}&q=80`;
        
        img.src = optimizedSrc;
    }
    
    supportsWebP() {
        // Check WebP support
        return document.createElement('canvas')
            .toDataURL('image/webp')
            .indexOf('data:image/webp') === 0;
    }
    
    // Preload critical images
    preloadCriticalImages(imageUrls) {
        imageUrls.forEach(url => {
            if (!this.loadedImages.has(url)) {
                const link = document.createElement('link');
                link.rel = 'preload';
                link.as = 'image';
                link.href = url;
                document.head.appendChild(link);
                
                this.loadedImages.add(url);
            }
        });
    }
}

// 5. JavaScript Bundle Optimization
class BundleOptimizer {
    // Code splitting with dynamic imports
    async loadComponent(componentName) {
        try {
            const module = await import(`./components/${componentName}.js`);
            return module.default;
        } catch (error) {
            console.error(`Failed to load component ${componentName}:`, error);
            return null;
        }
    }
    
    // Service worker for aggressive caching
    registerServiceWorker() {
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => {
                    console.log('SW registered:', registration);
                })
                .catch(error => {
                    console.log('SW registration failed:', error);
                });
        }
    }
    
    // Resource prioritization
    prioritizeResources() {
        // Critical resources
        const criticalScripts = ['/js/critical.js', '/js/framework.js'];
        const nonCriticalScripts = ['/js/analytics.js', '/js/social.js'];
        
        // Load critical scripts first
        criticalScripts.forEach(script => {
            const scriptElement = document.createElement('script');
            scriptElement.src = script;
            scriptElement.defer = true;
            document.head.appendChild(scriptElement);
        });
        
        // Load non-critical scripts after page load
        window.addEventListener('load', () => {
            setTimeout(() => {
                nonCriticalScripts.forEach(script => {
                    const scriptElement = document.createElement('script');
                    scriptElement.src = script;
                    scriptElement.async = true;
                    document.head.appendChild(scriptElement);
                });
            }, 1000);
        });
    }
}

// Service Worker for Advanced Caching
// sw.js
const CACHE_NAME = 'app-cache-v2';
const STATIC_CACHE = 'static-cache-v2';
const DYNAMIC_CACHE = 'dynamic-cache-v1';

// Cache strategies
const CACHE_STRATEGIES = {
    'cache-first': ['images', 'fonts', 'css'],
    'network-first': ['api', 'html'],
    'stale-while-revalidate': ['js']
};

self.addEventListener('install', (event) => {
    event.waitUntil(
        Promise.all([
            caches.open(STATIC_CACHE).then(cache => {
                return cache.addAll([
                    '/',
                    '/css/critical.css',
                    '/js/critical.js',
                    '/fonts/main.woff2',
                    '/images/logo.svg'
                ]);
            })
        ])
    );
});

self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);
    
    // Skip non-GET requests
    if (request.method !== 'GET') {
        return;
    }
    
    // Handle different resource types
    if (url.pathname.startsWith('/api/')) {
        event.respondWith(networkFirst(request));
    } else if (url.pathname.match(/\.(js|css)$/)) {
        event.respondWith(staleWhileRevalidate(request));
    } else if (url.pathname.match(/\.(png|jpg|jpeg|gif|svg|webp)$/)) {
        event.respondWith(cacheFirst(request));
    } else {
        event.respondWith(networkFirst(request));
    }
});

// Cache strategies
async function cacheFirst(request) {
    const cached = await caches.match(request);
    
    if (cached) {
        return cached;
    }
    
    try {
        const response = await fetch(request);
        
        if (response.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, response.clone());
        }
        
        return response;
    } catch (error) {
        // Return fallback for images
        if (request.url.match(/\.(png|jpg|jpeg|gif|svg|webp)$/)) {
            return caches.match('/images/fallback.jpg');
        }
        throw error;
    }
}

async function networkFirst(request) {
    try {
        const response = await fetch(request);
        
        if (response.ok) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, response.clone());
        }
        
        return response;
    } catch (error) {
        const cached = await caches.match(request);
        if (cached) {
            return cached;
        }
        throw error;
    }
}

async function staleWhileRevalidate(request) {
    const cached = await caches.match(request);
    
    // Fetch fresh version in background
    const fetchPromise = fetch(request).then(response => {
        if (response.ok) {
            const cache = caches.open(DYNAMIC_CACHE);
            cache.then(c => c.put(request, response.clone()));
        }
        return response;
    });
    
    // Return cached version immediately if available
    return cached || fetchPromise;
}
```

### React Performance Optimization

```jsx
import React, { 
    memo, 
    useMemo, 
    useCallback, 
    useState, 
    useEffect,
    Suspense,
    lazy
} from 'react';

// 1. Component Memoization
const ExpensiveComponent = memo(({ data, onUpdate }) => {
    // This component only re-renders when data or onUpdate changes
    const processedData = useMemo(() => {
        // Expensive calculation
        return data.map(item => ({
            ...item,
            calculated: item.value * 2.5,
            formatted: `$${item.value.toFixed(2)}`
        }));
    }, [data]);
    
    // Memoize event handlers
    const handleClick = useCallback((id) => {
        onUpdate(id);
    }, [onUpdate]);
    
    return (
        <div className="expensive-component">
            {processedData.map(item => (
                <div key={item.id} onClick={() => handleClick(item.id)}>
                    {item.formatted}
                </div>
            ))}
        </div>
    );
});

// 2. Code Splitting and Lazy Loading
const LazyDashboard = lazy(() => import('./Dashboard'));
const LazyReports = lazy(() => import('./Reports'));
const LazySettings = lazy(() => import('./Settings'));

const App = () => {
    const [currentView, setCurrentView] = useState('dashboard');
    
    const renderView = () => {
        switch (currentView) {
            case 'dashboard':
                return <LazyDashboard />;
            case 'reports':
                return <LazyReports />;
            case 'settings':
                return <LazySettings />;
            default:
                return <div>Select a view</div>;
        }
    };
    
    return (
        <div className="app">
            <nav>
                <button onClick={() => setCurrentView('dashboard')}>Dashboard</button>
                <button onClick={() => setCurrentView('reports')}>Reports</button>
                <button onClick={() => setCurrentView('settings')}>Settings</button>
            </nav>
            
            <main>
                <Suspense fallback={<div className="loading">Loading...</div>}>
                    {renderView()}
                </Suspense>
            </main>
        </div>
    );
};

// 3. Virtualized Lists for Large Datasets
import { FixedSizeList as List } from 'react-window';

const VirtualizedList = ({ items }) => {
    const Row = memo(({ index, style }) => (
        <div style={style} className="list-item">
            <div>{items[index].name}</div>
            <div>{items[index].value}</div>
        </div>
    ));
    
    return (
        <List
            height={600}        // Container height
            itemCount={items.length}
            itemSize={60}       // Height of each item
            width="100%"
        >
            {Row}
        </List>
    );
};

// 4. Optimized State Management
import { createStore } from 'zustand';
import { subscribeWithSelector } from 'zustand/middleware';

// Efficient store with selectors
const useAppStore = createStore(
    subscribeWithSelector((set, get) => ({
        users: [],
        products: [],
        orders: [],
        
        // Optimized actions
        addUser: (user) => set(state => ({
            users: [...state.users, user]
        })),
        
        updateUser: (id, updates) => set(state => ({
            users: state.users.map(user => 
                user.id === id ? { ...user, ...updates } : user
            )
        })),
        
        // Memoized selectors
        getUserById: (id) => get().users.find(user => user.id === id),
        
        getActiveUsers: () => get().users.filter(user => user.active),
        
        getUserCount: () => get().users.length
    }))
);

// Component with optimized subscriptions
const UserList = () => {
    // Subscribe only to users array, not entire store
    const users = useAppStore(state => state.users);
    const activeUsers = useAppStore(state => state.getActiveUsers());
    
    // Only re-render when user count changes
    const userCount = useAppStore(
        state => state.users.length,
        // Custom equality function
        (oldCount, newCount) => oldCount === newCount
    );
    
    return (
        <div>
            <h2>Users ({userCount})</h2>
            {activeUsers.map(user => (
                <UserCard key={user.id} user={user} />
            ))}
        </div>
    );
};

const UserCard = memo(({ user }) => {
    return (
        <div className="user-card">
            <h3>{user.name}</h3>
            <p>{user.email}</p>
        </div>
    );
});
```

### CSS Performance Optimization

```css
/* 1. Efficient CSS Selectors */
/* ❌ Inefficient - descendant selector */
.container .header .nav .menu .item {
    color: blue;
}

/* ✅ Efficient - class selector */
.nav-menu-item {
    color: blue;
}

/* 2. Hardware Acceleration */
.accelerated-element {
    /* Trigger hardware acceleration */
    transform: translateZ(0);
    /* or */
    will-change: transform, opacity;
}

.smooth-animation {
    /* Use transform instead of changing layout properties */
    transition: transform 0.3s ease;
}

.smooth-animation:hover {
    /* ✅ Good - only affects composite layer */
    transform: scale(1.05);
    
    /* ❌ Bad - triggers layout recalculation */
    /* width: 120%; height: 120%; */
}

/* 3. Critical CSS Inlining */
/* Above-the-fold styles - inline in HTML */
.hero-section {
    background: linear-gradient(45deg, #1e3c72, #2a5298);
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.hero-title {
    font-size: 3rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 1rem;
}

/* 4. CSS Grid and Flexbox Performance */
.performance-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
    /* More efficient than float-based layouts */
}

.performance-flex {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    /* More efficient than table-based layouts */
}

/* 5. Contain Property for Performance */
.isolated-component {
    /* Isolate layout, style, and paint operations */
    contain: layout style paint;
}

.size-contained {
    /* Hint that size won't change */
    contain: size;
}

/* 6. Optimized Animations */
@keyframes optimized-fade-in {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in-element {
    animation: optimized-fade-in 0.3s ease-out;
    /* Hint browser about changes */
    will-change: opacity, transform;
}

/* Remove will-change after animation */
.fade-in-element.animation-done {
    will-change: auto;
}

/* 7. Font Performance */
@font-face {
    font-family: 'OptimizedFont';
    src: url('/fonts/font.woff2') format('woff2'),
         url('/fonts/font.woff') format('woff');
    font-display: swap; /* Show fallback font immediately */
    font-weight: 300 700; /* Variable font range */
}

/* 8. Media Queries for Performance */
/* Mobile-first approach */
.responsive-layout {
    /* Base styles for mobile */
    display: block;
}

/* Only load desktop styles on larger screens */
@media (min-width: 768px) {
    .responsive-layout {
        display: grid;
        grid-template-columns: 1fr 3fr;
    }
}

/* Reduce animations on low-end devices */
@media (prefers-reduced-motion: reduce) {
    .animated-element {
        animation: none;
        transition: none;
    }
}
```

---

## 🔧 Backend Performance Optimization {#backend}

### API Performance Optimization

```python
import asyncio
import time
from functools import wraps
from typing import Dict, Any, Optional
import redis
import json
import hashlib
from contextlib import asynccontextmanager

class APIPerformanceOptimizer:
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.metrics = {}
    
    def cache_response(self, ttl: int = 3600):
        """Decorator to cache API responses"""
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                # Create cache key from function name and arguments
                cache_key = self._generate_cache_key(func.__name__, args, kwargs)
                
                # Try to get from cache
                cached_result = self.redis_client.get(cache_key)
                if cached_result:
                    return json.loads(cached_result)
                
                # Execute function and cache result
                result = await func(*args, **kwargs)
                self.redis_client.setex(cache_key, ttl, json.dumps(result))
                
                return result
            return wrapper
        return decorator
    
    def rate_limit(self, requests_per_minute: int = 60):
        """Decorator for API rate limiting"""
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                # Extract user/client identifier
                client_id = kwargs.get('client_id', 'anonymous')
                
                # Check rate limit
                key = f"rate_limit:{func.__name__}:{client_id}"
                current_count = self.redis_client.get(key)
                
                if current_count and int(current_count) >= requests_per_minute:
                    raise Exception(f"Rate limit exceeded: {requests_per_minute} requests per minute")
                
                # Increment counter
                pipe = self.redis_client.pipeline()
                pipe.incr(key)
                pipe.expire(key, 60)  # Reset every minute
                pipe.execute()
                
                return await func(*args, **kwargs)
            return wrapper
        return decorator
    
    def _generate_cache_key(self, func_name: str, args: tuple, kwargs: dict) -> str:
        """Generate deterministic cache key"""
        key_data = f"{func_name}:{str(args)}:{str(sorted(kwargs.items()))}"
        return hashlib.md5(key_data.encode()).hexdigest()

# Database Connection Pooling
import asyncpg
import asyncio
from asyncio import Queue

class DatabasePool:
    def __init__(self, dsn: str, min_size: int = 10, max_size: int = 50):
        self.dsn = dsn
        self.min_size = min_size
        self.max_size = max_size
        self.pool: Optional[asyncpg.Pool] = None
        self.connection_count = 0
    
    async def initialize(self):
        """Initialize connection pool"""
        self.pool = await asyncpg.create_pool(
            self.dsn,
            min_size=self.min_size,
            max_size=self.max_size,
            command_timeout=30,
            server_settings={
                'application_name': 'high_performance_app',
                'jit': 'off'  # Disable JIT for predictable performance
            }
        )
    
    @asynccontextmanager
    async def get_connection(self):
        """Get connection from pool with proper cleanup"""
        async with self.pool.acquire() as connection:
            try:
                yield connection
            except Exception:
                # Reset connection on error
                await connection.reset()
                raise
    
    async def execute_query(self, query: str, *args) -> list:
        """Execute query with connection from pool"""
        async with self.get_connection() as conn:
            return await conn.fetch(query, *args)
    
    async def execute_transaction(self, queries: list) -> bool:
        """Execute multiple queries in a transaction"""
        async with self.get_connection() as conn:
            async with conn.transaction():
                for query, args in queries:
                    await conn.execute(query, *args)
                return True

# Response Compression
from gzip import compress
import json

class ResponseCompressor:
    @staticmethod
    def compress_json_response(data: Dict[str, Any]) -> bytes:
        """Compress JSON response with gzip"""
        json_str = json.dumps(data, separators=(',', ':'))
        return compress(json_str.encode('utf-8'))
    
    @staticmethod
    def should_compress(content_length: int, content_type: str) -> bool:
        """Determine if response should be compressed"""
        # Only compress text-based content over 1KB
        compressible_types = ['application/json', 'text/html', 'text/css', 'application/javascript']
        return content_length > 1024 and any(ct in content_type for ct in compressible_types)

# Async Processing with Background Tasks
import asyncio
from celery import Celery

# Celery for heavy background tasks
celery_app = Celery('performance_app', broker='redis://localhost:6379')

@celery_app.task
def process_large_dataset(dataset_id: str):
    """Process large dataset in background"""
    # Simulate heavy processing
    import pandas as pd
    import time
    
    # Load dataset
    df = pd.read_csv(f"datasets/{dataset_id}.csv")
    
    # Heavy processing
    processed_df = df.groupby('category').agg({
        'value': ['sum', 'mean', 'std'],
        'quantity': 'sum'
    })
    
    # Save results
    processed_df.to_csv(f"results/{dataset_id}_processed.csv")
    
    return f"Processed {len(df)} records"

# FastAPI with performance optimizations
from fastapi import FastAPI, BackgroundTasks, Depends
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

app = FastAPI(title="High Performance API")

# Add compression middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Security middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*.example.com", "localhost"])

# Dependency for database pool
async def get_db_pool() -> DatabasePool:
    return db_pool

@app.on_event("startup")
async def startup_event():
    global db_pool
    db_pool = DatabasePool("postgresql://user:pass@localhost/db")
    await db_pool.initialize()

@app.get("/users/{user_id}")
async def get_user(user_id: int, db: DatabasePool = Depends(get_db_pool)):
    """Optimized user endpoint with caching"""
    
    @cache_response(ttl=300)  # Cache for 5 minutes
    async def fetch_user_data(uid: int):
        query = """
        SELECT u.id, u.name, u.email, 
               COUNT(o.id) as order_count,
               SUM(o.total) as total_spent
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        WHERE u.id = $1
        GROUP BY u.id, u.name, u.email
        """
        
        result = await db.execute_query(query, uid)
        
        if result:
            return dict(result[0])
        return None
    
    user_data = await fetch_user_data(user_id)
    
    if not user_data:
        return {"error": "User not found"}
    
    return user_data

@app.post("/process-dataset")
async def process_dataset(dataset_id: str, background_tasks: BackgroundTasks):
    """Endpoint with background processing"""
    
    # Add task to background processing
    background_tasks.add_task(process_large_dataset.delay, dataset_id)
    
    return {"message": f"Processing started for dataset {dataset_id}"}
```

---

## 🗃️ Database Performance Tuning {#database}

### PostgreSQL Optimization

```sql
-- 1. Index Optimization
-- Efficient compound index
CREATE INDEX CONCURRENTLY idx_orders_customer_date 
ON orders(customer_id, order_date DESC) 
WHERE status = 'completed';

-- Partial index for common queries
CREATE INDEX CONCURRENTLY idx_active_users 
ON users(last_login_date) 
WHERE active = true;

-- Expression index for computed values
CREATE INDEX CONCURRENTLY idx_orders_total_rounded 
ON orders(ROUND(total_amount));

-- 2. Query Optimization
-- ❌ Slow - SELECT *
SELECT * FROM orders WHERE customer_id = 123;

-- ✅ Fast - Specific columns
SELECT id, total_amount, order_date 
FROM orders 
WHERE customer_id = 123
ORDER BY order_date DESC
LIMIT 10;

-- 3. Window Functions for Analytics
SELECT 
    customer_id,
    order_date,
    total_amount,
    -- Running total
    SUM(total_amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date 
        ROWS UNBOUNDED PRECEDING
    ) as running_total,
    -- Rank within customer
    ROW_NUMBER() OVER (
        PARTITION BY customer_id 
        ORDER BY total_amount DESC
    ) as amount_rank
FROM orders;

-- 4. Efficient Pagination
-- ❌ Slow - OFFSET for large datasets
SELECT * FROM products 
ORDER BY created_at DESC 
LIMIT 20 OFFSET 10000;

-- ✅ Fast - Cursor-based pagination
SELECT * FROM products 
WHERE created_at < '2024-01-15 10:00:00'
ORDER BY created_at DESC 
LIMIT 20;

-- 5. Bulk Operations
-- ❌ Slow - Individual inserts
INSERT INTO products (name, price) VALUES ('Product 1', 29.99);
INSERT INTO products (name, price) VALUES ('Product 2', 39.99);

-- ✅ Fast - Bulk insert
INSERT INTO products (name, price) 
VALUES 
    ('Product 1', 29.99),
    ('Product 2', 39.99),
    ('Product 3', 49.99);

-- Even faster - COPY from CSV
COPY products(name, price) 
FROM '/path/to/products.csv' 
WITH (FORMAT csv, HEADER true);
```

### Database Connection Optimization

```python
import asyncpg
import asyncio
from typing import Dict, Any, List
import logging
import time
from contextlib import asynccontextmanager

class OptimizedDatabaseManager:
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.pool = None
        self.query_cache = {}
        self.logger = logging.getLogger(__name__)
    
    async def initialize_pool(self):
        """Initialize optimized connection pool"""
        self.pool = await asyncpg.create_pool(
            self.dsn,
            min_size=10,
            max_size=50,
            max_queries=50000,  # Queries per connection
            max_inactive_connection_lifetime=3600,  # 1 hour
            command_timeout=30,
            server_settings={
                'application_name': 'optimized_app',
                'shared_preload_libraries': 'pg_stat_statements',
                'max_connections': '200',
                'shared_buffers': '256MB',
                'effective_cache_size': '1GB',
                'work_mem': '4MB',
                'maintenance_work_mem': '64MB'
            }
        )
        
        self.logger.info("Database pool initialized")
    
    @asynccontextmanager
    async def get_connection(self):
        """Get connection with automatic cleanup"""
        start_time = time.time()
        
        async with self.pool.acquire() as connection:
            try:
                yield connection
            finally:
                duration = time.time() - start_time
                if duration > 1.0:  # Log slow connections
                    self.logger.warning(f"Slow connection usage: {duration:.2f}s")
    
    async def execute_prepared_statement(self, query: str, *args) -> List[Dict[str, Any]]:
        """Execute prepared statement for better performance"""
        
        # Cache prepared statements
        if query not in self.query_cache:
            async with self.get_connection() as conn:
                stmt = await conn.prepare(query)
                self.query_cache[query] = stmt
                
                # Analyze query performance
                explain_query = f"EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) {query}"
                plan = await conn.fetchval(explain_query, *args)
                
                execution_time = plan[0]['Execution Time']
                if execution_time > 100:  # Log slow queries
                    self.logger.warning(f"Slow query detected: {execution_time:.2f}ms")
        
        async with self.get_connection() as conn:
            stmt = self.query_cache[query]
            return await stmt.fetch(*args)
    
    async def bulk_upsert(self, table: str, data: List[Dict[str, Any]], 
                         conflict_column: str) -> int:
        """Optimized bulk upsert operation"""
        if not data:
            return 0
        
        columns = list(data[0].keys())
        placeholders = ', '.join([f'${i+1}' for i in range(len(columns))])
        
        # Build upsert query
        query = f"""
        INSERT INTO {table} ({', '.join(columns)})
        VALUES ({placeholders})
        ON CONFLICT ({conflict_column})
        DO UPDATE SET {', '.join([f'{col} = EXCLUDED.{col}' for col in columns if col != conflict_column])}
        """
        
        async with self.get_connection() as conn:
            async with conn.transaction():
                # Use executemany for batch processing
                await conn.executemany(query, [tuple(row[col] for col in columns) for row in data])
        
        return len(data)

# Advanced Caching Strategies
class MultiLevelCache:
    def __init__(self):
        # L1: In-memory cache (fastest)
        self.l1_cache = {}
        self.l1_max_size = 1000
        
        # L2: Redis cache (fast, shared)
        self.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
        
        # L3: Database query cache
        self.query_cache = {}
    
    async def get(self, key: str) -> Any:
        """Multi-level cache get"""
        # Try L1 cache first
        if key in self.l1_cache:
            return self.l1_cache[key]
        
        # Try L2 cache (Redis)
        redis_value = self.redis_client.get(key)
        if redis_value:
            value = json.loads(redis_value)
            # Promote to L1 cache
            self._set_l1(key, value)
            return value
        
        return None
    
    async def set(self, key: str, value: Any, ttl: int = 3600):
        """Multi-level cache set"""
        # Set in L1
        self._set_l1(key, value)
        
        # Set in L2 (Redis)
        self.redis_client.setex(key, ttl, json.dumps(value))
    
    def _set_l1(self, key: str, value: Any):
        """Set value in L1 cache with LRU eviction"""
        if len(self.l1_cache) >= self.l1_max_size:
            # Remove oldest entry (simple FIFO, could improve with LRU)
            oldest_key = next(iter(self.l1_cache))
            del self.l1_cache[oldest_key]
        
        self.l1_cache[key] = value

# Async Request Processing
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

class AsyncRequestProcessor:
    def __init__(self, max_concurrent_requests: int = 100):
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            connector=aiohttp.TCPConnector(
                limit=100,  # Total connection limit
                limit_per_host=30,  # Per host limit
                keepalive_timeout=30
            )
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def make_concurrent_requests(self, urls: List[str]) -> List[Dict[str, Any]]:
        """Make multiple HTTP requests concurrently"""
        
        async def fetch_url(url: str) -> Dict[str, Any]:
            async with self.semaphore:  # Limit concurrency
                try:
                    async with self.session.get(url) as response:
                        return {
                            'url': url,
                            'status': response.status,
                            'data': await response.json(),
                            'headers': dict(response.headers)
                        }
                except Exception as e:
                    return {
                        'url': url,
                        'error': str(e),
                        'status': 0
                    }
        
        tasks = [fetch_url(url) for url in urls]
        return await asyncio.gather(*tasks)

# CPU-bound task optimization
class CPUOptimizer:
    def __init__(self, max_workers: int = None):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
    
    async def parallel_cpu_task(self, data_chunks: List[Any], process_func: callable) -> List[Any]:
        """Process CPU-intensive tasks in parallel"""
        loop = asyncio.get_event_loop()
        
        tasks = [
            loop.run_in_executor(self.executor, process_func, chunk)
            for chunk in data_chunks
        ]
        
        return await asyncio.gather(*tasks)
```

---

## 🗄️ Database Performance Tuning {#database}

### Advanced Query Optimization

```python
import asyncpg
import pandas as pd
from typing import List, Dict, Any, Optional
import numpy as np
from dataclasses import dataclass
import logging

@dataclass
class QueryPerformanceMetrics:
    query_text: str
    execution_time_ms: float
    rows_examined: int
    rows_returned: int
    buffer_usage_mb: float
    index_usage: bool
    suggestions: List[str]

class DatabasePerformanceTuner:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool
        self.logger = logging.getLogger(__name__)
        self.slow_query_threshold_ms = 100
    
    async def analyze_query_performance(self, query: str, *args) -> QueryPerformanceMetrics:
        """Analyze query performance with EXPLAIN"""
        
        async with self.pool.acquire() as conn:
            # Execute with analysis
            explain_query = f"EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) {query}"
            plan = await conn.fetchval(explain_query, *args)
            
            # Execute actual query for timing
            start_time = time.time()
            result = await conn.fetch(query, *args)
            execution_time = (time.time() - start_time) * 1000
            
            # Parse execution plan
            plan_data = plan[0]
            
            suggestions = []
            
            # Check for sequential scans
            if 'Seq Scan' in str(plan_data):
                suggestions.append("Consider adding an index - sequential scan detected")
            
            # Check for large sort operations
            if plan_data.get('Sort', {}).get('Sort Method') == 'external merge':
                suggestions.append("Increase work_mem - external sort detected")
            
            # Check buffer usage
            buffer_usage = plan_data.get('Shared Hit Blocks', 0) + plan_data.get('Shared Read Blocks', 0)
            buffer_usage_mb = buffer_usage * 8 / 1024  # 8KB per block
            
            if buffer_usage_mb > 100:
                suggestions.append("High buffer usage - consider query optimization")
            
            return QueryPerformanceMetrics(
                query_text=query,
                execution_time_ms=execution_time,
                rows_examined=plan_data.get('Actual Rows', 0),
                rows_returned=len(result),
                buffer_usage_mb=buffer_usage_mb,
                index_usage='Index' in str(plan_data),
                suggestions=suggestions
            )
    
    async def optimize_table_statistics(self, table_name: str):
        """Update table statistics for better query planning"""
        async with self.pool.acquire() as conn:
            await conn.execute(f"ANALYZE {table_name}")
            self.logger.info(f"Updated statistics for table: {table_name}")
    
    async def create_missing_indexes(self, table_name: str):
        """Suggest and create missing indexes based on query patterns"""
        
        # Find most common WHERE clauses
        query = """
        SELECT query, calls, mean_exec_time
        FROM pg_stat_statements 
        WHERE query LIKE '%' || $1 || '%'
        ORDER BY calls DESC
        LIMIT 10
        """
        
        async with self.pool.acquire() as conn:
            common_queries = await conn.fetch(query, table_name)
            
            for row in common_queries:
                query_text = row['query']
                
                # Simple heuristic for index suggestions
                if 'WHERE' in query_text.upper():
                    # Extract WHERE conditions (simplified)
                    where_part = query_text.upper().split('WHERE')[1].split('ORDER BY')[0]
                    
                    if 'AND' in where_part:
                        self.logger.info(f"Consider compound index for: {where_part.strip()}")
                    else:
                        self.logger.info(f"Consider single column index for: {where_part.strip()}")

# MongoDB Performance Optimization
import pymongo
from pymongo import MongoClient
import time

class MongoPerformanceTuner:
    def __init__(self, connection_string: str):
        self.client = MongoClient(
            connection_string,
            maxPoolSize=50,
            minPoolSize=10,
            maxIdleTimeMS=30000,
            waitQueueMultiple=10
        )
        self.db = self.client.get_default_database()
    
    def create_optimal_indexes(self, collection_name: str, query_patterns: List[Dict[str, Any]]):
        """Create indexes based on query patterns"""
        collection = self.db[collection_name]
        
        for pattern in query_patterns:
            query_fields = list(pattern.keys())
            sort_fields = pattern.get('sort', {})
            
            # Create compound index
            index_spec = []
            
            # Add query fields first
            for field in query_fields:
                if field != 'sort':
                    index_spec.append((field, 1))
            
            # Add sort fields
            for field, direction in sort_fields.items():
                if (field, direction) not in index_spec:
                    index_spec.append((field, direction))
            
            # Create index
            try:
                index_name = collection.create_index(
                    index_spec, 
                    background=True,
                    name=f"idx_{'_'.join(f[0] for f in index_spec)}"
                )
                print(f"Created index: {index_name}")
            except Exception as e:
                print(f"Index creation failed: {e}")
    
    def optimize_aggregation_pipeline(self, collection_name: str, pipeline: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Optimize aggregation pipeline"""
        optimized_pipeline = []
        
        # Move $match stages to beginning
        match_stages = [stage for stage in pipeline if '$match' in stage]
        other_stages = [stage for stage in pipeline if '$match' not in stage]
        
        # Add match stages first for better performance
        optimized_pipeline.extend(match_stages)
        
        # Add $project early if possible to reduce data size
        project_stages = [stage for stage in other_stages if '$project' in stage]
        if project_stages:
            optimized_pipeline.append(project_stages[0])
            other_stages = [stage for stage in other_stages if '$project' not in stage]
        
        # Add remaining stages
        optimized_pipeline.extend(other_stages)
        
        return optimized_pipeline
    
    def analyze_slow_operations(self, threshold_ms: int = 100):
        """Analyze slow operations using profiler"""
        # Enable profiler
        self.db.set_profiling_level(2, slow_ms=threshold_ms)
        
        # Get slow operations
        slow_ops = list(self.db.system.profile.find().sort('ts', -1).limit(50))
        
        for op in slow_ops:
            duration = op.get('durationMillis', 0)
            command = op.get('command', {})
            
            print(f"Slow operation: {duration}ms")
            print(f"Command: {command}")
            print(f"Collection: {op.get('ns', 'unknown')}")
            print("---")
```

---

## 💾 Caching Strategies {#caching}

### Redis Caching Patterns

```python
import redis
import json
import pickle
import hashlib
import time
import asyncio
from typing import Any, Optional, Union, List, Dict
from functools import wraps
from datetime import datetime, timedelta

class RedisCacheManager:
    def __init__(self, host='localhost', port=6379, db=0, max_connections=50):
        self.redis_pool = redis.ConnectionPool(
            host=host, 
            port=port, 
            db=db,
            max_connections=max_connections,
            decode_responses=False  # Handle binary data
        )
        self.redis_client = redis.Redis(connection_pool=self.redis_pool)
    
    # 1. Simple Key-Value Caching
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache"""
        try:
            value = self.redis_client.get(key)
            if value:
                return pickle.loads(value)
            return None
        except Exception as e:
            print(f"Cache get error: {e}")
            return None
    
    async def set(self, key: str, value: Any, ttl: int = 3600):
        """Set value in cache with TTL"""
        try:
            serialized = pickle.dumps(value)
            self.redis_client.setex(key, ttl, serialized)
        except Exception as e:
            print(f"Cache set error: {e}")
    
    # 2. Cache-aside Pattern
    async def cache_aside(self, key: str, fetch_func: callable, ttl: int = 3600) -> Any:
        """Implement cache-aside pattern"""
        # Try cache first
        cached_value = await self.get(key)
        if cached_value is not None:
            return cached_value
        
        # Fetch from source
        value = await fetch_func()
        
        # Store in cache
        await self.set(key, value, ttl)
        
        return value
    
    # 3. Write-through Cache
    async def write_through(self, key: str, value: Any, update_func: callable, ttl: int = 3600):
        """Write-through cache pattern"""
        # Update source first
        await update_func(value)
        
        # Then update cache
        await self.set(key, value, ttl)
    
    # 4. Write-behind (Write-back) Cache
    class WriteBehindCache:
        def __init__(self, cache_manager, flush_interval: int = 60):
            self.cache_manager = cache_manager
            self.dirty_keys = set()
            self.flush_interval = flush_interval
            self.pending_writes = {}
            self._start_flush_worker()
        
        async def set(self, key: str, value: Any):
            """Set value and mark as dirty"""
            await self.cache_manager.set(key, value)
            self.dirty_keys.add(key)
            self.pending_writes[key] = value
        
        def _start_flush_worker(self):
            """Start background worker to flush dirty data"""
            async def flush_worker():
                while True:
                    if self.dirty_keys:
                        await self._flush_dirty_keys()
                    await asyncio.sleep(self.flush_interval)
            
            asyncio.create_task(flush_worker())
        
        async def _flush_dirty_keys(self):
            """Flush dirty keys to persistent storage"""
            keys_to_flush = list(self.dirty_keys)
            self.dirty_keys.clear()
            
            # Batch write to database
            batch_data = [(key, self.pending_writes[key]) for key in keys_to_flush]
            
            try:
                await self._batch_write_to_db(batch_data)
                
                # Remove from pending writes
                for key in keys_to_flush:
                    self.pending_writes.pop(key, None)
                    
            except Exception as e:
                # On failure, mark as dirty again
                self.dirty_keys.update(keys_to_flush)
                print(f"Write-behind flush failed: {e}")
    
    # 5. Distributed Cache with Consistent Hashing
    class DistributedCache:
        def __init__(self, nodes: List[str]):
            self.nodes = [redis.Redis.from_url(node) for node in nodes]
            self.ring = self._build_hash_ring()
        
        def _build_hash_ring(self):
            """Build consistent hash ring"""
            ring = {}
            for i, node in enumerate(self.nodes):
                for j in range(160):  # Virtual nodes for better distribution
                    key = hashlib.md5(f"{i}:{j}".encode()).hexdigest()
                    ring[key] = node
            return dict(sorted(ring.items()))
        
        def _get_node(self, key: str) -> redis.Redis:
            """Get node for key using consistent hashing"""
            if not self.ring:
                return self.nodes[0]
            
            key_hash = hashlib.md5(key.encode()).hexdigest()
            
            for ring_key in self.ring:
                if key_hash <= ring_key:
                    return self.ring[ring_key]
            
            # Wrap around to first node
            return list(self.ring.values())[0]
        
        async def get(self, key: str) -> Optional[Any]:
            """Get from distributed cache"""
            node = self._get_node(key)
            try:
                value = node.get(key)
                if value:
                    return pickle.loads(value)
            except:
                pass
            return None
        
        async def set(self, key: str, value: Any, ttl: int = 3600):
            """Set in distributed cache"""
            node = self._get_node(key)
            try:
                serialized = pickle.dumps(value)
                node.setex(key, ttl, serialized)
            except Exception as e:
                print(f"Distributed cache set error: {e}")

# Application-level caching decorator
def cached(ttl: int = 3600, key_prefix: str = ""):
    """Decorator for caching function results"""
    def decorator(func):
        cache_manager = RedisCacheManager()
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate cache key
            key_data = f"{key_prefix}:{func.__name__}:{str(args)}:{str(sorted(kwargs.items()))}"
            cache_key = hashlib.md5(key_data.encode()).hexdigest()
            
            # Try cache first
            cached_result = await cache_manager.get(cache_key)
            if cached_result is not None:
                return cached_result
            
            # Execute function
            result = await func(*args, **kwargs)
            
            # Cache result
            await cache_manager.set(cache_key, result, ttl)
            
            return result
        
        return wrapper
    return decorator

# Usage examples
@cached(ttl=1800, key_prefix="user_data")
async def get_user_profile(user_id: int) -> Dict[str, Any]:
    """Get user profile with caching"""
    # Simulate database query
    await asyncio.sleep(0.1)
    return {
        "user_id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }
```

---

## 🔄 Load Testing & Performance Monitoring {#testing}

### Comprehensive Load Testing

```python
import asyncio
import aiohttp
import time
import statistics
from typing import Dict, List, Any
import json
import matplotlib.pyplot as plt
from dataclasses import dataclass, asdict

@dataclass
class LoadTestMetrics:
    total_requests: int
    successful_requests: int
    failed_requests: int
    avg_response_time_ms: float
    p50_response_time_ms: float
    p95_response_time_ms: float
    p99_response_time_ms: float
    max_response_time_ms: float
    min_response_time_ms: float
    requests_per_second: float
    error_rate_percent: float
    test_duration_seconds: float

class LoadTester:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.results = []
        
    async def run_load_test(self, 
                           endpoint: str,
                           concurrent_users: int = 10,
                           duration_seconds: int = 60,
                           ramp_up_seconds: int = 10) -> LoadTestMetrics:
        """Run comprehensive load test"""
        
        print(f"Starting load test: {concurrent_users} users for {duration_seconds}s")
        
        # Create semaphore for concurrency control
        semaphore = asyncio.Semaphore(concurrent_users)
        
        # Track metrics
        response_times = []
        error_count = 0
        success_count = 0
        
        start_time = time.time()
        end_time = start_time + duration_seconds
        
        async def make_request(session):
            """Make single request"""
            async with semaphore:
                request_start = time.time()
                try:
                    async with session.get(f"{self.base_url}{endpoint}") as response:
                        await response.text()  # Consume response body
                        
                        request_time = (time.time() - request_start) * 1000
                        response_times.append(request_time)
                        
                        if response.status == 200:
                            return 'success'
                        else:
                            return 'error'
                except:
                    return 'error'
        
        # Create session with optimized settings
        timeout = aiohttp.ClientTimeout(total=30)
        connector = aiohttp.TCPConnector(
            limit=concurrent_users + 10,
            keepalive_timeout=30,
            enable_cleanup_closed=True
        )
        
        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            tasks = []
            
            # Ramp up users gradually
            users_added = 0
            ramp_interval = ramp_up_seconds / concurrent_users
            
            while time.time() < end_time:
                # Add users during ramp-up period
                if users_added < concurrent_users and len(tasks) < concurrent_users:
                    task = asyncio.create_task(make_request(session))
                    tasks.append(task)
                    users_added += 1
                    
                    if users_added < concurrent_users:
                        await asyncio.sleep(ramp_interval)
                
                # Wait for some requests to complete
                if len(tasks) >= concurrent_users:
                    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                    
                    # Process completed requests
                    for task in done:
                        result = await task
                        if result == 'success':
                            success_count += 1
                        else:
                            error_count += 1
                        
                        tasks.remove(task)
                    
                    # Add new request to maintain load
                    if time.time() < end_time:
                        new_task = asyncio.create_task(make_request(session))
                        tasks.append(new_task)
            
            # Wait for remaining tasks
            if tasks:
                results = await asyncio.gather(*tasks, return_exceptions=True)
                for result in results:
                    if result == 'success':
                        success_count += 1
                    else:
                        error_count += 1
        
        # Calculate metrics
        total_requests = success_count + error_count
        test_duration = time.time() - start_time
        
        if response_times:
            response_times.sort()
            metrics = LoadTestMetrics(
                total_requests=total_requests,
                successful_requests=success_count,
                failed_requests=error_count,
                avg_response_time_ms=statistics.mean(response_times),
                p50_response_time_ms=response_times[len(response_times) // 2],
                p95_response_time_ms=response_times[int(len(response_times) * 0.95)],
                p99_response_time_ms=response_times[int(len(response_times) * 0.99)],
                max_response_time_ms=max(response_times),
                min_response_time_ms=min(response_times),
                requests_per_second=total_requests / test_duration,
                error_rate_percent=(error_count / total_requests * 100) if total_requests > 0 else 0,
                test_duration_seconds=test_duration
            )
        else:
            metrics = LoadTestMetrics(
                total_requests=0, successful_requests=0, failed_requests=0,
                avg_response_time_ms=0, p50_response_time_ms=0, p95_response_time_ms=0,
                p99_response_time_ms=0, max_response_time_ms=0, min_response_time_ms=0,
                requests_per_second=0, error_rate_percent=100, test_duration_seconds=test_duration
            )
        
        return metrics
    
    def generate_report(self, metrics: LoadTestMetrics):
        """Generate load test report"""
        print("\n" + "="*50)
        print("LOAD TEST RESULTS")
        print("="*50)
        print(f"Total Requests: {metrics.total_requests}")
        print(f"Successful: {metrics.successful_requests}")
        print(f"Failed: {metrics.failed_requests}")
        print(f"Success Rate: {100 - metrics.error_rate_percent:.2f}%")
        print(f"Requests/Second: {metrics.requests_per_second:.2f}")
        print(f"")
        print("Response Times:")
        print(f"  Average: {metrics.avg_response_time_ms:.2f}ms")
        print(f"  50th percentile: {metrics.p50_response_time_ms:.2f}ms")
        print(f"  95th percentile: {metrics.p95_response_time_ms:.2f}ms")
        print(f"  99th percentile: {metrics.p99_response_time_ms:.2f}ms")
        print(f"  Min: {metrics.min_response_time_ms:.2f}ms")
        print(f"  Max: {metrics.max_response_time_ms:.2f}ms")
        print(f"")
        print(f"Test Duration: {metrics.test_duration_seconds:.2f}s")
        print("="*50)

# Usage
async def run_performance_tests():
    tester = LoadTester("http://localhost:3000")
    
    # Test different endpoints
    endpoints = [
        "/api/users",
        "/api/products", 
        "/api/orders"
    ]
    
    for endpoint in endpoints:
        print(f"\nTesting {endpoint}...")
        metrics = await tester.run_load_test(
            endpoint=endpoint,
            concurrent_users=50,
            duration_seconds=30
        )
        
        tester.generate_report(metrics)

if __name__ == "__main__":
    asyncio.run(run_performance_tests())
```

---

## 🏆 Real-World Case Studies {#case-studies}

### Case Study: E-commerce Performance Optimization

**Problem**: E-commerce site loading in 8+ seconds, 60% bounce rate

**Solution Implementation**:

```python
# 1. Database Query Optimization
class EcommerceOptimizer:
    async def optimize_product_queries(self):
        """Optimize product listing queries"""
        
        # Before: N+1 query problem
        # products = await get_products()
        # for product in products:
        #     product.reviews = await get_product_reviews(product.id)
        
        # After: Single optimized query with JOIN
        query = """
        SELECT 
            p.id, p.name, p.price, p.image_url,
            COALESCE(r.avg_rating, 0) as avg_rating,
            COALESCE(r.review_count, 0) as review_count
        FROM products p
        LEFT JOIN (
            SELECT 
                product_id,
                AVG(rating) as avg_rating,
                COUNT(*) as review_count
            FROM reviews 
            GROUP BY product_id
        ) r ON p.id = r.product_id
        WHERE p.active = true
        ORDER BY p.featured DESC, p.name
        LIMIT $1 OFFSET $2
        """
        
        # Result: Query time reduced from 2.5s to 45ms
        
    async def implement_search_optimization(self):
        """Implement Elasticsearch for product search"""
        
        from elasticsearch import AsyncElasticsearch
        
        es_client = AsyncElasticsearch(['http://localhost:9200'])
        
        # Optimized search with filters and aggregations
        search_body = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"name": "laptop"}},
                        {"range": {"price": {"gte": 500, "lte": 2000}}}
                    ],
                    "filter": [
                        {"term": {"active": True}},
                        {"terms": {"category": ["electronics", "computers"]}}
                    ]
                }
            },
            "aggs": {
                "price_ranges": {
                    "range": {
                        "field": "price",
                        "ranges": [
                            {"to": 500},
                            {"from": 500, "to": 1000},
                            {"from": 1000, "to": 2000},
                            {"from": 2000}
                        ]
                    }
                },
                "brands": {
                    "terms": {"field": "brand", "size": 10}
                }
            },
            "size": 20,
            "from": 0
        }
        
        response = await es_client.search(index="products", body=search_body)
        
        # Result: Search time reduced from 3.2s to 120ms
        return response
```

**Results**:
- ⚡ Page load time: 8s → 1.2s (85% improvement)
- 📈 Conversion rate: 2.1% → 4.8% (130% increase)  
- 👥 Bounce rate: 60% → 25% (58% reduction)
- 🚀 Revenue increase: 180% over 6 months

### Case Study: API Performance at Scale

**Problem**: API serving 10k requests/min with 500ms average response time

**Solution**:

```python
# Before: Synchronous processing
def slow_api_endpoint(request):
    user = database.query(f"SELECT * FROM users WHERE id = {request.user_id}")
    orders = database.query(f"SELECT * FROM orders WHERE user_id = {user.id}")
    recommendations = ml_service.get_recommendations(user.id)  # 300ms external call
    
    return {
        "user": user,
        "recent_orders": orders[-5:],
        "recommendations": recommendations
    }

# After: Async + caching + optimization
class OptimizedAPI:
    def __init__(self):
        self.cache = RedisCacheManager()
        self.db_pool = DatabasePool("postgresql://...")
    
    @cached(ttl=300)  # 5 minute cache
    async def get_user_recommendations(self, user_id: int):
        """Cached recommendation service call"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://ml-service/recommendations/{user_id}") as resp:
                return await resp.json()
    
    async def optimized_api_endpoint(self, request):
        """Optimized endpoint with parallel processing"""
        
        # Execute queries in parallel
        user_task = self.get_user_data(request.user_id)
        orders_task = self.get_recent_orders(request.user_id)
        recommendations_task = self.get_user_recommendations(request.user_id)
        
        # Wait for all to complete
        user, orders, recommendations = await asyncio.gather(
            user_task, orders_task, recommendations_task
        )
        
        return {
            "user": user,
            "recent_orders": orders,
            "recommendations": recommendations
        }

# Results:
# - Response time: 500ms → 85ms (83% improvement)
# - Throughput: 10k req/min → 45k req/min (350% increase)
# - CPU usage: 80% → 35% (56% reduction)
```

---

## ✅ Performance Best Practices Summary {#best-practices}

### Frontend Checklist
- ✅ Implement lazy loading for images and components
- ✅ Use modern image formats (WebP, AVIF)
- ✅ Enable compression (Gzip/Brotli)
- ✅ Minimize and bundle JavaScript/CSS
- ✅ Implement service worker for caching
- ✅ Use CDN for static assets
- ✅ Optimize critical rendering path
- ✅ Implement virtual scrolling for large lists

### Backend Checklist  
- ✅ Use connection pooling for databases
- ✅ Implement response caching (Redis)
- ✅ Use async processing for I/O operations
- ✅ Background processing for heavy tasks
- ✅ API rate limiting and throttling
- ✅ Database query optimization
- ✅ Horizontal scaling with load balancers
- ✅ Monitor and profile regularly

### Database Checklist
- ✅ Create proper indexes on query columns
- ✅ Use EXPLAIN to analyze query performance  
- ✅ Implement read replicas for scaling reads
- ✅ Partition large tables by date/range
- ✅ Regular VACUUM and ANALYZE (PostgreSQL)
- ✅ Optimize memory settings (shared_buffers, work_mem)
- ✅ Use materialized views for complex aggregations
- ✅ Monitor slow query logs

### Infrastructure Checklist
- ✅ Use CDN for global content delivery
- ✅ Implement auto-scaling groups
- ✅ Monitor resource utilization
- ✅ Use SSD storage for databases
- ✅ Optimize network configuration
- ✅ Implement health checks and alerting
- ✅ Use containerization for consistent environments
- ✅ Regular performance testing in CI/CD

---

## 🎯 Performance Optimization Roadmap

### Beginner (0-6 months)
1. **Learn Fundamentals**: Understand performance concepts and metrics
2. **Master Profiling Tools**: Chrome DevTools, browser performance tabs
3. **Basic Optimizations**: Image compression, minification, caching
4. **Database Basics**: Learn SQL optimization and indexing
5. **Monitoring Setup**: Implement basic performance monitoring

### Intermediate (6-18 months)
1. **Advanced Frontend**: Code splitting, lazy loading, service workers
2. **Backend Optimization**: Connection pooling, async processing
3. **Caching Strategies**: Redis, CDN, application-level caching
4. **Load Testing**: Implement comprehensive load testing
5. **Database Tuning**: Advanced query optimization, partitioning

### Advanced (18+ months)
1. **Infrastructure Scaling**: Auto-scaling, load balancing, CDNs
2. **Microservices Performance**: Distributed system optimization
3. **Real-time Systems**: WebSocket optimization, event streaming
4. **Security vs Performance**: Balance security and performance
5. **Enterprise Systems**: Large-scale performance architecture

---

## 🚀 Conclusion

Performance optimization is a continuous journey that directly impacts user experience and business success. With the techniques in this guide, you can:

- ✅ Build lightning-fast user interfaces
- ✅ Scale backend systems to handle millions of requests
- ✅ Optimize databases for complex queries
- ✅ Implement effective caching strategies
- ✅ Monitor and maintain performance in production

Remember: **Measure first, optimize second, validate third!**

Keep optimizing and building amazing high-performance systems! ⚡🚀
"""
Demo Project 19: Async Web Scraper
Part 4: Advanced Topics - Hour 34
Difficulty: ⭐⭐⭐⭐ Expert

Features:
- Asynchronous web scraping
- asyncio and aiohttp
- Concurrent processing
- Performance optimization
"""

# Note: This requires aiohttp and beautifulsoup4
# pip install aiohttp beautifulsoup4

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from datetime import datetime
import time

class AsyncWebScraper:
    """Asynchronous web scraper"""
    
    def __init__(self):
        self.results = []
    
    async def fetch_url(self, session, url):
        """Fetch a single URL"""
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    html = await response.text()
                    return {
                        'url': url,
                        'status': 'success',
                        'content_length': len(html),
                        'title': self.extract_title(html)
                    }
                else:
                    return {
                        'url': url,
                        'status': f'error_{response.status}',
                        'content_length': 0
                    }
        except Exception as e:
            return {
                'url': url,
                'status': 'error',
                'error': str(e)
            }
    
    def extract_title(self, html):
        """Extract title from HTML"""
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title_tag = soup.find('title')
            return title_tag.text.strip() if title_tag else 'No title'
        except:
            return 'Error parsing'
    
    async def scrape_urls(self, urls):
        """Scrape multiple URLs concurrently"""
        start_time = time.time()
        
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
        
        elapsed_time = time.time() - start_time
        
        return {
            'results': results,
            'total_urls': len(urls),
            'elapsed_time': elapsed_time,
            'avg_time_per_url': elapsed_time / len(urls) if urls else 0
        }
    
    def print_results(self, data):
        """Print scraping results"""
        print("\n" + "="*60)
        print("WEB SCRAPING RESULTS")
        print("="*60)
        print(f"Total URLs: {data['total_urls']}")
        print(f"Total Time: {data['elapsed_time']:.2f} seconds")
        print(f"Average Time per URL: {data['avg_time_per_url']:.2f} seconds")
        print("\nResults:")
        print("-"*60)
        
        for result in data['results']:
            status = "✅" if result['status'] == 'success' else "❌"
            print(f"{status} {result['url']}")
            if result['status'] == 'success':
                print(f"   Title: {result.get('title', 'N/A')}")
                print(f"   Content Length: {result['content_length']} bytes")


async def main():
    """Demo async web scraper"""
    try:
        scraper = AsyncWebScraper()
        
        # Example URLs (replace with real URLs for actual scraping)
        urls = [
            'https://www.python.org',
            'https://www.github.com',
            'https://www.stackoverflow.com',
            'https://www.reddit.com',
            'https://www.wikipedia.org'
        ]
        
        print("🕷️ Starting async web scraping...")
        print(f"Scraping {len(urls)} URLs concurrently...\n")
        
        results = await scraper.scrape_urls(urls)
        scraper.print_results(results)
        
        print("\n💡 Note: This demo uses example URLs.")
        print("   Replace with actual URLs for real web scraping.")
        print("   Always respect robots.txt and website terms of service!")
        
    except ImportError:
        print("❌ Required packages not installed!")
        print("Install with: pip install aiohttp beautifulsoup4")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nNote: Web scraping requires internet connection.")
        print("Some URLs may be blocked or require authentication.")


if __name__ == "__main__":
    # Run async main function
    asyncio.run(main())



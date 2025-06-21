#!/usr/bin/env python
"""Generate sws_context.txt scraping SitoWebSicuro via Crawl4AI.
Run: python generate_context.py
Requires: pip install crawl4ai
"""
import asyncio
from crawl4ai import AsyncWebCrawler
import pathlib

URLS = [
    "https://www.sitowebsicuro.com/it/",
    "https://www.sitowebsicuro.com/it/security-checker",
    "https://www.sitowebsicuro.com/it/password-checker",
    "https://www.sitowebsicuro.com/it/wordpress-scanner",
    "https://www.sitowebsicuro.com/it/verifica-messaggi-truffa",
    "https://www.sitowebsicuro.com/it/gdpr-checker",
    "https://www.sitowebsicuro.com/it/accessibilita-checker",
    "https://www.sitowebsicuro.com/it/privacy-scanner",
    "https://www.sitowebsicuro.com/it/cookie-scanner",
    "https://www.sitowebsicuro.com/it/hosting-sicuro",
    "https://www.sitowebsicuro.com/it/dominio-sicuro",
    "https://www.sitowebsicuro.com/it/email-sicura",
    "https://www.sitowebsicuro.com/it/prezzi",
    "https://www.sitowebsicuro.com/it/blog",
    "https://www.sitowebsicuro.com/it/contattaci",
    "https://www.sitowebsicuro.com/it/calcola-preventivo",
    "https://www.sitowebsicuro.com/it/privacy-policy",
    "https://www.sitowebsicuro.com/it/cookie-policy",
]

OUTPUT_DIR = pathlib.Path(__file__).parent / "context"
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "sws_context.txt"

print("[Crawl4AI] Crawling", URLS)

async def main():
    async with AsyncWebCrawler(max_concurrent_tasks=4) as crawler:
        results = await crawler.arun_many(urls=URLS)
        parts = []
        for r in results:
            if r.success:
                parts.append(r.markdown.fit_markdown or r.markdown.raw_markdown or "")
            else:
                print("[warn] crawl failed", r.url)
        OUTPUT_FILE.write_text("\n\n".join(parts), encoding="utf-8")

asyncio.run(main())
print("Context salvato in", OUTPUT_FILE) 
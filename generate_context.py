#!/usr/bin/env python
"""Generate sws_context.txt scraping SitoWebSicuro via Crawl4AI.
Run: python generate_context.py
Requires: pip install crawl4ai
"""
import asyncio
from crawl4ai import AsyncWebCrawler
import pathlib

SITE_URL = "https://www.sitowebsicuro.com/it/"
OUTPUT_DIR = pathlib.Path(__file__).parent / "context"
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "sws_context.txt"

print("[Crawl4AI] Crawling", SITE_URL)

async def run():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=SITE_URL)
        if not result.success:
            print("Crawl failed:", result.error_message)
            raise SystemExit(1)
        text = result.markdown.fit_markdown or result.markdown.raw_markdown or ""
        OUTPUT_FILE.write_text(text, encoding="utf-8")

asyncio.run(run())
print("Context salvato in", OUTPUT_FILE) 
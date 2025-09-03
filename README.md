Graduate Programs Scraper

This project scrapes graduate program information from Midwestern State University’s Graduate School website
.

It uses asynchronous requests (aiohttp + asyncio) to fetch program pages concurrently, then parses program details (headings + content) with BeautifulSoup.

Features

Extracts all graduate program links from the main degree listing page.

Asynchronously fetches each program’s detail page for faster scraping.

Parses and organizes program content into a structured dictionary.

Handles errors gracefully (e.g., missing content or network issues).

Displays execution time for benchmarking performance.

Tech Stack

Python 3.8+

aiohttp → asynchronous HTTP requests

asyncio → concurrent task execution

requests → initial HTML fetch

BeautifulSoup (bs4) → HTML parsing
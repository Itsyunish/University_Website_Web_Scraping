# 🎓 Graduate Programs Scraper

This project scrapes graduate program information from Midwestern State University’s Graduate School
.

It uses asynchronous requests (aiohttp + asyncio) to fetch program pages concurrently, and BeautifulSoup to parse program details into a clean structure.

# ✨ Features

🔗 Extracts all graduate program links from the main degree listing page

⚡ Asynchronously fetches program detail pages for faster scraping

📝 Parses headings + content from accordion sections

🛡️ Handles errors gracefully (network failures, missing content, etc.)

⏱️ Displays total execution time

# 🛠️ Tech Stack

Python 3.8+

aiohttp
 → asynchronous HTTP requests

asyncio
 → task concurrency

requests
 → initial HTML fetch

BeautifulSoup (bs4)
 → HTML parsing

# 📦 Installation

Clone the repository and install dependencies:
git clone https://github.com/Itsyunish/University_Website_Web_Scraping.git
cd University_Website_Web_Scraping
uv sync


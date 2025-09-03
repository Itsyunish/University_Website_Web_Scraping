import aiohttp
import requests
import asyncio
from bs4 import BeautifulSoup
import time


async def fetch_and_parse(session, url):
    """Fetch a URL and parse it with Beautiful Soup"""
    try:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            data = {}
            accordion_items = soup.find_all('div', class_="accordion-item")

            for item in accordion_items:
                heading_tag = item.find('h2', class_="panel-heading")
                heading = heading_tag.get_text(strip=True) if heading_tag else "No Heading"

                content_tag = item.find('div', class_="accordion-content")
                if content_tag:
                    for br in content_tag.find_all("br"):
                        br.replace_with("\n")
                    content = content_tag.get_text(" ", strip=True)
                else:
                    content = "No Content"

                data[heading] = content

            return {'url': url, 'data': data}

    except Exception as e:
        return {'url': url, 'error': str(e)}


def extract_links(html: str):
    """Extract all graduate program links"""
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all('div', class_="uk-width-medium-1-1")
    base_url = "https://msutexas.edu/academics/graduate-school/"

    links = []
    for div in divs:
        for tag in div.find_all('a', href=True):
            href = base_url + tag['href']
            links.append(href)

    print("Number of links:", len(links))
    return links


async def main():
    # Fetch the initial page and extract program links
    webpage = requests.get("https://msutexas.edu/academics/graduate-school/graduate-degrees.php")
    link_result = extract_links(webpage.text)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_parse(session, url) for url in link_result]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(f"URL: {result['url']}")
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                for heading, content in result['data'].items():
                    print(f"{heading}:\n{content}\n")
            print("-" * 50)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print("Execution time:", end - start, "seconds")

import requests
from bs4 import BeautifulSoup
def find_apple_us_subsidiaries(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    session = requests.Session()
    session.headers.update(headers)
    try:
        response = session.get(link)
        if response.status_code != 200:
            return f"Failed to retrieve the webpage, Status code: {response.status_code}"
        soup = BeautifulSoup(response.content, 'html.parser')
        font_elements = soup.find_all('font')
        us_subsidiaries = []
        for i in range(0, len(font_elements) - 1, 2):
            name = font_elements[i].get_text(strip=True)
            location = font_elements[i + 1].get_text(strip=True)

            if "U.S." in location or "United States" in location or "Delaware" in location or "Arizona" in location or "Nevada" in location:
                us_subsidiaries.append((name, location))

        return us_subsidiaries

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
link = 'https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/a10-kexhibit2119252021.htm'
us_apple_subsidiaries = find_apple_us_subsidiaries(link)
for subsidiary, location in us_apple_subsidiaries:
    print(f"Subsidiary: {subsidiary}, Location: {location}")

import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url):
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return ' '.join(p.text.strip() for p in soup.find_all("p") if p.text.strip())
    except Exception:
        return ""
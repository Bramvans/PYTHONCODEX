def scrape(url):
    """Scrape URLs to generate previews."""
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    r = requests.get(url, headers)
    raw_html = r.content
    soup = BeautifulSoup(raw_html, 'html.parser')
    print(soup.prettify())
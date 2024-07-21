from selectorlib import Extractor
import requests

class Temperature:

    # Scraper

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url

    def scrape(self):
        url = self.build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        content = r.text
        raw_content = extractor.extract(content)
        return raw_content

    def get(self):
        # Cleans the output of scrape
        scraped_content = self.scrape()
        return float(scraped_content['temp'].replace("°F", "").strip())


if __name__ == "__main__":
    temperature = Temperature(country="us", city="santa-barbara")
    print(temperature.get())


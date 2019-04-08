import requests
from bs4 import BeautifulSoup


class WebScrapper:

    def __init__(self, url):

        webpage = requests.get(url)
        self.soup = BeautifulSoup(webpage.text, 'html.parser')


    def getPrice(self):

        return self.soup.find_all(atrrs={'class': 'price'})


page = 'https://www.ceneo.pl/;szukaj-geforce+rtx+2070'

ws = WebScrapper(page)
print(ws.getPrice())

import requests
from bs4 import BeautifulSoup


class WebScrapper:

    def __init__(self, url):

        webpage = requests.get(url)
        self.soup = BeautifulSoup(webpage.text, 'html.parser')

    def getPrice(self):

        divs = self.soup.find_all("div", {"class": "cat-prod-row-content"})
        gpuDivs = self.soup.find_all('a', {"class": "js_seoUrl js_clickHash go-to-product"})

        return gpuDivs

    def saveHtml(self):

        with open("html.txt", 'w') as htmlfile:
            htmlfile.write(self.soup.text)


page = 'https://www.ceneo.pl/;szukaj-geforce+rtx+2070+oc'

ws = WebScrapper(page)
# ws.saveHtml()
print(ws.getPrice())


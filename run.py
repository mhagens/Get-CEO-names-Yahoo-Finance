from bs4 import BeautifulSoup
import requests


url = 'https://finance.yahoo.com/quote/GTVI/profile?p=GTVI'
page = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
})
soup = BeautifulSoup(page.text, 'html.parser')
price = soup.find_all("tr", {"class": "C($primaryColor) BdB Bdc($seperatorColor) H(36px)"})


print(soup.select_one("td > span").text)


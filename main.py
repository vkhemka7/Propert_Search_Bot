import requests
from bs4 import BeautifulSoup
from form import Form

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSd4WguC3foHn-mG7bnsKmi9dJaOAPfoHBiLpcub5R5B6N_4iQ/viewform?usp=sf_link"
chrome_driver_path = "C:\Development\chromedriver.exe"

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "accept-language":"en-US,en;q=0.9"
}
url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")

prices = [price.text for price in soup.find_all(name="div", class_="list-card-price")]
addresses = [address.text for address in soup.find_all(name="address", class_="list-card-addr")]
links = [link["href"] for link in soup.find_all(name='a', class_="list-card-link")]
prices[0] = prices[0].split("+")[0] + "/mo"
prices[1] = prices[1].split("+")[0] + "/mo"
for i in range(len(links)-1):
    if links[i][0] != "h":
        links[i] = "https://www.zillow.com/" + links[i]

new_links = []

for i in range(len(links)-1):
    if i % 2 == 0:
        new_links.append(links[i])


bot = Form()
for i in range(len(prices) - 1):
    bot.fill_form(prices[i], new_links[i], addresses[i])

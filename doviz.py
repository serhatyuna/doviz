from bs4 import BeautifulSoup as bs
import requests

url = 'http://tlkur.com/'
page = requests.get(url)

if page.status_code == 200:
	soup = bs(page.text, 'html.parser')
	count = 0
	while count < 4:
		name = soup.select('#major_rates > tr')[count].select('td')[1].text
		price = soup.select('#major_rates > tr')[count].select('td')[3].text
		change = soup.select('#major_rates > tr')[count].select('td')[4].text
		tab = "₺\t\t(" if count != 3 else "₺\t("
		print(name + "\t->\t" + price + tab + change + ")")
		count += 1
else:
	print("Siteye bağlanılamıyor. Tekrar deneyiniz!")
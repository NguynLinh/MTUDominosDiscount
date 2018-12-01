import bs4
import datetime
from datetime import date, timedelta
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.michigantechhuskies.com/sports/mice/2018-19/schedule'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("tbody",{"class":"event-group"})

def disc():

	date = datetime.datetime.now()
	yesterday = date.today() - timedelta(1)
	last_month = date.replace(day=1) - timedelta(days=1)

	month = date.strftime("%B")

	if date.strftime("%d") == '01':
		month = last_month.strftime("%B")

	for container in containers:
		month_container = container.findAll("tr", {"class":"month-title"})
		if month_container[0].text.strip() == month:
			games_container = container.findAll("tr",{"class":"event-row"})
			break

	for game in games_container:
		if yesterday.strftime("%d") == game.td.text.strip()[5:]:
			result = game.find("td",{"class":"e_result"})

	result_text = result.text.strip()
	first_score = result_text[3]
	second_score = result_text[5]

	if result_text[0] == 'W':
		if first_score > second_score:
			discount = first_score
		else:
			discount = second_score
	elif result_text[0] == 'L':
		if first_score < second_score:
			discount = first_score
		else:
			discount = second_score
	else:
		discount = first_score

	discount = int(discount)
	if discount > 5:
		discount = 5

	discount = discount * 10
	return discount
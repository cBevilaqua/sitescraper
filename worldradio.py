from bs4 import BeautifulSoup
import requests

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# BASE_URL = "https://worldradiohistory.com/Archive-Short-Wave-Television/30s/"

BASE_URL = "https://worldradiohistory.com/Archive-Short-Wave-Television/40s/"

response = requests.get(BASE_URL)
page_html = response.text
soup = BeautifulSoup(page_html, 'html.parser')
file_links = soup.select("td a")

def download(url, directory):
	file_name = url.rsplit('/', 1)[1]
	r = requests.get(url, allow_redirects=True)
	open(directory + '/' + file_name, 'wb').write(r.content)

for link in file_links:
	href = link['href']
	if ".pdf" in href:
		full_url = BASE_URL + link['href']
		#download(full_url, 'worldradio_30s')
		download(full_url, 'worldradio_40s')



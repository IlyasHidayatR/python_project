from bs4 import BeautifulSoup
import requests
import pysolr

base_url = "https://indeks.kompas.com/";

for i in range (1, 100):
  req = requests.get(base_url + "?site=hype&page=" + str(i))
  soup = BeautifulSoup(req.text, "html.parser")
# print(soup.prettify())

print(soup.title.text)
for p in soup.find_all('p'):
  print(p.text)

def scrap(url):
  # req = []
  # soup = []
  # for i in range (1, 10):
  #   req.append(requests.get(url))
  #   soup.append(BeautifulSoup(req[i].text, "html.parser"))

  #   title = soup[i].title.text

  #   for p in soup[i].find_all('p'):
  #     body += p.text

  #     return {"id": url, "title": title, "body": body}

  # req = requests.get(url)
  # soup = BeautifulSoup(req.text, "html.parser")
  title = soup.title.text

  body = ""
  for p in soup.find_all('p'):
    body += p.text

    return {"id": url, "title_txt_id": title, "body_txt_id":body}

data = []
for i in range(1, 100):
  data.append(scrap("https://indeks.kompas.com/?site=hype&page=" + str(i)))
  print(data)

solr = pysolr.Solr("http://192.168.99.100:8983/solr/tugas/")
# solr.ping()
counter = 500
for i in data:
  for a in soup.find_all('a',href=True):
    url = a['href']
    #print(url)
    if (url[0:33] == "https://www.kompas.com/hype/read/"):
      #   print(url)
      req = requests.get(url)
      soup = BeautifulSoup(req.text, "html.parser")
      i = scrap(url)
      solr.add(i)
      solr.commit(i)
      counter -= 1

    elif (counter==0):
      break

# solr.delete(q="*:*")
# solr.commit()
from bs4 import BeautifulSoup
import requests
import pysolr

base_url = "https://www.kompas.com";

req = requests.get(base_url + "/hype/read/2022/05/24/105405566/dokter-saksi-ahli-bantah-pernyataan-johnny-depp-soal-ujung-jari-yang-putus")
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.prettify())

print(soup.h1.text)
for p in soup.find_all('p'):
  print(p.text)

def scrap(url):
  req = requests.get(url)
  soup = BeautifulSoup(req.text, "html.parser")

  title = soup.h1.text

  body = ""
  for p in soup.find_all('p'):
    body += p.text

    return {"id": url, "title_txt_id": title, "body_txt_id":body}

data = scrap("https://www.kompas.com/hype/read/2022/05/24/105405566/dokter-saksi-ahli-bantah-pernyataan-johnny-depp-soal-ujung-jari-yang-putus")

solr = pysolr.Solr("http://192.168.99.100:8983/solr/tugas/")
# solr.ping()
counter = 10
for a in soup.find_all('a',href=True):
  url = a['href']
  #print(url)
  if (url[0:33] == "https://www.kompas.com/hype/read/"):
    #   print(url)
    data = scrap(url)
    solr.add(data)
    solr.commit()
    counter -= 1

  elif (counter==0):
    break
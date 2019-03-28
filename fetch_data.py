import io
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.gutenberg.org/files/2852/2852-0.txt')
if response.status_code != 200:
  print "Request failure"

p = response.content

soup = BeautifulSoup(p, "html.parser").encode("utf-8")

with io.open("hounds.txt", "wb") as f:
  f.write(soup)
__author__ = 'htom'
from bs4 import BeautifulSoup
import urllib2
wiki = "https://en.wikipedia.org/wiki/List_of_English_animal_nouns"
header = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
table = soup.find("table", { "class" : "wikitable sortable" })




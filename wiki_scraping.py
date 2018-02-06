from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from html.parser import HTMLParser
import os
import io
import hhh as g

#Google search result for the query
query = input("Type name to search")
with io.open(query+'.txt', "a", encoding="utf-8") as f44:

    query=query.lower()

    for j in g.search(query, tld='com', lang='en', tbs='0', safe='off', num=10, start=0,
                      stop=10, domains=None, pause=2.0, only_standard=False):
        # print(j)
        f44.write(j)
        f44.write('\n')
f44.close()

#finding the relative wikipedia query

string="https://en.wikipedia.org/wiki/%s"
my_url=string % query[0]
with io.open(query + '.' + 'txt', "r", encoding="utf-8") as f1:
    for line in f1:
        line1 = line.lower()
        result = line1.find(my_url)
        if result == -1:
            continue
        else:
            final_url=line

f1.close()

#function to connect to URL
def fetchdata(url):

                         try:
                                client=urlopen(url)
                                return (client)
                         except:
                                    print ("failed try again")
                                    return fetchdata(url)




uClient=fetchdata(final_url)

#Scraping of TEXT from HTML data parsed

page_html=uClient.read()
uClient.close()
page_soup=soup(page_html ,"html.parser")
#mw-content-text
containers=page_soup.findAll("div", {"id": "mw-content-text"})
container=containers[0]
#print(container.text)
a=container.text
#print(soup.prettify(page_soup))
#a=soup.prettify(page_soup)
with io.open(query+'1.txt', "a", encoding="utf-8") as f:
    f.write(a)
#f=open("name.txt",'w')

f.close()







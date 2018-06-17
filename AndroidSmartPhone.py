from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import os
import re
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from html.parser import HTMLParser
import io
import hhh as g

db = GraphDatabase("http://localhost:7474", username="neo4j", password="shaktisingh")
my_url = "https://en.wikipedia.org/wiki/Xiaomi_Redmi"
my_url1 = "https://en.wikipedia.org/wiki/Acer_Liquid_A1"


def fetchdata1(U_rl):
    try:
        client = urlopen(U_rl)
        return (client)
    except:
        print("failed try again")
        return fetchdata1(my_url1)

def fetchdata(url):
    try:
        client = urlopen(my_url)
        return (client)
    except:
        print("failed try again")
        return fetchdata(my_url)


uClient = fetchdata(my_url)
# uClient=urlopen(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.find("div", {"class": "navbox"})
# print(soup.prettify(containers))
# container=containers[0]

headers = containers.find("table",{"class":"nowraplinks hlist collapsible collapsed navbox-inner"})
rows=headers.findAll("tr")
f = open(
    "C:/Users/IBM_ADMIN/AppData/Roaming/Neo4j Desktop/Application/neo4jDatabases/database-7f83e15b-2553-485c-ac9b-8721d02222e6/installation-3.3.3/import/smartphone1.txt", "a")
#print(len(rows))
for x in range (1,len(rows)-1):
    headings=rows[x].findAll("a",href=True)
    #print(len(headings))
    for y in range(1,len(headings)):
        link=headings[y]["href"]
        link = "https://en.wikipedia.org"+link+"\n"
        f.write(link)
        #print(link)
f.close()
f1 = open(
    "C:/Users/IBM_ADMIN/AppData/Roaming/Neo4j Desktop/Application/neo4jDatabases/database-7f83e15b-2553-485c-ac9b-8721d02222e6/installation-3.3.3/import/smartphone1.txt", "r")
data=f1.read()
linkstring=data.split("\n")
print(len(linkstring))
count=0
for yourl in linkstring:
    U_rl=yourl
    print(U_rl)
    count=count+1
    count1=str(count)
    print("link no."+count1+" in progress")
    try:
        uClient1 = fetchdata1(U_rl)
        # uClient=urlopen(my_url)
        page_html1 = uClient1.read()
        uClient1.close()
        page_soup1 = soup(page_html1, "html.parser")
        containers1 = page_soup1.find("table", {"class": "infobox hproduct"})
        caption = containers1.find("caption", {"class": "fn"})
        caption = caption.text
        caption = caption.replace(" ", "_")
        q = 'MERGE (n:' + caption + ')'
        db.query(q)
        rows = containers1.findAll("tr")

        for row in rows:
            try:
                heading = row.find("th")
                heading = heading.text
                heading = heading.replace(" ", "_")
                print(heading)
                defintion = row.find("td")
                defintion = defintion.text
                print(defintion)
                q = 'MATCH (n:' + caption + ')SET n.' + heading + '="' + defintion + '"'
                print(q)
                db.query(q)
            except:
                try:
                    heading = row.find("th")
                    heading = heading.text
                    heading = heading.replace(" ", "_")
                    print(heading)
                    defintion = row.find("td")
                    defintion = defintion.text
                    print(defintion)
                    q = "MATCH (n:" + caption + ")SET n." + heading + "='" + defintion + "'"
                    print(q)
                    db.query(q)
                except:
                    continue

    except:
        print("link no."+count1+" failed")
        continue
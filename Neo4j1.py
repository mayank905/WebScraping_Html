from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from html.parser import HTMLParser
import os
import io
import hhh as g

# Google search result for the query
query = input("Type name to search")
with io.open(query + '.txt', "a", encoding="utf-8") as f44:
    query = query.lower()

    for j in g.search(query, tld='com', lang='en', tbs='0', safe='off', num=10, start=0,
                      stop=10, domains=None, pause=2.0, only_standard=False):
        # print(j)
        f44.write(j)
        f44.write('\n')
f44.close()

# finding the relative wikipedia page

string = "https://en.wikipedia.org/wiki/%s"
my_url = string % query[0]
with io.open(query + '.' + 'txt', "r", encoding="utf-8") as f1:
    for line in f1:
        line1 = line.lower()
        result = line1.find(my_url)
        if result == -1:
            continue
        else:
            final_url = line
            break


f1.close()


# function to connect to URL
def fetchdata(url):
    try:
        client = urlopen(url)
        return (client)
    except:
        print("failed try again")
        return fetchdata(url)


# Hello GitHub
uClient = fetchdata(final_url)

# Scraping of TEXT from HTML data parsed

page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")  # html page retrievedtext
a = ""
# mw-content-
#
# Retrieve basic information from wiki table
#
'''
with io.open(query + 'table.txt', "w", encoding="utf-8") as f:
    try:
        containers = page_soup.find("table", {"class": "infobox vcard"})
        Infotable = containers.findAll("th",{"style":"text-align:center;background-color: #b0c4de"})
        for k in Infotable:
            print(k.text)
    except:
        print("all heading not found")

    '''

with io.open(query + 'table1_2.csv', "w", encoding="utf-8") as f:
    headers = "Celebrity_name,Born,Residence\n"
    f.write(headers)
    try:
        containers = page_soup.find("table", {"class": "infobox biography vcard"})
        # tbbody=containers.find("tbody")
        Infotable = containers.findAll("tr")
        # with io.open(query + 'table.txt', "w", encoding="utf-8") as f:

        for tr1 in Infotable:
            try:

                th1 = tr1.find("th")
                try:
                    td1 = tr1.find("td")
                    print(th1.text + "(original)th present")
                    print(td1.text + "td present")

                   # a = a + "           " + th1.text
                    a = a + " [[[[  " + td1.text + "]]]]]]"
                    # a=a+" "+td1.txt
                    a = a + "\n"
                except:
                    th1 = tr1.find("th")
                    print(th1.text + "original th present but td not present")
                    a = a + "            " + th1.text

                    # a=a+" "+td1.txt
                    a = a + "\n"
            except:
                try:
                    td1 = tr1.find("td")
                    try:
                        th1 = tr1.find("th")
                        print(th1.text + "th present")
                        print(td1.text + "td present")

                        a = a + th1.text
                        a = a + " [[[[[[[  " + td1.text + "]]]]]]]]]"
                        # a=a+" "+td1.txt
                        a = a + "\n"
                    except:
                        td1 = tr1.find("td")
                        print(td1.text + "td present but th not present")
                        a = a + "[[[[[[[[" + td1.text + "]]]]]]]]]"
                        # a=a+" "+td1.txt
                        a = a + "\n"

                except:


                        continue

        f.write(a)

    except:
        containers = page_soup.find("table", {"class": "infobox vcard"})
        Infotable = containers.findAll("tr")
        # with io.open(query + 'table.txt', "w", encoding="utf-8") as f:

        for tr1 in Infotable:
            try:

                th1 = tr1.find("th")
                try:
                    td1 = tr1.find("td")
                    print(th1.text + "(original)th present")
                    print(td1.text + "td present")

                    a = a + "           " + th1.text
                    a = a + " [[[[  " + td1.text + "]]]]]]"
                    # a=a+" "+td1.txt
                    a = a + "\n"
                except:
                    th1 = tr1.find("th")
                    print(th1.text + "original th present but td not present")
                    a = a + "            " + th1.text

                    # a=a+" "+td1.txt
                    a = a + "\n"
            except:
                try:
                    td1 = tr1.find("td")
                    try:
                        th1 = tr1.find("th")
                        print(th1.text + "th present")
                        print(td1.text + "td present")

                        a = a + th1.text
                        a = a + " [[[[[[[  " + td1.text + "]]]]]]]]]"
                        # a=a+" "+td1.txt
                        a = a + "\n"
                    except:
                        td1 = tr1.find("td")
                        print(td1.text + "td present but th not present")
                        a = a + "[[[[[[[[" + td1.text + "]]]]]]]]]"
                        # a=a+" "+td1.txt
                        a = a + "\n"

                except:

                    continue

        f.write(a)

# container=containers[0]
# print("birthday is on " + containers.text)
# a=containers.text
# print(soup.prettify(page_soup))
# a=soup.prettify(containers)
# with io.open(query+'table.txt', "w", encoding="utf-8") as f:
# with io.open('pretty.txt', "a", encoding="utf-8") as f:
#   f.write(a)
# f=open("name.txt",'w')

f.close()







#! C:/Users/IBM_ADMIN/PycharmProjects/WebScraping_Html/venv/Scripts/python.exe

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import os
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import cgi, cgitb
print("Content-type:text/html\r\n\r\n")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
#first_name = form.getvalue('first_name')
FinalQuery  = form.getvalue('Query')
#first_name=first_name.lower()
#last_name=last_name.lower()
FinalQuery=FinalQuery.lower()


db = GraphDatabase("http://localhost:7474", username="neo4j", password="shaktisingh")

def jaccard(a, b):
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

labelquery="MATCH (r) RETURN labels(r);"
#Q2='MATCH  (a:iphone),(b:redmi) WHERE toInteger(a.Price)<50000 AND toInteger(b.Price)>10000 MERGE (b)-[r:isEqualTo]->(a) RETURN b, type(r),a '
'''
results = db.query(finalquery)
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["Name"], r[2]["Name"]))

results = db.query(finalquery, returns=(client.Node, str, client.Node))
for r in results:
    print("(%s)-[%s]->(%s)" % (r[0]["Name"], r[1], r[2]["Name"]))
'''
#MATCH (r) RETURN labels(r);

results = db.query(labelquery, returns=(str))
label=[]
small_label=[]
smallabel=[]
for r in results:
    ttt=r[0]
    ttt1=ttt.replace('[','')
    ttt2=ttt1.replace(']','')
    ttt3=ttt2.replace("'","")
    if ttt3=="Word":
        continue
    else:
        label.append(ttt3)
        ttt3=ttt3.lower()
        smallabel.append(ttt3)
        ttt3 = ttt3.replace("_", " ")
        small_label.append(ttt3)
#label=list(set(label))
#small_label=list(set(small_label))
#label=list(set(label))
#small_label=list(set(small_label))
#print(label)
#print(small_label)
sla=len(small_label)
la=len(label)
## MATCH (p)  RETURN keys(p)
property_query="MATCH (p)  RETURN keys(p);"
results = db.query(property_query, returns=(str))
property=[]
for p in results:
    property=property+p
property = ''.join(property)
property=property.replace('[', '')
property=property.replace(']', '')
property=property.replace('"', '')
property=property.replace("'", '')
property=property.replace(' ', '')
#property=property.replace(',', ' ')
#print(property)
property=property.split(',')
property=list(set(property))
Orig_Property=list(property)
key=0
lent=len(property)
for key in range(lent):
    property[key]=property[key].lower()
#print(property)

#Natural_Language_query=input("enter the query ")
#Natural_Language_query=Natural_Language_query.lower()
Natural_Language_query=FinalQuery
Natural_Language_query=Natural_Language_query.split(" ")
Label=[]
Property=[]
lll=len(Natural_Language_query)
k=0
h=0
while h <lll:
    try:
        for r in range(sla):

            word = ""
            sl = small_label[r].split(" ")
            s = len(sl)

            for j in range(s):
                if sl[j] == Natural_Language_query[h + j]:
                    # print("s1[j]="+ sl[j])
                    # print("natural query"+Natural_Language_query[h+j])
                    k = k + 1
                    word = word + Natural_Language_query[h + j] + "_"

                    # print(word)
                else:
                    k = 0
                    break

            word = word[:-1]

            if word:
                try:
                    # print("word to be search")
                    i = smallabel.index(word)
                    # print(label[i])
                    Label.append(label[i])

                    h = h + j
                    break
                except:
                    continue

        for r in range(lent):

            word = ""
            sl = property[r].split(" ")
            s = len(sl)

            for j in range(s):
                if sl[j] == Natural_Language_query[h + j]:
                    word = word + Natural_Language_query[h + j] + "_"
                    # print(word)
                else:
                    break

            word = word[:-1]
            # print(word)

            if word:
                try:
                    j1 = property.index(word)
                    # print(Orig_Property[j1])
                    Property.append(Orig_Property[j1])
                    h = h + j
                    break
                except:
                    continue

        h = h + 1
    except:
        print("<h2>incorrect query or data not found</h2>")



#print(Label)
#print(Property)
#print(Orig_Property[j1])
#print(label[i])
#print(word)
if Label != []:
    for node in Label:
        query = "MATCH"
        query = query + '(' + node + ':' + node + '),'
        query = query[:-1]
        query = query + " RETURN "
        iteration = len(Property)
        if iteration !=0:

            for key in Property:
                query = query + node + '.' + key + ','
            query = query[:-1]
            query = query + ";"
            results = db.query(query)
            if results != []:
                i = 0
                for r in results:
                    #print("\n")
                    for i in range(iteration):
                        print("<h2>%s %s(%s)</h2>" % (node, Property[i], r[i]))
            else:
                print("<h2>Data incorrect or Not found</h2>")
        else:
            print("<h2>Properties of %s are</h2>"% (node))
            query = query + 'keys('+node+")"
            query = query + ";"
            results = db.query(query)
            if results != []:
                for r in results:

                    print("<h2>%s</h2>"%(r[0]))
                   # print("\n")
            else:
                print("<h2>This Product has no property stored</h2>")

else:
    print("<h2>Device name incorrect or Not found</h2>")

print("<form action = 'second.py' method = 'post'>")

print('<input type = "submit" value = "CLEAR" />')
print("</form>")


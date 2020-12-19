import data as data
from bs4 import BeautifulSoup
import urllib.request as urllib2

#extragem codul html
def verif_titlu(url):
    page=urllib2.urlopen(url)
    #convertim codul in format beautifulsoup
    soup=BeautifulSoup(page,'html.parser')
    titlu=soup.title.text.split()
    if titlu !="":
        print("Exista titlu! \n",titlu)
    else:
        print("Nu exista titlu!")

#extragere tag h1
def extr_h1(url):
    page = urllib2.urlopen(url)
    # convertim codul in format beautifulsoup
    soup = BeautifulSoup(page, 'html.parser')
    for i in soup.find_all(["h1"]):
        print(i.text.strip())


#Extragere filme
def top_filme():
    url='https://www.imdb.com/chart/top/'                  #url top
    page=urllib2.urlopen(url)                              #deschide url
    soup=BeautifulSoup(page,'html.parser')                 #Conversie format beautifulsoup
    lista=soup.find_all('div',{"class":"lister"})          #lista=clasa in care se afla titlul si ratingul
    lista_filme=[]
    lista_rating=[]
    for i in lista:
        for j in i.find_all(['a']):                        #in <a din lista se afla titlul sub forma de text
            lista_filme.append(j.text)
        for k in i.find_all(['strong']):                   #in <string din lista se afla ratingul sub forma de text
            lista_rating.append(k.text.strip())
    for i in lista_filme:                                  #eliminare spatii din lista filme
        if i==' \n':
            lista_filme.remove(i)
    i=0
    while i<250:
        print("%d. %s     rating: %s"%(i+1,lista_filme[i],lista_rating[i]))   #afisare
        i+=1
print("Verif_titlu ruleaza...\n")
verif_titlu("https://www.imdb.com/chart/top/")
print("extr_h1 ruleaza...\n")
extr_h1("https://www.imdb.com/chart/top/")
print("Topul filmelor este: ")
top_filme()

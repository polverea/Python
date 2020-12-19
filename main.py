import urllib.request as urllib2
url="https://google.ro"
raspuns_server=urllib2.urlopen(url)
date=raspuns_server.read()
print (date)
fisier_html=open("site.html","w")
fisier_html.write(str(date))
fisier_html.close()

lista=["https://www.google.ro/imghp?hl=ro&tab=wi","https://maps.google.ro/maps?hl=ro&tab=wl","https://www.youtube.com/?gl=RO&tab=w1","https://news.google.com/?tab=wn","https://mail.google.com/mail/?tab=wm","https://drive.google.com/?tab=wo","https://drive.google.com/?tab=wo","https://www.google.com/calendar?tab=wc","http://www.google.ro/history/optout?hl=ro","http://www.google.ro/intl/ro/services/"]

for i in lista:
    raspuns_server = urllib2.urlopen(i)
    date=raspuns_server.read()
    fisier_html = open("site.html", "a")
    fisier_html.write(str(date))
fisier_html.close()
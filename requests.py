import nmap, os

#Alocare variabile
obiect=nmap.PortScanner()
ports='20-80'
#Obtinerea device-urilor
devices=os.popen('arp -n | cut  -f1 -d \' \' | grep [0-9]').read()
print (devices)
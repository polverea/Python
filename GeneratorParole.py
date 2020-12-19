import random
import string
f=open("parola.txt","w")
litere=string.ascii_letters
cifre=string.digits
punctuatie=string.punctuation
def lungime_parola():
    lungime=input("Cate caractere va contine parola?")
    return int(lungime)

def generare_parola():
    printable=litere+cifre+punctuatie
    printable=list(printable)
    random.shuffle(printable)
    random_password=random.choices(printable,k=lungime_parola())
    #random_password=''.join(random_password)
    password=""
    for i in random_password:
        password+=i
    f.write(password)
generare_parola()
f.close()
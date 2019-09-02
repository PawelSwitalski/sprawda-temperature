import requests
from bs4 import BeautifulSoup


def miasto(st):
    Miasto = ""
    for i in range(59, 100):
        if st[i] == "/":
            break
        Miasto += st[i]
    #print(*Miasto)
    return Miasto

def stopnie(st):
    wypisz = ""
    for i in range(st.find("/") + 2, st.find("°C") + 2):
        wypisz += st[i]
    #print(*wypisz)

    return str(wypisz).replace("Pogoda", "temperatura: ")

def dzien_godzina(st):
    wypisz = ""
    for i in range(st.find("°C") + 2, st.find("\n")):
        wypisz += st[i]
    #print(*wypisz)
    return wypisz

class Pogoda_Dane:
    def __init__(self, Miasto, Temperatura, Dzien_Godzina):
        self.Miasto = str(Miasto)
        self.Temperatura = str(Temperatura)
        self.Dzien_Godzina = str(Dzien_Godzina)



def Wyjsciowe():
    strona = requests.get("https://www.google.com/search?q=pogoda&oq=pogoda&aqs=chrome..69i57j0l4j69i61.4905j1j7&sourceid=chrome&ie=UTF-8")

    if (strona.status_code == 200):
        html_doc = strona.text
        szukanie = BeautifulSoup(html_doc, "html.parser")

        znalezione2 = (szukanie.text[szukanie.text.find("G5eFlf") : szukanie.text.find("G5eFlf")+200])
        #miasto(znalezione2)
        #stopnie(znalezione2)
        #dzien_godzina(znalezione2)

        dane_pogodowe = Pogoda_Dane(miasto(znalezione2), stopnie(znalezione2), dzien_godzina(znalezione2))

        print(dane_pogodowe.Dzien_Godzina, " ", dane_pogodowe.Temperatura)
        return dane_pogodowe

    else:
        print("blad strony")
        return 0


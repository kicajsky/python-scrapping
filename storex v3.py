import requests
import time
import ctypes
import sys
import winsound
duration = 10000  # milliseconds
freq = 440  # Hz
from bs4 import BeautifulSoup
import time

MessageBox = ctypes.windll.user32.MessageBoxW

url0 = 'https://mediamarkt.pl/konsole-i-gry/konsola-nintendo-switch-nowa-wersja-v2-animal-crossing-new-horizons-edition'
url1 = 'https://mediamarkt.pl/konsole-i-gry/gra-nintendo-switch-nintendo-labo-variety-kit-21'
url2 = 'https://mediamarkt.pl/konsole-i-gry/etui-hori-alumi-case-zelda-do-nintendo-switch'
url3 = 'https://mediamarkt.pl/konsole-i-gry/konsola-nintendo-switch-nowa-wersja-v2-joy-con-niebiesko-czerwony-nintendo-labo-variety-kit'
url4 = 'https://mediamarkt.pl/konsole-i-gry/gra-nintendo-switch-ring-fit-adventure'
url5 = 'https://mediamarkt.pl/konsole-i-gry/gra-nintendo-switch-ring-fit-adventure?utm_medium=affiliate&utm_content=lowcygier.pl+PL&utm_campaign=tradedoubler&utm_term=Premium_2,5&utm_source=tradedoubler'

url6 = 'https://mediamarkt.pl/konsole-i-gry/gra-nintendo-switch-nintendo-labo-variety-kit'

CHECK_TIME_IN_s = 60*10

def adress(url, nazwa):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find(itemprop="price").get_text()

    if "Produkt chwilowo" in r.text:
        None
        #print(nazwa +"\t-> Nope")
    else:
        print(nazwa +"\t-> OK "+price+' PLN')
        #winsound.Beep(freq, 1000)
        #MessageBox(None, 'Yaay!', 'You found it!', 0)
        #sys.exit()

while(True):
    r = requests.get(url0)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find(itemprop="price").get_text()
    if "Produkt chwilowo" in r.text:
        #print("Animal Crossing\t\t-> Nope")
        None
    else:
        winsound.Beep(freq, duration)
        print("Animal Crossing -> OK"+price+' PLN')
        MessageBox(None, 'Yaay! Animal Crossing\n\t'+price+' PLN', 'You found it!', 0)
        #sys.exit()

    r = requests.get(url6)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find(itemprop="price").get_text()
    if "chwilowo" in r.text:
        None
    else:
        int_price = int(price)
        if int_price<269:
            print("Labo -> OK"+price+' PLN')

    #--------------------------
    adress(url0, 'Animal')
    adress(url1, 'Labo')
    adress(url2, 'Hori Alumi')
    adress(url3, 'Color+Lab')
    adress(url4, 'Ring Fit1')
    adress(url5, 'Ring Fit2')
    #--------------------------
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    print(current_time, " -------------------------")
    time.sleep(CHECK_TIME_IN_s)

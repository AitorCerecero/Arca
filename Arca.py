from bs4 import BeautifulSoup
import requests
import pandas as pd

data = requests.get("https://www.highspeedinternet.com/in/mexico")
print(data.status_code)

xtract = BeautifulSoup(data.content,"html.parser")


ISP = xtract.find_all("div",class_="columns small-12 medium-6 small-only-text-center font-medium")
Loc = xtract.find_all("div",class_="columns small-12 medium-6 small-only-text-center medium-up-text-right align-self-middle font-small")
Speed = xtract.find_all("div",class_="provider-card-item small-only-text-center")

isp = list()
loc = list()
speed = list()

for x in ISP:
    isp.append(x.text)


for x in Loc:
    loc.append(x.text)


for x in Speed:
    speed.append(x.text)

datalink = ('Nombre: ',isp,'Disponibilidad:',loc,'Velocidad:',speed)

DL = pd.DataFrame(data=datalink)

DL.to_csv('ISP_Data.csv')

print(isp)
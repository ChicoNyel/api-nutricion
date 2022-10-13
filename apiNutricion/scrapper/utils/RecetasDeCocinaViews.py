import requests
import time
from bs4 import BeautifulSoup
from kernel.models import Food

class Config:

    url = 'https://recetasdecocina.elmundo.es/tabla-calorias'


def get_data() -> bool:

    url = Config.url
     
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find(class_='td-container tdc-content-wrap').find_all("table")

    for data in tables:

        tds = data.find_all('tr')

        cont = 0
        
        for td in tds:

            if cont > 0:

                formato = {
                    "nombre": None,
                    "calorias": None,
                    "equivalencia" : "100 g"
                }

                if "<a " in str(td):

                    partesTD = str(td).split('<')
                    formato['nombre'] = partesTD[3].split(">")[1]
                    formato['calorias'] = partesTD[6].split(">")[1]

                else:

                    partesTD = str(td).split('<')
                    formato['nombre'] = partesTD[2].split(">")[1]
                    formato['calorias'] = partesTD[4].split(">")[1]

                print(formato)

                try:
                    food = Food.objects.get(name=formato['nombre'])
                except:
                    Food.objects.create(
                        name = formato['nombre'],
                        calories = formato['calorias'],
                        equivalence = formato['equivalencia'],
                        measure = None,
                        letter = formato['nombre'][0:1]
                    )

            cont += 1

    return True
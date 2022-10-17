import requests
import time
from bs4 import BeautifulSoup
from kernel.models import Food

class Config:

    url = 'https://www.tabladecalorias.net/alimento/platos-y-comidas'


def get_data() -> bool:

    url = Config.url
     
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_='table-responsive').find_all("table")[0]
    rows = table.find_all('tr')

    cont = 0
    
    for row in rows:

        if cont > 0:

            formato = {
                "nombre": None,
                "calorias": None,
                "equivalencia" : None
            }

            formato['nombre'] = str(row).split('>')[3].split('<')[0]
            formato['equivalencia'] = str(row).split('>')[7].split('<')[0] + ' g'
            formato['calorias'] = str(row).split('>')[19].split('<')[0] + ' kcal'

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
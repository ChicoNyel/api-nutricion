import requests
import time
from kernel.models import Food

class Config:

    url = 'https://www.clinicasantamaria.cl/calculadoras/calorias/resultado?letra={letra}'
    letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def get_data() -> bool:

    for letra in Config.letras:

        url = Config.url.format(letra=letra)

        response = requests.post(url).json()

        for data in response['_calorias']:

            try:
                food = Food.objects.get(name=data['_alimento'])
            except:
                Food.objects.create(
                    name = data['_alimento'],
                    calories = data['_calorias'],
                    equivalence = data['_equivalencia'],
                    measure = data['_medida'],
                    letter = data['_letra']
                )

        print(response)

    return True
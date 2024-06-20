import requests
import json
import os


def formar_json():
    dic_data = {
        'swtiches': [
            {"model": 'CAT3750', "model2": 'CAT3760'}
        ]
    }
    # Imprimir el diccionario formateado
    print(json.dumps(dic_data, indent=4, sort_keys=True))

    # Guardar el diccionario en un archivo JSON
    with open("./data/infraestructura.json", "w") as file:
        json.dump(dic_data, file, indent=4, sort_keys=True)

def get_api_ips():
    response = requests.get('http://ip-api.com/json/24.48.0.1')
    print(response.json())

#Consumir la Apy de la plataforma 2, y una consultas de devnet

if __name__ == '__main__':
    #formar_json()
    get_api_ips()


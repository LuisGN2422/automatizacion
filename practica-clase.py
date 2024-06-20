import requests
import json
import os

"""API Información del anfitrión
Devuelve todos los servicios que se han encontrado en la IP del host determinada."""
def get_api_anfitrion():
    response = requests.get('https://api.shodan.io/shodan/host/8.8.8.8?key=iQQGPSUV733eBHml1V31jRX3XYxY6Fks')
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None

"""API Enumeración de todos los puertos que Shodan rastrea en Internet.
Este método devuelve una lista de números de puertos que buscan los rastreadores."""
def get_api_puertos():
    response = requests.get('https://api.shodan.io/shodan/ports?key=iQQGPSUV733eBHml1V31jRX3XYxY6Fks')
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error {response.status_code}: {response.text}')
        return None

def get_devnet():

    url = "https://api.meraki.com/api/v1/organizations"

    payload = None

    headers = {
        "X-Cisco-Meraki-API-Key": "75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.request('GET', url, headers=headers, data=payload)

    print(response.text.encode('utf8'))


def main():
    anfitrion_info = get_api_anfitrion()
    puertos_info = get_api_puertos()
    devnet_info = get_devnet()

    all_info = {
        'anfitrion_info': anfitrion_info,
        'puertos_info': puertos_info,

    }

    # Imprimir la información combinada en orden
    print("Información del Anfitrión:")
    print(json.dumps(anfitrion_info, indent=2))
    print("\nInformación de Puertos:")
    print(json.dumps(puertos_info, indent=2))
    print("\nInformación de DevNet:")
    print(json.dumps(devnet_info, indent=2))

    # Asegurarse de que el directorio existe
    os.makedirs('./data', exist_ok=True)

    # Guardar el diccionario combinado en un archivo JSON
    with open("./data/APIs.json", "w") as file:
        json.dump(all_info, file, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()

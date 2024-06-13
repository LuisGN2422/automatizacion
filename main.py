import json
dic_data = {'swtiches':[
    {"model":'CAT3750',
     "model":'CAT3760'}[
     'routers':{'name':'CSR100V',
                'vendor': 'cisco',
                'type': 'hardware'
                }
    ]

]}

#Tarea hacer un diccionario de nuestros cuatro elementos
#O hacer una infraestructura o diccionario con 4 componentes local
print(json.dumps(dic_data, indent=2))

if __name__ == '__main__':
    pass

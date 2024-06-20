import json
dic_data = {'swtiches':[
    {"model":'CAT3750',
     "model":'CAT3760'}

]}

dic_data2={
    'router':[
    {"model":'7206VXR',
     "so" :'Cisco IOS',
     "vendor" :'Cisco',
     "type" :'hardware'
     }],
    'server1':[
    {'name':'Servidor 1',
     'service':'WEB',
     'remote_conection':'SSH',
     'linux distribution':'Mint'
                }],
    'server2':[
    {'name':'Servidor 2',
     'service1':'DNS',
     'service2':'WEB',
     'linux distribution':'Centos 8'
                }],
    'server3':[
    {'name':'Servidor 3',
     'service1':'FTP',
     'service2':'DHCP',
     'linux distribution':'Mint'
                }]
    }
#Tarea hacer un diccionario de nuestros cuatro elementos
#O hacer una infraestructura o diccionario con 4 componentes local
print(json.dumps(dic_data, indent=2))
print(json.dumps(dic_data2, indent=3))

if __name__ == '__main__':
    pass

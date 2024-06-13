import paramiko
import json
import re

# Credenciales SSH
hostname = '192.168.100.120'
port = 22
username = 'devasc'
password = 'Cisco123!'

# Conexión SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname, port=port, username=username, password=password)
    print(f'Conexión SSH establecida a {hostname}')

    # Diccionario para información del sistema
    system_info = {}
    stdin, stdout, stderr = client.exec_command('hostname')
    system_info['hostname'] = stdout.read().decode('utf-8').strip()

    stdin, stdout, stderr = client.exec_command('uname -s')
    system_info['system'] = stdout.read().decode('utf-8').strip()

    stdin, stdout, stderr = client.exec_command('uname -r')
    system_info['release'] = stdout.read().decode('utf-8').strip()

    stdin, stdout, stderr = client.exec_command('uname -m')
    system_info['architecture'] = stdout.read().decode('utf-8').strip()

    stdin, stdout, stderr = client.exec_command('uname -p')
    system_info['processor'] = stdout.read().decode('utf-8').strip()

    # Diccionario para información de la red
    network_info = {}
    stdin, stdout, stderr = client.exec_command('ip -4 addr show')
    ip_output = stdout.read().decode('utf-8').strip()
    # Extraer la IP de la interfaz principal (generalmente eth0 o ens33)
    match = re.search(r'inet (\d+\.\d+\.\d+\.\d+)', ip_output)
    if match:
        network_info['ip_address'] = match.group(1)
    # Agregar la dirección IP del servidor
    network_info['connected_ip'] = hostname

    # Diccionario para información de almacenamiento
    storage_info = {}
    stdin, stdout, stderr = client.exec_command('df -h /')
    disk_usage = stdout.read().decode('utf-8').strip().split('\n')
    if len(disk_usage) > 1:
        storage_info['disk_usage'] = disk_usage[1].split()[4]  # porcentaje de uso

    # Diccionario para información de usuarios
    users_info = {}
    stdin, stdout, stderr = client.exec_command('cut -d: -f1 /etc/passwd')
    users_list = stdout.read().decode('utf-8').strip().split('\n')
    filtered_users = [user for user in users_list if user in ['devasc', 'root']]
    users_info['users'] = filtered_users

    # Imprimir los diccionarios con formato JSON
    print("Información del Sistema:")
    print(json.dumps(system_info, indent=2))
    print("\nInformación de Tarjetas de Red:")
    print(json.dumps(network_info, indent=2))
    print("\nAlmacenamiento Usado del 100%:")
    print(json.dumps(storage_info, indent=2))
    print("\nUsuarios Registrados:")
    print(json.dumps(users_info, indent=2))

except paramiko.AuthenticationException:
    print(f'Error de autenticación al conectar a {hostname}')
except paramiko.SSHException as ssh_err:
    print(f'Error SSH al conectar a {hostname}: {ssh_err}')
finally:
    client.close()

if __name__ == '__main__':
    pass



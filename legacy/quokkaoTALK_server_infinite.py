# quokkaoTALK_server_infinite.py
# 텍스트를 인터넷으로 주고 받는 프로그램 (서버)

import socket
import os

# 클라이언트에게 메시지 전송 
def send_message(sock):
    message = input("Enter message: ")
    sock.send(message.encode('utf-8'))
    print("waiting for client...")

# 클라이언트로부터 메시지 수신 
def receive_message(sock):
    data = sock.recv(1024).decode('utf-8')
    print("Received: ", data)

# 서버 소켓 설정 
HOST = 'localhost' # 서버의 IP 주소 또는 호스트명 
PORT = 8888 # 사용 가능한 포트 번호 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP/IP 소켓 생성 (AF_INET : IPv4, SOCK_STREAM : TCP)
server_socket.bind((HOST,PORT)) # 주어진 HOST와 PORT에 소켓 바인딩 
server_socket.listen(1) # 수신 대기, 동시에 1개의 연결만 허용

print("quokkaoTALK Server started. Waiting for a client to connect...")

# 클라이언트의 연결 수락
client_socket, client_address = server_socket.accept()  # 클라이언트의 연결을 수락하고 소켓과 주소 반환 
print("Connected to client: ", client_address)  # 연결된 클라이언트의 주소 출력 

while True:
    try:
        receive_message(client_socket) # 클라이언트로부터 메시지 수신
        send_message(client_socket) # 클라이언트에게 메시지 전송 
    except Exception as e:
        print("클라이언트 연결이 끊어졌습니다...")
        os.system('pause')
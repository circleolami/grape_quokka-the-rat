#quokkaoTALK_client_infinite.py
# 텍스트를 인터넷으로 주고 받는 프로그램 (클라이언트)

import socket

# 서버에게 메시지 전송 
def send_message(sock):
    message = input("Enter message: ")
    sock.send(message.encode('utf-8'))
    print("waiting for server...")

# 서버로부터 메시지 수신 
def receive_message(sock):
    data = sock.recv(1024).decode('utf-8')
    print("Received: ", data)

# 클라이언트 소켓 설정 
HOST = 'localhost' # 서버의 IP 주소나 호스트명 사용 
PORT = 5000 # 서버와 동일한 포트 번호 사용 

print("quokkaoTALK client start...")

while True:
    try:
        # TCP 소켓 객체 생성 (AF_INET: IPv4, SOCK_STREAM: TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST,PORT)) # 주어진 HOST와 POST로 서버에 연결 요청 
            # 연결된 상태에서 메시지 주고 받기 
            while True:
                send_message(client_socket) # 서버에 메시지 전송 
                receive_message(client_socket) # 서버의 응답 수신
    except Exception as e:
        print(e)
        pass # 오류를 무시하고 다시 연결 시도 
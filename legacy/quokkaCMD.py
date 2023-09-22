# quokkaCMD.py
# 파일과 폴더를 엿보는 프로그램 (파일 탐색기)

import os

# 현재 스크립트 파일의 절대 경로 
current_directory_path = os.path.dirname(os.path.abspath(__file__))
print(f"script executing path : {current_directory_path}")

# 작업 디렉터리를 현재 스크립트 파일이 있는 디렉터리로 변경 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

os.system("dir")    # dir : 파일 리스트 출력 시스템 명령어
os.system("pause")  # pause : 사용자가 키를 누를 때까지 일시 중지 

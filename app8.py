#지금까지는, 앱 개발을 할 때, 파일 하나로 코드작성을 모두 했다.

#실무에서는 파일을 여러 개로 쪼개서 개발합니다.
#파일을 나눠서 개발하는 장점.

#1. 유지보수 (중요)!
#2. 협업가능!

import streamlit as st
from app_home import run_home_app  # 1. 파일 쪼개기 / 임포트 먼저
from app_eda import run_eda_app
from app_ml import run_ml_app

def main() :
    st.title('파일 분리 앱')
    menu = ['Home','EDA','ML'] # 메뉴명이 변경될 수 있기에 수정하기 쉽도록 만듦, 여기서 수정하면 아래까지 수정된다.
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home_app()  # 2. 파일 쪼개기 / 파일 안의 함수 호출

    elif choice == menu[1] :
        run_eda_app()

    elif choice == menu[2] : 
        run_ml_app()

if __name__ == '__main__' :
    main()


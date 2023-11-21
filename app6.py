import streamlit as st
import pandas as pd



def main():
    st.title('App6-Testing')
    
    # 텍스트를 입력 받는 방법

    name = st.text_input('이름을 입력하세요')
    
    st.info('제 이름은 ' + name + ' 입니다.')

    # max_chars == 최대 입력 값 / placeholder == 입력 전 투명한 글씨
    st.text_input('이름 입력', max_chars=5, placeholder='기우석') 

    text = st.text_area('메세지를 입력하세요')

    st.text(text)

    # 숫자 입력 받는 방법
    number = st.number_input('출생년도를 입력하세요' , 1900 , 2023)
    st.text(str(number) + '년 출생')

    st.number_input('실수를 입력하세요', -2.00 , 100.00, step=0.01)

    # 날짜 입력 받는 방법
    my_date = st.date_input('약속 날짜 입력')
    
    st.text(my_date)
    
    # "2023년-11월-11일 월요일 입니다." 라고 웹하면에 표시

    st.text(my_date.strftime('%Y년 %m월 %d일 %A 입니다'))

    # 시간 입력 받는 방법

    my_time = st.time_input('약속 시간 선택')

    st.text(my_time.strftime('%H:%M 에 약속시간을 잡았습니다'))

    # 비밀번호 입력받는 방법

    password = st.text_input('비밀번호 입력', type='password')

    print(password)

    # 색깔 입력 방법

    color =  st.color_picker('색을 선택하세요')
    st.text(color)

    

if __name__ == '__main__' :
    main()

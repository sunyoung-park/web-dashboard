import streamlit as st
def main():
    #텍스트를 입력받는 방법
    name = st.text_input('이름을 입력하세요.') 

    st.subheader('제 이름은' + name + '입니다.')

    st.text_input('이름 입력', max_chars=5, placeholder ='홍길동')
    # palceholder = '홍길동'

    text = st.text_area('메세지를 입력하세요')

    st.text(text)

    #숫자 입력 받는 방법
    birth_year = st.number_input('출생년도를 입력하세요', 1900, 2023)

    st.text('제 출생년도는 ' + str(birth_year) + '입니다.')

    st.number_input('실수를 입력하세요.', -2.0, 100.0, step = 0.01) #.0 이라고 쓰면 파이썬은 flot으로 인식

    # 날짜 입력받는 방법

    my_date = st.date_input('약속 날짜 입력')

    print(my_date)
    # st.write(my_date)

    print(type(my_date))
    # st.text(type(my_date))

    # "2023년 11월 12일 화요일입니다. 라고 웹화면에 표시!

    st.subheader(my_date.strftime('%Y년 %m월 %d일 %A 입니다.')) # 데이터 타입을 사람이 원하는 형식으로 쉽게 가공)

    # 시간 입력받는 방법
    my_time = st.time_input('약속 시간 선택')
    print(type(my_time))
    st.text(my_time.strftime('%H:%M에 약속시간을 잡았습니다.'))

    # 비밀번호 입력받는 방법

    passeward =st.text_input('비밀번호 입력', type='password')

    print(passeward)

    #색깔 입력
    color = st.color_picker('색을 선택하세요.')
    st.text(color)
    


if __name__ == '__main__':
    main()

# 여기까지 기본 형식
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title('App4 - 아이리스 꽃의 종류')

    df = pd.read_csv('./data/iris.csv')

    # 버튼 만드는 방법

    if st.button('데이터프레임 보기'):
        st.dataframe(df)

    name = 'Mike'
    if st.button('대문자'):
        st.subheader( name.upper() )

    if st.button('소문자'):
        st.subheader( name.lower() )

    # 라디오 버튼 만드는 방법
    selected = st.radio( '정렬을 선택하세요' , ['오름차순 정렬','내림차순 정렬'] )
    if selected == '오름차순 정렬':
        st.dataframe( df.sort_values('petal_length') )
    elif selected == '내림차순 정렬':
        st.dataframe( df.sort_values('petal_length' , ascending=False))

    #체크박스를 나타내는 방법

    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df)
    else :
        st.error('박스를 체크 해주십시오')
    
    #셀렉트박스 : 여러개 중에서 한개를 선택할 때
    language = ['Pyhton', 'Java','C','PHP','GO']

    my_choice = st.selectbox('좋아하는 언어를 선택하시오', language)

    st.text( '저는 {}언어를 좋아합니다.'.format(my_choice) )

    if my_choice == language[0] or my_choice == language[3] or  my_choice == language[4]:
        st.text('배우기 쉽습니다')

    elif my_choice == language[1] or my_choice == language[-3]:
        st.text('배우기 어렵습니다')

    #멀티셀렉트 : 여러개를 동시에 선택 가능
    
    selected_list = st.multiselect('여러개 선택 가능',df.columns)

    print(selected_list)

    if len(selected_list) != 0:
        st.dataframe(df[selected_list])
    else :
        st.text('')

    # 슬라이더

    age = st.slider('나이' , 0 , 100)

    #st.text('제 나이는 {}살 입니다'.format(age))
    st.text('제 나이는 ' + str(age) + '세 입니다')

    st.slider('데이터',50,200,step=10)   ###step = 증가 단위

    st.slider('나이' , 0 , 100, value=28)    #value = 초기 셋팅 값

    st.slider('데이터',-0.5,2.7,step=0.1,value=1.0)

    with st.expander('상세내용보기') :
        st.text('상세 내용 입니다')



if __name__ == '__main__':
    main()

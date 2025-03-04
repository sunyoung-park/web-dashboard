import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

def main() :
    df = pd.read_csv('./data/lang_data.csv')

    st.dataframe(df)

    # 멀티셀렉트를 만들어서,
    # 컬럼이름 중에서 프로그래밍 언어를 보여주고, 
    # 유저가 선택한 언어만 차트로 표시하려고 한다.***

    print(df.columns[ 1 : ])

    column_menu = df.columns[ 1 : ]

    choice_list = st.multiselect('언어를 선택하세요', column_menu)

    print(choice_list)

    if len(choice_list) != 0 : # choice_list가 0이 아니면
        # 유저가 선택한 언어의 수치를, 차트로 그린다.

        # 먼저, 선택한 컬럼의 데이터프레임을 가져온다.
        df_selected =df[choice_list] # 여러개의 컬럼 액세스와 같음

        # 스트림릿에서 제공하는, 라인차트
        st.line_chart(data=df_selected)

        # 스트림릿에서 제공하는, 영역차트
        st.area_chart(data= df_selected)

        # 스트림릿에서 제공하는, 바차트
        st.bar_chart(df_selected) # 첫번째가 데이터 자리라 data= 빼도 됌

        ### 매우우우우 중요요요
        ### 2017년 4월부터 2018년 3월까지의 데이터를
        ### 바 차트로 나타내시오
        # 1. 조건문 완성
        # print로 확인
        # print((df['Week'] >='2017-04') & (df['Week'] <='2018-03'))

        my_filter = (df['Week'] >='2017-04') & (df['Week'] <='2018-03')

        df_2017_2018=df.loc[my_filter,]

        df3 = df_2017_2018[choice_list]

        st.bar_chart(data= df3)

    df_iris =pd.read_csv('./data/iris.csv')

    # 두 컬럼간의 관계를 표시하되.
    # 종 정보까지 표시하는 방법 (color= 'species')

    chart = alt.Chart(data= df_iris).mark_circle().encode(x='petal_length', y='petal_width', color= 'species')
    st.altair_chart(chart)

    # 위치 정보를 가지고, 지도에 표시하는 방법
    # 스트림릿의 map차트.

    df_location = pd.read_csv('./data/location.csv', index_col=0)
    #인덱스 왼쪽으로 보내기(index_col=0)

    st.dataframe(df_location)

    st.map(data=df_location)       


    ## plotly 차트 그리는 방법

    df_prog = pd.read_csv('./data/prog_languages_data.csv', index_col=0)

    st.dataframe(df_prog)

    # 1. pie 차트
    # names= <-- lable과 같음
    chart2 =  px.pie(df_prog, names='lang', values='Sum', title='각 언어별 파이차트')
    st.plotly_chart(chart2) # plotly chart 출력

    # 2. bar 차트

    # 정렬해서 보여주기

    df_prod_sorted = df_prog.sort_values('Sum',ascending=False)

    chart3 = px.bar(df_prod_sorted, x='lang', y='Sum')

    st.plotly_chart(chart3)


if __name__ == '__main__' :
    main()


import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

def main() :
    st.title('App10-Testing')
    df = pd.read_csv('./data/lang_data.csv')
    st.dataframe(df)

    print(df.columns[ 1 : ] )
    column_menu = df.columns[ 1 : ]
    choice_list = st.multiselect('언어를 선택하세요' , column_menu)

    if len(choice_list) !=0 :
        # 유저가 선택한 언어의 수치를, 차트로 그린다.

        # 먼저, 선택한 컬럼의 데이터프레임을 가져온다.
        df_selected = df[ choice_list ]

        # 스트림릿에서 제공하는, 라인차트
        st.line_chart(data = df_selected)

        # 스트림릿에서 제공하는, 영역차트
        st.area_chart(df_selected)

        # 스트림릿에서 제공하는, 바(Bar) 차트
        st.bar_chart(df_selected)

        ### 2017년 4월부터 2018년 3월까지를 바 차트로 나타내시오###

        my_filter = (df['Week'] >= '2017-04') & (df['Week'] <= '2018-03')
        df_2017_2018 = df.loc[ my_filter , ]
        df3 = df_2017_2018[choice_list]
        st.bar_chart(data = df3)

        # 관계를 표시하는 방법

        df_iris = pd.read_csv('./data/iris.csv')
        chart = alt.Chart(data = df_iris).mark_circle().encode(x='petal_length',y='petal_width',color='species')
        st.altair_chart(chart)

        # 위치정보를 가지고, 지도에 표시하는 방법
        # 스트림릿의 map 차트

        df_location = pd.read_csv('./data/location.csv', index_col=0)
        st.dataframe(df_location)

        st.map(data = df_location)

        ## plotly 차트 그리는 방법

        df_prog = pd.read_csv('./data/prog_languages_data.csv', index_col=0)
        st.dataframe(df_prog)

        # 1. pie 차트
        chart2 = px.pie(data_frame=df_prog, names='lang',values='Sum', title='각 언어별 파이 차트')
        st.plotly_chart(chart2)

        # 2. bar 차트
        chart3 = px.bar(data_frame=df_prog.sort_values('Sum',ascending=False), x='lang',y='Sum')
        st.plotly_chart(chart3)


if __name__ == '__main__' :
    main()
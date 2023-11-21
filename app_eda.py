import streamlit as st
import pandas as pd

def run_eda_app() :
    st.subheader('EDA 화면')
    df = pd.read_csv('./data/iris.csv') # 파일 읽어오기
    st.dataframe(df)
    st.subheader('상관계수')
    st.dataframe(df.corr(numeric_only=True)) # 상관계수 구하기(numeric_only : 숫자로 된 것만 상관계수로 뽑아라)

    # 들여쓰기 맞춤 단축기 : shift + tap
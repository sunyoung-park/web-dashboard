import streamlit as st
import pandas as pd

def main() :
    st.title('Testing My App')

    st.header('Header')
    st.subheader('Subheader')
    st.write('Write')
    st.text('text')
    st.info('Info')
    st.error('Error')
    st.success('Success')
    st.warning("warining")

    df = pd.read_csv('./data/iris.csv')
    st.header('아이리스의 꽃 종류')
    st.dataframe(df)
    st.button('보기')

    name ='Mike'
    if st.button('대문자') :
        st.subheader(name.upper())
    if st.button('소문자') :
        st.subheader(name.lower())


if __name__ == '__main__':
    main()
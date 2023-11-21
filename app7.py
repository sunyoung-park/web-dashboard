import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image
from datetime import datetime

# 1. 이미지 파일 업로드
# 2. CSV 파일 업로드

# 디렉토리(폴더)명과 파일을 알려주면,
# 해당 디렉토리에 파일을 저장해 주는 함수!
def save_uploaded_file(directory,file) :
    # 1. 위의 디렉토리가 있는지 먼저 확인 후,
    #    없으면 디렉토리를 새로 생성하고,
    #    그렇지 않으면 새로 생성할 필요가 없다.
    if not os.path.exists(directory) :
        os.makedirs(directory)

    # 2. 디렉토리가 존재 하니까, 파일을 이 디렉토리 안에 저장한다.
    with open(os.path.join(directory, file.name) , 'wb') as f:
        f.write(file.getbuffer())

    # 3. 파일저장이 성공했으니, 유저한테 웹하면에 보여주자.
    return st.success( directory + '에' + file.name + '파일이 잘 저장 되었습니다.')


# save_uploaded_file('tme' , file)

def main() :
    st.title('파일 업로드 프로젝트')

    #사이드 바 호출
    choice =  st.sidebar.selectbox('메뉴' , ['Image','CSV'])
    if choice == 'Image' :
        st.subheader('이미지 파일 업로드')

        file =  st.file_uploader('이미지 파일을 업로드 하세요',type=['jpg','jpeg','png','jfif'])

        if file is not None :

            # 파일명을 일관성있게 관리할 수 있도록
            # 회사에 들어가면, 파일명 작명 규칙대로 바꿔준다.

            # 현재시간을 조합하여 파일명을 만들면,
            # 유니크하게 파일명을 지을 수 있다.

            current_time = datetime.now()
            # isoformat = 문자열로 만들어줌
            print(current_time.isoformat().replace(':','_').replace('.','_') + '.jpg')
            file.name = current_time.isoformat().replace(':','_').replace('.','_') + '.jpg'

            # 파일이 업로도 되었을때만, 파일 저장하는 코드
            save_uploaded_file('tme', file)

            # 웹 화면에 저장된 이미지파일을 보여주자.
            img = Image.open(file)
            st.image(img)

    elif choice == 'CSV' :
        st.subheader('CSV 파일 업로드')

        file = st.file_uploader('CSV 파일을 업로드 하세요' , type=['csv'])

        if file is not None:

            #파일명을 유니크하게 만든다.
            current_time = datetime.now()

            print(current_time.isoformat().replace(':','_').replace('.','_') + '.csv')

            file.name = current_time.isoformat().replace(':','_').replace('.','_') + '.csv'

            # 파일을 저장한다.
            save_uploaded_file('csv' , file)

            # csv 파일을, 판다스 데이터프레임으로 읽어서 
            # 웹화면에 보여준다.

            df = pd.read_csv(file)

            st.dataframe(df)

            

if __name__ == '__main__' :
    main()
import streamlit as st
import pandas as pd
import numpy as np

# 이미지 / 동영상을 화면에 보여주기
from PIL import Image 

def main() :
    st.title('App5 Testing..')
    my_image = Image.open('./data/image_03.jpg')
    st.image(my_image)
    st.image(my_image, use_column_width= True)

    video_file = open('./data/video1.mp4' , 'rb')
    st.video(video_file)

    
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdzrt4e4KQFd70f0Puk7cnjvsrx3jWFC1TFw&usqp=CAU' , use_column_width= True)

if __name__ == '__main__' :
    main()
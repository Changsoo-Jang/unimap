import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm 

## 한글 폰트 설정
fpath = os.path.join(os.getcwd(), 'Nanum_Gothic/NanumGothic-Bold.ttf')
prop = fm.FontProperties(fname=fpath)
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False

uni_m_f_path = r"4년제일반대학교_등록금_좌표.xlsx"
uni_m_df = pd.read_excel(uni_m_f_path,engine='openpyxl', header=0)
uni_m_df.columns = ['학교명', '주소', 'x', 'y','사이트','등록금액','등급','심볼주소']
filtered_df = uni_m_df
data_df = filtered_df[['학교명','등급','주소']]
uName_list = filtered_df['학교명'].to_list()

st.title(' 전국 4년제 대학 클래스 :red[2024년] 기준 ')
st.dataframe(data_df, use_container_width=True)

fig, ax = plt.subplots()
fig.set_figheight(50)  # 적절한 세로 크기로 설정
fig.set_figwidth(10)   # 가로 크기를 20 인치로 설정
bars = ax.bar(data_df['등급'], data_df['학교명'])

for i, bar in enumerate(bars):
    yval = bar.get_height()
    ax.text(bar.get_x(), yval, s=data_df['학교명'][i] , va='bottom', color='RED', fontsize=9, rotation=45)
    # va: vertical alignment  # ha value for align; 'center', 'right', 'left'

st.markdown('<h1 style="font-size:20px; text-align:center">4년제 일반대학교 클래스 등급별 학교명</h1>', unsafe_allow_html=True)
st.pyplot(fig)
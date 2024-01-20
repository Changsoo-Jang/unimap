# -*- coding:utf-8 -*-
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager as fm 


##################################################################
import streamlit.components.v1 as components

components.html("""
    <style>
    body {
        font-family: 'NanumGothic', sans serif;
    }
    </style>
    """, height=0)

# def unique(list):
#     x = np.array(list)
#     return np.unique(x)

# @st.cache_data
# def fontRegistered():
#     font_dirs = [os.getcwd() + '/zzzzn']
#     font_files = fm.findSystemFonts(fontpaths=font_dirs)

#     for font_file in font_files:
#         fm.fontManager.addfont(font_file)
#     fm._load_fontmanager(try_read_cache=False)
    

# def main():
    
#     fontRegistered()
#     fontNames = [f.name for f in fm.fontManager.ttflist]
#     fontname = st.selectbox("폰트 선택", unique(fontNames))

#     plt.rc('font', family=fontname)
#     tips = sns.load_dataset("tips")
#     fig, ax = plt.subplots()
#     sns.scatterplot(data=tips, x = 'total_bill', y = 'tip', hue='day')
#     ax.set_title("한글 테스트")
#     st.pyplot(fig)
    
#     st.dataframe(tips)
    

# if __name__ == "__main__":
#     main()
# fpath = os.path.join(os.getcwd(), 'NanumGothic.ttf')
# if os.path.isfile(fpath):
#     print('file exist')

# font_name = fm.FontProperties(fname="NanumGothic.ttf").get_name()
# plt.rc('font', family=font_name)
# print(font_name)


# 한글폰트작업
# window의 폰트 위치 -> C:/Windows/Fonts/NGULIM.TTF
# font_name = fm.FontProperties(fname="ngulim.ttf").get_name()
# rc('font', family=font_name)
# plt.rcParams['axes.unicode_minus'] = False

#####################################
# ## 한글 폰트 설정
fpath1 = 'C:\\Windows\\Fonts\\NanumGothic.ttf'
fpath2 = 'C:\\Windows\\Fonts\\NanumGothicBold.ttf'
prop30 = fm.FontProperties(fname=fpath2 , size=30)
prop18 = fm.FontProperties(fname=fpath2 , size=18)
prop9 = fm.FontProperties(fname=fpath1 , size=9)
plt.rcParams["font.family"] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False
print(plt.rcParams["font.family"])
########################################################################
uni_m_f_path = r"4년제일반대학교_등록금_좌표.xlsx"
uni_m_df = pd.read_excel(uni_m_f_path,engine='openpyxl', header=0)
uni_m_df.columns = ['학교명', '주소', 'x', 'y','사이트','등록금액','등급','심볼주소']
filtered_df = uni_m_df
data_df = filtered_df[['학교명','등급','주소']]
uName_list = filtered_df['학교명'].to_list()


########

# plt.plot(range(50), data, 'r')
# plt.title('시간별 가격 추이', fontproperties=fontprop)
# plt.ylabel('주식 가격', fontproperties=fontprop)
# plt.xlabel('시간(분)', fontproperties=fontprop)
# plt.show()

########


st.title('전국 4년제 대학 레벨 :red[2024년] 기준')
# # plt.title('전국 4년제 대학 레벨 [2024년] 기준', fontproperties=prop30)
st.dataframe(data_df, use_container_width=True)

fig, ax = plt.subplots()
fig.set_figheight(50)  # 적절한 세로 크기로 설정
fig.set_figwidth(10)   # 가로 크기를 20 인치로 설정
bars = ax.bar(data_df['등급'], data_df['학교명'])
plt.xlabel('대학 클래스', fontproperties=prop18 )
# custom_css = """
# <style>
#     body {
#         font-family: 'NanumGothic', sans-serif;
#     }
# </style>
# """
# st.markdown(custom_css, unsafe_allow_html=True)

for i, bar in enumerate(bars):
    yval = bar.get_height()
    ax.text(bar.get_x(), yval, s=data_df['학교명'][i], va='bottom', color='RED', fontsize=9, rotation=45, fontproperties=prop9)
    # va: vertical alignment  # ha value for align; 'center', 'right', 'left'

st.markdown('<h1 style="font-size:20px; text-align:center">4년제 일반대학교 클래스 등급별 학교명</h1>', unsafe_allow_html=True)
st.pyplot(fig)


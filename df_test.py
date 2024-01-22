# -*- coding:utf-8 -*-
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager as fm 

##################################################################
# import streamlit.components.v1 as components
# components.html("""
#     <style>
#     body {
#         font-family: 'NanumGothic', sans serif;
#     }
#     </style>
#     """, height=0)

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
    
# if __name__ == "__main__":    ###   모듈이 스크립트로 직접 실행될 때에만 특정 함수를 실행하고자 할 때 이 조건을 사용할 수 있습니다. 이는 해당 모듈이 라이브러리로 사용될 때에는 특정 함수가 실행되지 않도록하고, 스크립트로 실행될 때에만 특정 기능이 작동하도록 할 수 있는 유용한 방법입니다.
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

# import matplotlib as mpl
# print ('버전: ', mpl.__version__)
# print ('설치 위치: ', mpl.__file__)
# print ('설정 위치: ', mpl.get_configdir())
# print ('캐시 위치: ', mpl.get_cachedir())
# print ('설정파일 위치: ', mpl.matplotlib_fname())

#####################################
# ## 한글 폰트 설정  :   그래프 내부에 적용하기 위함
fpath1 = './NanumGothic.ttf'
fpath2 = './NanumGothicBold.ttf'
fpath3 = './NotoSansKR-Regular.ttf'
prop30 = fm.FontProperties(fname=fpath1 , size=30)     
prop18 = fm.FontProperties(fname=fpath1 , size=18)
prop9 = fm.FontProperties(fname=fpath1 , size=9)
prop8 = fm.FontProperties(fname=fpath3 , size=8)
font_name = fm.FontProperties(fname=fpath1, size=10).get_name()

# plt.rc('font', family='NanumGothic')
plt.rcParams["font.family"] = 'NanumGothic'
# plt.rcParams['font.family'] = 'Noto Sans KR'
# plt.rcParams['font.family'] = 'Noto Sans KR', 'sans serif'    ##  전역 한글폰트 설정으로  로컬에서만 적용됨 배포시에는 적용이 안됨,   .streamlit/config.toml  안에    font-family : sans serif ; 산세리프체가 기본이므로   font-family 을 삭제함.
plt.rcParams['axes.unicode_minus'] = False                      ##  한글폰트적용으로 음수값이 깨지는 문제 해결을 위한 코드

########################################################################
uni_m_f_path = r"4년제일반대학교_등록금_좌표.xlsx"
uni_m_df = pd.read_excel(uni_m_f_path,engine='openpyxl', header=0)
uni_m_df.columns = ['학교명', '주소', 'x', 'y','사이트','등록금액','등급','심볼주소']
filtered_df = uni_m_df
data_df = filtered_df[['학교명','등급','주소']]
uName_list = filtered_df['학교명'].to_list()
uGrade_list = filtered_df['등급'].to_list()

st.title('전국 4년제 대학 레벨 :red[2024년] 기준')
st.dataframe(data_df, use_container_width=True)                 ###   True : 기본 확장으로 화면중앙에 어느정도 크기로 보여줌,  False : 매우 좁아짐(True, 에 비해 좁은 화면) 

fig, ax = plt.subplots()                                        # 그래프를 그리기 위한 플롯 객체 생성
fig.set_figheight(50)                                           # 적절한 세로 크기를 50 인치로 설정
fig.set_figwidth(10)                                            # 적절한 가로 크기를 20 인치로 설정

bars = ax.bar(data_df['등급'], data_df['학교명'])    # bottom = 8 : 막대그래프의 시작점을 8로 설정 , 가로축이 등급이고, 세로축이 학교명임
# bars = ax.bar(data_df['등급'], data_df['학교명'], bottom = 8)    # bottom = 8 : 막대그래프의 시작점을 8로 설정 , 가로축이 등급이고, 세로축이 학교명임
# bars = ax.barh(data_df['학교명'], data_df['등급'])             # barh : 가로 막대그래프

## 1번 위치
# x축과 y축 눈금의 위치 설정
## ax.set_xticks(range(len(data_df['등급'])))                   # x축 눈금의 위치를 0부터 1씩 증가하도록 설정  현재는 숫자 값이 아니라서 에러 발생
# ax.set_yticks(range(len(data_df['학교명'])))

## ===============================  한글폰트 적용을 위한 코드 Streamlit  Deploy 과정 에서 한글폰트 안되는 문제 이것으로 해결
# x축과 y축 세부 요소에 한글 폰트 적용    
# ax.set_xticklabels(data_df['등급'], fontproperties=prop9)
ax.set_yticklabels(data_df['학교명'], fontproperties=prop8)
## ===============================  한글폰트 적용을 위한 코드 Streamlit  Deploy 과정 에서 한글폰트 안되는 문제 이것으로 해결

# y축 레이블 설정 한글폰트 적용
# x축 레이블 설정 한글폰트 적용
##   그래프가 여러개 인 경우
# ax.set_xlabel(uGrade_list[0], fontproperties=prop18)
# ax.set_ylabel(uName_list[0], fontproperties=prop18)
##   그래프가 하나인 경우
plt.xlabel('[등급]            ', fontproperties=prop18)         
plt.ylabel('학교명', fontproperties=prop18)                     


for i, bar in enumerate(bars):
    # yval = bar.get_height() * 1.06              #  막대그래프의 높이 1.06배 위치에서 텍스트를 출력함
    yval = bar.get_height()              #  막대그래프의 높이 1.06배 위치에서 텍스트를 출력함
    ax.text(bar.get_x(), yval, s=data_df['학교명'][i], va='bottom', color='RED', rotation=45, fontproperties=prop9)     ## 막대그래프의 x축 위치, y축 위치, s = 텍스트
    # va: vertical alignment                    # ha value for align; 'center', 'right', 'left'

### streamlit run df_test.py 을 실행하기 전 로컬에서 실행되는지 확인하기 위해서 plt.show()를 호출함 실제 실행 화면과는 다름
# plt.show()

## 2번 위치
# ax.set_yticks(range(len(data_df['학교명'])))
# ax.set_yticklabels(data_df['학교명'], fontproperties=prop9)

plt.ylim(0,bar.get_height() * 1.07)  # 상단을 7% 비우기
# plt.ylim(0,bar.get_height())  # 상단을 7% 비우기
st.markdown('<h1 style="font-size:20px; text-align:center">4년제 일반대학교 클래스 등급별 학교명</h1>', unsafe_allow_html=True)
st.pyplot(fig)


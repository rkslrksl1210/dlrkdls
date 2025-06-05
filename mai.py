import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 예시용: 시/구/동/도로명 데이터 (실제로는 csv 등에서 로드)
# 실제 데이터로 바꾸셔야 함
data = {
    '서울특별시': {
        '중구': {
            '명동': ['명동길', '퇴계로', '충무로'],
            '회현동': ['남대문로', '남산순환로']
        },
        '강남구': {
            '역삼동': ['테헤란로', '논현로'],
            '삼성동': ['봉은사로', '영동대로']
        }
    },
    '부산광역시': {
        '해운대구': {
            '우동': ['해운대로', '중동1로']
        }
    }
}

st.title("도로명 선택 기반 교통량 시뮬레이터")

# 1. 시 선택
sido = st.selectbox("시/도 선택", list(data.keys()))
if sido:
    gu_list = list(data[sido].keys())
    gu = st.selectbox("구 선택", gu_list)
    if gu:
        dong_list = list(data[sido][gu].keys())
        dong = st.selectbox("동 선택", dong_list)
        if dong:
            road_list = data[sido][gu][dong]
            road = st.selectbox("도로명 선택", road_list)
            if road:
                st.write(f"선택한 도로명: {sido} {gu} {dong} {road}")

                # 교통량 시뮬레이션 (예시)
                base_traffic = np.array([50, 40, 30, 20, 15, 10, 25, 50, 80, 120, 150, 180, 
                                         200, 220, 230, 210, 180, 160, 140, 100, 80, 60, 55, 50])
                noise = np.random.normal(0, 5, 24)
                traffic = base_traffic + noise
                traffic = np.clip(traffic, 0, None)

                # 그래프 그리기
                hours = [f"{h}:00" for h in range(24)]
                plt.figure(figsize=(10, 4))
                plt.plot(hours, traffic, marker='o')
                plt.title(f"{road} 시간대별 예상 교통량")
                plt.xlabel("시간대")
                plt.ylabel("교통량 (대)")
                plt.xticks(rotation=45)
                plt.grid(True)
                st.pyplot(plt)

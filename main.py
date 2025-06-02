
import streamlit as st
import time

# 페이지 설정
st.set_page_config(
    page_title="🌈 MBTI 직업 추천기",
    page_icon="🧠",
    layout="wide"
)

# 🎨 CSS 애니메이션 (별이 위로 올라가는 효과)
st.markdown("""
    <style>
    .star {
        position: absolute;
        color: #f1c40f;
        animation: floatUp 3s ease-in infinite;
        font-size: 24px;
    }
    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(-200px); opacity: 0; }
    }
    .star-container {
        position: relative;
        height: 0px;
    }
    </style>
    <div class="star-container">
        <div class="star" style="left:10%;">⭐</div>
        <div class="star" style="left:30%;">🌟</div>
        <div class="star" style="left:50%;">✨</div>
        <div class="star" style="left:70%;">🌠</div>
        <div class="star" style="left:90%;">💫</div>
    </div>
""", unsafe_allow_html=True)

# 헤더
st.markdown("<h1 style='text-align: center; color: #6C5CE7;'>✨ MBTI 기반 직업 추천 웹앱 ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #00B894;'>🌟 당신의 성격에 딱 맞는 직업을 찾아보세요! 🌟</h3>", unsafe_allow_html=True)
st.markdown("---")

# MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]
selected_mbti = st.selectbox("🔍 당신의 MBTI를 선택하세요!", mbti_list)

# MBTI 직업 설명 데이터
mbti_jobs = {
    "INTJ": [
        ("🧪 데이터 과학자", "논리적 사고와 분석력을 살려 방대한 데이터를 다루며 통찰을 도출합니다. \n협업보다는 독립적인 환경에서 성과를 내는 데 강합니다. \n트렌드를 예측하고 비즈니스 전략에 기여하는 역할을 합니다."),
        ("🛰️ 전략 컨설턴트", "문제를 구조화하고 효율적인 해결책을 제시하는 데 강한 성향을 보입니다. \n복잡한 프로젝트를 리드하며 장기적인 방향성을 제시합니다. \n다양한 산업의 문제 해결 경험을 쌓을 수 있습니다."),
        ("🧠 AI 연구원", "창의적이고 분석적인 사고를 활용해 인공지능 모델을 개발합니다. \n끊임없이 변화하는 기술 트렌드에 맞춰 학습하고 실험합니다. \n새로운 기술의 경계를 넓히는 데 기여합니다.")
    ],
    "ENFP": [
        ("🎙️ 크리에이터", "에너지 넘치는 성격과 창의성을 발휘해 다양한 콘텐츠를 제작합니다. \n자기표현과 소통을 통해 많은 사람에게 영향을 줄 수 있습니다. \n유튜브, 팟캐스트, 블로그 등 다양한 채널에서 활동할 수 있습니다."),
        ("🌍 NGO 활동가", "세상에 긍정적인 영향을 주고자 하는 열정이 크며, 사회 정의와 인권 문제에 관심이 많습니다. \n사람들과의 협업을 즐기며 변화를 이끌어내는 데 능숙합니다. \n현장에서 직접 변화를 만들어가는 역할을 수행합니다."),
        ("🎬 영화 감독", "풍부한 상상력과 감성을 활용해 감동적인 스토리를 영상으로 구현합니다. \n팀워크와 리더십을 바탕으로 다양한 예술가들과 협업합니다. \n관객의 감정을 움직일 수 있는 작품을 창조합니다.")
    ],
    # (다른 MBTI도 같은 방식으로 추가하면 됨)
}

# 애니메이션 효과
if selected_mbti:
    with st.spinner('✨ 마법처럼 어울리는 직업을 찾고 있어요...'):
        time.sleep(2)

    st.balloons()  # 풍선 효과

    st.markdown(f"## 🎁 {selected_mbti} 유형에게 어울리는 직업은?")
    for job, desc in mbti_jobs.get(selected_mbti, []):
        with st.expander(job):
            st.markdown(desc)

    st.success("🎉 이 직업들이 당신의 성향에 꼭 맞아요! 관심 있는 분야를 깊이 탐구해보세요 🚀")

# 하단 이모지 배경/장식
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 30px;'>🌟💼🎓🧠🎨📊🎤🎬💻🛠️📚</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Made with 💖 by 진로상담봇 | MBTI Career Finder 2025</p>", unsafe_allow_html=True)

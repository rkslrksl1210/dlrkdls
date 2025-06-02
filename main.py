
import streamlit as st

st.set_page_config(
    page_title="🌈 MBTI 직업 추천기",
    page_icon="🧠",
    layout="wide"
)

# 🌟 타이틀
st.markdown("<h1 style='text-align: center; color: #6C5CE7;'>✨ MBTI 기반 직업 추천 웹앱 ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #00B894;'>당신의 성격에 꼭 맞는 직업을 찾아보세요! 😄</h3>", unsafe_allow_html=True)
st.markdown("---")

# 🧠 MBTI 선택
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("🔍 당신의 MBTI를 선택하세요!", mbti_list)

# 💼 직업 추천 사전
mbti_jobs = {
    "INTJ": ["🧪 데이터 과학자", "🛰️ 전략 컨설턴트", "🧠 AI 연구원"],
    "INTP": ["💡 발명가", "📊 빅데이터 분석가", "🧬 연구 과학자"],
    "ENTJ": ["📈 CEO", "🏛️ 경영 컨설턴트", "⚖️ 변호사"],
    "ENTP": ["🎤 창업가", "📢 마케팅 디렉터", "🎮 게임 기획자"],
    "INFJ": ["🧘 심리상담가", "📚 작가", "🎨 예술가"],
    "INFP": ["📝 시인", "🎼 작곡가", "🎭 드라마 작가"],
    "ENFJ": ["🎓 교육자", "🤝 HR 매니저", "🎤 퍼실리테이터"],
    "ENFP": ["🎙️ 크리에이터", "🌍 NGO 활동가", "🎬 영화 감독"],
    "ISTJ": ["🔍 감사 전문가", "💼 회계사", "📚 사서"],
    "ISFJ": ["🏥 간호사", "📋 행정 직원", "🏛️ 복지사"],
    "ESTJ": ["🏗️ 프로젝트 매니저", "🗃️ 조직 관리자", "🧾 세무사"],
    "ESFJ": ["👩‍🏫 교사", "🎯 고객 서비스 관리자", "🧑‍🍳 식음료 매니저"],
    "ISTP": ["🛠️ 엔지니어", "🛩️ 항공정비사", "🚗 정비공"],
    "ISFP": ["🎨 디자이너", "📷 사진작가", "🎻 연주가"],
    "ESTP": ["🎢 이벤트 플래너", "🚀 세일즈", "🏎️ 레이서"],
    "ESFP": ["🎤 연예인", "🎭 배우", "🎉 파티 플래너"]
}

# 💫 추천 출력
if selected_mbti:
    st.markdown(f"## 🎁 당신에게 어울리는 직업은?")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

    st.markdown("---")
    st.success("🎉 나와 어울리는 직업을 찾았나요? 다음 단계는 그 꿈을 향해 나아가는 거예요! 🚀")

# 🎨 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Made with 💖 by 진로상담봇 | MBTI Career Finder 2025</p>", unsafe_allow_html=True)

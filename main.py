import streamlit as st

# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 여행코스 추천기",
    page_icon="🧳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🎉 타이틀
st.title("🧭 MBTI 여행코스 추천기")
st.subheader("당신의 성격에 딱 맞는 여행지는 어디일까요? ✈️")

# 📌 MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 💡 사용자 MBTI 선택
user_mbti = st.selectbox("당신의 MBTI를 선택해주세요 💬", mbti_list)

# 🚀 추천 코스 사전
recommendations = {
    "INTJ": ("📚 교토, 일본", "고요한 절과 사색의 산책길에서 내면을 돌아보는 여행"),
    "INTP": ("🧪 베를린, 독일", "예술과 철학, 역사적 깊이를 만나는 탐구 여행"),
    "ENTJ": ("🌆 뉴욕, 미국", "도시의 에너지를 흡수하며 미래를 설계하는 리더의 여행"),
    "ENTP": ("🎭 바르셀로나, 스페인", "열정 넘치는 거리예술과 혁신적인 건축 투어"),
    "INFJ": ("🌲 핀란드 라플란드", "오로라 아래에서 마음을 정화하는 명상여행"),
    "INFP": ("🍀 아일랜드 골웨이", "감성 충만한 시골길과 동화 속 같은 여행"),
    "ENFJ": ("🎡 런던, 영국", "사람과 연결되며 문화와 가치를 나누는 여행"),
    "ENFP": ("🎨 암스테르담, 네덜란드", "자유로운 분위기 속에서 영감을 받는 창조 여행"),
    "ISTJ": ("🏰 프라하, 체코", "질서정연한 거리와 역사 탐방 루트"),
    "IS

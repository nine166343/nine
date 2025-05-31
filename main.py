import streamlit as st

# 💅 페이지 설정
st.set_page_config(
    page_title="여름 헤어스타일 추천기",
    page_icon="🌞",
    layout="centered"
)

# 🎀 타이틀
st.title("☀️ 올여름, 나에게 어울리는 헤어스타일은?")
st.subheader("얼굴형, 머리 길이, 분위기를 골라보면 취향 저격 헤어스타일을 추천해드릴게요 💇‍♀️✨")

st.markdown("---")

# 🪞 얼굴형 선택
face_shape = st.selectbox("🧡 당신의 얼굴형은?", [
    "계란형 (oval)", 
    "둥근형 (round)", 
    "각진형 (square)", 
    "긴 얼굴형 (long)", 
    "하트형 (heart)"
])

# ✂️ 머리 길이 선택
hair_length = st.radio("💇‍♀️ 원하는 머리 길이는?", [
    "쇼트", 
    "미디엄", 
    "롱"
])

# 🌈 스타일 무드 선택
style_mood = st.selectbox("🌸 원하는 분위기는?", [
    "청순하고 내추럴 🍃",
    "상큼하고 발랄하게 🍊",
    "시크하고 도시적 ✨",
    "귀엽고 러블리하게 🍓",
    "로맨틱하고 부드럽게 🌷"
])

st.markdown("---")

# 🎨 추천 로직
with st.spinner("✨ 당신만의 썸머 스타일을 찾는 중..."):
    
    # 기본값 설정
    hairstyle = "기본 스타일"
    vibe = "기본 분위기"
    tip = "여름철, 두피 관리도 함께 해주세요 🌿"

    # 얼굴형별 추천 조합 (심화)
    if face_shape == "계란형 (oval)":
        hairstyle = "시스루 뱅 + 내추럴 웨이브"
        tip = "어떤 스타일이든 잘 어울려요! 특히 레이어드컷 추천 💫"
    elif face_shape == "둥근형 (round)":
        hairstyle = "C컬 보브컷 or 턱 아래 기장 레이어드"
        tip = "볼륨을 아래쪽으로 주어 얼굴을 길어보이게 해줘요 📏"
    elif face_shape == "각진형 (square)":
        hairstyle = "사이드 뱅 + 부드러운 S컬"
        tip = "턱 라인을 감싸주며 부드러운 인상 연출 💖"
    elif face_shape == "긴 얼굴형 (long)":
        hairstyle = "풀뱅 + 롱 웨이브"
        tip = "이마를 덮어 비율을 예쁘게 보정해요 🎀"
    elif face_shape == "하트형 (heart)":
        hairstyle = "중단발 + 애교머리 + C컬"
        tip = "광대 옆 볼륨으로 얼굴 밸런스 잡아줘요 💡"

    # 길이와 분위기에 따라 추가 설명 조합
    vibe = f"{style_mood}에 어울리는 {hair_length} 스타일이에요!"

    st.success("✨ 스타일 분석 완료!")
    st.markdown(f"### 💇 추천 스타일: {hairstyle}")
    st.markdown(f"#### 🌈 스타일 무드: {vibe}")
    st.markdown(f"📝 스타일 팁: {tip}")
    st.balloons()

st.markdown("---")
st.caption("💡 스타일은 유행보다 '나에게 어울리는 것'이 제일 중요해요! 자신감을 잃지 마세요 💕")

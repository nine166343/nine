import streamlit as st

# 🖼️ 페이지 설정
st.set_page_config(
    page_title="내향·외향 연애궁합 추천기",
    page_icon="💞",
    layout="centered"
)

# 🎀 타이틀
st.title("💖 내향형 vs 외향형 연애 궁합 추천기")
st.subheader("당신의 성향에 딱 맞는 연애 스타일을 알아보세요 💌")

# ☕ 성격 선택
personality = st.radio("당신은 어떤 성향인가요?", ["🧘 내향형 (I)", "🎉 외향형 (E)"])

# 📖 추천 내용 사전
recommendations = {
    "🧘 내향형 (I)": {
        "궁합": "🎉 외향형 (E) 파트너와 환상의 케미!",
        "설명": "내향형은 조용하고 깊은 대화를 즐기며, 외향형은 에너지와 활동적인 스타일로 서로에게 활력을 줄 수 있어요. 서로의 부족한 점을 채워주는 최고의 조합! 💫"
    },
    "🎉 외향형 (E)": {
        "궁합": "🧘 내향형 (I) 파트너와의 균형잡힌 사랑!",
        "설명": "외향형은 사교적이고 활동적인 반면, 내향형은 감정적 안정과 배려가 깊어요. 둘이 만나면 세상을 함께 바라보는 시선이 넓어져요. 🌈"
    }
}

# 🥰 결과 출력
if personality:
    with st.spinner("사랑의 궁합을 계산 중입니다... 💘"):
        st.success("운명의 연애 스타일은?! 💫")
        st.markdown(f"## {recommendations[personality]['궁합']}")
        st.write(f"📝 {recommendations[personality]['설명']}")
        st.balloons()  # 🎈 로맨틱 풍선 효과!


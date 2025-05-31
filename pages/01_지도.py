import streamlit as st
import pandas as pd
import pydeck as pdk

# 앱 기본 설정
st.set_page_config(page_title="🇰🇷 한국 인기 여행지 TOP 10", page_icon="🧳", layout="centered")

st.title("🧳 한국인이 사랑하는 🇰🇷 여행지 TOP 10")
st.markdown("""
### ✨ 어디로 떠나볼까요?
한국에서 가장 사랑받는 여행지 10곳을 소개해요!  
감성 가득한 여행지 정보와 함께, 지도에서 위치도 확인해보세요 💗
""")

# 여행지 데이터 (위도, 경도, 간단 설명 포함)
travel_data = pd.DataFrame({
    '여행지': [
        "제주도 🌴", "부산 해운대 🌊", "경주 역사 유적지 🏯", "강릉 경포대 🏖️", "서울 경복궁 🏰",
        "속초 설악산 ⛰️", "전주 한옥마을 🏡", "남해 독일마을 🇩🇪", "양양 서핑 해변 🏄", "담양 죽녹원 🎋"
    ],
    '위도': [33.4996, 35.1587, 35.8562, 37.7960, 37.5796, 38.1194, 35.8144, 34.8389, 38.0702, 35.3222],
    '경도': [126.5312, 129.1604, 129.2247, 128.8889, 126.9770, 128.4656, 127.1532, 128.0604, 128.6282, 126.6930],
    '설명': [
        "푸른 바다와 자연이 어우러진 섬, 국내 여행 1순위! 🍊",
        "활기찬 해변과 야경이 매력적인 도시 💙",
        "천년 고도, 역사와 전통의 낭만이 있는 도시 📜",
        "해돋이 명소와 감성 카페가 어우러진 바다 도시 ☕",
        "고궁의 고요함 속에서 힐링하는 시간 🕊️",
        "사계절 내내 아름다운 산과 케이블카 🌄",
        "전통 한옥의 멋과 먹거리가 풍부한 도시 🍲",
        "독일 감성이 가득한 남쪽 바닷마을 🏘️",
        "서퍼들의 천국! 자유로운 바다 🌊",
        "대나무 숲길이 힐링을 선물해요 🎐"
    ]
})

# 여행지 선택
selected = st.selectbox("🔍 가고 싶은 여행지를 골라보세요!", travel_data['여행지'])

# 선택한 여행지 정보 표시
row = travel_data[travel_data['여행지'] == selected].iloc[0]
st.markdown(f"### 📍 {row['여행지']}")
st.markdown(f"{row['설명']}")

# 지도에 핀 표시
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=row['위도'],
        longitude=row['경도'],
        zoom=11,
        pitch=30,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=travel_data[travel_data['여행지'] == selected],
            get_position='[경도, 위도]',
            get_color='[255, 105, 180, 160]',
            get_radius=500,
        ),
    ],
))

# 전체 지도 보기 옵션
if st.checkbox("🗺️ TOP 10 전체 여행지를 지도에서 보기"):
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=36.5,
            longitude=127.9,
            zoom=6,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=travel_data,
                get_position='[경도, 위도]',
                get_color='[135, 206, 250, 200]',
                get_radius=700,
            ),
        ],
    ))

# 마무리
st.markdown("---")
st.markdown("✈️ 어딜 가도 멋진 한국 여행지들! 당신의 다음 여행은 어디인가요? 💕")
st.caption("Made with ❤️ by ChatGPT")

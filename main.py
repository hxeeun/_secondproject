import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="🎮 가위바위보 게임 🥳",
    page_icon="✂️🪨📄",
    layout="centered"
)

# 스타일 적용 (배경, 글자, 버튼 등)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1 {
    color: #fff;
    text-shadow: 2px 2px 4px #00000088;
    font-size: 3.5rem;
    text-align: center;
}
.game-result {
    font-size: 2rem;
    font-weight: bold;
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
    text-align: center;
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
}
.win {
    background: #4CAF50;
    color: white;
}
.lose {
    background: #f44336;
    color: white;
}
.draw {
    background: #FFC107;
    color: white;
}
.stButton > button {
    font-size: 2rem !important;
    padding: 15px 25px !important;
    margin: 10px !important;
    border-radius: 15px !important;
    border: none !important;
    cursor: pointer !important;
    box-shadow: 2px 2px 10px #00000033 !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    transform: scale(1.1) !important;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.title("🎮 가위바위보 게임에 오신 것을 환영합니다! 🥳")

st.write("👇 아래 버튼 중 하나를 눌러서 당신의 선택을 해주세요! 👇")

# 선택지
choices = ["가위", "바위", "보"]
emoji_map = {"가위":"✂️", "바위":"🪨", "보":"📄"}

# 사용자 선택 초기값 None
user_choice = None

# 버튼 3개 가로배치
col1, col2, col3 = st.columns(3)

with col1:
    if st.button(f"{emoji_map['가위']} 가위"):
        user_choice = "가위"
with col2:
    if st.button(f"{emoji_map['바위']} 바위"):
        user_choice = "바위"
with col3:
    if st.button(f"{emoji_map['보']} 보"):
        user_choice = "보"

# 게임 결과 처리
if user_choice:
    comp_choice = random.choice(choices)

    st.markdown(f"### 당신의 선택: {emoji_map[user_choice]} {user_choice}")
    st.markdow

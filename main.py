import streamlit as st
import random

st.set_page_config(
    page_title="🎮 가위바위보 게임 🥳",
    page_icon="✂️🪨📄",
    layout="centered"
)

# 간단 스타일
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1 {
    color: white;
    text-shadow: 2px 2px 4px black;
    text-align: center;
}
.result {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
}
.win {
    color: green;
}
.lose {
    color: red;
}
.draw {
    color: orange;
}
.stButton > button {
    font-size: 24px !important;
    padding: 15px 30px !important;
    margin: 10px !important;
    border-radius: 15px !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    transform: scale(1.1) !important;
    transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 가위바위보 게임 🥳")

st.write("아래 버튼 중 하나를 선택하세요!")

choices = ["가위", "바위", "보"]
emoji_map = {"가위":"✂️", "바위":"🪨", "보":"📄"}

user_choice = None

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

if user_choice:
    comp_choice = random.choice(choices)

    st.write(f"**당신의 선택:** {emoji_map[user_choice]} {user_choice}")
    st.write(f"**컴퓨터의 선택:** {emoji_map[comp_choice]} {comp_choice}")

    if user_choice == comp_choice:
        st.markdown('<p class="result draw">😐 비겼어요! 다시 해보세요! 😐</p>', unsafe_allow_html=True)
    elif (user_choice == "가위" and comp_choice == "보") or \
         (user_choice == "바위" and comp_choice == "가위") or \

import streamlit as st
import random

st.set_page_config(page_title="🎮 가위바위보 게임 🥳", page_icon="✂️🪨📄", layout="centered")

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
}
.game-result {
    font-size: 2rem;
    font-weight: bold;
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
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
.choice-btn {
    font-size: 2rem;
    padding: 15px 25px;
    margin: 10px;
    border-radius: 15px;
    border: none;
    cursor: pointer;
    box-shadow: 2px 2px 10px #00000033;
    transition: all 0.3s ease;
}
.choice-btn:hover {
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 가위바위보 게임에 오신 것을 환영합니다! 🥳")

st.write("👇 아래 버튼 중 하나를 눌러서 당신의 선택을 해주세요! 👇")

choices = {
    "✂️ 가위": "가위",
    "🪨 바위": "바위",
    "📄 보": "보"
}

user_choice = None

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✂️ 가위", key="scissors"):
        user_choice = "가위"
with col2:
    if st.button("🪨 바위", key="rock"):
        user_choice = "바위"
with col3:
    if st.button("📄 보", key="paper"):
        user_choice = "보"

if user_choice:
    comp_choice = random.choice(["가위", "바위", "보"])

    st.markdown(f"### 당신의 선택: {user_choice}")
    st.markdown(f"### 컴퓨터의 선택: {comp_choice}")

    if user_choice == comp_choice:
        st.markdown(f'<div class="game-result draw">😐 비겼어요! 다시 해보세요! 😐</div>', unsafe_allow_html

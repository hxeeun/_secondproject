import streamlit as st
import random

st.set_page_config(
    page_title="🎉🔥화려한 가위바위보 게임🔥🎉",
    page_icon="✂️🪨📄",
    layout="centered"
)

# CSS 꾸미기 (화려한 배경 + 반짝이는 효과 + 커다란 버튼 + 결과 강조)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

body {
    background: radial-gradient(circle at top left, #ff9a9a, #ffd6d6);
    font-family: 'Orbitron', sans-serif;
    color: #222;
}
h1 {
    font-size: 4rem;
    color: #e60073;
    text-shadow: 0 0 10px #ff0080, 0 0 20px #ff33a6, 0 0 30px #ff66c1;
    text-align: center;
    margin-bottom: 30px;
}
.stButton > button {
    font-size: 3rem !important;
    padding: 25px 40px !important;
    margin: 15px !important;
    border-radius: 30px !important;
    border: 3px solid #ff3399 !important;
    background: linear-gradient(45deg, #ff66cc, #ff3399);
    color: white !important;
    font-weight: 900 !important;
    cursor: pointer !important;
    box-shadow: 0 0 15px #ff3399;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(45deg, #ff3399, #ff66cc);
    box-shadow: 0 0 25px #ff66cc;
    transform: scale(1.15);
}
.result {
    font-size: 2.5rem;
    font-weight: 900;
    margin-top: 30px;
    text-align: center;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 25px #ff3399;
    color: white;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
}
.win {
    background: #ff33aa;
    text-shadow: 0 0 15px #ff99cc;
}
.lose {
    background: #ff0066;
    text-shadow: 0 0 15px #cc0055;
}
.draw {
    background: #ff99cc;
    color: #550033;
    text-shadow: 0 0 10px #cc6699;
}
.choices {
    font-size: 3rem;
    text-align: center;
    margin-top: 20px;
    user-select: none;
}
footer {
    text-align: center;
    margin-top: 60px;
    color: #ff3399;
    font-weight: bold;
    font-size: 1rem;
    text-shadow: 0 0 10px #ff66cc;
}
</style>
""", unsafe_allow_html=True)

st.title("🎉🔥 화려한 가위바위보 게임 🔥🎉")

st.write("👇 아래 버튼을 눌러 당신의 선택을 해주세요! 👇")

choices = ["가위", "바위", "보"]
emoji_map = {"가위": "✂️", "바위": "🪨", "보": "📄"}

user_choice = None

col1, col2, col3 = st.columns(3)
with col1:
    if st.button(f"✂️ 가위 ✂️"):
        user_choice = "가위"
with col2:
    if st.button(f"🪨 바위 🪨"):
        user_choice = "바위"
with col3:
    if st.button(f"📄 보 📄"):
        user_choice = "보"

if user_choice:
    comp_choice = random.choice(choices)

    st.markdown(
        f'<div class="choices">👤 당신: {emoji_map[user_choice]}  VS  🤖 컴퓨터: {emoji_map[comp_choice]}</div>',
        unsafe_allow_html=True,
    )

    if user_choice == comp_choice:
        st.markdown(
            '<div class="result draw">🤝 비겼어요! 다시 도전해보세요! 🤝</div>',
            unsafe_allow_html=True,
        )
    elif (user_choice == "가위" and comp_choice == "보") or \
         (user_choice == "바위" and comp_choice == "가위") or \
         (user_choice == "보" and comp_choice == "바위"):
        st.markdown(
            '<div class="result win">🎉 축하합니다! 당신이 이겼어요! 🎉</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="result lose">😭 아쉽지만 컴퓨터가 이겼어요! 다시 도전! 😭</div>',
            unsafe_allow_html=True,
        )
else:
    st.info("아래 버튼에서 선택해 주세요!")

st.markdown("---")

st.markdown('<footer>Made with ❤️ by ChatGPT</footer>', unsafe_allow_html=True)

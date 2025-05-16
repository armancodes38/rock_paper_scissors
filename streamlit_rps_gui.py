import streamlit as st
import random
import time

# Title
st.set_page_config(page_title="Rock Paper Scissors", layout="centered")
st.title("🎮 Rock Paper Scissors")

# Initialize session state
if "your_score" not in st.session_state:
    st.session_state.your_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "result_text" not in st.session_state:
    st.session_state.result_text = ""

# Emojis for choices
emoji_choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Scoreboard
st.markdown(f"### 🧑 You: {st.session_state.your_score} &nbsp;&nbsp;&nbsp;&nbsp; 🤖 Computer: {st.session_state.computer_score}")

# Game logic
def play_game(user_choice):
    youDict = {"Rock": 1, "Paper": -1, "Scissors": 0}
    reverseDict = {1: "🪨 Rock", -1: "📄 Paper", 0: "✂️ Scissors"}

    computer = random.choice([-1, 0, 1])
    you = youDict[user_choice]

    if computer == you:
        result = "🤝 It's a draw!"
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        result = "🎉 You win!"
        st.session_state.your_score += 1
    else:
        result = "😢 You lose!"
        st.session_state.computer_score += 1

    user_text = reverseDict[you]
    comp_text = reverseDict[computer]
    st.session_state.result_text = f"You chose: {user_text} \nComputer chose: {comp_text} \n\n{result}"

# Button layout
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🪨", use_container_width=True):
        play_game("Rock")
with col2:
    if st.button("📄", use_container_width=True):
        play_game("Paper")
with col3:
    if st.button("✂️", use_container_width=True):
        play_game("Scissors")

# Result display (animated simulation)
if st.session_state.result_text:
    with st.container():
        st.markdown("### ⏱️ Result:")
        placeholder = st.empty()
        for i in range(1, len(st.session_state.result_text) + 1):
            placeholder.markdown(f"```{st.session_state.result_text[:i]}```")
            time.sleep(0.01)

# Reset button
st.markdown("---")
if st.button("🔄 Reset Scores"):
    st.session_state.your_score = 0
    st.session_state.computer_score = 0
    st.session_state.result_text = ""
    st.experimental_rerun()

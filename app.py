import random
import streamlit as st
import logic_utils as utils

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

def reset_game(difficulty_name):
    low, high = utils.get_range_for_difficulty(difficulty_name)
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.current_difficulty = difficulty_name
    # We keep the total session score unless it's a completely fresh start, 
    # but for a "New Game" button, usually we just want to play again.
    # Optionally reset score: st.session_state.score = 0

st.title("🎮 Game Glitch Investigator")
st.caption("Investigate and fix the glitches in this AI-generated game.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]
low, high = utils.get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# Initialize state
if "score" not in st.session_state:
    st.session_state.score = 0

if "current_difficulty" not in st.session_state:
    reset_game(difficulty)

# Detect difficulty change and reset if needed
if st.session_state.current_difficulty != difficulty:
    reset_game(difficulty)
    st.info(f"Difficulty changed to {difficulty}. New game started!")

st.subheader("Make a guess")

attempts_left = attempt_limit - st.session_state.attempts
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {max(0, attempts_left)}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

# Using a unique key for the text input is good, but we want it to clear on reset.
# Streamlit clears components when the key changes or on rerun if not managed.
raw_guess = st.text_input(
    "Enter your guess:",
    key="guess_input"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀", disabled=(st.session_state.status != "playing"))
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    reset_game(difficulty)
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success(f"You won! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
    else:
        st.error(f"Game over! The secret was {st.session_state.secret}. Final score: {st.session_state.score}")
    st.info("Click 'New Game' to play again.")
    st.stop()

if submit:
    if not raw_guess:
        st.warning("Please enter a number first!")
    else:
        # FIX: Used Copilot Agent to refactor this logic from app.py to logic_utils.py
        ok, guess_int, err = utils.parse_guess(raw_guess)

        if not ok:
            st.error(err)
        else:
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)

            # FIXME: Logic breaks here - the check_guess function was returning incorrect hints (Higher/Lower)
            # FIX: Used Copilot to separate logic from UI. Refactored check_guess to logic_utils.py
            outcome, message = utils.check_guess(guess_int, st.session_state.secret)

            if show_hint:
                if outcome != "Win":
                    st.warning(message)

            st.session_state.score = utils.update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
                difficulty=difficulty
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.success(f"🎉 Correct! You found it in {st.session_state.attempts} attempts.")
                st.rerun()
            elif st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error("❌ Out of attempts!")
                st.rerun()

st.divider()
st.caption("Glitch Investigator Mode: Active")

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")

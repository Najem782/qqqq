import streamlit as st
import random

st.title("I have an important question for you...")
st.write("Will you be my Valentine? 💖")

# Define CSS to position the "No" button dynamically
button_style = """
<style>
    div[data-testid="stButton"] {
        position: absolute;
        left: {}%;
        top: {}%;
    }
</style>
"""

# Initialize session state for button position if not set
if "no_x" not in st.session_state:
    st.session_state.no_x = 50  # Center horizontally
    st.session_state.no_y = 50  # Center vertically

# Display Yes Button
yes_clicked = st.button("Yes 💘")
if yes_clicked:
    st.success("sahiit bb! 😘")

# Apply the CSS for dynamic button positioning
st.markdown(button_style.format(st.session_state.no_x, st.session_state.no_y), unsafe_allow_html=True)

# Display No Button
no_clicked = st.button("No 💔", key="no_button")
if no_clicked:
    # Move "No" button to a new random position
    st.session_state.no_x = random.randint(10, 80)  # Avoid edges
    st.session_state.no_y = random.randint(10, 80)
    st.rerun()

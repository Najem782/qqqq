import streamlit as st
import random

st.title("Will you be my Valentine? 💖")
st.write("I have an important question for you...")

# Initialize session state for button position if not set
if "no_x" not in st.session_state:
    st.session_state.no_x = 0.5
    st.session_state.no_y = 0.5

col1, col2, col3 = st.columns([3, 1, 3])

with col1:
    yes_clicked = st.button("Yes 💘")
    if yes_clicked:
        st.success("sahiit bb! 😘")

with col3:
    no_clicked = st.button("No 💔", key="no_button", help="Try clicking me!")
    
    if no_clicked:
        # Move button to a random position
        st.session_state.no_x = random.uniform(0.2, 0.8)
        st.session_state.no_y = random.uniform(0.2, 0.8)
        st.experimental_rerun()

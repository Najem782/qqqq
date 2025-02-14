import streamlit as st
import random

st.title("I have an important question for you...")
st.write("Will you be my Valentine? 💖")

# Initialize session state for button position if not set
if "no_x" not in st.session_state:
    st.session_state.no_x = 50  # Initial horizontal position
    st.session_state.no_y = 50  # Initial vertical position
if "last_x" not in st.session_state:
    st.session_state.last_x = 50
    st.session_state.last_y = 50
if "choice_made" not in st.session_state:
    st.session_state.choice_made = ""

# Display Yes Button
yes_clicked = st.button("Yes 💘")
if yes_clicked:
    st.success("sahiit bb! 😘")
    st.write("chneya theb naamlou nhaar el valentine")
    
    last_placeholder = st.empty()
    with last_placeholder.container():
        col1, col2, col3 = st.columns([3, 3, 3])
        
        with col1:
            if st.button("njibou sghiir", key="choice1"):
                st.session_state.choice_made = "ellila tbeet hdheeya bb! 😍"
                st.rerun()
        with col2:
            if st.button("i eat you", key="choice2"):
                st.session_state.choice_made = "ellila tbeet hdheeya bb! 😍"
                st.rerun()
        with col3:
            if st.button("nakraw sap", key="last_choice"):
                st.session_state.last_x = random.randint(10, 80)
                st.session_state.last_y = random.randint(10, 80)
                st.rerun()
    
if st.session_state.choice_made:
    st.success("ellila tbeet hdheeya bb! 😍")

# Create a placeholder to update "No" button dynamically
no_placeholder = st.empty()

# Generate a dynamic No button at a new position
with no_placeholder.container():
    col1, col2, col3 = st.columns([st.session_state.no_x, 1, 100 - st.session_state.no_x])
    
    with col2:
        no_clicked = st.button("No 💔", key="no_button")

# If "No" is clicked, move it to a random position
if "no_button" in st.session_state and st.session_state.no_button:
    st.session_state.no_x = random.randint(10, 80)  # Avoid edges
    st.session_state.no_y = random.randint(10, 80)
    st.rerun()

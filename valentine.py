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

# Display Yes Button
yes_clicked = st.button("Yes 💘")
if yes_clicked:
    st.success("sahiit bb! 😘")
    st.write("chneya theb naamlou nhaar el valentine")
    
    last_placeholder = st.empty()
    with last_placeholder.container():
        col1, col2, col3 = st.columns([st.session_state.last_x, 1, 100 - st.session_state.last_x])
        
        with col2:
            choice = st.radio("Choose one:", ["njibou sghiir", "i eat you", "nakraw sap"], key="valentine_choice")
    
    if choice == "nakraw sap":
        st.session_state.last_x = random.randint(10, 80)
        st.session_state.last_y = random.randint(10, 80)
        st.rerun()

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

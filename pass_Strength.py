import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        feedback.append("Use special characters (!@#$%^&* etc).")

    # Determine password strength
    if strength_score <= 2:
        strength = "Weak ❌"
        color = "red"
    elif strength_score == 3 or strength_score == 4:
        strength = "Moderate ⚠️"
        color = "orange"
    else:
        strength = "Strong ✅"
        color = "green"

    return strength, color, feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Input field for password
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, feedback = check_password_strength(password)

    # Show strength result
    st.markdown(f"### Strength: <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)

    # Show improvement suggestions
    if feedback:
        st.subheader("⚡ Tips to Improve Password Strength:")
        for tip in feedback:
            st.write(f"✅ {tip}")
    else:
        st.success("Your password is strong! 💪")

# Footer
st.markdown("---")
st.markdown("Developed by **Muhammad Tabish Ali** 🚀")

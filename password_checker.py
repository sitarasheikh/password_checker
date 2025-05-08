# import re
# import random

# # List of common weak passwords
# blacklist = ["password", "123456", "qwerty", "letmein", "password123", "admin", "welcome", "abc123"]

# # Function to check password strength
# def check_password_strength(password):
#     score = 0

#     # Check if the password is blacklisted
#     if password.lower() in blacklist:
#         print("❌ This password is too common. Please choose a more secure one.")
#         return

#     # Length check
#     if len(password) >= 8:
#         score += 1
#     else:
#         print("❌ Password should be at least 8 characters long.")

#     # Uppercase and lowercase letters
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         print("❌ Include both uppercase and lowercase letters.")

#     # Digit check
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         print("❌ Add at least one number (0-9).")

#     # Special character check
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         print("❌ Include at least one special character (!@#$%^&*).")

#     # Final rating
#     if score == 4:
#         print("✅ Strong Password!")
#     elif score == 3:
#         print("⚠️ Moderate Password - Consider adding more security features.")
#     else:
#         print("❌ Weak Password - Improve it using the suggestions above.")

# # Function to generate a strong password
# def generate_strong_password(length=12):
#     upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lower = "abcdefghijklmnopqrstuvwxyz"
#     digits = "0123456789"
#     special = "!@#$%^&*"

#     # Ensure at least one from each group
#     password = [
#         random.choice(upper),
#         random.choice(lower),
#         random.choice(digits),
#         random.choice(special)
#     ]

#     # Fill remaining length with mixed characters
#     all_chars = upper + lower + digits + special
#     while len(password) < length:
#         password.append(random.choice(all_chars))

#     random.shuffle(password)
#     return ''.join(password)

# # === Main Program ===
# print("🔐 Password Strength Checker 🔐")
# password = input("Enter your password: ")
# check_password_strength(password)

# # Offer to generate a strong password if current one is weak
# choice = input("Do you want a suggestion for a strong password? (yes/no): ").lower()
# if choice == "yes":
#     strong_pass = generate_strong_password()
#     print("💡 Suggested Strong Password:", strong_pass)

import streamlit as st
import re
import random

# Blacklisted passwords
blacklist = ["password", "123456", "qwerty", "letmein", "password123", "admin", "welcome", "abc123"]

# Password strength checker
def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ This password is too common. Please choose a more secure one.")
        return feedback, score

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return feedback, score

# Password generator
def generate_strong_password(length=12):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*"

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    all_chars = upper + lower + digits + special
    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

# Streamlit UI
st.title("🔐 Password Strength Checker")

password_input = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password_input:
        feedback, score = check_password_strength(password_input)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
            for item in feedback:
                st.write(item)
    else:
        st.warning("⚠️ Please enter a password to check.")

if st.button("Suggest a Strong Password"):
    strong_pass = generate_strong_password()
    st.info("💡 Suggested Strong Password:")
    st.code(strong_pass, language='text')

import streamlit as st
import secrets
import string

st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

st.title("🔑 Password Generator")

# Sidebar options
st.sidebar.header("Options")

length = st.sidebar.slider("Password length", min_value=4, max_value=64, value=12)
count = st.sidebar.number_input("How many passwords?", min_value=1, max_value=20, value=1)

use_lower = st.sidebar.checkbox("Include lowercase letters (a-z)", value=True)
use_upper = st.sidebar.checkbox("Include uppercase letters (A-Z)", value=True)
use_digits = st.sidebar.checkbox("Include digits (0-9)", value=True)
use_symbols = st.sidebar.checkbox("Include symbols (!@#$...)", value=False)

# Build character set
charset = ""
if use_lower:
    charset += string.ascii_lowercase
if use_upper:
    charset += string.ascii_uppercase
if use_digits:
    charset += string.digits
if use_symbols:
    charset += "!@#$%^&*()-_=+[]{};:,.<>?/|"

# Generate password function
def generate_password(length, charset):
    return ''.join(secrets.choice(charset) for _ in range(length))

# Generate button
if st.button("Generate Password(s)"):
    if not charset:
        st.error("Please select at least one character set!")
    else:
        st.subheader("Generated Passwords")
        for i in range(count):
            pwd = generate_password(length, charset)
            # Show with copy button
            st.code(pwd, language="")

            st.download_button(
                label="📋 Copy to clipboard (download trick)",
                data=pwd,
                file_name="password.txt",
                mime="text/plain",
                key=f"copy_{i}"
            )

import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")

    # E-posta başlığını ve içeriği oluşturun
    subject = f"New email from {user_email}"
    from_email = f"From: {user_email}"
    message_body = f"{from_email}\n{raw_message}"

    # "message" değişkenini oluşturun
    message = f"""\
Subject: {subject}

{message_body}
"""

    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Message sent successfully")

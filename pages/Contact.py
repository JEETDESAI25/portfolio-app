import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    option = st.selectbox(
        "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
    )

    message = f"""\
Subject: New emial from {user_email}


from: {user_email}
{raw_message}

Preferred way to connect is {option}.
    """

    button = st.form_submit_button("submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully.")

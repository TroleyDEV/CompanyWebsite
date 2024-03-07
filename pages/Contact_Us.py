import pandas
import streamlit as st

from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")

    # Select Box Topics
    df = pandas.read_csv("topics.csv")
    topic = st.selectbox("Topic", options=df)

    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}\n
Topic: {topic}\n
From: {user_email}\n
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message, user_email)
        st.info("Your email was sent successfully")

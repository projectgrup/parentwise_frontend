
import streamlit as st
import requests

BACKEND_URL = "https://your-backend-url.com"

st.title("👶 ParentWise AI: Smart Parenting Assistant")

menu = ["Parenting Q&A", "Schedule Planner", "Feedback", "Login", "Story Generator"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Login":
    st.subheader("User Login (Firebase)")
    token = st.text_input("Firebase ID Token")
    if st.button("Verify"):
        res = requests.post(f"{BACKEND_URL}/auth/verify", data={"token": token})
        st.json(res.json())

elif choice == "Parenting Q&A":
    st.subheader("Ask Parenting Question")
    question = st.text_input("Question")
    lang = st.selectbox("Language", ["en", "hi", "fr", "es"])
    if st.button("Ask"):
        res = requests.post(f"{BACKEND_URL}/qa/ask", data={"question": question, "lang": lang})
        st.success(res.json()["response"])

elif choice == "Schedule Planner":
    st.subheader("Generate Toddler Routine")
    age = st.number_input("Toddler Age (years)", 1, 6)
    wake = st.time_input("Wake Up Time")
    sleep = st.time_input("Sleep Time")
    if st.button("Generate Schedule"):
        res = requests.post(f"{BACKEND_URL}/schedule/generate", data={
            "age": age,
            "wake_time": str(wake),
            "sleep_time": str(sleep)
        })
        st.json(res.json())

elif choice == "Feedback":
    st.subheader("Submit Feedback")
    question = st.text_input("Your Question")
    answer = st.text_input("Answer Received")
    rating = st.slider("Rate Answer (1-5)", 1, 5)
    if st.button("Submit Feedback"):
        res = requests.post(f"{BACKEND_URL}/feedback/submit", data={
            "question": question,
            "answer": answer,
            "rating": rating
        })
        st.success(res.json()["status"])

elif choice == "Story Generator":
    st.subheader("Generate Bedtime Story")
    age = st.number_input("Child Age", 1, 10)
    theme = st.text_input("Story Theme")
    if st.button("Generate Story"):
        res = requests.post(f"{BACKEND_URL}/story/generate", data={"age": age, "theme": theme})
        st.success(res.json()["story"])

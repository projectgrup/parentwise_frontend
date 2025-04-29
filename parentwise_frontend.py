import streamlit as st
import requests

BACKEND_URL = "https://parentwise-backend.onrender.com"

st.title("👶 ParentWise AI: Smart Parenting Assistant")

menu = ["Parenting Q&A", "Schedule Planner", "Feedback", "Login", "Story Generator"]
choice = st.sidebar.selectbox("Menu", menu)

# 🔐 Firebase Login
if choice == "Login":
    st.subheader("User Login (Firebase)")
    token = st.text_input("Firebase ID Token")
    if st.button("Verify"):
        try:
            res = requests.post(f"{BACKEND_URL}/auth/verify", data={"token": token})
            st.json(res.json())
        except Exception as e:
            st.error("Error verifying token.")
            st.text(str(e))

# 💬 Parenting Q&A
elif choice == "Parenting Q&A":
    st.subheader("Ask Parenting Question")
    question = st.text_input("Question")
    lang = st.selectbox("Language", ["en", "hi", "fr", "es"])
    if st.button("Ask"):
        try:
            res = requests.post(f"{BACKEND_URL}/qa/ask", data={"question": question, "lang": lang})
            result = res.json()
            if "response" in result:
                st.success(result["response"])
            else:
                st.warning("No response returned from backend.")
        except Exception as e:
            st.error("❌ Could not decode response from backend.")
            st.text(f"Raw response: {res.text}")

# ⏰ Toddler Schedule Generator
elif choice == "Schedule Planner":
    st.subheader("Generate Toddler Routine")
    age = st.number_input("Toddler Age (years)", 1, 6)
    wake = st.time_input("Wake Up Time")
    sleep = st.time_input("Sleep Time")
    if st.button("Generate Schedule"):
        try:
            res = requests.post(f"{BACKEND_URL}/schedule/generate", data={
                "age": age,
                "wake_time": str(wake),
                "sleep_time": str(sleep)
            })
            st.json(res.json())
        except Exception as e:
            st.error("❌ Failed to generate schedule.")
            st.text(str(e))

# ⭐ Feedback Submission
elif choice == "Feedback":
    st.subheader("Submit Feedback")
    question = st.text_input("Your Question")
    answer = st.text_input("Answer Received")
    rating = st.slider("Rate Answer (1-5)", 1, 5)
    if st.button("Submit Feedback"):
        try:
            res = requests.post(f"{BACKEND_URL}/feedback/submit", data={
                "question": question,
                "answer": answer,
                "rating": rating
            })
            result = res.json()
            if "status" in result:
                st.success(result["status"])
            else:
                st.warning("Feedback not saved.")
        except Exception as e:
            st.error("❌ Could not submit feedback.")
            st.text(str(e))

# 📚 Bedtime Story Generator
elif choice == "Story Generator":
    st.subheader("Generate Bedtime Story")
    age = st.number_input("Child Age", 1, 10)
    theme = st.text_input("Story Theme")
    if st.button("Generate Story"):
        try:
            res = requests.post(f"{BACKEND_URL}/story/generate", data={"age": age, "theme": theme})
            result = res.json()
            if "story" in result:
                st.success(result["story"])
            else:
                st.warning("No story returned.")
        except Exception as e:
            st.error("❌ Error generating story.")
            st.text(f"Raw response: {res.text}")

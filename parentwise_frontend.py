import streamlit as st
import requests

# ✅ Replace with your actual deployed backend URL
BACKEND_URL = "https://your-backend.onrender.com"

st.title("👶 ParentWise AI: Smart Parenting Assistant")

menu = ["Parenting Q&A", "Schedule Planner", "Feedback", "Login"]
choice = st.sidebar.selectbox("Select Module", menu)

# 🔐 Login
if choice == "Login":
    st.subheader("Firebase Login (Demo)")
    token = st.text_input("Firebase ID Token")
    if st.button("Verify"):
        try:
            res = requests.post(f"{BACKEND_URL}/auth/verify", json={"token": token})
            st.json(res.json())
        except Exception as e:
            st.error("Login failed.")
            st.text(str(e))

# 💬 Q&A
elif choice == "Parenting Q&A":
    st.subheader("Ask a Parenting Question")
    question = st.text_input("Enter your question:")
    if st.button("Ask"):
        try:
            res = requests.post(f"{BACKEND_URL}/ask_question", json={"question": question})
            if res.status_code == 200:
                st.success(res.json().get("answer", "No answer returned."))
            else:
                st.error("Backend error.")
                st.text(f"Status code: {res.status_code}")
        except Exception as e:
            st.error("❌ Could not connect to backend.")
            st.text(str(e))

# 🕒 Schedule Planner
elif choice == "Schedule Planner":
    st.subheader("Generate Toddler Schedule")
    age = st.slider("Toddler Age", 1, 6)
    wake = st.time_input("Wake-up Time")
    nap = st.selectbox("Nap Preference", ["No nap", "1 nap", "2 naps"])
    meals = st.slider("Meals per day", 3, 6)
    if st.button("Generate Schedule"):
        try:
            res = requests.post(f"{BACKEND_URL}/generate_schedule", json={
                "age": age,
                "wake_time": str(wake),
                "nap_pref": nap,
                "meals": meals
            })
            if res.status_code == 200:
                st.text_area("Routine:", res.json()["routine"], height=250)
            else:
                st.error("Backend error.")
                st.text(res.text)
        except Exception as e:
            st.error("Could not generate schedule.")
            st.text(str(e))

# ⭐ Feedback
elif choice == "Feedback":
    st.subheader("Submit Feedback")
    question = st.text_input("Your Question")
    answer = st.text_input("Answer Received")
    rating = st.slider("Rate Answer (1-5)", 1, 5)
    if st.button("Submit Feedback"):
        try:
            res = requests.post(f"{BACKEND_URL}/submit_feedback", json={
                "question": question,
                "answer": answer,
                "rating": rating
            })
            if res.status_code == 200:
                st.success("Feedback submitted successfully!")
            else:
                st.error("Failed to submit feedback.")
        except Exception as e:
            st.error("Backend error.")
            st.text(str(e))

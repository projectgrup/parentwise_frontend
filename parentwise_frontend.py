import streamlit as st
import requests

BACKEND_URL = "https://parentwise-backend.onrender.com"  # ✅ Replace with your actual backend URL

st.set_page_config(page_title="ParentWise AI", layout="wide")
st.title("👶 ParentWise AI: Smart Parenting Assistant")

menu = ["Parenting Q&A", "Schedule Planner", "Feedback", "Story Generator", "Login"]
choice = st.sidebar.selectbox("Select Module", menu)

# 🔐 Login (Firebase - placeholder)
if choice == "Login":
    st.subheader("User Login (Firebase)")
    token = st.text_input("Firebase ID Token")
    if st.button("Verify Token"):
        try:
            res = requests.post(f"{BACKEND_URL}/auth/verify", json={"token": token})
            st.json(res.json())
        except Exception as e:
            st.error("Error verifying token.")
            st.text(str(e))

# 💬 Parenting Q&A
elif choice == "Parenting Q&A":
    st.subheader("Ask Your Parenting Question")
    question = st.text_input("Enter your question:")
    lang = st.selectbox("Select response language:", ["en", "hi", "es", "fr", "de"])
    if st.button("Get Answer"):
        if question:
            try:
                res = requests.post(f"{BACKEND_URL}/ask_question",
                                    json={"question": question, "target_language": lang})
                answer = res.json().get("answer")
                if answer:
                    st.success(answer)
                else:
                    st.warning("No answer returned.")
            except Exception as e:
                st.error("❌ Backend error.")
                st.text(str(e))
        else:
            st.warning("Please enter a question.")

# ⏰ Schedule Planner
elif choice == "Schedule Planner":
    st.subheader("Generate Toddler Schedule")
    age = st.slider("Toddler Age (1-6)", 1, 6)
    wake = st.time_input("Wake Time")
    nap = st.selectbox("Nap Preference", ["No nap", "1 nap", "2 naps"])
    meals = st.slider("Meals per day", 3, 6)
    if st.button("Generate Schedule"):
        try:
            res = requests.post(f"{BACKEND_URL}/generate_schedule",
                                json={"age": age, "wake_time": str(wake), "nap_pref": nap, "meals": meals})
            routine = res.json().get("routine")
            st.text_area("Suggested Routine", routine, height=250)
        except Exception as e:
            st.error("❌ Failed to generate routine.")
            st.text(str(e))

# ⭐ Feedback Submission
elif choice == "Feedback":
    st.subheader("Submit Feedback on Answers")
    question = st.text_input("Question You Asked")
    answer = st.text_area("Answer You Received")
    rating = st.slider("Rating (1 = Poor, 5 = Great)", 1, 5)
    if st.button("Submit Feedback"):
        try:
            res = requests.post(f"{BACKEND_URL}/submit_feedback",
                                json={"question": question, "answer": answer, "rating": rating})
            if res.status_code == 200:
                st.success("Feedback submitted successfully!")
            else:
                st.warning("Failed to save feedback.")
        except Exception as e:
            st.error("Error submitting feedback.")
            st.text(str(e))

# 📚 Bedtime Story Generator
elif choice == "Story Generator":
    st.subheader("Generate a Bedtime Story")
    age = st.number_input("Child's Age", min_value=1, max_value=10)
    theme = st.text_input("Enter a story theme (e.g., jungle, friendship)")
    if st.button("Generate Story"):
        try:
            res = requests.post(f"{BACKEND_URL}/story/generate", json={"age": age, "theme": theme})
            story = res.json().get("story")
            if story:
                st.success(story)
            else:
                st.warning("No story returned.")
        except Exception as e:
            st.error("❌ Error generating story.")
            st.text(str(e))


       

          



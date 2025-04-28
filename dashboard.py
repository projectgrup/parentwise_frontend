
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 ParentWise AI: Feedback Dashboard")

# Dummy feedback data
feedback_data = [
    {"question": "How much sleep?", "answer": "12 hours", "rating": 5},
    {"question": "Best food?", "answer": "Fruits and vegetables", "rating": 4},
    {"question": "Potty training?", "answer": "Reward system", "rating": 3}
]

df = pd.DataFrame(feedback_data)

st.subheader("Feedback Table")
st.dataframe(df)

st.subheader("Rating Distribution")
fig, ax = plt.subplots()
df['rating'].value_counts().sort_index().plot(kind='bar', ax=ax)
plt.xlabel('Rating')
plt.ylabel('Count')
st.pyplot(fig)

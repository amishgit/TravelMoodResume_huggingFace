import streamlit as st
from transformers import pipeline

# Hugging Face free sentiment model
#sentiment_pipe = pipeline("sentiment-analysis")
sentiment_pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Sidebar
st.sidebar.title("AI Hackathon Project")
choice = st.sidebar.radio("Choose an App", 
                          ["Travel Guide", "Resume Coach", "Mood Detector"])

# --- Travel Guide ---
if choice == "Travel Guide":
    st.header("AI Travel Guide (Demo)")
    city = st.text_input("Enter city:")
    days = st.number_input("Days to travel:", 1, 15, 3)
    budget = st.selectbox("Budget:", ["Low", "Medium", "High"])

    if st.button("Generate Itinerary"):
        if city:
            st.success(
                f"Here’s a sample {days}-day plan for {city} (Budget: {budget}):\n"
                "- Visit top tourist attractions\n"
                "- Try local street food\n"
                "- Explore cultural spots\n"
                "- Relax in nature parks\n"
                "(This is a lightweight demo — replace with OpenAI API if available.)"
            )
        else:
            st.warning("Please enter a city.")

# --- Resume Coach ---
elif choice == "Resume Coach":
    st.header("AI Resume & Interview Coach (Demo)")
    resume_text = st.text_area("Paste your resume:")

    if st.button("Analyze Resume"):
        if resume_text.strip():
            st.success(
                "Resume Feedback:\n"
                "- Add measurable achievements\n"
                "- Keep bullet points concise\n"
                "- Highlight technical + soft skills"
            )
        else:
            st.warning("Please paste some text.")

    st.subheader("Mock Interview")
    job_role = st.text_input("Enter a job role (e.g., Data Scientist)")

    if st.button("Generate Interview Question"):
        if job_role.strip():
            st.info(f"Sample Interview Question for {job_role}:\nTell me about a project where you applied {job_role} skills.")
        else:
            st.warning("Please enter a job role.")

# --- Mood Detector ---
elif choice == "Mood Detector":
    st.header("AI Mood Detector (Hugging Face)")
    user_text = st.text_area("How are you feeling today?")

    if st.button("Detect Mood"):
        if user_text.strip():
            with st.spinner("Analyzing mood..."):
                result = sentiment_pipe(user_text)[0]
                label = result['label'].upper()
                mood_map = {"POSITIVE": "Positive", "NEGATIVE": "Negative", "NEUTRAL": "Neutral"}
                st.success(f"Detected Mood: {mood_map.get(label, label)}")
        else:
            st.warning("Please type something first.")

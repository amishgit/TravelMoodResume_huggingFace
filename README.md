# TravelMoodResume_huggingFace
# 🤖 AI Hackathon Project

This project was built for [Hackathon Name] in under 48 hours.  
It demonstrates **3 AI-powered features** in a single Streamlit app:  

1. **🌍 Travel Guide (Demo)**  
   - Enter a city, budget, and days → get a **sample travel itinerary**.  
   - Currently uses **rule-based demo responses** (lightweight for free hosting).  
   - Can be upgraded with **OpenAI GPT** or **Hugging Face LLMs** for richer itineraries.  

2. **💼 Resume & Interview Coach (Demo)**  
   - Paste your resume text → get **quick feedback & suggestions**.  
   - Generates **mock interview questions** based on job role.  
   - Currently demo-based; can be upgraded with OpenAI/Cohere for professional results.  

3. **😀 Mood Detector (Hugging Face)**  
   - Enter text about your feelings → AI detects **Positive / Negative / Neutral** mood.  
   - Powered by Hugging Face **BERT sentiment-analysis pipeline**.  
   - Runs free on CPU (no API key needed).  

---

## 🚀 Tech Stack
- [Streamlit](https://streamlit.io) – for the interactive UI  
- [Hugging Face Transformers](https://huggingface.co/transformers/) – sentiment analysis  
- (Optional upgrade) [OpenAI API](https://platform.openai.com/) – for Travel & Resume modules  

---

## ▶️ Run Locally
Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/ai-hackathon-project.git
cd ai-hackathon-project
pip install -r requirements.txt
streamlit run app.py

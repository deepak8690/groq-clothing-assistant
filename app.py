import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load workspace environment variables
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq core connection client
if my_api_key:
    client = Groq(api_key=my_api_key)
else:
    st.error("⚠️ GROQ_API_KEY environment variable missing! Please configure your .env file.")
    st.stop()

# Set up webpage layout parameters
st.set_page_config(page_title="Groq AI Clothing Brand Manager", page_icon="🧥", layout="centered")

st.title("🧥 Groq AI Clothing Brand Manager")
st.caption("🚀 An intelligent assistant to help build, name, and scale your fashion brand.")

# System core expert rule setup
SYSTEM_INSTRUCTION = {
    "role": "system",
    "content": (
        "You are an expert fashion brand manager and retail strategist. Your goal is to help "
        "the user build, name, and scale their clothing company. Provide precise, creative, "
        "and actionable business advice. When suggesting names, keep them sharp and modern."
    )
}

# Initialize browser session storage state memory array
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_INSTRUCTION]

# Render persistent historical user-assistant conversation to web frame
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Capture live user browser terminal input prompt execution string
if user_prompt := st.chat_input("Ask your AI Brand Manager..."):
    
    # Render user query directly to active chat window layer
    with st.chat_message("user"):
        st.write(user_prompt)
    
    # Store interaction dictionary to localized session list
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    # Dispatch inference text pipeline to Groq infrastructure endpoint
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.messages,
                    temperature=0.7
                )
                ai_response = response.choices[0].message.content
                st.write(ai_response)
                
                # Append finalized contextual payload history to array frame
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            except Exception as e:
                st.error(f"🚨 API Execution Error: {str(e)}")

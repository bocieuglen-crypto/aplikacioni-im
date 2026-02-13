import streamlit as st
import google.generativeai as genai

# Zëvendëso AIza... me kodin e ri që krijove te Google AI Studio
genai.configure(api_key="AIzaSyA...") 

st.title("AI Chatbot Im - Live")

model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Shkruaj diçka..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.write(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Gabim: {e}")

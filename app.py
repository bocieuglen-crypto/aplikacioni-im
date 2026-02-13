import streamlit as st
from google import genai

# Konfigurimi me librarinë e re
client = genai.Client(api_key="AIzaSyAaC3E9yvo_i8hP5EKi-naocH8DpwOqOPE")

st.title("AI-ja Ime (Versioni i Ri)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Shkruaj diçka..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Mënyra e re e thirrjes së modelit
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Gabim: {e}")

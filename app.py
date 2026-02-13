import streamlit as st
from google import genai

# Konfigurimi
client = genai.Client(api_key="AIzaSyAaC3E9yvo_i8hP5EKi-naocH8DpwOqOPE")

st.title("AI-ja Ime (Versioni Final)")

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
        # Përdorim modelin 'gemini-1.0-pro' - ky është më i pajtueshmi
        response = client.models.generate_content(
            model="gemini-1.0-pro", 
            contents=prompt
        )
        
        with st.chat_message("assistant"):
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.error("AI nuk ktheu përgjigje. Provo një pyetje tjetër.")
    except Exception as e:
        st.error(f"Gabim: {e}")



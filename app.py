import streamlit as st
import google.generativeai as genai

# Konfigurimi i API
genai.configure(api_key="AIzaSyAaC3E9yvo_i8hP5EKi-naocH8DpwOqOPE")

# Përdorim modelin bazë Gemini Pro që është më i qëndrueshmi për deploy
model = genai.GenerativeModel("gemini-pro") 

st.title("AI-ja Ime")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Shkruaj mesazhin këtu..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Përdorim gjenerimin e thjeshtë
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Gabim: {e}")

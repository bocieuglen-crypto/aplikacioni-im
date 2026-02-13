import streamlit as st
import google.generativeai as genai

# Konfigurimi i faqes (Dizajni)
st.set_page_config(page_title="AI Chatbot Im", page_icon="🤖", layout="centered")

# Stili vizual (Ngjyrat)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Lidhja me Gemini
genai.configure(api_key="AIzaSyAaC3E9yvo_i8hP5EKi-naocH8DpwOqOPE")
model = genai.GenerativeModel("models/gemini-1.5-flash")

# --- MEMORJA (Session State) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Chatbot me Memorie")
st.write("---")

# Shfaq bisedat e kaluara
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kutia e mesazhit (input)
if prompt := st.chat_input("Shkruaj mesazhin këtu..."):
    # Shto mesazhin e përdoruesit në memorie
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Merr përgjigjen nga AI
    with st.chat_message("assistant"):
        # Krijojmë historikun për AI
        history = [{"role": m["role"], "parts": [m["content"]]} for m in st.session_state.messages]
        chat = model.start_chat(history=[])
        
        # Përgjigjja
        response = chat.send_message(prompt)
        st.markdown(response.text)
        
        # Shto përgjigjen e AI në memorie
        st.session_state.messages.append({"role": "assistant", "content": response.text})

# Butoni për të fshirë memorien në Sidebar
if st.sidebar.button("Fshij Bisedën"):
    st.session_state.messages = []

    st.rerun()

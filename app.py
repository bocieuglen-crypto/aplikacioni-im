import streamlit as st
import google.generativeai as genai

# Konfigurimi i API Key
genai.configure(api_key="AIzaSy...") # Sigurohu që ky është Key i ri

st.title("AI Chatbot Im - Live")

# KJO ESHTE PJESA KRITIKE:
# Listojmë modelet e disponueshme për të parë cilin pranon ky Key
try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    # Zgjedhim modelin e parë që punon (zakonisht gemini-1.5-flash)
    target_model = available_models[0] if available_models else "gemini-1.5-flash"
    model = genai.GenerativeModel(target_model)
except Exception as e:
    st.error(f"Nuk u gjet asnjë model: {e}")
    target_model = "gemini-1.5-flash"
    model = genai.GenerativeModel(target_model)

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
        st.error(f"Gabim teknik: {e}")

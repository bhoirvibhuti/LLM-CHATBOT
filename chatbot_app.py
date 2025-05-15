import streamlit as st
import openai

st.set_page_config(page_title="LLM Chatbot", layout="wide")
st.title("🤖 LLM Chatbot")

# Get API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "You are a helpful AI chatbot."}]

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
prompt = st.chat_input("Say something...")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["messages"]
        )
        reply = response.choices[0].message["content"]
        st.chat_message("assistant").write(reply)
        st.session_state["messages"].append({"role": "assistant", "content": reply})

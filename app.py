import streamlit as st
from chatbot import get_ai_response, clear_chat

st.set_page_config(
    page_title="Simple AI Chat Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Simple AI Chat Assistant")
st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    reply = get_ai_response(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(reply)

if st.button("🗑️ Clear Chat"):
    clear_chat()
    st.session_state.messages = []
    st.rerun()
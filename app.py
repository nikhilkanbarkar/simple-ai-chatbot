import streamlit as st
from chatbot import get_ai_response, clear_chat

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="Simple AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- Custom CSS --------------------

st.markdown("""
<style>

/* Main container */
.block-container{
    max-width: 1200px;
    margin: auto;
    padding-top: 2rem;
}

/* Bigger title */
h1{
    font-size: 2.5rem !important;
    text-align:center;
}

/* Bigger normal text */
html, body, [class*="css"]{
    font-size:18px;
}

/* Chat message */
.stChatMessage{
    padding:18px;
    border-radius:15px;
    margin-bottom:12px;
}

/* Chat input */
.stChatInput input{
    font-size:18px !important;
}

/* Buttons */
.stButton button{
    width:100%;
    font-size:17px;
    border-radius:10px;
}

/* Sidebar text */
section[data-testid="stSidebar"]{
    font-size:17px;
}

/* Sidebar width */
section[data-testid="stSidebar"]{
    width:320px !important;
}

</style>
""", unsafe_allow_html=True)
# -------------------- Title --------------------

st.title("🤖 Simple AI Chat Assistant")
st.caption("Powered by Google Gemini")
st.divider()

# -------------------- Session State --------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- Sidebar --------------------

with st.sidebar:

    st.header("Settings")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        clear_chat()
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.markdown("### Model")
    st.info("Gemini")

    st.markdown("---")

    st.write("Developed by")
    st.write("**Nikhil Kanbarkar**")

# -------------------- Display Chat --------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- Chat Input --------------------

prompt = st.chat_input("Type your message...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                reply = get_ai_response(prompt)

            except Exception as e:

                reply = f"❌ Error:\n\n{e}"

            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
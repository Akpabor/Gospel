import streamlit as st
from openai import OpenAI

# Load API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page setup
st.set_page_config(
    page_title="FaithChat - Bible-Based AI",
    page_icon="📖",
    layout="centered"
)

# Set system prompt
SYSTEM_PROMPT = (
    "You are a conservative Baptist biblical counselor. For every user question:\n"
    "1. Answer using only the New King James Version (NKJV) Bible.\n"
    "2. Provide a modern-language explanation that is biblically accurate and practical.\n"
    "3. Include a short, relevant quote or insight from Charles Spurgeon where applicable.\n"
    "Do not use other theologians. If Scripture is silent, admit it and apply general biblical principles.\n"
    "Speak clearly, compassionately, and with reverence for truth."
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Title
st.title("📖 FaithChat")
st.markdown("Ask anything about faith, life, or the Bible — and receive Scripture-based answers grounded in Baptist doctrine.")

# Display chat history
for msg in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask a question or follow-up...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Searching the Scriptures..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.messages
                )
                reply = response.choices[0].message.content
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# Optional: Add a clear chat button
with st.sidebar:
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.rerun()

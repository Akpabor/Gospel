import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ─────────────────────────────────────────────
# Page setup
st.set_page_config(
    page_title="FaithChat - Bible-Based AI",
    page_icon="📖",
    layout="centered"
)

# ─────────────────────────────────────────────
# Hero Section
st.markdown(
    """
    <div style='text-align: center; padding-top: 2rem;'>
        <h1 style='font-size: 3rem;'>📖 FaithChat</h1>
        <h3 style='color: gray;'>Biblical guidance, powered by Scripture</h3>
        <p style='font-size: 1.1rem; max-width: 600px; margin: 0 auto;'>
            FaithChat is an AI-based assistant trained to respond using the King James Bible and conservative Baptist doctrine.
            Ask a question about life, faith, or decisions — and receive guidance rooted in God's Word.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ─────────────────────────────────────────────
# Feature Highlights
st.subheader("🙌 What FaithChat Can Help With:")
features = [
    "💬 Get biblical answers to personal, moral, or spiritual questions",
    "📖 Responses are grounded in KJV Scripture — not opinion",
    "⛪ Reflects Baptist doctrine and conservative Christian values",
    "🧠 Great for counseling, devotional study, and discipleship",
]
for f in features:
    st.markdown(f"- {f}")

st.markdown("---")

# ─────────────────────────────────────────────
# Chat Input Section
st.header("✍️ Ask a Question")
st.markdown("*Let the Word of God guide your heart today.*")

user_input = st.text_input("What would you like to ask?", placeholder="e.g., How do I get closer to God?")

if user_input:
    with st.spinner("Praying and searching Scripture... 🙏"):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": (
                        "You are a conservative Baptist biblical counselor. Always respond using only the King James Version (KJV) Bible and sound Baptist doctrine. "
                        "When the Bible does not clearly address a topic, do not speculate or invent historical claims. Instead, explain biblical principles that apply and admit when Scripture is silent. "
                        "Do not rely on cultural opinions, denominational traditions, or modern interpretations. Be clear, compassionate, and Christ-centered in all your responses."
                    )},
                    {"role": "user", "content": user_input}
                ]
            )
            answer = response.choices[0].message.content
            st.success("📖 Here's what the Bible says:")
            st.markdown(answer)

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")

# ─────────────────────────────────────────────
# Footer
st.markdown("---")
st.markdown(
    "<small style='color: gray;'>FaithChat is a spiritual support tool, not a substitute for pastoral counseling. Seek godly counsel and prayer in all things.</small>",
    unsafe_allow_html=True
)

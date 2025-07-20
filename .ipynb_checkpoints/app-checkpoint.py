import streamlit as st
from prompts import build_prompt
from utils import query_openai

st.set_page_config(page_title="CineMatch", page_icon="🎬")
st.title("🎭 CineMatch – Which Character Are You?")

st.markdown("Describe your vibe, personality, dreams, whatever. Let AI match you to your onscreen twin ✨")

user_input = st.text_area("📝 Tell me about yourself:", placeholder="e.g. I love helping others, I overthink a lot, I’m fiercely independent but get hurt easily...")

if st.button("🔮 Find My Match"):
    with st.spinner("Casting your cinematic soul..."):
        prompt = build_prompt(user_input)
        result = query_openai(prompt)
        st.markdown("### 🧬 Your CineMatch is...")
        st.success(result)

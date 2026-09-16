from deep_translator import GoogleTranslator
import streamlit as st

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es"
}

source = st.selectbox("Source", list(languages.keys()))
target = st.selectbox("Target", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        try:
            translated = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)

            st.success(translated)

        except Exception as e:
            st.error(f"Error: {str(e)}")
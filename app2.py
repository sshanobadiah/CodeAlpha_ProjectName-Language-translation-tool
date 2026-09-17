import streamlit as st
from googletrans import Translator

translator = Translator()

st.title("🌏 Language Translation Tool")

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
    elif source == target:
        st.info("Source and target are same")
    else:
        try:
            result = translator.translate(
                text,
                src=languages[source],
                dest=languages[target]
            )
            st.success("Translation Successful")
            st.text_area("Translated Text", result.text, height=150)

        except Exception as e:
            st.error("Error occurred")
            st.write(str(e))

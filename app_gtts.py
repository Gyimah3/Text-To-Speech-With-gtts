from gtts import gTTS
import streamlit as st
import os

# Function to save and return the audio file
def text_to_speech(text, lang, slow):
    tts = gTTS(text=text, lang=lang, slow=slow)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# Streamlit app layout
st.title("Text-to-Speech Web App (gTTS)")
text_input = st.text_area("Enter text here...")

# List of languages and accents
languages = {
    'English (US)': 'en',
    'English (UK)': 'en-uk',
    'English (India)': 'en-in',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Chinese': 'zh-cn',
    'Japanese': 'ja',
    'Korean': 'ko'
}

lang_choice = st.selectbox("Choose a language", list(languages.keys()))
lang_code = languages[lang_choice]

# Speed control
slow = st.checkbox("Slow speed", value=False)

if st.button("Speak"):
    if text_input:
        audio_file = text_to_speech(text_input, lang_code, slow)

        # Ensure the file is properly closed before reading it again
        with open(audio_file, 'rb') as f:
            audio_bytes = f.read()
            st.audio(audio_bytes, format='audio/mp3')

        # Provide download link for the audio file
        with open(audio_file, "rb") as f:
            st.download_button(
                label="Download audio",
                data=f,
                file_name="output.mp3",
                mime="audio/mp3"
            )
    else:
        st.warning("Please enter some text to convert to speech.")




# from gtts import gTTS
# import streamlit as st
# import os

# # Function to save and return the audio file
# def text_to_speech(text, lang):
#     tts = gTTS(text=text, lang=lang)
#     tts.save("output.mp3")
#     return "output.mp3"

# # Streamlit app layout
# st.title("Text-to-Speech Web App (gTTS)")
# text_input = st.text_area("Enter text here...")

# # List of languages and accents
# languages = {
#     'English (US)': 'en',
#     'English (UK)': 'en-uk',
#     'English (India)': 'en-in',
#     'French': 'fr',
#     'Spanish': 'es',
#     'German': 'de',
#     'Chinese': 'zh-cn',
#     'Japanese': 'ja',
#     'Korean': 'ko'
# }

# lang_choice = st.selectbox("Choose a language", list(languages.keys()))
# lang_code = languages[lang_choice]

# if st.button("Speak"):
#     if text_input:
#         audio_file = text_to_speech(text_input, lang_code)

#         # Read the audio file and play it in the Streamlit app
#         audio_bytes = open(audio_file, 'rb').read()
#         st.audio(audio_bytes, format='audio/mp3')
#     else:
#         st.warning("Please enter some text to convert to speech.")

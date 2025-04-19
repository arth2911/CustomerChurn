
import streamlit as st
from googletrans import Translator

def translate_to_english(self, text):
        """
        Translates the input text to English.
        
        :param text: The text to be translated.
        :return: Translated text in English.
        """
        translation = self.translator.translate(text, dest='en')
        return translation.text

def translate_to_target_language(self, text, target_language):
    """
    Translates the input text to a specified target language.
    
    :param text: The text to be translated.
    :param target_language: The language code of the target language (e.g., 'fr' for French).
    :return: Translated text in the target language.
    """
    translation = self.translator.translate(text, dest=target_language)
    return translation.text


st.title("Text Tone Detector")

user_input = st.text_area("Enter your text here:")

if st.button("Detect Tone"):
   
    translator = Translator()
    detected_language = translator.detect(user_input).lang

    if detected_language != 'en':
        user_input = translator.translate(user_input, dest='en').text
        #st.info(f"Text was translated from {detected_language} to English")
    
    
    


    #st.write("Tone detection logic goes here.")

from googletrans import Translator

class TranslatorService:
    
    def __init__(self):
        self.translator = Translator()

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

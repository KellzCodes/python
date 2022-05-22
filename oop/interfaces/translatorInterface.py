import io


class TranslatorInterface:
    def translate(self, text):
        raise NotImplementedError

    def untranslate(self, text):
        raise NotImplementedError


class SpanishTranslator(TranslatorInterface):
    def translate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hello":
                words[i] = "hola"
            elif word == "world":
                words[i] = "mundo"
        return " ".join(words)

    def untranslate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hola":
                words[i] = "hello"
            elif word == "mundo":
                words[i] = "world"
        return " ".join(words)


class FrenchTranslator(TranslatorInterface):
    def translate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "hello":
                words[i] = "bonjour"
            elif word == "world":
                words[i] = "monde"
        return " ".join(words)

    def untranslate(self, text):
        words = text.split(" ")
        for i, word in enumerate(words):
            if word == "bonjour":
                words[i] = "hello"
            elif word == "monde":
                words[i] = "world"
        return " ".join(words)


TRANSLATORS = {
    "spanish": SpanishTranslator(),
    "french": FrenchTranslator(),
}

# In order to check that the translator works correctly, we first
# translate "hello world" into that language, and then re-translate
# the result. At the end, we should be getting "hello world" back.
def check_translator_accuracy(language):
    translator = TRANSLATORS[language]

    original_text = "hello world"
    translated = translator.translate(original_text)
    new_text = translator.untranslate(translated)

    if original_text != new_text:
        raise Exception(f"Translator {language} does not work correctly!")

    print(f"The {language} translator is correct!")


check_translator_accuracy("spanish")
check_translator_accuracy("french")

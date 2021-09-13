import pyttsx3


class TextToSpeech:

    def __init__(self):
        self.engine = pyttsx3.init()

    def say_sentence(self, sentence: str):
        self.engine.say(sentence + '.')
        self.engine.runAndWait()

    def say_multiple_sentences(self, sentences: list, separator:str='.'):
        for sentence in sentences:
            self.engine.say(sentence + separator)
        self.engine.runAndWait()

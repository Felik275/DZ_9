#Task 2 TextProcessor
from string import punctuation

class TextProcessor(object):
    def get_clean_string(string):
        new_string = ''.join([x for x in string if x not in punctuation])
        return print(new_string)

    def is_punktiantian(string):
        for char in string:
            print(char in punctuation)
class TextLoader:
    def __init__(self):
        self._text_processor = TextProcessor()
        self._clean_string = ""

    def set_clean_text(self, text):
        self._clean_string = self._text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Cleaned text:", self._clean_string)
        return self._clean_string


class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, texts):
        for text in texts:
            self._text_loader.set_clean_text(text)
            _ = self._text_loader.clean_string
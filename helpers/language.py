import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector


@Language.factory("language_detector")
def create_language_detector(nlp, name):
    return LanguageDetector(language_detection_function=None)


def get_language_detector():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("language_detector")

    return nlp


def detect_language(nlp, text):
    doc = nlp(text)
    detect_language = doc._.language

    return detect_language

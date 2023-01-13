import spacy as spacy
from flask import Flask
import pandas as pd
import numpy as np
import re
# import seaborn as sns
# import matplotlib.pyplot as plt
from langdetect import detect
from spacy.language import Language
import spacy_langdetect
from spacy_langdetect import LanguageDetector
import warnings

warnings.simplefilter("ignore")
app = Flask(__name__)


# @Language.factory("language_detector")
def get_lang_detector(nlp, name):
    return LanguageDetector()


def spacy_language_detection(text, model):
    pipeline = list(dict(model.pipeline).keys())

    if (not "language_detector" in pipeline):
        Language.factory("language_detector", func=get_lang_detector)
        model.add_pipe("language_detector", last=True)

    doc = model(text)
    return doc._.language


@app.route("/")
def hello():
    pre_trained_model = spacy.load("en_core_web_sm")
    print(spacy_language_detection("Où est la boutique duty-free?", pre_trained_model))
    # print(detect("My name is"))
    return "<h1>Not Much Going On Here</h1>"


@app.route("/api/language-detection", methods=["POST"])
def detectLanguage():
    pass


@app.route("/api/sentiment-score", methods=["POST"])
def getSentimentScore():
    pass

app.run(host='0.0.0.0', port=50000)

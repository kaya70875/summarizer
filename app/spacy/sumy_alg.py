from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')

def summarize_paragraph(paragraph: str, r:int=200):
    sld = 400
    summarized_list = []

    parser = PlaintextParser.from_string(paragraph, Tokenizer("english"))

    summarizer = LsaSummarizer(Stemmer("english"))
    summarizer.stop_words = get_stop_words("english")

    sentences_count = round(len(paragraph) / (sld - r))

    summary = summarizer(parser.document, sentences_count if sentences_count > 0 else 1)
    for sentence in summary:
        summarized_list.append(sentence._text)

    return summarized_list

def calculate_efficiency(summary, paragraph: str):    
    summaryC = 0
    for sentence in summary:
        summaryC += len(sentence)

    efficiency = round(abs(((summaryC - len(paragraph)) / len(paragraph)) * 100), 2)
    return efficiency
    

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def summarize_paragraph(paragraph: str, summary_ratio: float = 0.3):

    """
    Summarizes a paragraph using a ratio of the original number of sentences.
    :param paragraph: The text to summarize.
    :param summary_ratio: The fraction of sentences to keep (e.g., 0.3 for 30%).
    """

    try:
        summarized_list = []
        
        parser = PlaintextParser.from_string(paragraph, Tokenizer("english"))
        original_sentences = list(parser.document.sentences)
        total_sentences = len(original_sentences)

        # Calculate the target number of sentences based on the original sentence count.
        target_sentence_count = max(1, round(total_sentences * summary_ratio))
        
        summarizer = LsaSummarizer(Stemmer("english"))
        summarizer.stop_words = get_stop_words("english")
        summary = summarizer(parser.document, target_sentence_count)

        for sentence in summary:
            summarized_list.append(sentence._text)

        return summarized_list
    except Exception as exc:
        print(f'An error occured while summarize paragraph {exc}')

def calculate_efficiency(summary, paragraph: str):
    try:
        summaryC = 0
        for sentence in summary:
            summaryC += len(sentence)

        efficiency = round(abs(((summaryC - len(paragraph)) / len(paragraph)) * 100), 2)
        return efficiency
    except Exception as e:
        print(f'An error occured while calculating efficiency {e}')
    

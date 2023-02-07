import spacy
from util import text, print_lemmatisation, filter_out_stop_words


if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")

    # Tokenisation
    doc = nlp(text)

    # Stop Word removal
    filter_out_stop_words(doc, nlp)

    print("\n")

    # Lemmatisation
    print_lemmatisation(doc)

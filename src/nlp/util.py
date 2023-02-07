import sys
from spacy.tokens import Doc
from spacy.language import Language

text: str = "Every year we go to Florida. \
We like to go to the beach. \
My favorite beach is called Emerson Beach. \
It is very long, with soft sand and palm trees. \
It is very beautiful. \
I like to make sandcastles and watch the sailboats go by. \
Sometimes there are dolphins and whales in the water! \
Every morning we look for shells in the sand. \
I found fifteen big shells last year. \
I put them in a special place in my room. \
This year I want to learn to surf. \
It is hard to surf, but so much fun! \
My sister is a good surfer. \
She says that she can teach me. \
I hope I can do it!"


def filter_out_stop_words(doc: Doc, nlp: Language):
    words: list[str] = []

    for token in doc:
        if not token.is_stop:
            words.append(token.text)

    new_doc = Doc(nlp.vocab, words=words)
    print("Text with stop words removed is:\n")
    print(new_doc)


def print_lemmatisation(doc: Doc):
    i = 0
    sys.stdout.write("The Lemmatisation of the document is:\n\n")
    sys.stdout.write("-" * (2 * 12 + 4) * 4)
    sys.stdout.write("\n|")
    for token in doc:
        if i < 3:
            sys.stdout.write(f"{token.text: >12} {token.lemma_: >12} | ")
            i += 1
        else:
            sys.stdout.write(f"{token.text: >12} {token.lemma_: >12} |\n")
            sys.stdout.write("-" * (2 * 12 + 4) * 4)
            sys.stdout.write("\n|")
            i = 0
    sys.stdout.write("\n")
    sys.stdout.write("-" * (2 * 12 + 4) * i)
    print("")

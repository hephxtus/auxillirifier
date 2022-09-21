"""
Method to help Carl be a better person
"""

import random
import nltk as nltk

# check if nltk average_perceptron_tagger is installed
try:
    from nltk import word_tokenize, pos_tag
except ImportError:
    print("nltk average_perceptron_tagger or punkt is not installed")
    print("Downloading now... Please wait")
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')

modal_words = ['can', 'could', 'may', 'might', 'must', 'will', 'would', 'shall', 'should', 'ought', 'dare', 'need to']

definitive_modal_words = ['must', 'shall', 'ought to', 'dare to', 'need to', 'will']
bad_modal_words = ['can', 'could', 'may', 'might', 'would', 'should']

# TODO: catorgorize the modal words into conditions with opposites
# liklihood_modal_words = ["should", "must"]
# possibility_modal_words = ["may", "might", "could", "would"]
# ability_modal_words = ["can"]
# permission_modal_words = ["can", "could", "may", "might", "must", "will", "would", "shall", "should", "ought", "dare", "need"]
# possibility_modal_words = ['can', 'could', 'may', 'might', 'must', 'will', 'would']
# obligation_modal_words = ['shall', 'should', 'ought', 'dare', 'need']


# main
if __name__ == "__main__":
    sentence = ""
    while sentence == "":
        sentence = input("Enter your purposeful statement: ")
        # sentence = sentence.lower()

        if sentence == "exit":
            exit()
        sentence = sentence.capitalize()
        sentence = sentence.replace(' i ', " I ")
        # check if the sentence contains punctuation
        if sentence[-1] in [".", "!", "?"]:
            # and remove it we dont need punctuation in our sentences this is englishgoddamit
            sentence = sentence[:-1]

        # tokenize and identify the sentence
        text = nltk.word_tokenize(sentence)
        result = nltk.pos_tag(text)
        # remove leading Presebt tense verbs
        name = ""
        for i, x in enumerate(result):
            try:
                if x[1] == "JJ":
                    name = (x[0].capitalize(), x[1])
                if result[i][1] == "MD" and result[i + 1][1] == "PRP":
                    result[i], result[i + 1] = result[i + 1], result[i]

                if result[i][1] == 'PRP' and result[i + 1][1] == 'MD':
                    if name != "":
                        result.insert(i + 1, name)
                    result = result[i:]
                    break
            except IndexError:
                # TODO: handle exception
                print("Index out of range")
        sentence_words = [x[0] for x in result]

        # replace bad modal words with good ones
        for i, r in enumerate(result):
            if r[1] == "MD" and r[0] not in definitive_modal_words:
                sentence_words[i] = random.choice(definitive_modal_words).upper()

        # rejoin sentence
        sentence = " ".join(sentence_words)

        # add punctuation
        sentence += "!"
        # check if the sentence is a question

        print("assertive statement:", sentence)
        sentence = ""

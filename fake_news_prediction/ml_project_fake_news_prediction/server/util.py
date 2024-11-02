import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


__model = None
__vectorizer = None
port_stem = PorterStemmer()


def load_saved_artifacts():
    print("loading saved artifacts... start")
    global __model
    global __vectorizer

    # load model
    with open("./artifacts/fake_news_model.pickle", "rb") as f:
        __model = pickle.load(f)

    with open("./artifacts/fake_news_vectorizer.pickle", "rb") as f:
        __vectorizer = pickle.load(f)

    print("loading saved artifacts... done")


def stemming(content):
    # replace any non-alphabetic characters in the content variable with a space character
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)

    # Convert all words into lower case letters
    stemmed_content = stemmed_content.lower()

    # Split the words into list
    stemmed_content = stemmed_content.split()

    # generate a list of stemmed words from stemmed_content, excluding any stop words from the list
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]

    # Join the elements from the list 'stemmed_content' into a single string separated by spaces
    stemmed_content = " ".join(stemmed_content)

    return stemmed_content


def is_fake(title, author):
    content = author + " " + title
    content = stemming(content)
    X_vect = __vectorizer.transform([content])
    return __model.predict(X_vect)


title1 = "FLYNN: Hillary Clinton, Big Woman on Campus - Breitbart"
author1 = "Daniel J. Flynn"

title2 = "House Dem Aide: We Didnâ€™t Even See Comeyâ€™s Letter Until Jason Chaffetz Tweeted It"
author2 = "Darrell Lucus"



if __name__ == '__main__':
    load_saved_artifacts()
    print(is_fake(title1, author1))
    print(type(is_fake(title2, author2)))

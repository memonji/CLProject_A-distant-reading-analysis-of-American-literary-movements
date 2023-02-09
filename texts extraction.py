#CLProject_A-distant-reading-analysis-of-American-Literature - 2. [texts extraction]

# [A] for unified lists of urls ('unified_processed_texts')
# [B] for single urls lists ('processed_texts')
# [C] for single urls 

-----------------------------------------

# [A] for unified lists of urls (unified_processed_texts)

import urllib.request
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer

import urllib.request
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download("stopwords")

def preprocessing(text):
    nltk.download("stopwords")
    stop_words = set(nltk.corpus.stopwords.words("english"))

    lower_text = text.lower()
    #punc_chars = string.punctuation + '"'
    #no_punct_corpus = lower_text.translate(str.maketrans("", "", punc_chars))
    no_punct_corpus = lower_text.translate(str.maketrans ("", "", string.punctuation))
    no_number_corpus = re.sub(r'\d+', '', no_punct_corpus)
    no_number_corpus = str(no_number_corpus)
    tokenized_corpus = nltk.word_tokenize(no_number_corpus)
    lemmatizer = WordNetLemmatizer()
    first_lemmatized_corpus = " ".join(lemmatizer.lemmatize(word) for word in tokenized_corpus)
    lemmatized_corpus = nltk.word_tokenize(first_lemmatized_corpus)
    filtered_tokens = [word for word in lemmatized_corpus if word not in stop_words]
    return filtered_tokens

def process_url(url):
    raw = urllib.request.urlopen(url).read().decode().strip()
    processed_text = preprocessing(raw)
    return processed_text

urls = [
    "http://www.gutenberg.org/files/2147/2147-0.txt",
    "http://www.gutenberg.org/files/1342/1342-0.txt",
    "http://www.gutenberg.org/files/98/98-0.txt"
]

processed_texts = []
for url in urls:
    processed_text = process_url(url)
    processed_texts.append(processed_text)

unified_processed_text = [word for sublist in processed_texts for word in sublist]

-----------------------------------------

#[B] for single urls lists ('processed_texts')

import urllib.request
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer

import urllib.request
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download("stopwords")

def preprocessing(text):
    nltk.download("stopwords")
    stop_words = set(nltk.corpus.stopwords.words("english"))

    lower_text = text.lower()
    no_punct_corpus = lower_text.translate(str.maketrans ("", "", string.punctuation))
    no_number_corpus = re.sub(r'\d+', '', no_punct_corpus)
    no_number_corpus = str(no_number_corpus)
    tokenized_corpus = nltk.word_tokenize(no_number_corpus)
    lemmatizer = WordNetLemmatizer()
    first_lemmatized_corpus = " ".join(lemmatizer.lemmatize(word) for word in tokenized_corpus)
    lemmatized_corpus = nltk.word_tokenize(first_lemmatized_corpus)
    filtered_tokens = [word for word in lemmatized_corpus if word not in stop_words]
    return filtered_tokens


def process_url(url):
    raw = urllib.request.urlopen(url).read().decode().strip()
    processed_text = preprocessing(raw)
    return processed_text

urls = [
    "http://www.gutenberg.org/files/2147/2147-0.txt",
    "http://www.gutenberg.org/files/1342/1342-0.txt",
    "http://www.gutenberg.org/files/98/98-0.txt"
]

for url in urls:
    processed_text = process_url(url)
    print("Processed text from URL:", url)
    print(processed_text[:300])
    print("\n")

-----------------------------------------
    
# [C] for single urls (preprocessed_text)

import urllib.request
import re
import string
import nltk
from nltk.stem import WordNetLemmatizer

poeUrl = "http://www.gutenberg.org/files/2147/2147-0.txt"
poeString = urllib.request.urlopen(poeUrl).read().decode().strip()

def preprocessing(text):
    nltk.download("stopwords")
    stop_words = set(nltk.corpus.stopwords.words("english"))

    lower_text = text.lower()
    no_punct_corpus = lower_text.translate(str.maketrans ("", "", string.punctuation))
    no_number_corpus = re.sub(r'\d+', '', no_punct_corpus)
    no_number_corpus = str(no_number_corpus)
    tokenized_corpus = nltk.word_tokenize(no_number_corpus)
    lemmatizer = WordNetLemmatizer()
    first_lemmatized_corpus = " ".join(lemmatizer.lemmatize(word) for word in tokenized_corpus)
    lemmatized_corpus = nltk.word_tokenize(first_lemmatized_corpus)
    filtered_tokens = [word for word in lemmatized_corpus if word not in stop_words]
    return filtered_tokens

raw_text = poeString
preprocessed_text = nltk.word_tokenize(preprocessing(raw_text))
print(preprocessed_text)

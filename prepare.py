import re
import numpy as np
import acquire
from bs4 import BeautifulSoup
import os

import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords


def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string
    
def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(string, return_str=True)

def stem(string):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in string.split()]
    return ' '.join(stems)

def lemmatize(string):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    return ' '.join(lemmas)
    
def remove_stopwords(string, extra_words = '',exclude_words = ''):
    stopword_list = stopwords.words('english')
    if len(extra_words) >0:
        stopword_list.append(extra_words)
    if len(exclude_words)>0:
        stopword_list.remove(exclude_words)

    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]

    article_without_stopwords = ' '.join(filtered_words)

    return article_without_stopwords


def prep_article(article):
    dt = {}
    
    article1 = article['content']
    article1 = basic_clean(article1)
    article1 = tokenize(article1)
    stemmed = stem(article1)
    lemmatized = lemmatize(article1)
    cleaned =  remove_stopwords(article1)  
                           
    dt.update({'category': article['topic']})
    dt.update({'title': article['title']})
    dt.update({'original': article['content']})
    dt.update({'stemmed': stemmed})
    dt.update({'lemmatized': lemmatized})
    dt.update({'clean': cleaned})    
    return dt

def prepare_article_data(list):
    l = []
    for i in range(len(list)):
        l.append(prep_article(list[i]))
    return l
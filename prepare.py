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
    

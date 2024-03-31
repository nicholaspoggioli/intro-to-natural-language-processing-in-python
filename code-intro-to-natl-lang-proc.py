# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:18:07 2024

@author: nalan
"""

# Regular expressions using the re library
import re

my_string = 'abcdef'

re.match("abc", my_string)   # Searches for 'abc' in 'abcdef'
re.search("abc", my_string)

re.match("cde", my_string)
re.search("cde", my_string)

# Tokenization using the nltk library. Free book at https://www.nltk.org/book/ch01.html
import nltk
# nltk.download()
# from nltk.book import *

# Frequency distribution
fdist1 = FreqDist(text1)
print(fdist1)
fdist1.most_common(50)
fdist1["whale"]
fdist1.plot(50, cumulative = True)

fdist1.hapaxes() # Hapaxes are words that appear only once in the corpus


# Fine-grained word selection
V = set(text1)
long_words = [w for w in V if len(w) > 15]
# w for w in V means word for word in V and checks each word
#   in V to see if it is greater than length 15
sorted(long_words)

# Collocations and bigrams
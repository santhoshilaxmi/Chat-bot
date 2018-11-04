e# -*- coding: utf-8 -*-
#from sklearn.feature_extraction.text import CountVectorizer
#train_set = ("The sky is blue.", "The sun is bright.")
#test_set = ("The sun in the sky is bright.",
 #   "We can see the shining sun, the bright sun.")
#stop_words=set(['all', 'six', 'less', 'being', 'indeed', 'over', 'move', 'anyway', 'four', 'not', 'own', 'through', 'yourselves'])
#vectorizer = CountVectorizer(stop_words=set(['all', 'six', 'less', 'being', 'indeed', 'over', 'move', 'anyway', 'four', 'not', 'own', 'through', 'yourselves']))
#print vectorizer
#"CountVectorizer(train_set,stop_words=set(['all', 'six', 'less', 'being', 'indeed', 'over', 'move', 'anyway', 'four', 'not', 'own', 'through', 'yourselves']))
#vectorizer.fit_transform(train_set)
#print vectorizer.vocabulary
# list of text documents
#text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
#vectorizer = CountVectorizer()
# tokenize and build vocab
#vectorizer.fit(text)
# summarize
#print(vectorizer.vocabulary_)
# encode document
#vector = vectorizer.transform(text)
# summarize encoded vector
#print(vector.shape)
#print(type(vector))
#print(vector.toarray())
#messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]
#print messages

from __future__ import print_function
import sys
print(sys.argv[1:], len(sys.argv))


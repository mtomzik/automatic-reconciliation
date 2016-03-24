# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def find_occurence(word, sentence_dictionary) : #word to słowo w wersji podstawowej
    for k in sentence_dictionary.keys() :
        value = sentence_dictionary[k]
        if word == value[-1] :
            return True

def get_word_info(word, sentence_dictionary) : #word w wersji podstawowej -> funkcja pobiera odmianę słowa i jego tagi ze zdania
    for k in sentence_dictionary.keys() :
        value = sentence_dictionary[k]
        if (word == value[-1]) :
            return (k, value[0], value[-1])


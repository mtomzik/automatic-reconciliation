# -*- coding: utf-8 -*-
import sys
import offline_version
from offline_version import *
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

def check_if_sententence_has_other_noun_or_ppron(sentence_dictionary) : #czy w zdaniu jest inny rzeczownik lub zaimek np. "niej
    nouns = []
    for k in sentence_dictionary.keys() :
        word_info = sentence_dictionary[k]
        if(word_info[0].split(":")[0] in ["subst", "noun", "ppron3"]) :
            nouns.append(k)
    return nouns

def check_if_noun_has_the_same_tags(word_tags, noun, sentence_dictionary) : #czy znaleziony w zdaniu rzeczownik jest w tej samej formie co szukany
    #word_tags -> tagi pierwotnego słowa
    #noun -> rzeczownik znaleziony w zdaniu
    checked_tags = sentence_dictionary[noun][0]
    splitted = checked_tags.split(":")
    word_tags_splitted = word_tags.split(":")
    if(splitted[0] in ["noun", "subst"] and checked_tags == word_tags) :
        return True
    elif(splitted[0] == "ppron3") :
        i = 1
        is_equal = True
        while(is_equal and i <4) :
            if(not(splitted[i]==word_tags_splitted[i])) :
                return False
            i += 1
        return is_equal
    else :
        return  False

def get_word_info_from_first_occurence(word, sentences) : #word to słowo podane, sentences to lista zdań do przeszukania
    for sentence in sentences :
        concraft = call_concraft(sentence)
        sentence_dictionary = parse_concraft_output()
        for k in sentence_dictionary.keys() :
            tags = sentence_dictionary[k][0]
            base_form = sentence_dictionary[k][1]
            if(base_form == word) :
                return (tags, sentences.index(sentence))
    return []

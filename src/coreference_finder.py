# -*- coding: utf-8 -*-
import sys
import concraft_tagging
from concraft_tagging import *
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

def check_if_sentence_has_valid_ppron3_form(word_tags, sentence_dictionary) :
    word_tags_splitted = word_tags.split(":")
    for k in sentence_dictionary.keys() :
        info = sentence_dictionary[k]
        tags = info[0].split(":")
        if(tags[0] == "ppron3") :
            i = 1
            is_equal = True
            while(is_equal and i <4) :
                if(not(tags[i]==word_tags_splitted[i])) :
                    return False
                i += 1
    return is_equal

def check_of_sentence_has_other_noun(word, sentence_dictionary) :
    found_nouns = []
    for k in sentence_dictionary.keys() :
        word_type = sentence_dictionary[k].split(":")[0]
        word_from_sentence  = sentence_dictionary[k][-1]
        if(word_from_sentence!=word and word_type in ["subst", "noun"]) :
            found_nouns.append(k)
    return found_nouns

def check_if_sententence_has_other_noun_or_ppron(sentence_dictionary) : #czy w zdaniu jest inny rzeczownik lub zaimek np. "niej
    nouns = []
    for k in sentence_dictionary.keys() :
        word_info = sentence_dictionary[k]
        if(word_info[0].split(":")[0] in ["subst", "noun", "ppron3"]) :
            nouns.append(k)
    return nouns

def mark_sentences_with_searched_word(word, data_structure) :
    for entity in data_structure :
        dictionary = entity[1]
        if(find_occurence(word, dictionary)) :
            entity[-1] = True

def mark_sentences_with_ppron_coreference(word, word_tags, data_structure) :
    for entity in data_structure :
        dictionary = entity[1]
        if(len(check_of_sentence_has_other_noun(word, dictionary)) == 0 and check_if_sentence_has_valid_ppron3_form(word_tags, dictionary)) :
            entity[-1] = True

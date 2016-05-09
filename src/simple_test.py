# -*- coding: utf-8 -*-
import sys
import codecs
import os
from sentence_tokenizing import call_toki, parse_toki_output
from concraft_tagging import call_concraft, parse_concraft_output
from coreference_finder import *
from utils.check_utils import *
from utils.tagger_utils import *
from congruence_finder import find_congruent_words
from morfeusz_integration import *
reload(sys)
sys.setdefaultencoding("utf-8")


def get_tag(dictionary, word) :
    for i in dictionary.keys() :
        if(dictionary[i][1] == word) :
            return dictionary[i][0]

def get_word(dictionary, word) :
        for i in dictionary.keys() :
            if(dictionary[i][1] == word) :
                return i

def build_new_tags(tags, gender_to_replace) :
    new_tags = ""
    t = tags.split(":")
    if t[0] == "noun" :
        new_tags += "subst" + ":"
    else :
        new_tags += t[0] + ":"
    for i in range(1, 3) :
        new_tags += t[i] + ":"
    new_tags += gender_to_replace + ":"
    for i in range(5, len(t)) :
        new_tags += t[i] + ":"
    return new_tags

def change_word() :
    pass

input_file = "/home/tusia/Desktop/magisterka/sample_texts/9.txt"
try :
    text = ""
    tok = "text.txt"
    call_toki(input_file, tok)
    sentences = parse_toki_output(tok)
    word = "lot"
    word_versions = [word, word.capitalize()]
    prepared_sentences = tag(sentences, "online", "WCRFT")
    tags = get_tags(word_versions[0], prepared_sentences)
    mark_sentences_with_searched_word(word_versions[0], prepared_sentences)
    mark_sentences_with_searched_word(word_versions[1], prepared_sentences)
    mark_sentences_with_ppron_coreference(word_versions[0], tags, prepared_sentences)
    # for i in prepared_sentences :
    #     print i
    word_sub = "podróż"
    possibilities = get_possibilities(word_sub)
    poss_list = parse_morfeusz_output(possibilities)
    tagged = tag_word(word_sub, "online", "WCRFT")
    word_sub_tags = tagged.values()[0][0]
    gender = word_sub_tags.split(":")[3]
    for sentence in prepared_sentences :
        if(sentence[2]) :
            dictionary = sentence[1]
            word_tags = get_tag(dictionary, word)
            con = find_congruent_words(word, dictionary, word_tags)
            words = con[word]
            base = get_word(dictionary, word)
            new_tags_base = build_new_tags(word_tags, gender)
            new_base = get_variant(new_tags_base, poss_list)
            sentence[0] =  sentence[0].replace(base, new_base)
            for word_n in words :
                word_poss = get_possibilities(dictionary[word_n][1])
                word_poss_list = parse_morfeusz_output(word_poss)
                congruent_word_tags = dictionary[word_n][0]
                new_tags = build_new_tags(congruent_word_tags, gender)
                new_form = get_variant(new_tags, word_poss_list)
                sentence[0] =  sentence[0].replace(word_n, new_form)
            text += sentence[0]

        else :
            text += sentence[0]
    print text

except IOError as e:
    print e.message
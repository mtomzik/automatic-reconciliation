# -*- coding: utf-8 -*-
import sys
import codecs
import os
from src.sentence_tokenizing import call_toki, parse_toki_output
from src.concraft_tagging import call_concraft, parse_concraft_output
from src.coreference_finder import *
from utils.check_utils import *
from utils.tagger_utils import *
reload(sys)
sys.setdefaultencoding("utf-8")

def get_words() :
    cor = []
    with codecs.open("/home/tusia/Desktop/magisterka/sample_texts/coreference_words.txt", encoding="utf-8", errors='ignore') as words :
        lines = words.readlines()
        for l in lines :
            cor.append(l.split(", ")[-1])
    return cor

def test() :
    partial_path = "/home/tusia/Desktop/magisterka/sample_texts/"
    words = get_words()
    for i in range(1,31) :
        path = partial_path+str(i)+".txt"
        print "analyzing file: " + path
        tokenized_file = "tokenized"+str(i)+".txt"
        call_toki(path, tokenized_file)
        sentences = parse_toki_output(tokenized_file)
        word = words[i].strip()
        version = "offline"
        tagger = "Concraft"
        prepared_sentences = tag(sentences, version, tagger)
        tags = get_tags(word, prepared_sentences)
        mark_sentences_with_searched_word(word, prepared_sentences)
        mark_sentences_with_searched_word(word, prepared_sentences)
        mark_sentences_with_ppron_coreference(word, tags, prepared_sentences)
        print path
        for i in prepared_sentences :
            print i
        print "================ \n"

test()
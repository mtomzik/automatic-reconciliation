# -*- coding: utf-8 -*-
import sys
import sentence_tokenizing
from sentence_tokenizing import * 
import online_version
from online_version import *
import offline_version
from offline_version import *
import congruence_finder
from congruence_finder import * 
import synonyms_finder
from synonyms_finder import *
import utils
from utils import print_utils
import coreference_finder
from coreference_finder import *

reload(sys)
sys.setdefaultencoding("utf-8")

#testy jak to się wszystko integruje
#dostępne taggery [wersja online]: "WCRFT", "Pantera", "Concrafr", "WMBT", "Polita"

# print "processing started"
file_n = "plain.txt"
file_o = "sentenced.txt"
call_toki(file_n, file_o)
sentences = parse_toki_output(file_o)
word = "sprawa"
# for sentence in sentences :
#     print sentence
#     if(word in sentence) :
#         concraft = call_concraft(sentence)
#         sentence_dictionary = parse_concraft_output()
#         word_tags = sentence_dictionary[word][0]

for sentence in sentences :
    concraft = call_concraft(sentence)
    sentence_dictionary = parse_concraft_output()
    if coreference_finder.find_occurence(word, sentence_dictionary) :
        word_info = coreference_finder.get_word_info(word, sentence_dictionary)
        word_form = word_info[0]
        word_tags = word_info[1]

# for sentence in sentences :
#     concraft = call_concraft(sentence)
#     structure = parse_concraft_output()
#     congruent_words = find_congruent_words(word_form, structure, word_tags)
#     print(print_utils.pretty_print_congruence_dictionary(congruent_words))

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

reload(sys)
sys.setdefaultencoding("utf-8")

#testy jak to się wszystko integruje
#dostępne taggery [wersja online]: "WCRFT", "Pantera", "Concrafr", "WMBT", "Polita"

def pretty_print(lista) :
	res = ""
	for i in lista :
		res = res + " " + i
	return res

# print "processing started"
file_n = "plain.txt"
file_o = "sentenced.txt"
call_toki(file_n, file_o)
sentences = parse_toki_output(file_o)
for sentence in sentences : 
	print sentence
	# print "**** multiservice ****"
	multiservice = call_multiservice(sentence, "Concraft")
	# concraft = call_concraft(sentence)
	sentence_dictionary = parse_multiservice_output(multiservice)
	# sentence_dictionary = parse_concraft_output()
	con = find_congruent_words("sprawą", sentence_dictionary)
	for i, j in con.items() : 
		print i + " -> " + pretty_print(j)
	# for i, j in  parse_multiservice_output(multiservice).items() : 
	# 	print i + " -> " + j
	# print "**** concraft ****"
	# concraft = call_concraft(sentence)
	# for i, j in parse_concraft_output().items() : 
	# 	print i + " -> " + j
	# print "##############"
# print "done & saved to file"

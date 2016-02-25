# -*- coding: utf-8 -*-
import sys
import codecs
import subprocess

#podział pliku wejściowego na zdania
#wymaga zainstalowango toki od NLP Wroc

reload(sys)
sys.setdefaultencoding("utf-8")

def call_toki(file_name, file_out) : 
	command = 'toki-app -q -f "\$bs| \$orth" < ' + file_name + ' > ' + file_out 
	# print command
	p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	out, err = p.communicate()

def parse_toki_output(tokenized_file) : 
	with codecs.open(tokenized_file, encoding="utf-8", errors='ignore') as tokenized : 
		lines = tokenized.readlines()
		sentences_list = lines[0].split("|")
	return sentences_list[1:]

def parse_toki_output_for_coreference(tokenized_file) :
	with codecs.open(tokenized_file, encoding="utf-8", errors='ignore') as tokenized : 
		lines = tokenized.readlines()
		sentences_list = lines[0].split("|")[1:]
		chunks = [sentences_list[i:i+2] for i in range(0, len(sentences_list) - 1)]
		result = []
		for chunk in chunks : 
			sentence = ""
			for i in chunk :
				sentence += i
			result.append(sentence)
		return result



# file_n = "plain.txt"
# file_o = "sentenced.txt"
# call_toki(file_n, file_o)
# sentences = parse_toki_output_for_coreference(file_o)
# for i in sentences : 
# 	print i
# -*- coding: utf-8 -*-
import sys
import subprocess
import codecs
import sentence_tokenizing
from sentence_tokenizing import *

#wersja offline - wymaga zainstalowanego Concrafta

reload(sys)
sys.setdefaultencoding("utf-8")

def call_concraft(sentence):
	command = 'echo "' + sentence + '" | concraft-pl tag -p  nkjp-model-0.2.gz > output.plain'
	p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	out, err = p.communicate()

def chunks(tags_list, n):
    n = max(1, n)
    return [tags_list[i:i + n] for i in range(0, len(tags_list), n)]

def get_lines_with_base_words(lines_list) :
	lines = []
	for i in lines_list : 
		line = i.strip().split("\t")
		if ((len(line) == 3 and line[-1] == "disamb" and (line[1].split(":")[0] != "aglt")) or (len(line) == 2 and line[-1] == "space")) : 
				lines.append(line)
	return lines

def solve_conflicts(lines_list) :
	if(len(lines_list) % 2 == 0) :
		return lines_list
	else : 
		for i in xrange(0,len(lines_list),2): 
			if(len(lines_list[i]) == 3) :
				lines_list.remove(lines_list[i]) #te tagi są takie same, konflikt jest z powodu np. archaicznej formy albo nazwy własnej
				return lines_list

def prepare_tags(lines_list) : #struktura postaci słowo -> (tagi, wersja podstawowa)
	tags = {}
	paired = chunks(solve_conflicts(lines_list), 2)
	for i in paired : 
		key = i[0][0].encode("utf-8")
		value = i[1][1]
		base_form = i[1][0]
		tags[key] = (value, base_form)
	return tags

def parse_concraft_output() : 
	tags = {}
	with codecs.open("output.plain", encoding="utf-8", errors='ignore') as concrafted : 
		tagged = concrafted.readlines() 
		lines = get_lines_with_base_words(tagged)
		return prepare_tags(lines)

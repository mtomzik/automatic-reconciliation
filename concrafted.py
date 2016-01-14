# -*- coding: utf-8 -*-
import sys
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")

tags = {}

with codecs.open("output.plain") as concrafted : 
	lines = concrafted.readlines() 
	base_words = []
	for i in range(0, len(lines)) :
		line = lines[i].split("\t")
		if (len(line) == 2) :
			tags[line[0]] = []
			base_words.append(i)
	for i in base_words : 
		print i
		# print str(len(i.split("\t"))) + " -> " + str(lines.index(i)) 

for k,v in tags.items() : 
	print k + " -> " + str(v)
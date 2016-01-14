# -*- coding: utf-8 -*-

import sys
import subprocess
import re

reload(sys)
sys.setdefaultencoding("utf-8")

def get_words_from_sentence(input_sentence) :
	return [word.lower() for word in re.findall(ur"[a-zA-ZżółćęśąźńŻÓŁĆĘŚĄŹŃ]+", input_sentence)]

def clean_sentence(input_sentence) : 
	input_sentence.encode("utf-8")
	words = get_words_from_sentence(input_sentence)
	clean = ""
	for i in words : 
		clean = clean + " " + i
	return clean

def call_morfologik(sentence):
	# print sentence
  	p = subprocess.Popen(['java', '-jar', 'morfologik-tools-1.9.0-standalone.jar', 'plstem'],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)
  	out, _ = p.communicate(u"".join(sentence).encode("utf-8"))
  	return out

def parse_morfologik_output(output) :
	tab = output.split("\n")
	possible_forms = {}
	for i in range(0, len(tab) - 2) :
		line = tab[i]
		line_content = line.split("\t")
		possible_forms[line_content[0]] = ""
	
	for i in range(0, len(tab) - 2) :
		line = tab[i]
		line_content = line.split("\t")
		if possible_forms[line_content[0]]=="" :
			possible_forms[line_content[0]] = line_content[-1]
		else : 
			possible_forms[line_content[0]] += "+" + line_content[-1]
	
	for k, v in possible_forms.items() : 
		possible_forms[k] = v.split("+")
	
	for k in possible_forms :
		tmp = possible_forms[k]
		lis = []
		for i in tmp :
			lis.append(i.split(":"))
		possible_forms[k] = lis
	return possible_forms

def check_if_word_exists_in_sentence(word, input_sentence) :
	if word in get_words_from_sentence(input_sentence) :
		return True
	else :
		return False

def find_verbs(parsed_output) :
	verbs = []
	for k in parsed_output :
		forms = parsed_output[k] #tablica wszelakich form
		for i in forms : 
			if i[0] == "verb" and k not in verbs :
				verbs.append(k)
	return verbs

def find_participles(parsed_output) :
	participles = []
	for k in parsed_output :
		forms = parsed_output[k]
		for i in forms : 
			if (i[0] == "ppas" or i[0] == "pact") and (k not in participles) :
				participles.append(k)
	return participles

def find_nouns(parsed_output) :
	nouns = []
	for k in parsed_output :
		forms = parsed_output[k]
		for i in forms : 
			if (i[0] == "subst") and (k not in nouns) and (k != "się") :
				nouns.append(k)
	return nouns

def find_adjectives(parsed_output) :
	adjectives = []
	for k in parsed_output :
		forms = parsed_output[k]
		for i in forms : 
			if (i[0] == "adj") and (k not in adjectives) :
				adjectives.append(k)
	return adjectives

def find_numerals(parsed_output) :
	numerals = []
	for k in parsed_output :
		forms = parsed_output[k]
		for i in forms : 
			if (i[0] == "num") and (k not in numerals) :
				numerals.append(k)
	return numerals

def check_if_words_are_in_congruence(base_word, checked_word, parsed_output) :
	if base_word == checked_word : 
		return False
	elif base_word not in parsed_output.keys() or checked_word not in parsed_output.keys() :
		return False
	else :
		base_word_tags = parsed_output[base_word]
		checked_word_tags = parsed_output[checked_word]
		is_base_word_noun = False
		can_checked_word_be_in_congruence = False
		for i in base_word_tags :
			if i[0] == "subst" :
				is_base_word_noun = True
		for i in checked_word_tags : 
			if i[0] in ["verb", "ppas", "pact", "num", "adj"] :
				can_checked_word_be_in_congruence = True
		if is_base_word_noun == False : 
			return False
		if can_checked_word_be_in_congruence == False : 
			return False
		else : 
			possible_base_word_tags = []
			for i in base_word_tags : 
				if i[0] == "subst" :
					base_word_details = i[1:]
					possible_base_word_tags.append(base_word_details)
			for i in checked_word_tags :
				if (i[0] == "verb" and (i[1]=="praet" or i[1] == "pot")) : 
					sin_pl = i[2]
					gend = i[3]
					for j in possible_base_word_tags : 
						sg = j[0]
						gen = j[2]
						if(sin_pl == sg and (gen == gend or gen in gend.split("."))) :
							return True
				else :
					sg_or_pl = i[1]
					declination = i[2]
					gender = i[3]
					if (i[0] == "adj") or (i[0] == "ppas") :
						for j in possible_base_word_tags : 
							sg = j[0]
							dec = j[1]
							gen = j[2]
							if (sg_or_pl == sg) and (declination == dec) and (gender == gen or gen in gender.split(".")) : 
								return True
					elif (i[0] == "pact" or i[0] == "num") :
						for j in possible_base_word_tags : 
							sg = j[0]
							dec = j[1]
							gen = j[2]
							if (sg_or_pl == sg) and (declination == dec or declination in dec.split(".")) and (gender == gen or gen in gender.split(".")) : 
								return True
			return False

def get_congruent_words(base_word, output) :
	if base_word not in output.keys() :
		return {}
	else :
		congruent_words = {}
		for k in output.keys() : 
			if check_if_words_are_in_congruence(base_word, k, output) == True : 
				congruent_words[k] = output[k]
		return congruent_words

def pretty_print_list(lista) : 
	content = "["
	for i in lista : 
		item = "("
		for j in i : 
			item += j + " "
		item += ") "
		content += item
	return content + "]"


sentence = u"Jeden mój jutrzejszy męczacy lot do Berlina został odwołany."
print sentence
clean = clean_sentence(sentence)
morfologik = call_morfologik(clean) 
output = parse_morfologik_output(morfologik) 
words = get_congruent_words("lot", output)
for k,v in words.items() :
	print k + " -> " + pretty_print_list(v)
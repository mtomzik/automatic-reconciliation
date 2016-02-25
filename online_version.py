# -*- coding: utf-8 -*-
import sys
import subprocess
import re
import json
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")

#wersja online, wymaga zainstalowanego thrift_clienta od IPIPAN
#dostępne taggery [wersja online]: "WCRFT", "Pantera", "Concrafr", "WMBT", "Polita"
#dostępne narzędzia do koreferencji: Ruler, Bartek

def call_multiservice(sentence, tagger, coreference_tool):
	# print sentence
  	p = subprocess.Popen(['python', 'thrift_client.py', tagger, 'Nerf', 'Spejd', 'MentionDetector', coreference_tool],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)
  	out, _ = p.communicate(u"".join(sentence).encode("utf-8"))
  	return out

def parse_multiservice_output(output) :
  tagged = json.loads(output)
  tags = {}
  coreferenced_words = []
  for i in tagged["coreferences"] :
    if(len(i["mentionIds"]) > 1) :
      coreferenced_words.append(i["dominant"])
  paragraphs = tagged["paragraphs"]
  for i in paragraphs[0]["sentences"] : 
    for j in i["words"] :
      if (len(j["chosenInterpretation"]["ctag"]) != "interp") : 
        key = j["orth"].encode("utf-8")
        value = j["chosenInterpretation"]["ctag"].lower()+":"+j["chosenInterpretation"]["msd"]
        base_form = j["chosenInterpretation"]["base"]
        tags[key] = (value, base_form)
  return (tags, coreferenced_words)

# def resolve_coreference(tags_dictionary, words_table) :
#   for i in tags.keys() :
#     if tags[i][1] in coreferenced_words :




# file_n = "sample_texts/8.txt"
# resolve_coreference(file_n)
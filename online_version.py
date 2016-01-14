# -*- coding: utf-8 -*-
import sys
import subprocess
import re
import json

reload(sys)
sys.setdefaultencoding("utf-8")

#wersja online, wymaga zainstalowanego thrift_clienta od IPIPAN

def call_multiservice(sentence, tagger):
	# print sentence
  	p = subprocess.Popen(['python', 'thrift_client.py', tagger, 'Nerf', 'Spejd'],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)
  	out, _ = p.communicate(u"".join(sentence).encode("utf-8"))
  	return out

def parse_multiservice_output(output) :
  tagged = json.loads(output)
  tags = {}
  # print json.dumps(tagged, indent=4, sort_keys=True)
  paragraphs = tagged["paragraphs"]
  for i in paragraphs[0]["sentences"] : 
    for j in i["words"] :
      if (len(j["chosenInterpretation"]["ctag"]) != "interp") : 
        tags[j["orth"].encode("utf-8")] = j["chosenInterpretation"]["ctag"].lower()+":"+j["chosenInterpretation"]["msd"]
  return tags

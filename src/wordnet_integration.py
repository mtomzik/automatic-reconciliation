# -*- coding: utf-8 -*-
import sys
import requests
import json

reload(sys)
sys.setdefaultencoding("utf-8")

def build_url(word_to_search, relation_type) :
    return "http://api.slowosiec.clarin-pl.eu:8080/plwordnet-api/synsets/search?lemma=" + word_to_search +"&&&partOfSpeech=noun&relationType=" + str(relation_type) + "&&&&&"

def send_get(url) :
    request = requests.get(url)
    return request.content

def parse_content(content) :
    words = []
    parsed = json.loads(content)
    # print json.dumps(parsed, indent=4, sort_keys=True)
    # for i in parsed :
    #     print str(i["id"]) + " -> " + i["name"]
    for i in parsed :
        words.append(i["lemma"]["word"])
    return words


url = build_url("koń", 60)
# # url = "http://api.slowosiec.clarin-pl.eu:8080/plwordnet-api/relationTypes"
content = send_get(url)
for i in parse_content(content) :
    print i
url2 = build_url("koń", 10)
content2 = send_get(url2)
print "________________________"
for i in parse_content(content2) :
    print i

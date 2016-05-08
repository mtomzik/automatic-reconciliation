# -*- coding: utf-8 -*-
import sys
import requests
import  json

reload(sys)
sys.setdefaultencoding("utf-8")

def build_url(word_to_search) :
    return "http://api.slowosiec.clarin-pl.eu:8080/plwordnet-api/synsets/search?lemma=" + word_to_search +"&&&partOfSpeech=noun&&"

def send_get(url) :
    request = requests.get(url)
    return request.content

def parse_content(content) :
    parsed = json.loads(content)
    # print json.dumps(parsed, indent=4, sort_keys=True)
    # for i in parsed :
    #     print str(i["id"]) + " -> " + i["name"]
    for i in parsed :
        print i["lemma"]["word"]


url = build_url("wyspa")
# url = "http://api.slowosiec.clarin-pl.eu:8080/plwordnet-api/relationTypes"
content = send_get(url)
parse_content(content)

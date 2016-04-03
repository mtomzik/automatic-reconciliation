# -*- coding: utf-8 -*-
import sys
import codecs
import os
from sentence_tokenizing import call_toki, parse_toki_output
from offline_version import call_concraft, parse_concraft_output
from coreference_finder import *
from utils.check_utils import *
from utils.tagger_utils import *
reload(sys)
sys.setdefaultencoding("utf-8")

#prosty interfejs command line'owy dla użyszkodnika.


def solve_tags_conflict(tags, tags_capitalized) :
    if(len(tags) == 0) :
        return tags_capitalized[0]
    elif (len(tags_capitalized) == 0 ) :
        return tags[0]
    elif (tags[1] > tags_capitalized[1]) :
        return  tags_capitalized[0]
    elif (tags_capitalized[1] > tags[1]) :
        return tags[0]
    else :
        return ""

print "Automatyczne dopasowywanie wartości kategorii gramatycznych w polskich tekstach"
print "wersja 1.0"
input_file = str(input("\t > Podaj ścieżkę do pliku z tekstem \n\t > "))
try :
    print(check_if_file_exists(input_file))
    tokenized_file = "sentenced.txt"
    call_toki(input_file, tokenized_file)
    sentences = parse_toki_output(tokenized_file)
    word = str(input("\t > Podaj słowo, które chcesz znaleźć w tekście\n\t > \t"))
    word_versions = [word, word.capitalize()]
    version = str(input("\t > Podaj wersję taggera, z której chcesz korzystać: online lub offline \n \t > "))
    if(not(check_version(version))) :
        raise IOError("\t > Podałeś złą wersję. Dopuszczalne formy to 'online' lub 'offline'")
    tagger = ""
    if (version == "offline") :
        tagger = "none"
    elif (version == "online") :
        tagger = str(input("\t > Podaj tagger, z którego chcesz skorzystać. Dostępne narzędzia: WCFT, WMBT, Polita, Pantera, Concraft \n \t > "))
        if(not(check_tagger(tagger))) :
            raise IOError("\t > Podałeś złą nazwę taggera. Dopuszczalne formy to: WCFT, WMBT, Polita, Pantera, Concraft")
    prepared_sentences = tag(sentences, version, tagger)
    mark_sentences_to_refactor(word_versions[0], prepared_sentences)
    mark_sentences_to_refactor(word_versions[1], prepared_sentences)
    for i in prepared_sentences :
        print i
except IOError as e:
    print e.message
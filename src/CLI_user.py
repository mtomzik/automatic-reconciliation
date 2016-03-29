# -*- coding: utf-8 -*-
import sys
import codecs
import os
import sentence_tokenizing
from sentence_tokenizing import call_toki, parse_toki_output
import offline_version
from offline_version import call_concraft, parse_concraft_output
import coreference_finder
from coreference_finder import find_occurence
reload(sys)
sys.setdefaultencoding("utf-8")

#prosty interfejs command line'owy dla użyszkodnika.

def check_if_file_exists(file_name) :
    if(not(os.path.exists(file_name))) :
        return "\t > Błąd: podany plik nie istnieje. Sprawdź poprawnośc ścieżki: " + file_name
    else :
        return "\t > Ścieżka do pliku jest poprawna. Nastąpi otwarcie pliku"


print "Automatyczne dopasowywanie wartości kategorii gramatycznych w polskich tekstach"
print "wersja 1.0"
input_file = input("\t > Podaj ścieżkę do pliku z tekstem \n\t > ")
print "\t > Podałeś ścieżkę do pliku: " + input_file
try :
    print(check_if_file_exists(input_file))
    tokenized_file = "sentenced.txt"
    call_toki(input_file, tokenized_file)
    sentences = parse_toki_output(tokenized_file)
    word = input("\t > Podaj słowo, które chcesz znaleźć w tekście\n\t > ")
    word_versions = [word, word.capitalize()]
    for sentence in sentences :
        concraft = call_concraft(sentence)
        sentence_dictionary = parse_concraft_output()
        if coreference_finder.find_occurence(word_versions[0], sentence_dictionary) or coreference_finder.find_occurence(word_versions[1], sentence_dictionary) :
            print sentence
except IOError :
    print "Błąd: wystąpił błąd podczas próby otwarcia pliku. Sprawdź poprawnośc ścieżki: " + input_file
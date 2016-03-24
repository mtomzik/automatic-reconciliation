# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
def pretty_print_list(lista) :
    result = ""
    for i in lista:
        result += i + " "
    return result

def pretty_print_sentence_dictionary(dictionary) :
    result = ""
    for k,v in dictionary.items() :
       result += k + " -> " + pretty_print_list(v[0]) + " -> " + v[1] + "\n"
    return result

def pretty_print_congruence_dictionary(dictionary) :
    result = ""
    for k,v in dictionary.items() :
        result += k + " -> " + pretty_print_list(v)
    return result
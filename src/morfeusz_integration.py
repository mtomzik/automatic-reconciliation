# -*- coding: utf-8 -*-
import sys
from utils import command_line_utils
reload(sys)
sys.setdefaultencoding("utf-8")

#integracja z Morfeusz SGJP
#wymagany zainstalowan morfeusz
#przyjmuje tagi szukanego słowa i zwraca jego formę

def get_possibilities(word) :
    command = "echo '" + word + "' | morfeusz_generator "
    return command_line_utils.call_command(command)

def parse_morfeusz_output(output) :
    start = '['
    end = ']'
    possible_forms=output[output.find(start)+len(start):output.find(end)].split("\n")
    parsed_output = []
    for form in possible_forms :
        f = form.split(",")
        variant = (f[0].lstrip(), f[2])
        parsed_output.append(variant)
    return parsed_output

def get_variant(tags, variants_list) :
    for i in variants_list :
        if tags == i[1] :
            return i[0]
        else :
            taggs = tags.split(":")
            var = i[1].split(":")
            if(taggs[0] == var[0] and taggs[1] == var[1]) :
                if(taggs[2] == var[2] or taggs[2] in var[2].split(".")) :
                    if(taggs[3] == var[3] or taggs[3] in var[3].split(".")) :
                            return i[0]





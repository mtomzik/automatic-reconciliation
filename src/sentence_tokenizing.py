# -*- coding: utf-8 -*-
import sys
import codecs
import subprocess
import utils
from utils import command_line_utils


#podział pliku wejściowego na zdania
#wymaga zainstalowango toki od NLP Wroc

reload(sys)
sys.setdefaultencoding("utf-8")

def call_toki(file_name, file_out) : 
	command = 'toki-app -q -f "\$bs| \$orth" < ' + file_name + ' > ' + file_out
	command_line_utils.call_command(command)

def parse_toki_output(tokenized_file) : 
	with codecs.open(tokenized_file, encoding="utf-8", errors='ignore') as tokenized : 
		lines = tokenized.readlines()
		sentences_list = lines[0].split("|")
	return sentences_list[1:]

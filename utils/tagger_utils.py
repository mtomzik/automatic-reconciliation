import sys
import src.concraft_tagging
import src.multiservice_tagging
from src.multiservice_tagging import *
from src.concraft_tagging import *
from check_utils import check_tagger
reload(sys)
sys.setdefaultencoding("utf-8")

def tag(sentences_list, version, tagger) :
    output = []
    needs_refactor = False
    if(version == "offline") :
        for sentence in sentences_list :
            concraft = call_concraft(sentence)
            dictionary = parse_concraft_output()
            entity = [sentence, dictionary, needs_refactor]
            output.append(entity)
    elif (version == "online" and check_tagger(tagger)) :
        for sentence in sentences_list :
            multiservice = call_multiservice(sentence, tagger)
            dictionary = parse_multiservice_output(multiservice)
            needs_refactor = False
            entity = [sentence, dictionary, needs_refactor]
            output.append(entity)
    return output

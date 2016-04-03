import sys
import src.offline_version
import src.online_version
from src.online_version import *
from src.offline_version import *
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

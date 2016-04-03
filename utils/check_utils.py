# -*- coding: utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
def check_tagger(tagger) :
    if tagger in ["WCRFT", "WMBT", "Concraft", "Polita", "Pantera"] :
        return True
    else:
        return False

def check_version(version) :
    if version in ["online", "offline"] :
        return True
    else:
        return False

def check_if_file_exists(file_name) :
    if(not(os.path.exists(file_name))) :
        raise IOError("\t > Błąd: podany plik nie istnieje. Sprawdź poprawnośc ścieżki: " + file_name)
    else :
        return "\t > Ścieżka do pliku jest poprawna. Nastąpi otwarcie pliku"
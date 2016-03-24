# -*- coding: utf-8 -*-
import subprocess
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def call_command(command) :
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out
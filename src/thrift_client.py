#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Michał Lenart
# This is THRIFT client for Multiservice platform.
# It is available on the same license as the Multiservice itself.
#

import sys
import re
import jsonpickle
import json
import time
import StringIO
from optparse import OptionParser
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from multiservice.facade import Multiservice
from multiservice.facade.ttypes import *
from multiservice.types.ttypes import *

reload(sys)
sys.setdefaultencoding("utf-8")

    
def createSampleRequest(text, serviceNames):
    ttext=TText(paragraphs=[TParagraph(text=chunk) 
                            for chunk in re.split(r'\n\n+', text)])
                            
    chain = [RequestPart(serviceName=name) for name in serviceNames]	
    request = ObjectRequest(ttext, chain)
    return request

def getThriftTransportAndClient(host, port):
    transport = TSocket.TSocket(host, port)
    try:
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Multiservice.Client(protocol)
        transport.open()
        return (transport, client)
    except:
        transport.close()
        raise

def getResultAsJSON(result):
    jsonStr = jsonpickle.encode(result, unpicklable=False)
    return json.dumps(json.load(StringIO.StringIO(jsonStr)), sort_keys=True, indent=4)
    
    
def go():
    parser = OptionParser()
    parser.add_option('-p', '--port', type='int', action='store',
                      dest='port', default=20000,
                      help='multiservice port; default: 20000')
    parser.add_option('--host', type='string', action='store',
                      dest='host', default='multiservice.nlp.ipipan.waw.pl',
                      help='multiservice host; default: multiservice.nlp.ipipan.waw.pl')
    (opts, args) = parser.parse_args()

    if len(args) == 0:
    	print "Processing chain was not specified!"
    	return

    transport, client = getThriftTransportAndClient(opts.host, opts.port)
    request = createSampleRequest(sys.stdin.read(), args)
    try:
        token = client.putObjectRequest(request)
        status = None
        while status not in [RequestStatus.DONE, RequestStatus.FAILED]:
            status = client.getRequestStatus(token)
            time.sleep(0.1)
        if status == RequestStatus.DONE:
            result = client.getResultObject(token)
            print getResultAsJSON(result)
        else:
            print >> sys.stderr, client.getException(token)
    finally:
         transport.close()

if __name__ == '__main__':
    go()

#!/usr/bin/env python2.7
import sys
import os
sys.path.append( os.getcwd() )
sys.path.insert( 1, 'markdown' ) #Pickup libs, rdflib etc., from shipped lib directory
import rdflib
from sdotermsource import *
from sdoterm import *
from localmarkdown import Markdown

Markdown.setWikilinkCssClass("localLink")
Markdown.setWikilinkPrePath("/")


triplesfile = "data/schemaorg-all-https.nt"
termgraph = rdflib.Graph()
termgraph.parse(triplesfile, format="nt")

print ("loaded %s triples" % len(termgraph))

SdoTermSource.setQueryGraph(termgraph)
terms = terms = SdoTermSource.getAllTerms()
print ("Terms Count: %s" % len(terms))

import schemapages_pb2

sdotypemap = {
    SdoTerm.TYPE: schemapages_pb2.TermType.TYPE,
    SdoTerm.PROPERTY: schemapages_pb2.TermType.PROPERTY,
    SdoTerm.DATATYPE: schemapages_pb2.TermType.DATATYPE,
    SdoTerm.ENUMERATION: schemapages_pb2.TermType.ENUMERATION,
    SdoTerm.ENUMERATIONVALUE: schemapages_pb2.TermType.ENUMERATIONVALUE,
    SdoTerm.REFERENCE: schemapages_pb2.TermType.REFERENCE
}

def termdescriptorPopulate(termdesc,term):
    termdesc.termType = sdotypemap[term.termType]
    termdesc.uri = term.uri
    termdesc.label = term.label
    termdesc.acknowledgements.extend(term.acknowledgements)
    for i in term.superPaths:
        sp = termdesc.superPaths.add()
        sp.superPath.extend(i)
    termdesc.comment = term.comment
    termdesc.equivalents.extend(term.equivalents)
    termdesc.pending = term.pending
    termdesc.retired = term.retired
    termdesc.sources.extend(term.sources)
    

def populateMsg(msg=None,term=None):
    if term.expanded:
        return populateExpandedMsg(msg=msg,term=term)
    log.info("Pop %s type %s" %(term.id,term.termType))
    if msg:  
        log.info("Passed a %s" % msg.__class__.__name__)
    if not msg:
        if term.termType == SdoTerm.TYPE or term.termType == SdoTerm.DATATYPE or term.termType == SdoTerm.ENUMERATION:
            msg = schemapages_pb2.SDOBaseType()
        elif term.termType == SdoTerm.PROPERTY:
            msg = schemapages_pb2.SDOProperty()
        elif term.termType == SdoTerm.ENUMERATIONVALUE:
            msg = schemapages_pb2.SDOEnumerationValue()
        elif term.termType == SdoTerm.REFERENCE:
            msg = schemapages_pb2.SDOReference()
        else:
            print("Unknown term type '%s'" % term.termType)
        log.info("Alocated a %s" % msg.__class__.__name__)

    msg.id = term.id
    termdescriptorPopulate(msg.termdescriptor.add(),term)
    
    if term.termType == SdoTerm.TYPE or term.termType == SdoTerm.DATATYPE or term.termType == SdoTerm.ENUMERATION:
        msg.properties.extend(term.properties)
        msg.expectedTypeFor.extend(term.expectedTypeFor)
        msg.termStack.extend(term.termStack)
        msg.subs.extend(term.subs)
        msg.supers.extend(term.supers)
        msg.supersedes.extend(term.supersedes)
        if term.termType == SdoTerm.ENUMERATION:
            msg.enumerationMembers.extend(term.enumerationMembers)
    elif term.termType == SdoTerm.PROPERTY:
        msg.domainIncludes.extend(term.domainIncludes)
        msg.rangeIncludes.extend(term.rangeIncludes)
        msg.supersedes.extend(term.supersedes)
        msg.termStack.extend(term.termStack)
        msg.subs.extend(term.subs)
        msg.supers.extend(term.supers)
    elif term.termType == SdoTerm.ENUMERATIONVALUE:
        msg.enumerationParent = term.enumerationParent
        msg.supersedes.extend(term.supersedes)
    elif term.termType == SdoTerm.REFERENCE:
        pass
    
    return msg

def populateExpandedMsg(msg=None,term=None,inTermStack=True):
    log.info("EXPop %s type %s" %(term.id,term.termType)) 
    if msg:
        log.info("Passed a %s" % msg.__class__.__name__) 
    if not msg:
        if term.termType == SdoTerm.TYPE or term.termType == SdoTerm.DATATYPE or term.termType == SdoTerm.ENUMERATION:
            if not inTermStack:
                msg = schemapages_pb2.SDOBaseTypeExpanded()
            else:
                msg = schemapages_pb2.SDOBaseTypeExpandedProps()
        else:
            print("Unknown term type '%s'" % term.termType)
        log.info("Alocated a %s" % msg.__class__.__name__)

    msg.id = term.id
    msgterm = msg.termdescriptor.add()
    termdescriptorPopulate(msgterm,term)

    for i in term.properties:
        populateMsg(msg.properties.add(),i)
    for i in term.expectedTypeFor:
        populateMsg(msg.expectedTypeFor.add(),i)
    if inTermStack:
        msg.termStack.extend(term.termStack)
    else:
        for i in term.termStack:
            populateMsg(msg.termStack.add(),i,inTermStack=True)
    msg.subs.extend(term.subs)
    msg.supers.extend(term.supers)
    msg.supersedes.extend(term.supersedes)
    msg.supersedes.extend(term.supersedes)
    if term.termType == SdoTerm.ENUMERATION:
        msg.enumerationMembers.extend(term.enumerationMembers)
    return msg
    
def term2protomsgExpanded(termid):
    term = SdoTermSource.getTerm(termid,expanded=True)
    
    msg = populateMsg(term=term)
    
    msgstr = msg.SerializeToString()
    return msgstr
    
out = term2protomsgExpanded("Permit")
print(len(out))
sys.exit()
    
#print(':'.join(x.encode('hex') for x in msgstr))
import time,datetime
start = datetime.datetime.now()
for t in terms:
    tic = datetime.datetime.now()
    ms = term2protomsg(t)
    filename = "protomsgs/" + t +".msg"
    f = open(filename,"w")
    f.write(ms)
    f.close()
    print("Term: %s - %s" % (t, str(datetime.datetime.now()-tic)))
print ("All terms took %s seconds" % str(datetime.datetime.now()-start))
    




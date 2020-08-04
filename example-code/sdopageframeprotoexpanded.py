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
terms = SdoTermSource.getAllTerms()
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

#Populate termdescriptor - message common sub-message of all (except REFERENCE)
def termdescriptorPopulate(termdesc,term):
    termdesc.termType = sdotypemap[term.termType]
    termdesc.uri = term.uri
    if term.termType != SdoTerm.REFERENCE:
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
        termdesc.supersededBy = term.supersededBy
        termdesc.supersedes.extend(term.supersedes)
    
#Populate message for passed simple (non-expanded) term
#If msg != None the empty message will have been created by previous nested add() call
#If no msg passed one of appropriate type is created
def populateSimpleMsg(msg=None,term=None,inTermStack=False):
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

    msg.id = term.id
    if term.termType == SdoTerm.REFERENCE:
        #Reference message only has id & uri values
        msg.uri = term.uri
    else:
        #Populate standard submessage
        termdescriptorPopulate(msg.termdescriptor.add(),term)
    
        if term.termType == SdoTerm.TYPE or term.termType == SdoTerm.DATATYPE or term.termType == SdoTerm.ENUMERATION:
            msg.properties.extend(term.properties)
            msg.expectedTypeFor.extend(term.expectedTypeFor)
            msg.termStack.extend(term.termStack)
            msg.subs.extend(term.subs)
            msg.supers.extend(term.supers)
            if term.termType == SdoTerm.ENUMERATION:
                msg.enumerationMembers.extend(term.enumerationMembers)
        elif term.termType == SdoTerm.PROPERTY:
            msg.domainIncludes.extend(term.domainIncludes)
            msg.rangeIncludes.extend(term.rangeIncludes)
            msg.termStack.extend(term.termStack)
            msg.subs.extend(term.subs)
            msg.supers.extend(term.supers)
        elif term.termType == SdoTerm.ENUMERATIONVALUE:
            msg.enumerationParent = term.enumerationParent
    return msg

#Populate message for passed expanded term
#If msg != None the empty message will have been created by previous nested add() call
#If no msg passed one of appropriate type is created
def populateExpandedMsg(msg=None,term=None,inTermStack=False):
    if not msg:
        if term.termType == SdoTerm.TYPE or term.termType == SdoTerm.DATATYPE or term.termType == SdoTerm.ENUMERATION:
            if not inTermStack:
                msg = schemapages_pb2.SDOBaseTypeExpanded()
            else:
                #Termstack nested terms do not have their termstack expanded
                msg = schemapages_pb2.SDOBaseTypeExpandedPropsOnly()
        else:
            print("Unknown term type '%s'" % term.termType)

    msg.id = term.id
    termdescriptorPopulate(msg.termdescriptor.add(),term)

    for i in term.properties:
        populateMsg(msg.properties.add(),i)
    for i in term.expectedTypeFor:
        populateMsg(msg.expectedTypeFor.add(),i)
    if inTermStack:  #Nested expanded terms only have termStack as string array
        msg.termStack.extend(term.termStack)
    else:
        for i in term.termStack:
            populateMsg(msg.termStack.add(),i,inTermStack=True)
    msg.subs.extend(term.subs)
    msg.supers.extend(term.supers)
    if term.termType == SdoTerm.ENUMERATION:
        msg.enumerationMembers.extend(term.enumerationMembers)
    return msg

#Populate message for passed term 
#If msg != None the empty message will have been created by previous nested add() call
def populateMsg(msg=None,term=None,inTermStack=False):
    if term.expanded:
        if term.termType == SdoTerm.TYPE or term.termType == SdoTerm.DATATYPE or term.termType == SdoTerm.ENUMERATION:
            return populateExpandedMsg(msg=msg,term=term,inTermStack=inTermStack)
    
    return populateSimpleMsg(msg=msg,term=term,inTermStack=inTermStack)

    
import time,datetime

start = datetime.datetime.now() #debug
for t in terms:
    tic = datetime.datetime.now() #debug
    
    term = SdoTermSource.getTerm(t,expanded=True)
    msg = populateMsg(term=term).SerializeToString()
    filename = "protomsgs/" + t +".msg"
    f = open(filename,"wb")
    f.write(msg)
    f.close()
    
    print("Term: %s - %s" % (t, str(datetime.datetime.now()-tic))) #debug
print ("All terms took %s seconds" % str(datetime.datetime.now()-start)) #debug
    




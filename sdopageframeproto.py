#!/usr/bin/env python2.7
import rdflib
from sdotermsource import *
from sdoterm import *
from localmarkdown import Markdown

Markdown.setWikilinkCssClass("localLink")
Markdown.setWikilinkPrePath("/")


triplesfile = "schemaorg-all-https.nt"
termgraph = rdflib.Graph()
termgraph.parse(triplesfile, format="nt")

print ("loaded %s triples" % len(termgraph))

SdoTermSource.setQueryGraph(termgraph)
terms = terms = SdoTermSource.getAllTerms()
print ("Terms Count: %s" % len(terms))

import schemapages_pb2


def term2protomsg(termid):
    term = SdoTermSource.getTerm(termid)
    if term.termType == SdoTerm.TYPE:
        msg = schemapages_pb2.SDOType()
        msgTermType = schemapages_pb2.TermType.TYPE
    elif term.termType == SdoTerm.PROPERTY:
        msg = schemapages_pb2.SDOProperty()
        msgTermType = schemapages_pb2.TermType.PROPERTY
    elif term.termType == SdoTerm.DATATYPE:
        msg = schemapages_pb2.SDODataType()
        msgTermType = schemapages_pb2.TermType.DATATYPE
    elif term.termType == SdoTerm.ENUMERATION:
        msg = schemapages_pb2.SDOEnumeration()
        msgTermType = schemapages_pb2.TermType.ENUMERATION
    elif term.termType == SdoTerm.ENUMERATIONVALUE:
        msg = schemapages_pb2.SDOEnumerationValue()
        msgTermType = schemapages_pb2.TermType.ENUMERATIONVALUE
    elif term.termType == SdoTerm.REFERENCE:
        msg = schemapages_pb2.SDOReference()
        msgTermType = schemapages_pb2.TermType.REFERENCE
    else:
        print("Unknown term type '%s'" % term.termType)


    msg.id = term.id

    msgterm = msg.termdescriptor.add()

    msgterm.termType = msgTermType
    msgterm.uri = term.uri
    msgterm.label = term.label
    msgterm.acknowledgements.extend(term.acknowledgements)
    for i in term.breadcrumbs:
        bc = msgterm.breadcrumbs.add()
        bc.breadcrumb.extend(i)
    msgterm.comment = term.comment
    msgterm.equivalents.extend(term.equivalents)
    msgterm.pending = term.pending
    msgterm.retired = term.retired
    msgterm.sources.extend(term.sources)
    msgterm.subs.extend(term.subs)
    msgterm.supers.extend(term.supers)
    msgterm.supersededBy = term.supersededBy
    msgterm.supersedes.extend(term.supersedes)
    msgterm.termStack.extend(term.termStack)


    if term.termType == SdoTerm.TYPE:
        msg.properties.extend(term.properties)
        msg.allProperties.extend(term.allProperties)
        msg.expectedTypeFor.extend(term.expectedTypeFor)
    elif term.termType == SdoTerm.PROPERTY:
        msg.domainIncludes.extend(term.domainIncludes)
        msg.rangeIncludes.extend(term.rangeIncludes)
    elif term.termType == SdoTerm.DATATYPE:
        msg.properties.extend(term.properties)
        msg.allProperties.extend(term.allProperties)
        msg.expectedTypeFor.extend(term.expectedTypeFor)
    elif term.termType == SdoTerm.ENUMERATION:
        msg.properties.extend(term.properties)
        msg.allProperties.extend(term.allProperties)
        msg.expectedTypeFor.extend(term.expectedTypeFor)
    elif term.termType == SdoTerm.ENUMERATIONVALUE:
        msg.enumerationParent = term.enumerationParent
    elif term.termType == SdoTerm.REFERENCE:
        pass



    msgstr = msg.SerializeToString()
    return msgstr
    
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
    




#!/usr/bin/env python2.7
import rdflib
from sdotermsource import *
from sdoterm import *


triplesfile = "schemaorg-all-https.nt"
termgraph = rdflib.Graph()
termgraph.parse(triplesfile, format="nt")
termgraph.bind("schema","https://schema.org/")
termgraph.bind("owl","http://www.w3.org/2002/07/owl#")
termgraph.bind("dc","http://purl.org/dc/elements/1.1/")
termgraph.bind("dct","http://purl.org/dc/terms/")

print ("loaded %s triples" % len(termgraph))

SdoTermSource.setQueryGraph(termgraph)

term = SdoTermSource.getTerm("FoodEstablishment")

print("")
print("TYPE: %s" % term.termType)
print("URI: %s" % term.uri)
print("ID: %s" % term.id)
print("LABEL: %s" % term.label)

print("COMMENT: %s" % term.comment)
print("COMMENTS: %s" % term.comments)
print("EQIVALENTS: %s" % term.equivalents)
print("EXAMPLES: %s" % term.examples)
print("PENDING: %s" % term.pending)
print("RETIRED: %s" % term.retired)
print("SOURCES: %s" % term.sources)
print("SUBS: %s" % term.subs)
print("SUPERS: %s" % term.supers)
print("SUPERSEDEDBY: %s" % term.supersededBy)
print("SUPERSEDES: %s" % term.supersedes)
print("TERMSTACK: %s" % term.termStack)


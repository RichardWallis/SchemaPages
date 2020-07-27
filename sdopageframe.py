#!/usr/bin/env python2.7
import rdflib
from apirdfterm import *


triplesfile = "schemaorg-all-https.nt"
termgraph = rdflib.Graph()
termgraph.parse(triplesfile, format="nt")
termgraph.bind("schema","https://schema.org/")

print ("loaded %s triples" % len(termgraph))

VTerm.setQueryGraph(termgraph)

term = VTerm.getTerm("FoodEstablishment")

print()
print("TYPE: %s" % term.ttype)
print("URI: %s" % term.uri)
print("ID: %s" % term.id)
print("LABEL: %s" % term.label)
print("PARENT: %s" % term.parent)
print("PROPS: %s" % term.props)
print("COMMENT: %s" % term.comment)
print("TERMSSTACK: %s" % term.termStack)


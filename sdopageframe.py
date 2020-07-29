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

term = SdoTermSource.getTerm("CompleteDataFeed")

print("")
print("TYPE: %s" % term.termType)
print("URI: %s" % term.uri)
print("ID: %s" % term.id)
print("LABEL: %s" % term.label)

print("BREADCRUMBS: %s" % term.breadcrumbs)
print("COMMENT: %s" % term.comment)
print("EQIVALENTS: %s" % term.equivalents)
print("EXAMPLES: %s" % term.examples)
print("PENDING: %s" % term.pending)
print("RETIRED: %s" % term.retired)
print("SOURCES: %s" % term.sources)
print("acknowledgements" % term.acknowledgements)
print("SUBS: %s" % term.subs)
print("SUPERS: %s" % term.supers)
print("SUPERSEDEDBY: %s" % term.supersededBy)
print("SUPERSEDES: %s" % term.supersedes)
print("TERMSTACK: %s" % term.termStack)

for stackElement in term.termStack:
  print("Element: %s" % stackElement)
  
if term.termType == SdoTerm.TYPE or term.termType == SdoTerm.ENUMERATION:
    print("Properties: %s" % term.properties)
    print("All properties: %s" % term.allProperties)
    print("Expected Type for: %s" % term.expectedTypeFor)
      
if term.termType == SdoTerm.PROPERTY:
    print("Domain includes: %s" % term.domainIncludes)
    print("Range includes: %s" % term.rangeIncludes)

if term.termType == SdoTerm.ENUMERATION:
    print("Enumeration Members: %s" % term.enumerationMembers)
    
    
if term.termType == SdoTerm.ENUMERATIONVALUE:
    print("Parent Enumeration: %s" %  term.enumerationParent)
    
for p in term.properties:
  prop = SdoTermSource.getTerm(p)
  print("Prop: %s.  Pending: %s" % (prop.id,prop.pending))
  print("   Expected Types: %s" % prop.rangeIncludes)
  print("   Comment: %s" % prop.comment)




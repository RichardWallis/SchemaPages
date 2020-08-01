#!/usr/bin/env python2.7
import sys
import os
sys.path.append( os.getcwd() )
sys.path.insert( 1, 'markdown' ) #Pickup libs, rdflib etc., from shipped lib directory

import rdflib
from sdotermsource import *
from sdoterm import *
from localmarkdown import Markdown

import jinja2 
Markdown.setWikilinkCssClass("localLink")
Markdown.setWikilinkPrePath("/")


triplesfile = "data/schemaorg-all-https.nt"
termgraph = rdflib.Graph()
termgraph.parse(triplesfile, format="nt")

print ("loaded %s triples" % len(termgraph))

SdoTermSource.setQueryGraph(termgraph)
#print ("Types Count: %s" % len(SdoTermSource.getAllTypes(expanded=False)))
#print ("Properties Count: %s" % len(SdoTermSource.getAllProperties(expanded=False)))


jenv = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"),
        extensions=['jinja2.ext.autoescape'], autoescape=True, cache_size=0)

def templateRender(term):
    tvars = {
        'sitename': "SchemaPages",
        'menu_sel': "Schemas",
        'home_page': "False",
        'href_prefix': "/",
        'term': term
    }
    psge=None
    if term.termType == SdoTerm.TYPE:
        page = "TypePageEx.tpl"
    elif term.termType == SdoTerm.PROPERTY:
        page = "PropertyPage.tpl"
    elif term.termType == SdoTerm.ENUMERATION:
        page = "EnumerationPage.tpl"
    elif term.termType == SdoTerm.ENUMERATIONVALUE:
        page = "EnumerationValuePage.tpl"
    elif term.termType == SdoTerm.DATATYPE:
        page = "DataTypePage.tpl"
    else:
        print("Invalid term type: %s" % term.termType)
        return
        
    
    template = jenv.get_template(page)
    #print(template.render(tvars))
    return template.render(tvars)
    
terms = SdoTermSource.getAllTerms()
print("Processing %s terms" % len(terms))

#term = SdoTermSource.getTerm("Permit",expanded=True)
#pageout = templateRender(term)

#print(pageout)

terms = ["Permit"]

import timeit
start = timeit.timeit()
for t in terms:
    tic = timeit.timeit()
    term = SdoTermSource.getTerm(t,expanded=True)
    #term = SdoTermSource.getTerm("Book")
    pageout = templateRender(term)
    filename = "siteout/" + term.id +".html"
    f = open(filename,"w")
    f.write(pageout)
    f.close()
    toc = timeit.timeit()
    log.info("Term: %s - %s" % (t, toc -tic))
    
stop = timeit.timeit()
print ("All terms took %s seconds" % (stop - start))



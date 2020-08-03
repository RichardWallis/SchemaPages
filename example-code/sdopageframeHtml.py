#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

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
        'href_prefix': "",
        'term': term
    }
    psge=None
    if term.termType == SdoTerm.TYPE:
        page = "TypePageEx.tpl"
    elif term.termType == SdoTerm.PROPERTY:
        page = "PropertyPage.tpl"
    elif term.termType == SdoTerm.ENUMERATION:
        page = "EnumerationPageEx.tpl"
    elif term.termType == SdoTerm.ENUMERATIONVALUE:
        page = "EnumerationValuePageEx.tpl"
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

terms = ["Permit","Thing","about","CreativeWork","Audiobook","Recommendation","EBook","BookFormatType"]


import time,datetime
start = datetime.datetime.now()
lastCount = 0
for t in terms:
    tic = datetime.datetime.now()
    term = SdoTermSource.getTerm(t,expanded=True)
    pageout = templateRender(term)
    #filename = "SchemaPages/siteout/" + term.id +".html"
    filename = "siteout/" + term.id +".html"
    f = open(filename,"w")
    f.write(pageout)
    f.close()
    termsofar = len(SdoTermSource.termCache())
    created = termsofar - lastCount
    lastCount = termsofar
    print("Term: %s (%d) - %s" % (t, created, str(datetime.datetime.now()-tic)))
    
print ("All terms took %s seconds" % str(datetime.datetime.now()-start))




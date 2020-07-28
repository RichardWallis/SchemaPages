#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
logging.basicConfig(level=logging.INFO) # dev_appserver.py --log_level debug .
log = logging.getLogger(__name__)

#from testharness import *

import rdflib
from rdflib import URIRef
import io

VOCABURI="https://schema.org/"

class SdoTerm():
    TYPE = "Type"
    PROPERTY = "Property"
    DATATYPE = "Datatype"
    ENUMERATION = "Enumeration"
    ENUMERATIONVALUE = "Enumerationvalue"
    REFERENCE = "Reference"
    
    def __init__(self,termType,Id,uri,label):
        self.termType = termType
        self.uri = uri
        self.id = Id
        self.label = label
        
        self.acknowledgements = None
        self.comment = None
        self.comments = None
        self.equivalents = None
        self.examples = None
        self.pending = False
        self.retired = False
        self.sources = None
        self.subs = None
        self.supers = None
        self.supersededBy = None
        self.supersedes = None
        self.termStack = None
        

class SdoType(SdoTerm):

    def __init__(self,Id,uri,label):
        SdoTerm.__init__(self,SdoTerm.TYPE,Id,uri,label)
    
    
class SdoProperty(SdoTerm):

    def __init__(self,Id,uri,label):
        SdoTerm.__init__(self,SdoTerm.PROPERTY,Id,uri,label)
    
    
class SdoDataType(SdoTerm):

    def __init__(self,Id,uri,label):
        SdoTerm.__init__(self,SdoTerm.DATATYPE,Id,uri,label)


class SdoEnumeration(SdoTerm):

    def __init__(self,Id,uri,label):
        SdoTerm.__init__(self,SdoTerm.ENUMERATION,Id,uri,label)

    
class SdoEnumerationvalue(SdoTerm):

    def __init__(self,Id,uri,label):
        SdoTerm.__init__(self,SdoTerm.ENUMERATIONVALUE,Id,uri,label)

    
class SdoReference(SdoTerm):

    def __init__(self,Id,uri,label):
        SdoTerm.__init__(self,SdoTerm.REFERENCE,Id,uri,label)
    
    
        

        
        

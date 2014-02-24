# Copyright (c) 2012, Sven Thiele <sthiele78@gmail.com>
#
# This file is part of precursor.
#
# precursor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# precursor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with precursor.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-
import re
import xml.etree.ElementTree as etree  
from xml.etree.ElementTree import XML, fromstring, tostring
from pyasp.asp import *


def get_pseeds(xmlnode):
    element = None
    for e in xmlnode:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "precursor-compounds":
	  element = e
          break
    return element    

def get_bootstraps(xmlnode):
    element = None
    for e in xmlnode:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "bootstrap-compounds":
	  element = e
          break
    return element

def get_targets(xmlnode):
    element = None
    for e in xmlnode:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "target-compounds":
	  element = e
          break
    return element 

def get_forbidden(xmlnode):
    element = None
    for e in xmlnode:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "forbidden-compounds":
	  element = e
          break
    return element
  

def get_model(xmlnode):
    element = None
    for e in xmlnode:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "model":
	  element = e
          break
    return element    
        
def get_listOfSpecies(model):
    listOfSpecies = None
    for e in model:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "listOfSpecies":
	  listOfSpecies = e
          break
    return listOfSpecies 
    
def get_listOfReactions(model):
    listOfReactions = None
    for e in model:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "listOfReactions":
	  listOfReactions = e
          break
    return listOfReactions 
    
def get_listOfReactants(reaction):
    listOfReactants = None
    for e in reaction:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "listOfReactants":
	  listOfReactants = e
          break
    return listOfReactants
    
def get_listOfProducts(reaction):
    listOfProducts = None
    for e in reaction:
        if e.tag[0] == "{":
	  uri, tag = e.tag[1:].split("}")
	else: tag = e.tag
        if tag == "listOfProducts":
	  listOfProducts = e
          break
    return listOfProducts
 
def readSBMLnetwork(filename) :
  
   lpfacts = TermSet()
   
   tree = etree.parse(filename)
   sbml = tree.getroot()
   model = get_model(sbml)
   
   listOfSpecies = get_listOfSpecies(model)
   for e in listOfSpecies:
     if e.tag[0] == "{":
       uri, tag = e.tag[1:].split("}")
     else: tag = e.tag
     if tag == "species":
       #print e.attrib
       lpfacts.add(Term('species', ["\""+e.attrib.get("id")+"\""]))
  
   listOfReactions = get_listOfReactions(model)
   for e in listOfReactions:
     if e.tag[0] == "{":
       uri, tag = e.tag[1:].split("}")
     else: tag = e.tag
     if tag == "reaction":
       #print e.attrib
       reactionId = e.attrib.get("id")
       lpfacts.add(Term('reaction', ["\""+reactionId+"\""]))
       if(e.attrib.get("reversible")=="true"):  lpfacts.add(Term('reversible', ["\""+reactionId+"\""]))
       
       listOfReactants = get_listOfReactants(e)
       for r in listOfReactants:
         lpfacts.add(Term('reactant', ["\""+r.attrib.get("species")+"\"", "\""+reactionId+"\""]))
         
       listOfProducts = get_listOfProducts(e)
       for p in listOfProducts:
          lpfacts.add(Term('product', ["\""+p.attrib.get("species")+"\"", "\""+reactionId+"\""]))

   return lpfacts
                
def readPITUFU(filename) :
 
   targets = TermSet()
   seeds = TermSet()
   misc = TermSet()
   
   tree = etree.parse(filename)
   inputs = tree.getroot()
   
   target_d = get_targets(inputs)
   if len(target_d):
    for e in target_d:
      if e.tag[0] == "{":
	uri, tag = e.tag[1:].split("}")
      else: tag = e.tag
      if tag == "species":
	#print e.attrib
	targets.add(Term('target', ["\""+e.attrib.get("id")+"\""]))
   
   pseeds = get_pseeds(inputs)
   if pseeds:
    for e in pseeds:
      if e.tag[0] == "{":
	uri, tag = e.tag[1:].split("}")
      else: tag = e.tag
      if tag == "species":
	#print e.attrib
	seeds.add(Term('pseed', ["\""+e.attrib.get("id")+"\""]))

   bootstraps = get_bootstraps(inputs)
   if bootstraps:
    for e in bootstraps:
      if e.tag[0] == "{":
	uri, tag = e.tag[1:].split("}")
      else: tag = e.tag
      if tag == "species":
	#print e.attrib
	misc.add(Term('ubi', ["\""+e.attrib.get("id")+"\""]))
   
   forbidden = get_forbidden(inputs)   
   if forbidden:
    for e in forbidden:
      if e.tag[0] == "{":
	uri, tag = e.tag[1:].split("}")
      else: tag = e.tag
      if tag == "species":
	#print e.attrib
	misc.add(Term('forbidden', ["\""+e.attrib.get("id")+"\""]))   
       
   return targets, seeds, misc
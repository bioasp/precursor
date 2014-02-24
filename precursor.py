#!python
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
from pyasp.asp import *
import argparse
from __precursor__ import query, utils, sbml

if __name__ == '__main__':
       
    parser = argparse.ArgumentParser()
    parser.add_argument("net",
                        help="metabolic network in SBML format")
    parser.add_argument("inputs",
                        help="targets in XML format") 
                        #help="target, seed and ubiquitous metabolites in XML format") 
    
    parser.add_argument('--autoseeds', 
			help="compute possible seed metabolites",
			action="store_true")
    
    args = parser.parse_args()
    
    netfile = args.net
    targetsfile =  args.inputs
    
    print 'Reading network from ',netfile,'...',
    net = sbml.readSBMLnetwork(netfile)
    print 'done.'


    print 'Reading inputs from ',targetsfile,'...',
    targets, pseeds, misc  = sbml.readPITUFU(targetsfile)
    print 'done.'    
    print "   ", len(targets), "target metabolites." 
    print "   ", len(pseeds), "possible seed metabolites."    
    net = net.union(misc)
    #print misc
    
    #print 'Reading targets from ',targetsfile,'...',
    #targets = sbml.readSBMLtargets(targetsfile)
    #print 'done.'    
    #print "   ", len(targets), " target metabolites." 
    
    
    #if args.ubi :
      #print 'Reading ubiquitous metabolites from ',args.ubi,'...',
      #ubi = sbml.readSBMLubiquitous(args.ubi)
      #print 'done.'
      #print "   ", len(ubi), " ubiquitous metabolites." 
      #net = net.union(ubi)
    
    #if args.seeds :
      #print 'Reading possible seeds from ',args.seeds,'...',
      #pseeds = sbml.readSBMLseeds(args.seeds)
      #print 'done.'
      #print "   ", len(pseeds), " possible seeds."
    #else :
      #print 'Autocompute possible seeds ...',
      #pseeds = query.get_automatic_pseeds(net, targets)
      #print 'done.'
      #print "   ", len(pseeds), " possible seeds found."
      
    if args.autoseeds :
      print '\nAutocompute possible seeds ...',
      autoseeds = query.get_automatic_pseeds(net, targets)
      print 'done.'
      print "   ", len(autoseeds), "possible seeds found."
      pseeds = pseeds.union(autoseeds)
      
    print '\nTesting targets for producebility ...',     
    filtered_targets = TermSet()  
    for t in targets :
       singlet = String2TermSet(str(t))
       SAT = query.satcheck(net, pseeds, singlet)
       if not SAT : 
          filtered_targets.add(t)
    print 'done.'   
    
    if len(filtered_targets) > 0:
       print '   ',len(targets),' targets cannot be produced:'
       for t in filtered_targets : print '   ',t.arg(0)
       print 'cannot be produced.'
       
    targets = targets.difference(filtered_targets)
    
    if len(targets) > 0:
       print '   ',len(targets),' targets can be produced:'
       for t in targets : print '   ',t.arg(0)

       targets = targets.difference(filtered_targets)
    else:
      print '    No Target can be produced.'
      utils.clean_up()
      quit()
      
    
    net.to_file()
    pseeds.to_file()
    targets.to_file()

    print '\nCompute cardinality minimum for a precursor sets ...',
    solution = query.get_card_min_precursor_set(net, pseeds, targets)
    print 'done.'

    opt = solution.score[0]
    print '    Minimal size of a precursor set is',str(opt-1)+'.' 

    print '\nCompute all precursor sets of size',str(opt-1),'...',
    precursors = query.get_precursor_sets_of_size(net, pseeds, targets, opt)
    print 'done.'

    for min_set in precursors :
        utils.print_seeds(min_set)
	
    print '\nCompute subset minimal precursor sets ...',
    precursors = query.get_subset_min_precursor_sets(net, pseeds, targets)
    print 'done.'
        
    print len(precursors),' subset minimal precursor sets found.'
    for min_set in precursors :
        utils.print_seeds(min_set)
    

    utils.clean_up()




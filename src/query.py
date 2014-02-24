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
import os
import tempfile
from pyasp.asp import *


root = __file__.rsplit('/', 1)[0]

precursor_prg =      root + '/encodings/precursor.lp'
heu_prg                  =      root + '/encodings/heuristic.lp' 
#subset_min_precursor_prg =      root + '/encodings/min_precursor.lp' 
card_min_precursor_prg =      root + '/encodings/card_min_precursor.lp'
automatic_pseeds_prg =      root + '/encodings/automatic_pseed.lp'
satcheck_prg =      root + '/encodings/satcheck_precursor.lp'


def satcheck(net, pseeds, targets):
    net_f = net.to_file()
    pseed_f = pseeds.to_file()
    target_f = targets.to_file()
    prg = [satcheck_prg, net_f, pseed_f, target_f ]
    solver = GringoClasp()
    models = solver.run(prg,nmodels=1,collapseTerms=True,collapseAtoms=False)
    os.unlink(net_f)
    os.unlink(pseed_f)
    os.unlink(target_f)
    if len(models)>0 : return True
    return False

def get_precursor_sets_of_size(net, pseeds, targets,opt):
    net_f = net.to_file()
    pseed_f = pseeds.to_file()
    target_f = targets.to_file()
    prg = [card_min_precursor_prg, net_f, pseed_f, target_f ]
    coptions = '--project --opt-all='+str(opt)
    solver = GringoClasp(clasp_options=coptions)
    models = solver.run(prg,nmodels=0,collapseTerms=True,collapseAtoms=False)
    os.unlink(net_f)
    os.unlink(pseed_f)
    os.unlink(target_f)
    return models

def get_card_min_precursor_set(net, pseeds, targets):
    net_f = net.to_file()
    pseed_f = pseeds.to_file()
    target_f = targets.to_file()
    prg = [card_min_precursor_prg, net_f, pseed_f, target_f ]
    solver = GringoClaspOpt()
    solution = solver.run(prg,collapseTerms=True,collapseAtoms=False)
    os.unlink(net_f)
    os.unlink(pseed_f)
    os.unlink(target_f)
    if solution : return solution[0]
    return None

#def get_subset_min_precursor_sets(net, pseeds, targets):
    #net_f = net.to_file()
    #pseed_f = pseeds.to_file()
    #target_f = targets.to_file()
    #prg = [subset_min_precursor_prg, net_f, pseed_f, target_f ]
    #coptions = '--project'
    #solver = GringoClasp(clasp_options=coptions)
    #models = solver.run(prg,nmodels=0,collapseTerms=True,collapseAtoms=False)
    #os.unlink(net_f)
    #os.unlink(pseed_f)
    #os.unlink(target_f)
    #return models


def get_automatic_pseeds(net, targets):
    net_f = net.to_file()
    target_f = targets.to_file()
    prg = [automatic_pseeds_prg, net_f, target_f ]
    solver = GringoClasp()
    models = solver.run(prg,nmodels=10,collapseTerms=True,collapseAtoms=False)
    os.unlink(net_f)
    os.unlink(target_f)
    return models[0]
    
    
def get_subset_min_precursor_sets(net, pseeds, targets):
    net_f = net.to_file()
    pseed_f = pseeds.to_file()
    target_f = targets.to_file()
    prg = [precursor_prg, heu_prg, net_f, pseed_f, target_f ]
    solver = GringoHClasp(clasp_options='--heu=domain --enum-mode=record')
    solutions = solver.run(prg,nmodels=0,collapseTerms=True,collapseAtoms=False)
    os.unlink(net_f)
    os.unlink(pseed_f)
    os.unlink(target_f)
    return solutions
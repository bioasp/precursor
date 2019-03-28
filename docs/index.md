---
layout: index
title: precursor
tagline: Compute minimal precursors sets that enable the production of target metabolites
---

### Minimal nutrition sets to produce target metabolites

A qualitative approach to elaborating the bio-synthetic capacities of metabolic networks. 
Given a set of desired target metabolites, this approach applies a notion of bio-chemical producebility to metabolic reaction networks and allows to identify the minimal sets of precursors that are required to produce the target metabolites.


### Installation 

You can install precursor by running:

	$ pip install --user precursor

On Linux the executable script can then be found in ``~/.local/bin``

and on MacOS the script is under ``/Users/YOURUSERNAME/Library/Python/3.6/bin``.


### Usage

Typical usage is:
	
	$ precursor.py --autoseeds network targets 

For more options you can ask for help as follows:

	$ precursor.py --help
	usage: precursor.py [-h] [--autoseeds] net inputs

	positional arguments:
	  net          metabolic network in SBML format
	  inputs       targets in XML format

	optional arguments:
	  -h, --help   show this help message and exit
	  --autoseeds  compute possible seed metabolites


### Samples

An archive with sample files is available here:
      [precursor_data.tar.gz](http://bioasp.github.io/downloads/samples/precursor_data.tar.gz)

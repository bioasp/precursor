Installation 
============

You can install precursor by running::

	$ pip install --user precursor
	
The executable scripts can then be found in ~/.local/bin.

Usage
=====

Typical usage is::
	
	$ precursor.py --autoseeds network targets 

For more options you can ask for help as follows::

	$ precursor.py --help
	usage: precursor.py [-h] [--autoseeds] net inputs
  
	positional arguments:
	  net          metabolic network in SBML format
	  inputs       targets in XML format
  
	optional arguments:
	  -h, --help   show this help message and exit
	  --autoseeds  compute possible seed metabolites


Samples
=======

An archive with sample files is available here::
      precursor_data.tar.gz_

.. _precursor_data.tar.gz: http://bioasp.github.io/downloads/samples/precursor_data.tar.gz
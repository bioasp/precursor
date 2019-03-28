# Installation 

You can install precursor by running:

    $ pip install --user precursor
	
On Linux the executable script can then be found in `~/.local/bin`

and on MacOS the script is under `/Users/YOURUSERNAME/Library/Python/3.6/bin`.


## Usage

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


## Samples

An archive with sample files is available [here](http://bioasp.github.io/downloads/samples/precursor_data.tar.gz).

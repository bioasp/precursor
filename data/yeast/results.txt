> precursor.py --autoseeds yeast.xml inputForYeast.xml
Reading network from  yeast.xml ...done.
Reading inputs from  inputForYeast.xml ...done.
    10 target metabolites.
    0 possible seed metabolites.

Autocompute possible seeds ...done.
    96 possible seeds found.

Testing targets for producebility ...done.
    10  targets can be produced:
    "VAL"
    "L__45__ASPARTATE"
    "CYS"
    "MET"
    "HIS"
    "FADH2"
    "L__45__ALPHA__45__ALANINE"
    "LEU"
    "SER"
    "DGTP"

Compute cardinality minimum for a precursor sets ...done.
    Minimal size of a precursor set is 2.

Compute all cadinality minimal precursor sets...done.
1: "DGDP" "_3__45__CARBOXY__45__3__45__HYDROXY__45__ISOCAPROATE"  

Compute subset minimal precursor sets ...done.
3  subset minimal precursor sets found.
1: "LEU" "DGDP" "VAL"  
2: "LEU" "DIOH__45__ISOVALERATE" "DGDP"  
3: "DGDP" "_3__45__CARBOXY__45__3__45__HYDROXY__45__ISOCAPROATE"  

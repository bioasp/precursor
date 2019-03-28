> precursor.py --autoseeds bcicWithoutCofactors.xml inputForBcic.xml
Reading network from  bcicWithoutCofactors.xml ...done.
Reading inputs from  inputForBcic.xml ...done.
    10 target metabolites.
    0 possible seed metabolites.

Autocompute possible seeds ...done.
    15 possible seeds found.

Testing targets for producebility ...done.
    10  targets can be produced:
    "CPD__45__9454"
    "HEME_O"
    "MET"
    "OXALACETIC_ACID"
    "HIS"
    "PHOSPHO__45__ENOL__45__PYRUVATE"
    "CHORISMATE"
    "THF"
    "ERYTHROSE__45__4P"
    "_6__45__PYRUVOYL__45__5678__45__TETRAHYDROPTERIN"

Compute cardinality minimum for a precursor sets ...done.
    Minimal size of a precursor set is 7.

Compute all cadinality minimal precursor sets...done.
1: "VITAMIN_K_2" "GLN" "GLC__45__6__45__P" "DIHYDRO__45__NEO__45__PTERIN" "L__45__ALPHA__45__ALANINE" "PROTOHEME" "L__45__ASPARTATE"  

Compute subset minimal precursor sets ...done.
3  subset minimal precursor sets found.
1: "VITAMIN_K_2" "GLN" "HOMO__45__SER" "L__45__ASPARTATE" "DIHYDRO__45__NEO__45__PTERIN" "PROTOHEME" "ACETALD" "SULFATE" "GLC__45__6__45__P"  
2: "VITAMIN_K_2" "GLN" "HOMO__45__SER" "THR" "L__45__ASPARTATE" "DIHYDRO__45__NEO__45__PTERIN" "PROTOHEME" "SULFATE" "GLC__45__6__45__P"  
3: "VITAMIN_K_2" "GLN" "L__45__ASPARTATE" "DIHYDRO__45__NEO__45__PTERIN" "PROTOHEME" "GLC__45__6__45__P" "L__45__ALPHA__45__ALANINE"  

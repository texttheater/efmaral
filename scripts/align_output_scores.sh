#!/bin/bash

# Usage: align_symmetrize source.txt target.txt output.moses [method]
# Where method is one of the symmetrization methods from atools (the -c
# argument).


# if only one argument takes *salign file as input
#python3 efmaral.py -i "$1" >align.forward &
python3 efmaral.py -r -i "$1" #>align.reverse #&
#wait
#tools/cdec-2014-10-12/utils/atools -c intersect -i align.forward -j align.reverse > align.intersect
#tools/cdec-2014-10-12/utils/atools -c union -i align.forward -j align.reverse > align.union



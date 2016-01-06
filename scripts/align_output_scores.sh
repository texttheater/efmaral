#!/bin/bash

# Usage: align_symmetrize source.txt target.txt output.moses [method]
# Where method is one of the symmetrization methods from atools (the -c
# argument).

BASEDIR=$(dirname $0)/..
# if only one argument takes *salign file as input
python3 $BASEDIR/efmaral.py --probabilities -r -i "$1" #>align.reverse #&



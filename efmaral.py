#!/usr/bin/env python3

from cyalign import align
from gibbs import ibm_print

import sys, argparse, random

parser = argparse.ArgumentParser(
    description='efmaral: efficient Markov Chain word alignment')
parser.add_argument(
    '-r', '--reverse', dest='reverse',
    action='store_true', help='Align in the reverse direction')
parser.add_argument(
    '--null-prior', dest='null_prior', default=0.2, metavar='X',
    type=float, help='Prior probability of NULL alignment')
parser.add_argument(
    '--lexical-alpha', dest='lex_alpha', default=1e-3, metavar='X',
    type=float, help='Dirichlet prior parameter for lexical distributions')
parser.add_argument(
    '--null-alpha', dest='null_alpha', default=1e-3, metavar='X',
    type=float, help='Dirichlet prior parameter for NULL word distribution')
parser.add_argument(
    '--seed', dest='seed', default=None,
    type=int, help='Random seed')
parser.add_argument(
    '-n', '--samplers', dest='n_samplers', default=2, metavar='N',
    type=int, help='Number of independent samplers')
parser.add_argument(
    '-l', '--length', dest='length', default=1.0, metavar='X',
    type=float, help='Relative number of sampling iterations')
parser.add_argument(
    '-i', '--input', dest='inputs', type=str, nargs='+',
    metavar='filename',
    help='Input (either one fast_align-format file, or two Europarl-style)')

args = parser.parse_args()

seed = random.randint(0, 0x7ffffff) if args.seed is None else args.seed

if len(args.inputs) not in (1, 2):
    raise ValueError('Only one or two input files allowed!')

alignments_list, sent_ps_list = align(args.inputs, args.n_samplers, args.length,
            args.null_prior, args.lex_alpha, args.null_alpha,
            args.reverse, seed)

print('Writing alignments...', file=sys.stderr)
assert args.reverse, 'printout only works for reverse alignments'


for alignment, sent_ps in zip(alignments_list, sent_ps_list):
    # Each row is an unnormalized distribution over alignments from the 'French' language to the 'English'
    dist_per_foreign_token = sent_ps.reshape(len(alignment), len(sent_ps) / len(alignment)) 
    # Normalize each row
    dist_per_foreign_token = (dist_per_foreign_token.T / dist_per_foreign_token.sum(axis=1)).T
    for f_index, row in enumerate(dist_per_foreign_token):
        for e_index, val in enumerate(row):
            if val > 0.00001:
                print("{}-{} {:.8f}".format(e_index, f_index, val), end=' ')
    print()


#ibm_print(aaa, args.reverse, sys.stdout.fileno())




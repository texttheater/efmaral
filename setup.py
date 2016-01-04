#!/usr/bin/env python3
import numpy as np
from distutils.core import setup, Extension
from Cython.Build import cythonize
import os
os.environ["CC"] = "gcc-4.9"

gibbsmodule = Extension(
    'gibbs',
    sources=['gibbs.c'],
    libraries=[],
    extra_compile_args=['-std=c99', '-Wall', '-fopenmp'],
    extra_link_args=['-lgomp'])

setup(
    name = 'Gibbs aligner',
    ext_modules = cythonize("cyalign.pyx") + [gibbsmodule],
    include_dirs=[np.get_include(), '.']
)


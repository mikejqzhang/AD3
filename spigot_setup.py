import os

import numpy

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize


ad3_dir = '/data/mjqzhang/AD3'

setup(name="spigot",
        ext_modules=cythonize(
            [
                Extension(
                    "spigot_src.sparsemap",
                    ["spigot_src/sparsemap.pyx"],
                    include_dirs=["../src", ad3_dir, os.path.join(ad3_dir, 'python'),
                        numpy.get_include()],
                    library_dirs=[os.path.join(ad3_dir, 'ad3')],
                    language="c++"
                    ),
                Extension(
                    name="spigot_src.factors",
                    sources=["spigot_src/factors.pyx",
                        os.path.join('examples', 'cpp', 'parsing','FactorTree.cpp')],
                    include_dirs=['spigot_src', ad3_dir, os.path.join(ad3_dir, 'python'),
                        numpy.get_include()],
                    library_dirs=[os.path.join(ad3_dir, 'ad3')],
                    language="c++"
                    )
                ],
            compiler_directives = {'language_level':3},
            include_path = ['/data/mjqzhang/AD3/python']
            )
        )
# setup(name="sparsemap",
#       version="0.1.dev0",
#       ext_modules=cythonize(
#           [
#               Extension(
#                   name="spigot_src.factors",
#                   sources=[
#                       "spigot_src/factors.pyx",
#                       os.path.join('examples', 'cpp', 'parsing',
#                           'FactorTree.cpp')
#                       ],
#                   include_dirs=["src", 'python',
#                                 numpy.get_include()],
#                   libraries=['ad3'],
#                   library_dirs=[os.path.join('ad3')]
#                   )
#           ],
#           compiler_directives = {'language_level':3}
#       )
# )

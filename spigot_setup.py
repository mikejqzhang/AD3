import os

import numpy

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize



setup(name="spigot",
      ext_modules=cythonize(
          [
              Extension(
                  name="spigot_src.factors",
                  sources=["spigot_src/factors.pyx"],
                  include_dirs=["src", 'python',
                                numpy.get_include()],
                  libraries=['ad3'],
                  library_dirs=[os.path.join('ad3')]
                  )
          ],
          compiler_directives = {'language_level':3},
          include_path = ['/Users/michael/Projects/AD3/python']
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

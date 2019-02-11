import os

import numpy

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize



ad3_dir = os.getcwd()

setup(name="spigot",
        ext_modules=cythonize(
            [
                Extension(
                    "spigot.spigot",
                    ["spigot/spigot.pyx"],
                    include_dirs=["spigot", ad3_dir, os.path.join(ad3_dir, 'python'),
                        numpy.get_include()],
                    library_dirs=[os.path.join(ad3_dir, 'ad3')],
                    language="c++"
                    ),
                Extension(
                    "spigot.sparsemap",
                    ["spigot/sparsemap.pyx"],
                    include_dirs=["spigot", ad3_dir, os.path.join(ad3_dir, 'python'),
                        numpy.get_include()],
                    library_dirs=[os.path.join(ad3_dir, 'ad3')],
                    language="c++"
                    ),
                Extension(
                    name="spigot.factors",
                    sources=[
                        "spigot/factors.pyx",
                        os.path.join(ad3_dir, 'examples', 'cpp',
                            'parsing', 'FactorTree.cpp'),
                        ],
                    include_dirs=['spigot', ad3_dir, os.path.join(ad3_dir, 'python'),
                        numpy.get_include()],
                    library_dirs=[os.path.join(ad3_dir, 'ad3')],
                    language="c++"
                    )
                ],
            compiler_directives = {'language_level':3},
            include_path = ['/data/mjqzhang/AD3/python']
            )
        )

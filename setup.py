from distutils.core import setup
from Cython.Build import cythonize

setup(name='Variance Analysis App', ext_modules=cythonize("variance_analysis.pyx"))

from Cython.Build import cythonize
from distutils.core import Extension, setup


ext_modules = Extension(name="cython_mod",
                        sources=["cython_mod.pyx"],)
setup(ext_modules=cythonize(ext_modules))


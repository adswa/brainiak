from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
import sys
import os.path

assert sys.version_info >= (3,4), "Please use Python version 3.4 or higher, lower versions are not supported"

ext_modules = [
]

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

class BuildExt(build_ext):
    """A custom build extension for adding compiler-specific options."""
    c_opts = {
        'msvc': ['/EHsc'],
        'unix': ['-std=c++11'],
    }

    if sys.platform == 'darwin':
        c_opts['unix'] += ['-stdlib=libc++', '-mmacosx-version-min=10.7']

    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct, [])
        for ext in self.extensions:
            ext.extra_compile_args = opts
        build_ext.build_extensions(self)

setup(
    name='toolkit',
    version='0.0.1',
    install_requires = ['numpy', 'scikit-learn'],
    author='Princeton Neuroscience Institute and Intel Corporation',
    author_email='bryn.keller@intel.com',
    url='https://github.com/IntelPNI/toolkit',
    description='Scalable algorithms for advanced fMRI analysis',
    license = 'Apache 2',
    keywords='neuroscience, algorithm, fMRI, distributed, scalable',
    long_description=long_description,
    ext_modules=ext_modules,
    # install_requires=['pybind11'],
    cmdclass={'build_ext': BuildExt},
    # py_modules = ['phat'],
    packages = find_packages(exclude = ['doc', 'test'])
 )





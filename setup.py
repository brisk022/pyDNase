__author__ = 'Jason Piper'

import imp
current_version = imp.load_source('lol', 'pyDNase/_version.py').__version__

#Unfortunately, we have to ensure that the user has numpy is installed,
#as pip is bad at installing numpy and scipy at the same time, and just breaks

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension

setup(
    name='pyDNase',
    version=current_version,
    description='DNase-seq analysis library',
    long_description=open('README.rst',"rt").read(),
    author='Jason Piper',
    author_email='j.piper@warwick.ac.uk',
    url='http://jpiper.github.io/pyDNase',
    license='GPLv3',
    ext_modules = [Extension("pyDNase.footprinting.WellingtonC", sources = ["pyDNase/footprinting/WellingtonC.c"], extra_compile_args=['-std=c99'])],
    packages= [
        'pyDNase',
        'pyDNase.footprinting',
    ],

    install_requires=[
        # Note - not enforcing versions for numpy, scipy, and matplotlib
        "numpy", #Tested on >=1.5.0
        "matplotlib", #Tested on >=1.2
        "pysam >= 0.7.5",
        "clint >= 0.3.2",
    ],
    
    package_data = {'pyDNase':["data/*"]},
    
    scripts=[
        "pyDNase/scripts/dnase_average_profile.py",
        "pyDNase/scripts/dnase_to_javatreeview.py",
        "pyDNase/scripts/dnase_wig_tracks.py",
        "pyDNase/scripts/wellington_footprints.py",
        "pyDNase/scripts/dnase_to_JSON.py",
        "pyDNase/scripts/examples/example_footprint_scores.py",
        "pyDNase/scripts/dnase_to_JSON.py"],
    
    test_suite="test",
)

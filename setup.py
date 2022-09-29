from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize


extensions = [
	Extension(
		"sequence_aligner",
		["fragment_matcher_cython.pyx"],
	),
]


setup(
	name = "fragment_matcher_cython.pyx",
	packages = find_packages(),
	ext_modules = cythonize(extensions, annotate=True)
)
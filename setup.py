#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import PipelineERRBS

setup(
	name="PipelineERRBS",
	version=PipelineERRBS.__version__,
	packages=find_packages(),
 	description="ERRBS methylation analysis pipeline",
	long_description=open('README.md').read(),
	author='Jennifer Rondineau',
	author_email='jennifer.rondineau@etu.univ-nantes.fr',
	url="mettre github",
	#install_requires = ["Samtools", "bowtie2", "bismark","trim_galore","cutadapt", "fastqc","R", "methylKit", "eDMR"],
	classifiers=[
		"Programming Language :: Python"
	],
	entry_points = {
		'console_scripts': [
		'PipelineERRBS = PipelineERRBS.PipelineERRBS:main',
		],
	},
	package_data={'': ['*.r', '*.R']},
	include_package_data=True

)



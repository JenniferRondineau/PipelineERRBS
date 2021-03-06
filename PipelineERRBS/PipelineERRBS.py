#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jun 24, 2016

import os
import sys
import getopt
from ERRBSalign import *
from usage import *
from methylDiffbyPatient import *
from extractionCpG import *
from annotateDMR import *
from coveredCpG import *
from ChromHMMannotate import *

def main():
	__version__ = "0.0.1"  # version of PipelineERRBS

	# if any arguments are given print usage message and then exit the programm
	if len(sys.argv) == 1:
		usagePipeline()
		sys.exit(2)

	if sys.argv[1] == 'align':
		mainERRBSalign(sys.argv[1:])

	elif sys.argv[1] == 'methylDiffbyPatient':
		methylDiffbyPatient(sys.argv[1:])

	elif sys.argv[1] == 'extractionCpG':
		ExtractionCpG(sys.argv[1:])

	elif sys.argv[1] == 'CoveredCpG':
		CoveredCpG(sys.argv[1:])

	elif sys.argv[1] == 'annotate':
		annotateDMR(sys.argv[1:])

	elif sys.argv[1] == 'ChromHMMannotate':
		ChromHMMannotate(sys.argv[1:])


	else :
		usagePipeline()
		sys.exit(2)

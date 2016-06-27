#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# ERRBS DNA methylation analysis pipeline 
#
# Author: Jennifer Rondineau
# Date: Jun 24, 2016
#
# 

import os
import sys
import getopt
from usage import *
from CheckRequired import *
from extractionDMC import *

def methylDiffbyPatient(argv):
	__version__ = "0.0.1"  # version of methylDiffbyPatient

	# if any arguments are given print usage message and then exit the programm
	if len(argv) == 1:
		usageMethylDiffbyPatient()
		sys.exit(2)
	name = str()	

	# List of all options possible
	try:	   
		opts, args = getopt.getopt(argv[1:],"h1:2:o:",["control=","case=","name=","outputdir=","version"])
	except getopt.GetoptError:
		usageMethylDiffbyPatient()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h': # print usage message
			usageMethylDiffbyPatient() 
			sys.exit()
		elif opt in ("-1","--control"): # sorted control SAM file (or _CpG.txt)
			checkFile(arg)
			control = arg
		elif opt in ("-2","--case"): # sorted case SAM file (or _CpG.txt)
			checkFile(arg)
			case = arg
		elif opt in ("-o","--outputdir"): # Output directory
			outputdir = arg
		elif opt == '--name' : # identifier for the differential methylation
			name = arg
		elif opt == '--version': # print software version
			print "methylDiffbyPatient."+__version__
			sys.exit(0)

	# Check that all necessary arguments are given
	checkargsMethylDiff(control,case,outputdir,name)
	# Check control file (SAM or _CpG.txt), if it's a SAM file, then extraction CpG
	checkCpG(control,outputdir)
	# Check case file (SAM or _CpG.txt), if it's a SAM file, then extraction CpG
	checkCpG(case,outputdir)
	# Extraction of differential methylation
	extractionDMCDMR(control,case, outputdir,name)
	
	
	

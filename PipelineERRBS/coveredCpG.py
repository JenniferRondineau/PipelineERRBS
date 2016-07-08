#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jun 24, 2016

import os
import sys
import getopt, subprocess
from CheckRequired import *
from usage import *

def CoveredCpG(argv):

	__version__ = "0.0.1"  # version of CoveredCpG

	# if any arguments are given print usage message and then exit the programm
	if len(argv) == 1:
		usageCoveredCpG()
		sys.exit(2)

	name = str()

	# List of all options possible
	try:
		opts, args = getopt.getopt(argv[1:],"h1:2:o:",["control=","case=","name=","outputdir=","version"])
	except getopt.GetoptError:
		usageCoveredCpG()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h': # print usage message
			usageCoveredCpG()
			sys.exit()
		elif opt in ("-1","--control"): # sorted control SAM file (or _CpG.txt)
			checkFile(arg)
			checkCpGfile(arg)
			control = arg
		elif opt in ("-2","--case"): # sorted case SAM file (or _CpG.txt)
			checkFile(arg)
			checkCpGfile(arg)
			case = arg
		elif opt in ("-o","--outputdir"): # Output directory
			outputdir = arg
		elif opt == '--name' : # identifier for the CoveredCpG file
			name = arg
		elif opt == '--version': # print software version
			print "CoveredCpG."+__version__
			sys.exit(0)

    # Check that all necessary arguments are given
	checkargsMethylDiff(control,case,outputdir,name)
	path=os.popen("echo $PipelineERRBSdata_PATH").read()
	command = "Rscript $PipelineERRBS_PATH/covered_CpG.R " + control + " " + case + " " + outputdir + " "+ name + " "+ path
	subprocess.call(command, shell=True)

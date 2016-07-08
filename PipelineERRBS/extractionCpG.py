#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jun 24, 2016

import os
import sys
import getopt
from usage import *
from CheckRequired import *
from extractionDMC import *

# Function to extract CpGs of a SAM file and to obtain statistics on CpGs and coverage
def extractionCpG(file_in, outputdir):
	name = os.path.basename(file_in)
	idSample = os.path.splitext(name)
	command = "Rscript $PipelineERRBS_PATH/controle_qualite_methylkit.R " + file_in + " " + outputdir + " "+ idSample[0]
	subprocess.call(command, shell=True)


def ExtractionCpG(argv):

	# if any arguments are given print usage message and then exit the programm
	if len(argv) == 1:
		usageextraction()
		sys.exit(2)
	file_in = str()
	outputdir = str()

	# List of all options possible
	try:
		opts, args = getopt.getopt(argv[1:],"hf:o:",["outputdir="])
	except getopt.GetoptError:
		usageextraction()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h': # print usage message
			usageextraction()
			sys.exit()
		elif opt =='-f': # sorted SAM file
			file_in = arg
			if not os.path.isfile(file_in): # check if the input file does not exists
					print "Error, the specified file '"+file_in+"' does not exists"
					sys.exit(1)

		elif opt in ("-o","--outputdir"): # Output directory
			outputdir = arg

	# checks that all the necessary arguments are specified
	if file_in == '':
 		print "Error, the option -f is required to run this programm, please specify a SAM file to extract CpG"
		sys.exit(1)
	elif outputdir == '':
		print "Error, output directory is required, please run extractionCpG with the option -o"
		sys.exit(1)

	extractionCpG(file_in, outputdir)

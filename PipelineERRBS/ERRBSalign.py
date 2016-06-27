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
from filtering_data import *
from CheckRequired import *
from align import *
from usage import *


def mainERRBSalign(argv):
	__version__ = "0.0.1"  # version of ERRBSalign

	# Initialize all parameters to default values
	inputfileR1 = str() # R1 PE fastq file
	inputfileR2 = str() # R2 PE fastq file
	genomeref = str() # Reference genome directory
	outputdir = str() # Output directory
	paired= ''
	single=''

	# if any arguments are given print usage message and then exit the programm
	if len(argv) == 1:
		usageERRBSalign()
		sys.exit(2)

	# List of all options possible
	try:	   
		opts, args = getopt.getopt(argv[1:],"h1:2:g:o:",["paired","single=","genome_ref=","outputdir=","version"])
	except getopt.GetoptError:
		usageERRBSalign()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h': # print usage message
			usageERRBSalign() 
			sys.exit()
		elif opt == '--paired': # paired-end read
			paired = 'True'
		elif opt == '-1': # R1 PE fastq file
			checkFile(arg)
			inputfileR1 = arg
		elif opt == '-2': # R2 PE fastq file
			checkFile(arg)
			inputfileR2 = arg
		elif opt == '--single': # single-end read
			single = 'True'
			checkFile(arg)
			inputfileR1 = arg
		elif opt in ("-g","--genome_ref"): # Reference genome directory
			genomeref = arg
		elif opt in ("-o", "--outputdir"): # Output directory
			outputdir = arg
		elif opt == '--version': # print software version
			print "ERRBSalign."+__version__
			sys.exit(0)

	# Check that all necessary arguments are given
	checkargsAlign(paired,inputfileR1,inputfileR2,genomeref,outputdir)
	# Adapter filtering
	paired, single, R1, R2,outputdir = filtering(paired, single, inputfileR1, inputfileR2, outputdir)
	# Check that the given genome path exists and if the genome is already indexing or not
	checkGenome(genomeref)
	# alignment against the reference genome
	align(paired, single, R1, R2 , outputdir, genomeref)
	# Sorting the output file BAM and creation of a SAM file
	sortAlignFile(inputfileR1, outputdir, paired, single)
	sys.exit(0) # Exiting




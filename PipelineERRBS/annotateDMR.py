#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jun 24, 2016

import os
import sys
import getopt
from CheckRequired import *
from usage import *
import subprocess


def annotateDMR(argv):
	__version__ = "0.0.1"  # version of annotateDMR

	# Initialize all parameters to default values
	bedfile = str() # input bedfile with [chr] [start] [end] Differentially methylated regions
	outputfile = str() # name of the output file
	annstat = str() # name of statistic file associated with HOMER annotatePeaks.pl
	go = str() # filename of the analysis GO

	# if any arguments are given print usage message and then exit the programm
	if len(argv) == 1:
		usageannotate()
		sys.exit(2)

	# List of all options possible
	try:
		opts, args = getopt.getopt(argv[1:],"hb:o:s:",["outputfile=", "annStats=", "go="])
	except getopt.GetoptError:
		usageannotate()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h': # print usage message
			usageannotate()
			sys.exit()
		elif opt == '-b': # input bedfile
			checkFile(arg)
			bedfile = arg
		elif opt in ("-s", "--annStats"): # name of statistic file
			annstat = arg
		elif opt == '--go': # filename of the analysis GO
			go = arg
		elif opt in ("-o", "--outputfile"): # Output file
			outputfile = arg

	# checks that all the necessary arguments are specified
	if bedfile == '':
		print "Error,..."
	if outputfile == '':
		print "Error,..."

	# Annotation with "annotatePeak.pl" HOMER
	if annstat == '':
		if go == '':
			command = "annotatePeaks.pl " + bedfile + " hg19 > " + outputfile
			subprocess.call(command, shell=True)
		else :
			command = "annotatePeaks.pl " + bedfile + " hg19 -go "+go+" > " + outputfile
			subprocess.call(command, shell=True)
	elif annstat != '':
		if go == '':
			command = "annotatePeaks.pl " + bedfile + " hg19 -annStats " + annstat + " > " + outputfile
			subprocess.call(command, shell=True)
		else :
			command = "annotatePeaks.pl " + bedfile + " hg19 -annStats " + annstat + " -go "+go+" > "+ outputfile
			subprocess.call(command, shell=True)

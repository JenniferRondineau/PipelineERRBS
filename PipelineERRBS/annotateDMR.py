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
from CheckRequired import *
from usage import *
import subprocess


def annotateDMR(argv):
	__version__ = "0.0.1"  # version of ERRBSalign

	# Initialize all parameters to default values
	bedfile = str() # input bedfile with chr start end DMR
	outputfile = str() # name of the output file
	annstat = str() # name of statistique file associated with HOMER annotatePeaks.pl

	# if any arguments are given print usage message and then exit the programm
	if len(argv) == 1:
		usageannotate()
		sys.exit(2)

	# List of all options possible
	try:	   
		opts, args = getopt.getopt(argv[1:],"hb:o:s:",["outputfile=", "annStats="])
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
		elif opt in ("-s", "--annStats"):
			annstat = arg
		elif opt in ("-o", "--outputdir"): # Output file
			outputfile = arg

	
	if bedfile == '':
		print "Error,..."
	if outputfile == '':
		print "Error,..."

	if annstat == '':
		command = "annotatePeaks.pl " + bedfile + " hg19 > " + outputfile
		subprocess.call(command, shell=True)
	else :
		command = "annotatePeaks.pl " + bedfile + " hg19 --annStats " + annstat +" > " + outputfile
		subprocess.call(command, shell=True)
		

	

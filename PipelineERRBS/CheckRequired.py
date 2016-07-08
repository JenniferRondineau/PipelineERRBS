#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jun 24, 2016

import os
import sys
import subprocess
from subprocess import Popen, PIPE
from extractionCpG import *

# Check that the given input file exists
def checkFile(file_in):
	if not os.path.isfile(file_in): # if the input file does not exists, print an error message then exit the programm
		print "Error, the specified file '"+file_in+"' does not exists"
		sys.exit(1)

# Check that all necessary arguments are given for ERRBSalign
def checkargsAlign(paired,inputfileR1,inputfileR2,genomeref,outputdir):
	if inputfileR1 == '':
 		print "Error no options --paired (-1/-2) or --single have been used, these option are required to run this programm"
		sys.exit(1)
	elif (inputfileR2 == '' and paired == 'True') :
		print "Error, the option --paired require two fastq (-1/-2), if you have only one fastq, run ERRBSalign with the option --single or if you have one fastq R1 and one fastq R2, run ERRBSalign with the option --paired -1 fastqR1 -2 fastqR2"
		sys.exit(1)
	elif genomeref == '':
		print "Error, a reference genome file is required, please run ERRBSalign with the option -g"
		sys.exit(1)
	elif outputdir == '':
		print "Error, output file is required, please run ERRBSalign with the option -o"
		sys.exit(1)

# Check that the given genome path exists
def checkGenome(genomeref):
	print "Step 2: Check the reference genome and preparation"
	if not os.path.exists(genomeref): # If the genome path does not exists, print an error message then exit the programm
		print "Error, the specified genome path '"+genomeref+"' does not exists"
		sys.exit(1)
	path_to_bisulfite_genome = genomeref + "Bisulfite_Genome/"
	if not os.path.exists(path_to_bisulfite_genome): # check if the genome is already indexing
		command = "bismark_genome_preparation --verbose --bowtie2 " + genomeref
		subprocess.call(command, shell=True)


# Check that all necessary arguments are given for methylDiffbyPatient
def checkargsMethylDiff(control,case,outputdir,name):
	if control == '':
 		print "Error, the option --control (-1) is required to run this programm, please specify a SAM control file or _CpG.txt control file"
		sys.exit(1)
	elif case == '':
		print "Error, the option --case (-2) is required to run this programm, please specify a SAM case file or _CpG.txt case file"
		sys.exit(1)
	elif outputdir == '':
		print "Error, output directory is required, please run methylDiffbyPatient with the option -o"
		sys.exit(1)
	elif name == '':
		print "Error, a name is required ..."
		sys.exit(1)

# Check whether the file has an ".sam" extension and if so, extraction of CpGs.
def checkCpG(file_in, outputdir):
	split = os.path.splitext(file_in)
	extension = split[1]
	if (extension == '.sam' or extension == '.SAM'):
		extractionCpG(file_in, outputdir)

# Check whether the file has an ".txt" extension
def checkCpGfile(file_in):
	split = os.path.splitext(file_in)
	extension = split[1]
	if extension != '.txt\n':
		print 'Error, ' + file_in +' need to be a "_CpG.txt" file, please run extractionCpG before'

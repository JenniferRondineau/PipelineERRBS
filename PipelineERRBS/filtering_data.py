#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jun 24, 2016

import subprocess
import os

# Adapter trimming
def filtering(paired, single, inputfileR1, inputfileR2, outputdir):
	print "Step 1 : Filtering Data with Trim_Galore"

	if (paired == 'True') : # paired-end read
		command = "trim_galore -o " + outputdir + " --paired --rrbs --non_directional --fastqc " + inputfileR1 + " "+ inputfileR2
		subprocess.call(command, shell=True) # trimming with Trim_galore
		R1withoutfq = os.path.splitext(inputfileR1)
		R2withoutfq = os.path.splitext(inputfileR2)
		inputfileR1 = R1withoutfq[0] + "_val_1.fq" # name of fastqR1 trimming file
		inputfileR2 = R2withoutfq[0] + "_val_2.fq" # name of fastqR2 trimming file
		return paired, single, inputfileR1, inputfileR2, outputdir

	elif (single == 'True') : # single-end reads
		command = "trim_galore -o " + outputdir + " --rrbs --non_directional --fastqc " + inputfileR1
		subprocess.call(command, shell=True) # trimming with Trim_galore
		R1withoutfq = os.path.splitext(inputfileR1)
		inputfileR1 = R1withoutfq[0] + "_val_1.fq" # name of fastq trimming file
		print inputfileR1
		return paired, single, inputfileR1, inputfileR2, outputdir

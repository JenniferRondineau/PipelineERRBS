#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# ERRBS DNA methylation analysis pipeline 
#
# Author: Jennifer Rondineau
# Date: Jun 24, 2016
#
# 


import subprocess
from subprocess import Popen, PIPE
import os


# Alignment to the reference genome
def align(paired, single, R1, R2, outputdir, genomeref):
	print " "
	print "Step 3 : Alignment to the reference genome"
	if (paired == 'True') :  # paired-end read, alignment with bismark
		command = "bismark --bowtie2 --non_directional " + genomeref + " -1 " + R1 + " -2 " + R2 + " -o " + outputdir
		subprocess.call(command, shell=True)
	elif (single == 'True') : # single-end read, alignment with bismark
		command = "bismark --bowtie2 --non_directional " + genomeref + " " + R1 + " -o " + outputdir
		subprocess.call(command, shell=True)

# Sorting the output file BAM and creation of a SAM file
def sortAlignFile(inputfileR1, outputdir, paired, single):
	print "Step 4 : Sorting the output file BAM"
	if (paired == 'True') : # paired-end read
		name = os.path.basename(inputfileR1)
		prefix = os.path.splitext(name)
		Bamfile = outputdir +"/"+prefix[0] + "_val_1_bismark_bt2_pe.bam" # name of BAM file sorted
		command = "samtools sort " + Bamfile + " " + outputdir +"/"+ prefix[0] +".sort" 
		print "Step 5 : Creation of a SAM file"
		subprocess.call(command, shell=True)
		command = "samtools view -h " + outputdir +"/"+ prefix[0] +".sort.bam > "+ outputdir +"/"+   prefix[0] +"_pe.sort.sam"
		subprocess.call(command, shell=True)
	elif (single == 'True') : # single-end read
		name = os.path.basename(inputfileR1)
		prefix = os.path.splitext(name)
		Bamfile =  outputdir +"/"+prefix[0] + "_val_1_bismark_bt2.bam" # name of BAM file sorted
		command = "samtools sort " + Bamfile + " " + outputdir +"/"+ prefix[0] +".sort"
		print "Step 5 : creation of a SAM file"
		subprocess.call(command, shell=True)
		command = "samtools view -h " + outputdir +"/"+ prefix[0] +".sort.bam > " + outputdir +"/"+  prefix[0] +"_se.sort.sam"
		subprocess.call(command, shell=True)


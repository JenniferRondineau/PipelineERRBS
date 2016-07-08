#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jun 24, 2016

import subprocess
import os

#Function to extract differentially methylated cytosine (DMC) and differentially methylated regions (DMR)
def extractionDMCDMR(control,case, outputdir,name):

	split = os.path.splitext(control)
	extension = split[1]
	if not extension == '.txt':
		control = split[0] +"_CpG.txt"
	split = os.path.splitext(case)
	extension = split[1]
	if not extension == '.txt':
		case = split[0] +"_CpG.txt"

	# Obtaining the path where the script is located
	path=os.popen("echo $PipelineERRBSdata_PATH").read()

	command = "Rscript $PipelineERRBS_PATH/extraction_DMC_DMR.R " + control + " " + case + " " + outputdir + " "+ name + " "+ path
	subprocess.call(command, shell=True)

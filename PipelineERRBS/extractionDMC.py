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
import os

def extractionDMCDMR(control,case, outputdir,name):

	split = os.path.splitext(control)
	extension = split[1]
	if not extension == '.txt':
		control = split[0] +"_CpG.txt"
	split = os.path.splitext(case)
	extension = split[1]
	if not extension == '.txt':
		case = split[0] +"_CpG.txt"	
	command = "Rscript /home/stage/Bureau/PipelineERRBS/PipelineERRBS/scriptR/extraction_DMC_DMR.R " + control + " " + case + " " + outputdir + " "+ name
	subprocess.call(command, shell=True) 



def extractionDMCDMRGroup(control,case, outputdir,name):
	listfilecontrol = str()
	listtreatment = str()
	listID = str()
	listfile = str()
	controlfile = open(control,"r")
	for line in controlfile:
		listfilecontrol += line.rstrip('\n') +  ","
		listID += (os.path.basename(line.rstrip('\n'))).rstrip('_CpG.txt')+ ","
		listtreatment += "0,"
	controlfile.close()
	print listfilecontrol

	listfilecase = str()
	controlcase = open(case,"r")
	for line in controlcase:
		listfilecase += line.rstrip('\n') +  ","
		listID += (os.path.basename(line.rstrip('\n'))).rstrip('_CpG.txt')+ ","
		listtreatment += "1,"
	controlcase.close()
	listfile += listfilecontrol + listfilecase[:-1]
	print listtreatment[:-1]
	print listID[:-1]


	command = "Rscript /home/stage/Bureau/PipelineERRBS/PipelineERRBS/scriptR/extraction_DMC_DMR.R " + listfile + " "  + outputdir + " "+ name +" "+ listID[:-1] +" "+ listtreatment[:-1]
	subprocess.call(command, shell=True) 


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ERRBS DNA methylation analysis pipeline
# Author: Jennifer Rondineau
# Date: Jul 4, 2016

import os
import sys
import getopt
from CheckRequired import *
from usage import *
from intersect import *


def ChromHMMannotate(argv):
    	__version__ = "0.0.1"  # version of ChromHMMannotate

    	# Initialize all parameters to default values
    	bedfile = str() # input bedfile ([chr] [start] [end])
    	outputfile = str() # name of the output file
    	ChromHMMfile = str() # ChromHMM input file with segmentation
    	number = str() # number of ChromHMM segmentation

    	# if any arguments are given print usage message and then exit the programm
    	if len(argv) == 1:
    		usageChromHMMannotate()
    		sys.exit(2)

	# List of all options possible
    	try:
    		opts, args = getopt.getopt(argv[1:],"hb:o:c:n:",["outputfile=", "ChromHMMfile="])
    	except getopt.GetoptError:
            usageChromHMMannotateChromHMMannotate()
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h': # print usage message
                usageChromHMMannotate()
                sys.exit()
            elif opt == '-b': # input bedfile
                checkFile(arg)
                bedfile = arg
            elif opt in ("-c", "--ChromHMMfile"): # name of statistic file
                checkFile(arg)
                ChromHMMfile = arg
            elif opt == '-n': # filename of the analysis GO
                number = arg
            elif opt in ("-o", "--outputfile"): # Output file
                outputfile = arg
        command = "cat " + ChromHMMfile + "  | grep -v track | cut -f 4 | sort | uniq > temp.txt"
        subprocess.call(command, shell=True)
    #    with open("temp.txt", "r") as f:
        #  for line in f:
        command = "cat " + ChromHMMfile + " | grep 1_ | bedtools intersect -a "+ bedfile + " -b - -wa > " + outputfile +".txt"
        subprocess.call(command, shell=True)

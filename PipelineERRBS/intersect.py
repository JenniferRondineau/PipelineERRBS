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

def intersect(ChromHMMfile,bedfile,outputfile,ggg):
    command = "cat " + ChromHMMfile + "  | grep "+ ggg + " | bedtools intersect -a "+ bedfile + " -b - -wa > " + outputfile +".txt"
    subprocess.call(command, shell=True)

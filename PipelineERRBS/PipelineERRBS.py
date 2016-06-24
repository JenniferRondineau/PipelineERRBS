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
from ERRBSalign import *
from usage import *

__all__ = ['main']

def main():
	__version__ = "0.0.1"  # version of PipelineERRBS
	if len(sys.argv) == 1: 
		usagePipeline()
		sys.exit(2)
	if sys.argv[1] == 'ERRBSalign':
		mainERRBSalign(sys.argv[1:])

if __name__ == "__main__":
    main()

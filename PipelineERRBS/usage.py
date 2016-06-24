#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# ERRBS DNA methylation analysis pipeline 
#
# Author: Jennifer Rondineau
# Date: Jun 24, 2016
#
# 

def usageERRBSalign() :
	print ''
	print '#######################################################################'
	print 'ERRBSalign : Tool for alignment and filtration of reads, ERRBS analysis'
	print '#######################################################################'
	print ''
	print 'USAGE:\n '
	print "\t paired-end read: ERRBSalign --paired -1 <fastqR1> -2 <fastqR2> -g <genomefolder>  -o <outputdir>"
	print '\t single-end read: ERRBSalign --single <fastq> -g <genomefolder>  -o <outputfile>\n\n'
	print 'ARGUMENTS: \n '
	print '\t -h, --help : print the usage message'
	print '\t -v, --version : print the solfware version'
	print '\t --single FILE : name of single-end fastq file to analyze (must be .fastq or .fastq.gz) '
	print "\t or"
	print '\t --paired -1 FILE1 -2 FILE2	: name of fastq file for (-1) Read1 and (-2) Read2 for paired-end datas to analyze(must be .fastq or .fastq.gz)"'
	print '\t -g, -genome_ref DIR : name of the reference genome directory'
	print '\t -o, outputdir : name of the output directory\n'
	print 'LIMITATIONS: \n'
	print '\t Fastq file to analyze must be .fastq or .fastq.gz'
	print '\t Analyze only non-directional bisulfite sequencing\n'
	print 'AUTHORS:\n'
	print '\t Jennifer Rondineau, student in bioinformatics (M2, University of Nantes) wrote this code\n'
	print 'SEE ALSO:\n'
	print '\t Samtools website <http://samtools.sourceforge.net>'
	print '\t Trim_galore website <http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/>'
	print '\t Fastqc website <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>'
	print '\t Bismark website <http://www.bioinformatics.babraham.ac.uk/projects/bismark/>'
	print '\t Bowtie2 website <http://bowtie-bio.sourceforge.net/bowtie2/index.shtml>\n'
	
def usagePipeline() : 
	print ''
	print '#######################################################################'
	print 'PipelineERRBS : ERRBS DNA methylation analysis pipeline'
	print '#######################################################################'
	print ''
	print 'OPTIONS:\n '
	print '\t ERRBSalign'
	print '\t methylERRBS'
	print '\t annotateERRBS\n'
	print 'LIMITATIONS: \n'
	print '\t Fastq file to analyze must be .fastq or .fastq.gz'
	print '\t Analyze only non-directional bisulfite sequencing\n'
	print 'AUTHORS:\n'
	print '\t Jennifer Rondineau, student in bioinformatics (M2, University of Nantes) wrote this code\n'
	print 'SEE ALSO:\n'
	print '\t Samtools website <http://samtools.sourceforge.net>'
	print '\t Trim_galore website <http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/>'
	print '\t Fastqc website <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>'
	print '\t Bismark website <http://www.bioinformatics.babraham.ac.uk/projects/bismark/>'
	print '\t Bowtie2 website <http://bowtie-bio.sourceforge.net/bowtie2/index.shtml>\n'


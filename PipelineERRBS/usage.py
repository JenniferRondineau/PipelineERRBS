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
	print '\t single-end read: ERRBSalign --single <fastq> -g <genomefolder> -o <outputdir>\n\n'
	print 'ARGUMENTS: \n '
	print '\t -h, --help : print the usage message'
	print '\t -v, --version : print the solfware version'
	print '\t --single FILE : name of single-end fastq file to analyze (must be .fastq or .fastq.gz) '
	print "\t OR"
	print '\t --paired -1 FILE1 -2 FILE2 : name of fastq file (-1) Read1 and (-2) Read2 for paired-end datas to analyze (must be .fastq or .fastq.gz)"'
	print '\t -g, --genome_ref DIR : name of the reference genome directory'
	print '\t -o, --outputdir DIR : name of the output directory\n'
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
	print '\t extractionCpG'
	print '\t methylDiffbyPatient'
	print '\t annotateDMR\n'
	print 'LIMITATIONS: \n'
	print '\t Analyze only non-directional bisulfite sequencing'
	print '\t Analysis of diffential methylation events is only possible between a control file and a case file. An R script is available (/PipelineERRBS/scriptR//home/stage/Bureau/PipelineERRBS/PipelineERRBS/scriptR/extraction_DMC_DMR.R), for the analysis of a control group versus a case group (see documentation)\n'
	print 'AUTHORS:\n'
	print '\t Jennifer Rondineau, student in bioinformatics (M2, University of Nantes) wrote this code\n'
	print 'SEE ALSO:\n'
	print '\t Samtools website <http://samtools.sourceforge.net>'
	print '\t Trim_galore website <http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/>'
	print '\t Fastqc website <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>'
	print '\t Bismark website <http://www.bioinformatics.babraham.ac.uk/projects/bismark/>'
	print '\t Bowtie2 website <http://bowtie-bio.sourceforge.net/bowtie2/index.shtml>'
	print '\t methylKit website <https://github.com/al2na/methylKit>'
	print '\t eDMR website <https://github.com/ShengLi/edmr>'
	print '\t HOMER website <http://homer.salk.edu/homer/>\n'


def usageMethylDiffbyPatient():
	print ''
	print '#######################################################################'
	print 'MethylDiffbyPatient'
	print '#######################################################################'
	print ''
	print 'USAGE:\n '
	print '\t methylDiffbyPatient --control <sam> OR <_CpG.txt> --case <sam> OR <_CpG.txt> --name <str> -o <outputdir>\n'
	print 'ARGUMENTS: \n '
	print '\t -h, --help : print the usage message'
	print '\t -v, --version : print the solfware version'
	print '\t -1, --control FILE : name of the control SAM file which must be sorted (or "_CpG.txt" file)'
	print '\t -2, --case FILE : name of the case SAM file which must be sorted (or "_CpG.txt" file)'
	print '\t --name STR : an identifier for the differential methylation'
	print '\t -o, --outputdir DIR : name of the output directory\n'
	print 'AUTHORS:\n'
	print '\t Jennifer Rondineau, student in bioinformatics (M2, University of Nantes) wrote this code\n'
	print 'SEE ALSO:\n'
	print '\t methylKit website <https://github.com/al2na/methylKit>'
	print '\t eDMR website <https://github.com/ShengLi/edmr>\n'

def usageextraction():
	print ''
	print '#######################################################################'
	print 'Extraction CpG'
	print '#######################################################################'
	print ''
	print '#######################################################################\n'
	print 'USAGE:\n '
	print '\t extractionCpG -f <SAM FILE> -o <outputdir> \n'
	print 'ARGUMENTS: \n '
	print '\t -h, --help : print the usage message'
	print '\t -f, FILE : sorted SAM file to extract CpG'
	print '\t -o, --outputdir DIR : name of the output directory \n'
	print 'AUTHORS:\n'
	print '\t Jennifer Rondineau, student in bioinformatics (M2, University of Nantes) wrote this code\n'
	print 'SEE ALSO:\n'
	print '\t methylKit website <https://github.com/al2na/methylKit>'



def usageannotate():
	print ''
	print '#######################################################################'
	print 'Annotation DMR with HOMER (annotatePeak.pl)'
	print '#######################################################################'
	print ''
	print '#######################################################################\n'
	print 'USAGE:\n '
	print '\t annotateDMR -b <BEDFILE> -s <FILE> --go <output directory> -o <OUTPUTFILE>\n'
	print 'ARGUMENTS: \n '
	print '\t -h, --help : print the usage message'
	print '\t -b, FILE : name of bedfile containing DMRs (chr, start, end) '
	print '\t -s, --annStat FILE : name of annotation statistic file '
	print '\t --go DIR : filename of the analysis GO'
	print '\t -o, --outputfile FILE : name of the output file\n'
	print 'AUTHORS:\n'
	print '\t Jennifer Rondineau, student in bioinformatics (M2, University of Nantes) wrote this code\n'
	print 'SEE ALSO:\n'
	print '\t HOMER website <http://homer.salk.edu/homer/>\n'


*********************
# PipelineERRBS
*********************

# Description

PipelineERRBS is a software allowing to analyse ERRBS data :

	- filtering data,
	- alignement,
	- extraction of CpGs,
	- analysis of differential methylation events,
	- annotation of differential methylation events.

PipelineERRBS is designed only to analyze non-directional bisulfite sequencing. Furthermore, differential methylation analysis is only possible between a control file and a case file. An R script is available (/PipelineERRBS/scriptR/methylDiffbyGroup.R), for the analysis of a control group versus a case group.

# Requirements

PipelineERRBS requires :

	- Trim_galore
	- Cutadapt
	- Samtools
	- Bismark
	- Bowtie2
	- Fastqc
	- methylKit
	- edmr
	- HOMER

# Download

```shell
$ git clone "https://github.com/JenniferRondineau/PipelineERRBS.git"
```

# Installation

```shell
$ cd PipelineERRBS
$ python setup.py install
```

Add in your bashrc file:
```shell
export PipelineERRBS_PATH=<PATH>/PipelineERRBS/PipelineERRBS/scriptR
export PipelineERRBSdata_PATH=<PATH>/PipelineERRBS/PipelineERRBS/data
```
# Usage

Step 1. Data filtering and alignment of reads

```shell
paired-end read: PipelineERRBS align --paired -1 <fastqR1> -2 <fastqR2> -g <genomefolder>  -o <outputdir>
single-end read: PipelineERRBS align --single <fastq> -g <genomefolder> -o <outputdir>
```

Step 2. Extraction of CpGs

```shell
PipelineERRBS extractionCpG -f <SAM FILE> -o <outputdir>
```

Step 3. Differential methylation analysis between a control file and a case file

```shell
PipelineERRBS methylDiffbyPatient --control <sam> OR <_CpG.txt> --case <sam> OR <_CpG.txt> --name <str> -o <outputdir>
```

Step 4. Annotation of differentially methylation regions and GO ontology analysis

```shell
PipelineERRBS annotate -b <BEDFILE> -s <FILE> --go <output directory> -o <OUTPUTFILE>
```

Additional option :  

1) Differential methylation analysis between a control group and a case group : If you want to compare methylation profile of two groups, a R script is available in this package (PipelineERRBS/scriptR/methylDiffbyGroup.R). It suffices to add path of your files '\_CpG.txt' in the R script (see example in the R script), and then
```shell
Rscript $PipelineERRBS_PATH/methylDiffbyGroup.R
```
2) Option : coveredCpG, allows to obtain a bed file containing all CpGs sequenced in case and control file
```shell
PipelineERRBS coveredCpG --control <_CpG.txt> --case  <_CpG.txt> --name <str> -o <outputdir>
```

# Reference sequences

The annotation files (/PipelineERRBS/data/) refseq.hg19 and cpgi.hg19 come from UCSC Genome Browser (https://genome.ucsc.edu/).

The "all_enhancers" file was created by combining enhancers described by the ENCODE projet (https://sites.google.com/site/anshulkundaje/projects/epigenomeroadmap) and FANTOM (http://enhancer.binf.ku.dk/presets/), these data are derived from more than 100 different cell lines.



# Authors

Jennifer Rondineau, bioinformatics student (M2) wrote this code.

###### See also :
Samtools website <http://samtools.sourceforge.net> <br>
Trim_galore website <http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/><br>
Fastqc website <http://www.bioinformatics.babraham.ac.uk/projects/fastqc/><br>
Bismark website <http://www.bioinformatics.babraham.ac.uk/projects/bismark/><br>
Bowtie2 website <http://bowtie-bio.sourceforge.net/bowtie2/index.shtml><br>
methylKit website <https://github.com/al2na/methylKit><br>
eDMR website <https://github.com/ShengLi/edmr><br>
HOMER website <http://homer.salk.edu/homer/><br>

# Contact & Questions
If you have any questions : <jennifer.rondineau@etu.univ-nantes.fr>

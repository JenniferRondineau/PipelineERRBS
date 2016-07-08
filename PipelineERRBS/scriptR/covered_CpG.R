
args <- commandArgs(trailingOnly = TRUE)


library(methylKit)

if (length(args) == 5 ) {
	localisation_Control <- args[1]
	localisation_Case <- args[2]
	output <- args[3]
	IDifferentialMethylation <- args[4]
	path <- args[5]
	file.list=list(localisation_Control,localisation_Case)
	myobj=read( file.list, sample.id=list("Control","Case"),assembly="hg19",treatment=c(0,1))
}

# merge all samples to one tab
meth = unite(myobj)

#CALCULATE DIFFERENTIAL METHYLATION
# calculate differential methylation p-values and q-values
myDiff=calculateDiffMeth(meth)


#CALCULATE DIFFERENTIAL METHYLATION
# calculate differential methylation p-values and q-values
myDiff=calculateDiffMeth(meth)
# check how data part of methylDiff object looks like
head( myDiff )

#save CoveredCpG
CoveredCpG <- paste(output, IDifferentialMethylation, "_DMC.txt", sep="" )
write.table(myDiff, CoveredCpG, row.names=FALSE, sep="\t", dec=",",na=" ")

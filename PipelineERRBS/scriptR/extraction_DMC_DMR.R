
args <- commandArgs(trailingOnly = TRUE)

localisation_Control <- args[1]
localisation_Case <- args[2]
output <- args[3]
IDifferentialMethylation <- args[4]
listID <-args[5]
listtreatment<-args[6]


library(methylKit)

if (length(args) == 4 ) {
	localisation_Control <- args[1]
	localisation_Case <- args[2]
	output <- args[3]
	IDifferentialMethylation <- args[4]
	file.list=list(localisation_Control,localisation_Case)
	myobj=read( file.list, sample.id=list("Control","Case"),assembly="hg19",treatment=c(0,1))
}

meth = unite(myobj)

#CALCULATE DIFFERENTIAL METHYLATION
# calculate differential methylation p-values and q-values
myDiff=calculateDiffMeth(meth)
# check how data part of methylDiff object looks like
head( myDiff )
# get differentially methylated regions with 25% difference and qvalue<0.01
myDiff25p=get.methylDiff(myDiff,difference=25,qvalue=0.01)
# get differentially hypo methylated regions with 25% difference and qvalue<0.01
myDiff25pHypo =get.methylDiff(myDiff,difference=25,qvalue=0.01,type="hypo") 
# get differentially hyper methylated regions with 25% difference and qvalue<0.01
myDiff25pHyper=get.methylDiff(myDiff,difference=25,qvalue=0.01,type="hyper")


# FIGURE 5A
# plot percentages of differentially methylated bases over all chromosomes
pngfilename <- paste (output, "Rplot_03_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
diffMethPerChr(myDiff,plot=TRUE,qvalue.cutoff=0.01,meth.cutoff=25,exclude=c("chrM","chrY","chrX") )
dev.off()
# read-in the transcript locations to be used in annotation, a text file in BED format
# either full path to the text file or an URL to the BED file must be provided
gene.obj=read.transcript.features("~/Bureau/PipelineERRBS/PipelineERRBS/data/refseq.hg19.bed.txt")

# FIGURE 6B
# annotate differentially methylated Cs with promoter/exon/intron using annotation data
diffAnn=annotate.WithGenicParts(myDiff25p,gene.obj)
getTargetAnnotationStats(diffAnn,percentage=TRUE,precedence=TRUE)
pngfilename <- paste (output, "Rplot_04_", IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
plotTargetAnnotation(diffAnn,precedence=TRUE,main="Differential methylation annotation by genes")
dev.off()

# FIGURE 6A
# plot nearest distance to TSS
tss.assoc=getAssociationWithTSS(diffAnn)
# plot the distance as histogram, plot only the ones that are at most 100kb away
pngfilename <- paste (output, "Rplot_05_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
hist(tss.assoc$dist.to.feature[abs(tss.assoc$dist.to.feature)<=100000],main="Distance to nearest TSS",xlab="distance in bp",breaks=50,col="brown4")
dev.off()


# FIGURE 6D
enhancer.obj=read.bed("/home/stage/Bureau/PipelineERRBS/PipelineERRBS/data/all_enhancers.bed")  # read the annotation file for enhancers
enhancer.ann=annotate.WithFeature(myDiff25p,enhancer.obj,feature.name="enhancers") #  annotate differentially methylated bases with enhancers
pngfilename <- paste (output, "Rplot_06_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
plotTargetAnnotation(enhancer.ann, main="Differential methylation annotation by enhancers") # plot pie chart for annotation
dev.off()

# FIGURE 6C
cpg.obj=read.feature.flank(location="/home/stage/Bureau/PipelineERRBS/PipelineERRBS/data/cpgi.hg19.bed.txt",feature.flank.name=c("CpGi","shores"))
# annotate differentially methylated Cs with CpG islands/shores using annotation data
diffCpGann=annotate.WithFeature.Flank(myDiff25p,cpg.obj$CpGi,cpg.obj$shores,feature.name="CpGi",flank.name="shores")
getFeatsWithTargetsStats(diffAnn,percentage=TRUE)
pngfilename <- paste (output, "Rplot_07_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
plotTargetAnnotation(diffCpGann,col=c("green","gray","white"), main="Differential methylation annotation by CpG islands")
dev.off()

#save DMC
output_DMC <- paste(output, IDifferentialMethylation, "_DMC.txt", sep="" )
write.table(myDiff25p, output_DMC, row.names=FALSE, sep="\t", dec=",",na=" ")


############################################################################################################
## EDMR
############################################################################################################

library(edmr)
library(GenomicRanges)
library(IRanges)

# fitting the bimodal normal distribution to CpGs distribution
pngfilename <- paste (output, "Rplot_08_",IDifferentialMethylation,".png", sep="")
png(filename= pngfilename)
myMixmdl=myDiff.to.mixmdl(myDiff, plot=T, main="example")
dev.off()

# plot cost function and the determined distance cutoff
pngfilename <- paste (output, "Rplot_09_", IDifferentialMethylation,".png", sep="")
png(filename= pngfilename)
plotCost(myMixmdl, main="cost function")
dev.off()

# calculate all DMRs candidate
mydmr=edmr(myDiff, mode=1, ACF=TRUE)

# further filtering the DMRs
mysigdmr=filter.dmr(mydmr)

get.hyper.dmr(mysigdmr)

get.hypo.dmr(mysigdmr)

## annotation
# get genebody annotation GRangesList object
genebody=genebody.anno("/home/stage/Bureau/PipelineERRBS/PipelineERRBS/data/refseq.hg19.bed.txt")

# plot the eDMR genebody annotation
pngfilename <- paste (output, "Rplot_10_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
plotdmrdistr(mysigdmr, genebody)
dev.off()

# get CpG islands and shores annotation
cpgi=cpgi.anno(file="/home/stage/Bureau/PipelineERRBS/PipelineERRBS/data/cpgi.hg19.bed.txt")

# plot the eDMR CpG islands and shores annotation
pngfilename <- paste (output, "Rplot_11_", IDifferentialMethylation,".png", sep="")
png(filename= pngfilename)
plotdmrdistr(mysigdmr, cpgi)
dev.off()

#save DMR
output_DMR <- paste(output,IDifferentialMethylation, "_DMR.bed", sep="" )
df <- data.frame(seqnames=seqnames(mysigdmr),
                 starts=start(mysigdmr),
                 ends=end(mysigdmr),
                 strands=strand(mysigdmr), 
                 mean.meth.diff=mysigdmr$mean.meth.diff, 
                 DMR.pvalue=mysigdmr$DMR.pvalue, 
                 DMR.qvalue=mysigdmr$DMR.qvalue)

write.table(df, file=output_DMR, quote=F, sep="\t", row.names=F, col.names=F)

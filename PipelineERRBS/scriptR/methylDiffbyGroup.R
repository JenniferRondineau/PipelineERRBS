
args <- commandArgs(trailingOnly = TRUE)


library(methylKit)


file.list=list( $LIST_PATH_CPG_FILE_TO_ANALYZE )

myobj=read( file.list, sample.id=list( $LIST_ID_SAMPLE ),assembly="hg19",treatment=c( $LIST_TREATMENT_0:Control_1:Case ))

# Example
# file.list=list( "/PATH/Sample_1_CpG.txt","/PATH/Sample_2_CpG.txt","/PATH/Sample_3_CpG.txt","/PATH/Sample_4_CpG.txt")
# myobj=read( file.list, sample.id=list("Sample1", "Sample2","Sample3","Sample4"),assembly="hg19",treatment=c(0,1,0,1))
            

# merge all samples to one tab
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

# plot percentages of differentially methylated bases over all chromosomes
pngfilename <- paste (output, "Rplot_03_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
diffMethPerChr(myDiff,plot=TRUE,qvalue.cutoff=0.01,meth.cutoff=25,exclude=c("chrM","chrY","chrX") )
dev.off()

# read-in the transcript locations to be used in annotation, a text file in BED format
refseq <- paste (path, "/refseq.hg19.bed.txt", sep="")
gene.obj=read.transcript.features(refseq)

# annotate differentially methylated Cs with promoter/exon/intron using annotation data
diffAnn=annotate.WithGenicParts(myDiff25p,gene.obj)
getTargetAnnotationStats(diffAnn,percentage=TRUE,precedence=TRUE)
pngfilename <- paste (output, "Rplot_04_", IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
plotTargetAnnotation(diffAnn,precedence=TRUE,main="Differential methylation annotation by genes")
dev.off()

# plot nearest distance to TSS
tss.assoc=getAssociationWithTSS(diffAnn)
# plot the distance as histogram, plot only the ones that are at most 100kb away
pngfilename <- paste (output, "Rplot_05_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
hist(tss.assoc$dist.to.feature[abs(tss.assoc$dist.to.feature)<=100000],main="Distance to nearest TSS",xlab="distance in bp",breaks=50,col="brown4")
dev.off()

# read the annotation file for enhancers
all_enhancer <- paste (path, "/all_enhancers.bed", sep="")
enhancer.obj=read.bed(all_enhancer)  
# annotate differentially methylated bases with enhancers
enhancer.ann=annotate.WithFeature(myDiff25p,enhancer.obj,feature.name="enhancers")
pngfilename <- paste (output, "Rplot_06_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
plotTargetAnnotation(enhancer.ann, main="Differential methylation annotation by enhancers") # plot pie chart for annotation
dev.off()

# annotate differentially methylated Cs with CpG islands/shores using annotation data
CpGfile <- paste (path, "/cpgi.hg19.bed.txt", sep="")
cpg.obj=read.feature.flank(location=CpGfile,feature.flank.name=c("CpGi","shores"))
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
refseq <- paste (path, "/refseq.hg19.bed.txt", sep="")
genebody=genebody.anno(refseq)

# plot the eDMR genebody annotation
pngfilename <- paste (output, "Rplot_10_",IDifferentialMethylation, ".png", sep="")
png(filename= pngfilename)
plotdmrdistr(mysigdmr, genebody)
dev.off()

# get CpG islands and shores annotation
CpGfile <- paste (path, "/cpgi.hg19.bed.txt", sep="")
cpgi=cpgi.anno(file=CpGfile)

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


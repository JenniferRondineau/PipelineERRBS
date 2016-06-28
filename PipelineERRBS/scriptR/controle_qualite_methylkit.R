
args <- commandArgs(trailingOnly = TRUE)

localisation <- args[1]
output <- args[2]
IDsample <- args[3]

library(methylKit)

mydata<-read.bismark(localisation, sample.id = IDsample, assembly="hg19", save.context="CpG", read.context="CpG", save.folder = output)

# get methylation statistics
pngfilename <- paste (output, "Rplot", IDsample, ".png", sep="")
png(filename= pngfilename)
getMethylationStats(mydata, plot=T)
dev.off()

# get coverage statistics
pngfilename <- paste (output, "Rplot02", IDsample, ".png", sep="")
png(filename= pngfilename)
getCoverageStats(mydata, plot=T)
dev.off()


args <- commandArgs(trailingOnly = TRUE)


localisation <- args[1]
output <- args[2]
IDsample <- args[3]


if (length(args) != 3 ) {
   	print("usage :");
	print("argument 1 : localisation du fichier ");
	print("argument 2 : identifiant de l'échantillon");
	q();
} 

library(methylKit)

mydata<-read.bismark(localisation, sample.id = IDsample, assembly="hg19", save.context="CpG", read.context="CpG", save.folder = output)

pngfilename <- paste (output, "Rplot", IDsample, ".png", sep="")
png(filename= pngfilename)
getMethylationStats(mydata, plot=T)
dev.off()

pngfilename <- paste (output, "Rplot02", IDsample, ".png", sep="")
png(filename= pngfilename)
getCoverageStats(mydata, plot=T)
dev.off()

args=commandArgs(T)
library(UpSetR)
require(ggplot2); require(plyr); require(gridExtra); require(grid);
#png(args[2],1700,1200,res=300)
pdf(args[2],10,8)
da=read.table(args[1],head=T,sep="\t",check.names=F)
nameda=names(da)[-1]
nameda
upset(da,sets=nameda,sets.bar.color=rainbow(args[3]),mainbar.y.label = "Commen gene family number",sets.x.label = "Gene family number of species",scale.intersections="identity",order.by="freq",empty.intersections="on",main.bar.color ='blue',matrix.color="red",point.size=2,number.angles=30,text.scale=0.8)
dev.off()

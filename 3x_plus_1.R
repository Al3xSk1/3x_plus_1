xdata <- read.csv("answer.csv")
pdf("rplot.pdf")
plot(xdata[, 1], xdata[, -1], type = "l")
dev.off()
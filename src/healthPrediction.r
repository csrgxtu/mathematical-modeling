data<-read.csv("2009数据与标准数据Friendman秩和检验.csv",row.names=1)
data.ma<-as.matrix(data)
friedman.test(data.ma)

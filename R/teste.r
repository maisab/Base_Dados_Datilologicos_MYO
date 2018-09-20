library(ggplot2)
library(reshape2)

dados<-read.csv(file = "/home/maisa/UTFPR/Tcc/Arquivos gerados/arq_r.csv")
#ggplot(dados, x = dados$id, y = dados$mediaxacc, type = 'scatter', mode = 'lines')
#ggplot(dados, aes('wt', 'mpg')) + \
#geom_line()


reshape(dados,v.names = "id", idvar = "id", timevar="id",  direction="wide") 
dados1<-dcast(melt(as.matrix(dados)), Var2~paste0('r', Var1), value.var='value')


dados1<- dados1[-1,]
#dados1<- dados1[,-1]
#View(dados1)

ggplot(dados1, aes(x=dados1$Var2, y=dados1$r1,group=1, colour=1)) + 
geom_line(aes(x=dados1$Var2,y=dados1$r2,group=2, colour=2))+
geom_line(aes(x=dados1$Var2,y=dados1$r3,group=3, colour=3))+
geom_line(aes(x=dados1$Var2,y=dados1$r4,group=4, colour=4))+  
geom_line(aes(x=dados1$Var2,y=dados1$r5,group=5, colour=5))+  
geom_line(aes(x=dados1$Var2,y=dados1$r6,group=6, colour=6))+  
geom_line(aes(x=dados1$Var2,y=dados1$r7,group=7, colour=7))+  
  geom_line(aes(x=dados1$Var2,y=dados1$r7,group=7, colour=7))+
  geom_line(aes(x=dados1$Var2,y=dados1$r7,group=7, colour=7))+
  geom_line(aes(x=dados1$Var2,y=dados1$r7,group=7, colour=7))+
  geom_line(aes(x=dados1$Var2,y=dados1$r7,group=7, colour=7))+
geom_line()



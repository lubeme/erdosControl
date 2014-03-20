
library(RJSONIO)
library(ggplot2)

oo<-fromJSON("http://pregel.mat.upm.es/ErdosN500MC100.json")
data<-do.call(rbind,lapply(1:100,function(i){
  return(cbind(names(oo)[i],1:length(oo[[i]]),unlist(oo[[i]])))
}))
mode(data)<-"numeric"
df<-data.frame(data)
names(df)<-c("experiment","edges_added","controllers")

rm(data,oo) #clean memory
df<-df[df$controllers>1,] #less points in plot

ggplot(df,aes(x=edges_added,y=controllers,group=experiment))+geom_line()
ggplot(df,aes(x=edges_added,y=controllers,group=experiment))+geom_line(alpha=0.05)+xlim(c(1,5e3))+theme_classic()


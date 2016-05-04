#read
setwd("D:\\Datasets\\Del Mar Goldline Station\\2016 Del Mar Station TAP boardings")
tap<-read.csv("DelMarTransHistV-030115-033116shortdata.csv",header=TRUE)

#convert to POSIX
tap[,1]<-as.POSIXct(tap[,1],format="%m/%d/%Y %H:%M")
names(tap)[1]<-"dtm"

#aggregate by different time periods
tap.date=as.data.frame(table(factor(format(tap$dtm,"%y-%m-%d"))))
tap.time=as.data.frame(table(factor(format(tap$dtm,"%H:%M"))))

names(tap.date)<-c("date","count")
names(tap.time)<-c("time","count")

#normalize by number of dates with data
tap.time$count=tap.time$count/nrow(tap.date)

#tap.day=tap
#tap.time=tap
#tap.day$dtm=as.character(round(tap[,1] , "day"))
#tap.time$dtm=as.character(round(tap[,1] , "hour" ))

#plot
library(ggplot2)

#plot by hour
custom.hours=c('01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00')
ggplot(data=tap.time,aes(x=time,y=count))+geom_point(size=0)+geom_smooth(aes(x=as.numeric(time),y=count))+
  theme(axis.text.x = element_text(face="bold", color="#993333", 
                                   size=12, angle=90))+
  scale_x_discrete(breaks = custom.hours)+
  ggtitle("Metro TAP Entry by Minute (Averaged Over 2015-2016)")+
  labs(x="Time of Day",y="Yearly Average TAP Entries / Minute")

#breaks = tap.time$time[ c( rep(FALSE,60), TRUE ) ]
#factor(custom.hours,levels=custom.hours,ordered=TRUE)


#plot by date
custom.date=format(seq(as.Date("15-03-01"),as.Date("16-03-01"),by="1 month"),format="%y-%m-%d")
ggplot(data=tap.date,aes(x=date,y=count))+geom_point()+geom_smooth(aes(x=as.numeric(date),y=count))+
  theme(axis.text.x = element_text(face="bold", color="#993333", 
                                   size=10))+
  scale_x_discrete(breaks = custom.date)+
  ggtitle("Metro TAP Entry by Date (2015-2016)")+
  labs(x="Date",y="Number of Metro Tap Entries / Day")

#maxes are the Rose Bowl and CicLAvia Pasadena


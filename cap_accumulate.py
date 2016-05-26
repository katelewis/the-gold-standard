"""
    Takes in CSV and builds accumulation of capacity in time bins.
    Miguel Aroca-Ouellette
    05/21/2016
"""
import csv
import datetime as dt

#constants
c={'datetime':0,'in_out':1,'unknown':2,'free':3,'discount':4,'full_price':5}
date_form='%Y-%m-%d %H:%M:%S'

#files
path="D:\Datasets\Del Mar Goldline Station\parsed_mar\\"
names=['del_mar']#,'paseo','marengo','los_robles','holly']
#parameters
time_bin=10*60 #every ten minutes
pin_day=dt.datetime.strptime('2015-07-23 00:00:00',date_form) #due to bad data
pin_total=108
pin_full=10
pin_discount=22
pin_free=76
pin_unknown=0

for name in names:
    #parsing info
    min_car=600
    max_car=0
    in_count=0
    out_count=0
    net_out=0
    #initialization
    curr_time=dt.datetime.strptime('2015-03-01 00:00:00',date_form)
    num_car_total=28 #to put the worst day (Feb 24th 2016) at 600
    num_car_full=2
    num_car_discount=5 #average percent
    num_car_free=21
    num_car_unknown=0
    pin_done=False
    print "Parsing "+name+'_inout.csv..'
    with open(path+name+'_inout.csv','r') as f, open(path+name+'_flow.csv','w') as fo:
        csv_in = csv.reader(f, delimiter=',')
        csv_out= csv.writer(fo,delimiter=',',lineterminator='\n')

        #write out initial time
        csv_out.writerow([curr_time.strftime(date_form),str(num_car_total),str(num_car_discount)])

        header=next(csv_in)
        for row in csv_in:
            in_out=int(row[c['in_out']])
            mytime=dt.datetime.strptime(row[c['datetime']],date_form)
            unknown=int(row[c['unknown']])
            discount=int(row[c['discount']])
            free=int(row[c['free']])
            full_price=int(row[c['full_price']])

            if mytime>pin_day and not pin_done:
                print "Pin complete!"
                pin_done=True
                num_car_total=pin_total
                num_car_full=pin_full
                num_car_discount=pin_discount
                num_car_free=pin_free
                num_car_unknown=pin_unknown

            while mytime>=(curr_time+dt.timedelta(0,time_bin)): #while >10 minutes away
                curr_time+=dt.timedelta(0,time_bin)
                csv_out.writerow([curr_time.strftime(date_form),str(num_car_total),str(num_car_unknown),str(num_car_free),str(num_car_discount),str(num_car_full)])
                out_count+=1

            num_car_total+=in_out

            if discount:
                num_car_discount+=in_out
            elif unknown:
                num_car_unknown+=in_out
            elif free:
                num_car_free+=in_out
            elif full_price:
                num_car_full+=in_out
            else:
                print "IMPOSSIBLE"
                break

            if num_car_total>max_car:
                max_car=num_car_total

            if num_car_total<min_car:
                min_car=num_car_total

            in_count+=1

            if in_count%100000==0:
                print "Parsed datetime: "+curr_time.strftime(date_form)+" ",
                print row

            if curr_time.date()!=mytime.date():
                print "----"
                print (mytime-curr_time).seconds
                print "Parsed datetime: "+curr_time.strftime(date_form)+" ",
                print row
                break

    print "Parsed "+str(in_count)+" lines."
    print "Output "+str(out_count)+" lines."
    print "Peak capacity "+str(max_car)+" cars."
    print "Trough capacity "+str(min_car)+" cars."

    f.close()
    fo.close()


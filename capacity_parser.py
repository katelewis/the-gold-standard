"""
    Parser for capacity analysis.
    Miguel Aroca-Ouellette
    05/20/2016
"""

import csv

#car park dict
car_park={
         "Paseo":0,
         "Marengo":1,
         "Los Robles":2,
         "Holly":3,
         "Del Mar":4}

#column dict
col_dict={"Park Trans #":0,
          "Car Park #":1,
          "Entry Time":2,
          "Exit Time":3,
          "Net Price":4,
          "Net Turnover":5,
         }

#file vars
path="D:\Datasets\Del Mar Goldline Station\parsed_mar\\"
all_ent_ppa='all_ENT_PPA.csv'

for park in car_park.iterkeys():
    with open(path+'flow_'+park+'.csv','w') as fo, open(path+all_ent_ppa,'r') as f:
        csv_out = csv.writer(fo, delimiter=',',lineterminator='\n')
        csv_in = csv.reader(f, delimiter=',')
        for row in csv_in:
            if int(row[col_dict["Car Park #"]])==car_park[park]: #check that its the correct car park
                if row[col_dict["Net Price"]]==row[col_dict["Net Turnover"]]:
                    #full paying user
                    csv_out.writerow(row[col_dict["Entry Time"]:col_dict["Exit Time"]+1]+["0"])
                else:
                    #discounted user
                    csv_out.writerow(row[col_dict["Entry Time"]:col_dict["Exit Time"]+1]+["1"])
    fo.close()
    f.close()
    print park+" done."

"""
    File counter.
    Miguel Aroca-Ouellette
    05/20/2016
"""

import csv,os,glob
#constants

#file vars
path="D:\Datasets\Del Mar Goldline Station\\del_mar_complete"
file_end=["ENT","PAR","PPA","VAL","PAS",]
delim=';'

os.chdir(path)


for end in file_end:
    i = 0
    for myfile in glob.glob("*."+end):
        with open(myfile,'r') as f:
            line=f.readline() #header countains file count
            if len(line.strip())==0:
                print myfile+" is empty!"
                continue
            i+=int(line.strip().split(delim)[3])

    print "Total entries for "+end+" "+str(i)
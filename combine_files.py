import csv,sys

#constants
ppa_cols = {
    "Payment transaction number" : 0,
    "Position number": 1,
    "Car Park" : 2,
    "Device #" :3,
   	"Date/time of transaction" : 4,
    "Personal ID" : 5,
    "Trans Aborted" : 6,
    "Trans Cancel" : 7,
    "Price (Before Validation)" : 8,
    "Turnover (Amount Paid)" : 9,
    "Payment Type" :10,
    "Parking transaction number" : 11,
    "Net Price" : 12,
    "Net Turnover" : 13,
    "Rate #" :14,
    "Name" : 15,
    "Street" : 16,
    "City" : 17,
    "Tax Code" : 18,
    "Invoice Produced" : 19,
    "Invoice #" :20
}

ent_cols = {
    "Trans #" : 0,
    "Car Park #" : 1,
    "Entry Device" : 2,
    "Entry Date/Time" : 3,
    "Exit Device" : 4,
    "Exit Date/Time" : 5,
    "Date/time of last payment" : 6,
    "Device number cell entry column" : 7,
    "Date/time of cell entry" : 8,
    "Device number cell exit" : 9,
    "column Date/time of cell exit" :10,
    "Misuse" : 11,
    "Ticket type" : 12,
    "SKIDATA AG ticket number" : 13,
    "Article" : 14,
    "First Use" : 15,
    "Invoice #" : 16,
    "Date of Production" : 17,
    "CC Number" : 18,
    "CC Company" : 19,
    "Facility" : 20
}

#columns to keep
ppa_keep=[ppa_cols[k] for k in ("Payment transaction number",
                                   "Car Park",
                                   "Date/time of transaction",
                                   "Price (Before Validation)"
                                   )] #add whatever else you want

ent_keep=[ent_cols[k] for k in ("Trans #",
                                   "Entry Date/Time",
                                   "Exit Date/Time"
                                   )] #add whatever else you want

#file vars
path="sample_data/"
ppa_name="TR150301.PPA"
ent_name="TR150301.ENT"
out_name="combined.csv"
delim=';'

ppa_file = open(path+ppa_name, 'r')
d = {}
i = 0
expected = 0 #expected number of entries

for cur_line in ppa_file:
    i += 1
    if i==1:
        #header
        expected = int(cur_line.strip().split(';')[3])
        continue
    cur_line = cur_line.strip().split(delim)
    #only keep data you want from the column
    line_short= [cur_line[k] for k in ppa_keep]
    # Use the column you want to match
    d[cur_line[ppa_cols["Parking transaction number"]]] = line_short

print("Entries in ",ppa_name, i)

if (i-1) != expected:
    print("Warning: does not match expected", expected)

output_file = open(path+out_name, 'w')

ent_file = open(path+ent_name, 'r')
filewriter = csv.writer(output_file, delimiter=',')

i = 0
found = 0
missing = 0
for cur_line in ent_file:
    i += 1
    if i==1:
        #header
        expected = int(cur_line.strip().split(';')[3])
        continue
    cur_line = cur_line.strip().split(delim)
    #only keep data you want from column
    line_short = [cur_line[k] for k in ent_keep]
    # Use the column you want to match
    if cur_line[ent_cols["Trans #"]] in d:
        filewriter.writerow(d[cur_line[ent_cols["Trans #"]]]+ line_short)
        found += 1
    else:
        missing += 1

print("Entries in ",ent_name, i)
if (i-1) != expected:
    print("Warning: does not match expected", expected)
print("FOUND", found)
print("MISSING", missing)
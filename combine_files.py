import csv

ent_file = open("tran_data.txt", 'r')
d = {}
i = 0
for cur_line in ent_file:
    i += 1
    cur_line = cur_line.strip().split(',')
    # Use the column you want to match
    d[cur_line[9]] = cur_line

print("Entries in file 1", i)
output_file = open("ent_trans.txt", 'w', newline="")

tran_file = open("ent_data.txt", 'r')
filewriter = csv.writer(output_file, delimiter=',')


i = 0
found = 0
missing = 0
for cur_line in tran_file:
    i += 1
    cur_line = cur_line.strip().split(',')
    # Use the column you want to match
    if cur_line[0] in d:
        filewriter.writerow(d[cur_line[0]]+ cur_line)
        found += 1
    else:
        missing += 1

print("Entries in file 2", i)
print("FOUND", found)
print("MISSING", missing)
import re


f = open('sample_storm_log.log', 'r')
for line in f:
    if "r.AppendByteBolt" in line and "###################################" not in line:
        filtered_line = line.split('r.AppendByteBolt')[1].split(' [INFO] ')[1].split(',')
        if len (filtered_line) > 2:
            print (filtered_line[0] + ' ' + filtered_line[1] + ' ' + filtered_line[2])




f = open('sample_storm_log.log', 'r')
for line in f:
    if "r.AppendByteBolt" in line and "###################################" not in line:
        filtered_line = line.split('r.AppendByteBolt')[1].split(' [INFO] ')[1].split(',')
        if len (filtered_line) < 3:
            print(filtered_line[0]+ ' '+ filtered_line[1])


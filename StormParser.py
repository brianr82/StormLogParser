


f = open('sample_storm_log.log', 'r')
for line in f:
    if "r.AppendByteBolt" in line and "###################################" not in line:
        print(line)

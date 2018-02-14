import re

infile = "/home/patrick/aprs/KJ4OVR-2012.LOG"

with open(infile,'r') as f:
    data = f.read()
data_split = re.split(r'(: )', data)

print "\n".join(data_split)

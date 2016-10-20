'''
urllib、csv模块memo
'''

import urllib.request
fp = urllib.request.urlopen("http://www.python.org")

with open('/Uses/fanxn/Desktop/outfile', 'wb') as ofs:
    ofs.write(fb.read())


import csv
ifs = open('/Users/fanxn/Desktop/w1q1t1.csv')
cfs = csv.reader(ifs)
l1 = list(cfs)

cnt1 = 0
for line in l1[1:]:
    for val in line:
        if val.isdigit() and float(val) > 1000000:
            cnt1 += 1

for colidx in range(len(l1[0])):
    for row_idx in range(1, len(l1)):
        val = l1[row_idx][colidx]
        if val.isdigit() and float(val) >= 1000000:
            print(row_idx, colidx)
            cnt1 += 1
            break

print(cnt1)


[a.b.c, a.b.d. a.e]


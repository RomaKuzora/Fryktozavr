import csv
import math

date_cur = ''
time_cur = ''
lum_cur = 0
count_cur = 0
lum_prev = -math.inf
date_max = ''
time_max = ''
count_max = 0
fname = 'alpha_oriona.csv'
with open(fname) as csvf:
    rdr = csv.DictReader(csvf, delimiter=';')
    for row in rdr:
        lum = int(row['luminosity'])
        if lum > lum_prev:
            date_cur = row['date']
            time_cur = row['time']
            lum_cur = lum
            count_cur = 1
        else:
            count_cur += 1
            if count_cur > count_max:
                count_max = count_cur
                date_max = date_cur
                time_max = time_cur
        lum_prev = lum
print(count_max, date_max, time_max)

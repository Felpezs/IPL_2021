year = 2021
month = 1
day = 1

if(month == 1 or month == 2):
    y1 = year - 1
    m1 = month + 12

else:
    y1 = year
    m1 = month

y_cen = y1 % 100
cen = y1 // 100

w = (day + (13 * (m1 + 1) // 5) + y_cen + (y_cen//4) + (cen // 4) - 2 * cen) % 7

out = w
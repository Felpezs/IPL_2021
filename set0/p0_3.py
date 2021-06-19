kwh_used = 500
kwh_param = 500
tax = 0.2

# kwh_used <= 500
if(kwh_used <= kwh_param):
    out = kwh_used * 0.45

# 500 < kwh_used <= 1000
elif(kwh_used > kwh_param and kwh_used <= kwh_param * 2):
    kwh_excess = kwh_used - kwh_param
    out = kwh_excess * 0.74 + kwh_param * 0.45
        
# kwh_used >= 1500
elif(kwh_used > kwh_param * 2 and kwh_used <= kwh_param * 3):
    kwh_excess = kwh_used - kwh_param * 2
    out = kwh_param * 0.45 + kwh_param * 0.74 + kwh_excess * 1.25

else:
    kwh_excess = kwh_used - kwh_param * 3
    out = kwh_param * 0.45 + kwh_param * 0.74 + kwh_param * 1.25 + kwh_excess * 2.

out = out * tax + out

print(out)
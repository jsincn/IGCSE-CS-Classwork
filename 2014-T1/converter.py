ic = input("Input Currency")
inp = float(input("Input amount"))
oc = input("Output Currency")

if ic == "CNY":
    if oc == "GBP":
        out = inp/10
        ocs = "£"
    if oc == "EUR":
        out = inp/7
        ocs = "€"
elif ic == "GBP":
    if oc == "CNY":
        out = inp*10
        ocs = "¥"
    if oc == "EUR":
        out = inp*1.27685
        ocs = "€"
elif ic == "EUR":
    if oc == "GBP":
        out = inp/0.78276
        ocs = "£"
    if oc == "CNY":
        out = inp*7
        ocs = "¥"
else:
    print("Invalid Currency")
print(str(inp) + " " + ic + " is " + str(round(out,2)) + ocs)
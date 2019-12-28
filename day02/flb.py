flb=[0,1]
n = int(input("number lenth:"))
for i in range(n - 2):
    flb.append(flb[-1] + flb[-2])
print(flb)
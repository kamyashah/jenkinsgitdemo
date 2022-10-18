n = int(input("enter number of items:"))
maxwt = int(input("enter the maximum weight:"))
profit = []
weight = []
for i in range(n):
    p = int(input("enter the profit:"))
    profit.append(p)
    w = int(input("enter the weight:"))
    weight.append(w)

wt = 0
max_profit = 0
ppw = []
for i in range(n):
    ppw.append(profit[i] / weight[i])
order = []
for i in range(n):
    order.append(ppw.index(max(ppw)))
    ppw[ppw.index(max(ppw))] = 0
i = 0
print("\nitems in knapsack:")
while wt != maxwt:
    if (wt + weight[order[i]]) <= maxwt:
        max_profit += profit[order[i]]
        wt = weight[order[i]]
        print("%d\t%d\t%d\t\t1" % (order[i] + 1, weight[order[i]], profit[order[i]]))
    else:
        fraction = (maxwt - wt) / weight[order[i]]
        value = profit[order[i]] * fraction
        max_profit += value
        wt += (maxwt - wt)
        print("%d\t%d\t%0.2f\t\t%0.2f" % (order[i] + 1, weight[order[i]], value, fraction))
    i += 1
print("\nMaximum profit= %0.2f" % max_profit)


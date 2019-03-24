import sys, string, math
n = int(input())
n = int(input())
p = list(map(int,input().split()))
dic1 = {}
for i in p :
    if i in dic1 :
        dic1[i] += 1
    else :
        dic1[i] = 1
p = []
flag = 1
for k in dic1 :
    if dic1[k] > 1 :
        p.append(k)
        flag = 0
p2 = sorted(p)
if flag : print("unique")
else : print(*p2)

import sys, string, math
n = int(input())
p = list(map(int,input().split()))
for i in range(len(p)) :
    if p.count(p[i]) == 1 :
        print(p[i])
        break

import sys, string, math
n = int(input())
p = list(map(int,input().split()))
p2 = []
for i in range(n) :
    if p[i] == i : p2.append(i)
p3 = sorted(p2)
if len(p3) == 0 : print(-1)
else :     print(*p3)

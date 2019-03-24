import sys, string, math
n = int(input())
p = list(map(int,input().split()))
p2 = sorted(p)
k = len(p)
#print(L,L2,k)
sum1 = p2[0]
a = 10
for i in range(1,len(p2)) :
    sum1 = sum1 + p2[i]*a
    a = a*10
print(sum1)

n=int(input())
l=list(map(int,input().split()))
a=l.index(min(l))+1
b=l.index(max(l))+1
print(a,b,sep=" ")

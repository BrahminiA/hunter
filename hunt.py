n = int(input())
p = list(map(int,input().split()))
flag = 1
for i in range(len(p)) :
    if p.count(p[i]) > 1 :
        print(p[i])
        flag = 0
        break
if flag == 1 : print('unique')

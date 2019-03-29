n = int(input())
s = list(map(int,input().split()))
flag = 1
for i in range(len(s)) :
    if s.count(s[i]) > 1 :
        print(s[i])
        flag = 0
        break
if flag == 1 : print('unique')

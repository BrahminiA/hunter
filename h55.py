k,n =input().split()
n=int(n)
arr=map(int,input().split())
arr=list(arr)
for i in range(0, n):       
    first = arr[0];
    for j in range(0, len(arr)-1):       
        arr[j] = arr[j+1];       
    arr[len(arr)-1] = first;
for j in range(0,len(arr)):
    if(j==((len(arr)-1))):
        print(arr[j])
    else:
       print(arr[j],end=" ")



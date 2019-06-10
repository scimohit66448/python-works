N=int(input())
Arr=[eval(i) for i in input().split()]
for i in range(0,N):
    min=i
    for j in range(i,N):
        if Arr[j]<Arr[min]:
            min=j
    temp=Arr[min]
    Arr[min]=Arr[i]
    Arr[i]=temp
print(Arr)
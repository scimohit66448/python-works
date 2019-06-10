N=int(input())
k=0
Arr=list(map(eval,input().split()))
for i in range(0,N-1):
    for j in range(0,N-i-1):
        k=k+1
        if(Arr[j]>Arr[j+1]):
            temp=Arr[j]
            Arr[j]=Arr[j+1]
            Arr[j+1]=temp
print(Arr,k)
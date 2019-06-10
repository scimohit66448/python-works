def binsearch(Arr,Size,key):
    low=0 
    high=Size
    while(low<=high):
        mid=(low+high)//2
        if Arr[mid]==key:
            return mid
        if Arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    print("not found")
Size=int(input())
Arr=[eval(i) for i in input().split()]
key=eval(input())
index=binsearch(Arr,Size,key)
print("element "+str(key)+" " +"found at "+str(index+1)+" postion")      

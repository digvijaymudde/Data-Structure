

def linear_search(arr,item):
    for i in range(0,len(arr)):
        
        if arr[i]==item:
            return i
        
    return -1
        
arr =[1,2,12,4,54,65,676,23]

print(linear_search(arr,23))
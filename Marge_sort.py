def merge_sorted(arr1,arr2):
    i=j=0
    merge=[]
    while i <len(arr1)and j<len(arr2):
        if arr1[i]<=arr2[j]:
            merge.append(arr1[i])
            i+=1
        else:
            merge.append(arr2[j])
            j+=1

    while i < len(arr1):
        merge.append(arr1[i])
        i = i+1

    while j < len(arr2):
        merge.append(arr2[j])
        j=j+1
    return merge


def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted(left,right)




arr2=[3,5,7,8,9,10]

mergerd = merge_sort(arr2)
print(mergerd) 

s ='digvijay'
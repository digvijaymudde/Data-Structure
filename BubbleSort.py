def bubble_sort(arr):

    for i in range(0,len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    print(arr)


arr = [23,12,34,11,100,56,78]
bubble_sort(arr)
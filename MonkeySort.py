import random
"""a=[1,2,3,4]
random.shuffle(a)
print(a)"""


def is_sorted(data):
    sorted =True

    for i in range(0,len(data)-1):
        if data[i]>data[i+1]:
            sorted = False
        
    return sorted

def monkey_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
    print(arr)

monkey_sort([11,33,44,55,22])
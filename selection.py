import random

arr = [9,8,7, 7,6, 4, 2,1, 2, 4]
arr1 = [9,8,7, 7,6, 4, 2,1, 2, 4]
arr2 = [9,8,7, 7,6, 4, 2,1, 2, 4]

for i in range(10000):
    arr.append(i)
    arr1.append(i)
    arr2.append(i)

random.seed(1223434)

random.shuffle(arr)
random.shuffle(arr1)
random.shuffle(arr2)

def selection(arr):

    iter_count = 0
    j = 0
    while j < len(arr):
        min_el = j
        for i in range(j, len(arr)):
            iter_count+= 1
            if arr[i] < arr[min_el]:
                min_el = i
        arr[j], arr[min_el] = arr[min_el],arr[j]
        j+= 1
    print("Iter selection", iter_count)


def insertion(arr):
    k = 0
    iter_count = 0
    while k < len(arr):
        j = k
        while j > 0 and arr[j-1] > arr[j]:
            iter_count+= 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
        k += 1
    print("Iter insertion", iter_count)

def bubble(arr):
    l = 1
    iter_count = 0
    while l < len(arr):
        k = 0
        while k < len(arr) - l:
            iter_count+= 1
            if arr[k] >= arr[k + 1]:
                arr[k], arr[k + 1] = arr[k+1], arr[k]
            k+= 1
        l+=1
    print("Iter bubble", iter_count)

insertion(arr)

bubble(arr1)

selection(arr2)

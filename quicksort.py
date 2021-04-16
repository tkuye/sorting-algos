listy = [9, 8,7,6,5,4,3,2,1]


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(li, low, high):
    if len(li) == 1:
        return
    if low < high:

        pivot = partition(li, low, high)
        quickSort(li, low, pivot -1)
        quickSort(li, pivot+1, high)
   

print(listy)  
quickSort(listy, 0, len(listy) - 1)
print(listy)
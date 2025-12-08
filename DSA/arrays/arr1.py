arr = [1, 2, 4, 7, 7, 5, 5, 6]

def max(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
    
def sec_largest_better(arr, max = max(arr)):
    sl = -1
    for i in range(len(arr)):
        if arr[i] > sl and arr[i] < max:
            sl = arr[i]
            
    return sl
    
def sec_largest_optimal(arr):
    largest = arr[0]
    slargest = -1
    
    for i in range(1, len(arr)):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > slargest:
            slargest = arr[i]
            
    return slargest
    
    
print(max(arr))
print(sec_largest_better(arr))
print(sec_largest_optimal(arr))
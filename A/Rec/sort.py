def selectionSort(arr, n):
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        
        arr[i], arr[min] = arr[min], arr[i]


def bubbleSort(arr, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    n = int(input("Enter no of elements: "))
    arr = []
    for i in range(n):
        arr.append(int(input("Enter the element: ")))

    print(arr)

    bubbleSort(arr, n)
    print(arr)

    
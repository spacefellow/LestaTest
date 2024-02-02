def quicksort3(arr, low, high):
    if low < high:
        lt, gt = partition3(arr, low, high)
        quicksort3(arr, low, lt - 1)
        quicksort3(arr, gt + 1, high)

def partition3(arr, low, high):
    pivot_index = (low + high) // 2
    pivot = arr[pivot_index]
    lt = low
    i = low
    gt = high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

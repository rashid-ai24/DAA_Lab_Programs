# Ex No: 4 - IMPLEMENTATION OF HEAP SORT USING TRANSFORM AND CONQUER TECHNIQUE

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    root = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if root < n and array[largest] < array[root]:
        largest = root
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def Heap_Sort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

array = []
n = int(input("Enter array size: "))
print("Enter array elements:")
for _ in range(n):
    a = int(input())
    array.append(a)
print("The original array is:", array)
Heap_Sort(array)
print("Array after sorting:", array)

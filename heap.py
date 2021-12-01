
def heapify():
    pass
def heap_sort(arr):
    arr_len = len(arr)
    for i in range(((arr_len-1) // 2, -1, -1):
        heapify()




if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(f"정렬 전: {arr}")
    heap_sort(arr)
    print(f"정렬 후: {arr}")
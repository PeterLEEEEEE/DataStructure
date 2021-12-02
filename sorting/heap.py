'''
Heap 정렬
- 이진 트리를 이용한 정렬
- 상향식 정렬, 하향식 정렬이 존재
- inplace 알고리즘
Heap 이란?
- 최솟값이나 최댓갑을 빠르게 찾아내기 위해 완전 이진 트리를 기반으로 하는 트리(최소값, 최대값이 루트 노드에 위치함)
- 힙 정렬을 위해서는 데이터가 힙 구조를 만족해야 함 * 힙 구조란? 부모 노도가 자식보다 무조건적으로 커야함(최소 힙일 경우 작아야 함)

힙 정렬은 어떻게(최대 힙)?
- 우선 힙 조건을 만족시키는 알고리즘을 만들어야 한다(부모와 두 자식 중 최대값을 부모 노드에 위치시키는 알고리즘) - 시간 복잡도(logN)
- 데이터의 개수가 N개이면 전체 트리를 힙 정렬을 하는 시간 복잡도는 (N * logN) -> NlogN,, 모든 데이터를 기준으로 힙 알고리즘을 쓸 일이 없기 때문에 사실상 O(N)에 가까운 복잡도를 낼 수 있음

'''

def heapify(unsorted_arr, index, heap_size):
    largest = index
    left_child = index * 2 + 1
    right_child = index * 2 + 2

    if left_child < heap_size:
        pass

def heap_sort(unsorted_arr):
    arr_len = len(unsorted_arr)
    for i in range(((arr_len-1) // 2, -1, -1)):
        heapify(unsorted_arr, i, arr_len)




if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(f"정렬 전: {arr}")
    heap_sort(arr)
    print(f"정렬 후: {arr}")
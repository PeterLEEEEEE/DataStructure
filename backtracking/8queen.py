''' 
가정: 같은 행(row)에는 퀸을 놓지 않는다
구현: 같은 열(column)이나 같은 대각선(diagonal)에 놓이는 지 확인
'''

from typing import List

arr =[]

def prune(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag

def n_queen(i: int, col: List):
    n = len(col) - 1
    if prune(i, col):
        if i == n:
            print(col[1: n+1])
            arr.append(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queen(i+1, col)


n = int(input())
col = [0] * (n+1)
n_queen(0, col)
print(len(arr))


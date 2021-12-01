import sys
sys.setrecursionlimit(10**7)

def recur(n):
    print(n)
    return recur(n+1)

recur(1) # 996번 만에 stackoverflow 발생, 재귀 최대로 늘릴 시 20945에서 터짐
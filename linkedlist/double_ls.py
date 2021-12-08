# 중첩 클래스
class Dlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.nodeCnt = 0
    class Node:
        def __init__(self, data, prev=None, next=None) -> None:
            self.data = data
            self.prev = prev
            self.next = next
    def add_first(self, data):
        if self.head == None:
            self.head = self.Node(data)
            self.tail = self.head
        else:
            self.head = self.Node(data, next=self.head)
            #self.head = self.Node(data, next=self.head, prev=self.tail)
            self.head.next.prev = self.head
        self.nodeCnt += 1
    def add_last(self, data):
        if self.tail == None:
            self.tail = self.Node(data)
            self.head = self.tail
        else:
            self.tail = self.Node(data, prev=self.tail)
            # self.tail = self.Node(data, next=self.head, prev=self.tail)
            self.tail.prev.next = self.tail
        self.nodeCnt += 1
    def delete(self, data):
        n = self.head
        while True:
            if n.data == data:
                if n == self.head:  # 지울 녀석이 첫번째에 있을 때
                    self.head = n.next
                    del self.head.prev
                    self.head.prev = None
                elif n == self.tail:
                    self.tail = n.prev
                    del self.tail.next
                    self.tail.next = None
                else:
                    t = n.prev
                    t.next = n.text
                    del n
                    t.next.prev = t
                break
            n = n.next
            if not n:
                break
    def insert(self, data, idx):
        if idx >= self.nodeCnt or idx < 1:
            print("첫번째와 마지막 인덱스는 사용불가")
            print(f"노드의 개수: {self.nodeCnt}")
            return
        else:
            n = self.head
            for i in range(idx - 1):
                n = n.next
            t = self.Node(data, next=n.next)
            t.prev = n
            t.next.prev = t
            n.next = t
        self.nodeCnt += 1
    
    def print(self, rev=False):
        if rev == 'R':
            n = self.tail
            while True:
                if n.prev == None:
                    print(n.data, end=' ')
                    break
                else:
                    print(n.data, end=' ')
                    n = n.prev
        else:
            n = self.head
            while True:
                if n.next == None:
                    print(n.data, end=' ')
                    break
                else:
                    print(n.data, end=' ')
                    n = n.next
        print()

doublell = Dlist()
doublell.add_first('하이1')
doublell.add_last('하이2')
doublell.insert('인서트3', 1)
doublell.print('R')
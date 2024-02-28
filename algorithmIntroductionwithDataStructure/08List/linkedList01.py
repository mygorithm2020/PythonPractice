# 포인터로 연결리스트 구현

from __future__ import annotations
from enum import Enum
from typing import Any, Type

class Node:

    def __init__(self, data:Any = None, next : Node = None) -> None:
        self.data = data
        self.next = next
        

class LinkedList:

    def __init__(self) -> None:
        self.no = 0
        self.head = None
        self.current = None
    
    def __len__(self) -> int:
        return self.no
    
    def search(self, data:Any)-> int:
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0
    
    def add_first(self, data:Any) -> None:
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1
    
    def add_last(self, data:Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1
    
    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.current = self.head.next
            self.no -= 1
    
    def remove_last(self) -> None:
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -=1
    
    def remove(self, p:Node) -> None:
        if self.head is not None:
            if p is self.head: #첫번째면 
                self.remove_first()
            else:
                ptr = self.head

                # 해당 노드 찾기
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None: # 없음..
                        return
                
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
    
    def clear(self) -> None:
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0
    
    def print(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)
    
class LinkedListIterator:

    def __init__(self, head:Node) -> None:
        self.current = head
    
    def __iter__(self)-> LinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
        

Menu = Enum('MenuEnum', ["머리에", "꼬리에", "머리삭제", "꼬리삭제", "모든노드삭제", "검색", "모노출력", "스캔", "종료"])

for one in Menu:
    print(one)
lst = LinkedList()
for idx in range(4):
    lst.add_last(f"{idx}test")
lst.print()
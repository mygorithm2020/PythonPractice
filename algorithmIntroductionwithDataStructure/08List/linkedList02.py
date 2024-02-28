# 커서를 이용한 연결 리스트

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:

    def __init__(self, data = Null, next = Null, dnext = Null):
        self.data = data
        self.next = next
        self.dnext = dnext
    

class ArrayLinkedList:
    
    def __init__(self, capacity: int) -> None:
        self.head = Null
        self.current = Null
        self.max = Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self) -> int:
        return self.no
    
    def get_insert_index(self):
        if self.deleted == Null:
            if self.max +1 < self.capacity:
                self.max +=1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec
    
    def delete_index(self, idx:int)-> None:
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec
        
    def search(self, data:Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null
x = 3
y = 5
print(x and y)
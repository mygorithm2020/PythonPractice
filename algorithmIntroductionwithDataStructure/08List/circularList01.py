# 원형 이중 연결리스트

from __future__ import annotations
from typing import Any


class Node:

    def __init__(self, data:Any = None, prev : Node = None, next:Node = None) -> None:
        self.data = data
        self.prev = prev or self
        self.next = next or self
        pass

class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = self.currnet = Node()
        self.no = 0

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.head.next is self.head
    
    def search(self, data:Any) -> Any:

        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.currnet = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data: Any) ->bool:
        return self.search(data) >= 0
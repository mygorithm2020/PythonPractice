from __future__ import annotations
from enum import Enum
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next
        


class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity #해시 테이블 크기
        self.table = [None] * self.capacity   # 해시 테이블을 선언
    
    def hash_value(self, key:Any) -> int:
        if isinstance(key, int):
            return key% self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key:Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        
        return None
    
    def add(self, key:Any, value:Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            
            p = p.next
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key:Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
        
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end=" ")
            while p is not None:
                print(f" -> {p.key} ({p.value})", end=" ")
                p = p.next
            print()
    

st = "abc"
print(st)
print(st.encode())
print(hashlib.sha256(st.encode()))
print(hashlib.sha256(st.encode()).hexdigest())
print(int(hashlib.sha256(st.encode()).hexdigest(), 16))

Menu = Enum('Menu', ["추가", "삭제", "검색", "덤프", "종료"])

def select_menu() -> Menu:
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        n = int(input(": "))
        if 1<= n <= len(Menu):
            return Menu(n)

hashTable = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input("추가할 키를 입력하세요: "))
        val = input("추가할 값을 입력하세요 : ")
        if not hashTable.add(key, val):
            print("추가 실패")
    elif menu == Menu.삭제:
        key = int(input("삭제할 키를 입력하세요: "))
        if not hashTable.remove(key):
            print("삭제 실패")
    elif menu == Menu.검색:
        key = int(input("검색할 키를 입력하세요: "))
        t = hashTable.search(key)
        if t is not None:
            print(f"{key} : {t}")
        else:
            print(f"{key} : None")
        
    elif menu == Menu.덤프:
        hashTable.dump()
    else:
        break
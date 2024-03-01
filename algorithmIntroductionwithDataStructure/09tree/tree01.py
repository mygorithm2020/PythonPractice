# 이젠 트리, 이진 검색 트리

"""
# 특징
- 구조가 단순 
- 중위 순회의 깊이 우선 검색을 통하여 노드값을 오름차순으로 얻을 수 있음
- 이진 검색과 비슷한 방식으로 아주 빠르게 검색 가능
- 노드를 삽입하기 쉬움""" 
# 이진 검색 트리에 오름차순으로 노드를 삽입하면 트리의 높이가 계속 깊어져 선형 리스트처럼 됩니다.
# 위 문제를 해결하기 위한 방법이 균형 검색 트리(self-balancing seacrh tree)이며 높이를 logn 으로 제한합니다.
# 이진 균형 검색 트리 : AVL 트리, 레드 블랙 트리// 이진이 아닌 균형 검색 트리 : B 트리, 2-3 트리

from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, key:Any, value:Any, left: Node = None, right : Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, key:Any) -> Any:
        p = self.root
        while True:
            if p in None:
                return None
            
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
            
    def add(self, key:Any, value:Any) -> bool:
        
        def add_node(node:Node, key:Any, value:Any)-> None:
            if key == node.key:
                return False        # key 가 이미 이진트리에 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
        
    # remove는 3가지 케이스 1.삭제할 노드의 자식이 없는 경우, 2. 삭제할 노드의 자식이 1개인 경우, 3. 삭제할 노드의 자식이 2개인 경우
    def remove(self, key: Any) -> bool:
        p = self.root 
        parent = None
        is_left_child = True

        while True:
            if p is None:   # 해당 키는 없음
                return False 

            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:    # 현재 노드보다 작을 경우
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left    # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left
        else: #대상 키의 자식이 2개
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        
        return True
    

    
    def dump(self, reverse = True) -> None:

        # 모든 노드를 키의 오름차순으로 출력
        def print_subtree(node:Node):
            if node is not None:
                print_subtree(node.left)
                print(f"{node.key} : {node.value}")
                print_subtree(node.right)

        def print_subtree_rev(node:Node):
            if node is not None:                
                print_subtree(node.right)
                print(f"{node.key} : {node.value}")
                print_subtree(node.left)                
        
        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None
        
        p = self.root
        while p.left is not None:
            p = p.left
        
        return p.key

    


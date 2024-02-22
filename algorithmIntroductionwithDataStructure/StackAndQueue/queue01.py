
# 크기가 정해진 큐
class FixedQueue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:

        self.no =   # 데이터 개수
        self.front = 0
        self.rear = 0
        self.capacity = capacity        
        self.que = [None] * capacity
        
    
    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def enque(self, value:Any) -> None:
        # 방법 1.기존 데이터 유지
        if self.is_full():
            raise FixedStack.Full
        
        # 방법 2. 기존데이터 삭제하면서 최신화
        # if self.is_full():
        #     self.deque()

        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
        
        
    
    def deque(self) -> Any:
        if self.is_empty():
            raise self.Empty
    
        x = self.que[self.front]
        self.front +=1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
    
    def peek(self) -> Any:
        if self.is_empty():
            raise self.Empty
        return self.stk[self.front]
    
    def clear(self) -> None:
        self.no = self.front = self.rear = 0
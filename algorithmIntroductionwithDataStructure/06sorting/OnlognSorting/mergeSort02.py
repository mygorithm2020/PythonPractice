# 정렬을 마친 두 배열의 병합
# 파이썬 내장 sorted를 쓰는것보다 빠름
# 단, 정렬을 마친 두 배열이어야 함
import heapq

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))
print(a, b, c)


import copy
a = [[1,2, 3], [4, 5, 6]]
b = copy.deepcopy(a)
a[0][1] = 10
print(a, b)
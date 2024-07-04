import collections as cl

aa = ["a", "b", "C", "c", "c"]
bb = ["a", "a", "d", "d", "c"]

a = cl.Counter(aa)
b = cl.Counter(bb)

print(a, b)

q = a.most_common(1)
print(q)
a.subtract("C")

print(a)

a += cl.Counter()
print(a)

dp = cl.OrderedDict()
dp[0] = 5
dp[1] = 4
print(dp.popitem())
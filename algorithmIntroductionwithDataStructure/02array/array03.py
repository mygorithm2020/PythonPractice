from datetime import datetime

start = datetime.now()
print(start)
q = []
for i in range(12345678):
   q.append(i) 

newStart = datetime.now()
print(newStart - start)

w = [None] * 12345678
for j in range(12345678):
   w[j] = j
print(datetime.now() - newStart)
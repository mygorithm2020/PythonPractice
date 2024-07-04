# 슬라이딩 윈도우란 고정 사이즈의 윈도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 풀이하는 알고리즘
# 네트워크 패킷 흐름 제어를 위한 방법에서 가져온 이론

dic = dict({
    "a" : 3,
    "b" : 2,
    "c" : 1,
    "d" : 30,
})

dic02 = dict({
    "a" : 3,
    "c" : 0,
    "d" : 10,
})

import collections

print(collections.Counter() & collections.Counter())
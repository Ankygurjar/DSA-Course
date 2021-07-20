from collections import Counter

a = "aaavvbbbnnnnmmm"
nums = Counter(a)
print(nums.keys())
print(nums.most_common(1)[0][0])

from collections import namedtuple

p = namedtuple("Points", ["x", "y", "z", "g"])
pt = p(32, 54, 65, 78)
print(pt)

from collections import OrderedDict

od = OrderedDict()

od["a"] = 9
od["b"] = 1
od["c"] = 23
od["d"] = 0

print(od)

from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.append(5)
d.appendleft(23)
d.popleft()
print(d)
d.extendleft([12, 3, 4, 5])
print(d)




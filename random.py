from random import randint
from random import choice

def random_exclude(range_start, range_end, excludes):
    r = randint(range_start, range_end)
    if r in excludes:
        return random_exclude(range_start, range_end, excludes)
    return r

position = 0
used = [0] * 20
points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


i = 0
position = randint(1, 20)
print(str(position) + " " + str(points[position - 1]))

while i < 20:
    used[i] = position
    position = random_exclude(1, 20, used)
    print(str(position) + " " + str(points[position - 1]))
    i+=1

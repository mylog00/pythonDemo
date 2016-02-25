import sys
i = 1
while i < len(sys.argv):
    print(sys.argv[i], end=' ')
    i += 1

import math
r = float(input())
perimeter = 2 * math.pi * r
print(perimeter)

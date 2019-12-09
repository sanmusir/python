#迭代器
import sys
l = [1,2,3,4]
il = iter(l)

while True:
    try:
        print(next(il))
    except StopIteration:
        sys.exit(2)


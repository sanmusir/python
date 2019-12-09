from functools import reduce
def fn(x,y):
    return 10*x + y
print(reduce(fn,[1,4,6,7]))

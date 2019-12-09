#列表生成式
print([i*i for i in range(1,10) if i%2 !=0 ])
print([x + '=' +str(y) for x,y in {'a':1,'b':2}.items()])

#生成器
g = (i*i for i in range(1,10))
for i in g:
    print(i)
def fib(max):
    n, a, b = 1, 1, 1
    while n <= max:
        print(a)
        a,b = b,a+b
        n = n+1
    return 'done'
fib(6)

#生成器函数
def fib(max):
    n, a, b = 1, 1, 1
    while n <= max:
        yield(a)
        a,b = b,a+b
        n = n+1
    return 'done'
for i in fib(6):
    print (i)

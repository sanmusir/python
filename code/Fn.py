#!/usr/local/bin/python3.7
#函数的定义
def my_fn(x):
    print(x)
    return
my_fn('hello')

#空函数
def my_fn(x):
    pass
my_fn('hello')

#检查参数
def my_fn(x):
    if not isinstance(x, int):
        raise TypeError('请输入整型数字')
    print(x)

#my_fn('1')
my_fn(1)

#返回多个值
def my_fn(x, y):
    return x, y
a = my_fn(1,2)
print(a)

#函数的参数
#默认参数必须指向不变对象！
#可变参数
def my_fn(*args):
    for i in args:
        print(i)
my_fn(1)
my_fn(1,2,3)

a = [3,4,5]
b = (7,)
my_fn(*a)
my_fn(*b)

#关键字参数
def my_fn(name, age, **kw):
    print('my name is', name, 'age', age, 'other', kw)
my_fn('jj', 18)
my_fn('jj', 18, city="sz")
a = {'city':'sz', 'job':'cxy'}
my_fn('ljj', 100, **a)

#命名关键字参数
def my_fn(name, *, age='18', city):
    print(name,age,city)
my_fn('aaa',city='sz')

def my_fn(name, *args, age='18', city):
    print(name, args, age, city)
my_fn('ddd',1,2,3,city='sz')

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f2(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f2(1, 2, 3, 'a','c', d='b', x=99,y=101)
f2(*(1,2,3,'a','c'),**{'d':'b', 'x':99, 'y':101})

#递归函数
def my_fn(n):
    if n == 1:
        return 1
    return n * my_fn(n-1)
print(my_fn(5))

#高阶函数
#map--reduce--filter--sorted

#map 作用于可迭代对象的每个元素
a = [1,2,3,4,5,6]
b = map(lambda x: "this is " + str(x),a)
print(list(b))


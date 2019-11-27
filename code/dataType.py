#!/usr/local/bin/python3.7
"""
变量-
    | 变量由字符串、数字、下划线组成，区分大小写。
    | _foo 单下划线开头，代表不能直接访问类属性，需通过类接口访问。
    | __foo 双下划线开头，代表类的私有成员。
    | __foo__ 双下划线开头和结尾，代表 Python 里的特殊方法。

常量- 
    | 大写变量名表示常量

标准数据类型-
            | 数字-
		  | 整型 var = 1 
		  | 浮点型 var = 2.2
		  | 复数 var = 1 + 2j

            | 字符串-
                    | s = 'abcdef'
                    | s[1:-1] = 'bcde'
                    | s[0:-1:2] = 'ace'
		    | s * 2 = 'abcdefabcdef'
                    | s + 'g' = 'abcdefg'
		
            | 列表-
		  | 使用 [] 标识  s = ['a', 'b', 'c']
                  | [头下标:尾下标:步长] 截取元素
                  | len(s) 获取长度
                  | s.append('d') 添加元素到末尾
                  | s.insert(2,'c2') 往指定位置添加元素
                  | s.pop(i) 删除指定位置元素，默认是末尾

            | 元组-
                  | 使用() 标识  s = ('a', 'b', 'c')
                  | 相当于只读列表

            | 字典-
		  | 使用 {} 标识 {'name': 'tom', 'age':8}
                  | 由 key - value 组成
                  | s.get('name', 'a') 获取指定key，若key不存在，返回默认值 a
            
	    | 集合-
	          | s = set([1,2,3,4,4])
		  | s.add(5)
                  | s.remove(1)

"""
s = 'abcdef'
print(s[1:-1])
print(s[0:-1:2])
print(s * 2)
print(s + 'g')

s = ['a', 'b', 'c']
s[1] = 'b1'
print(s)
s.append('d')
print(s)
s.insert(1,'a1')
print(s)
s.pop
print(s)

s = ('a', 'b', 'c')
print(s[1:3])

s = {'name': 'tom', 'age':8}
print(s['name'])

s = set([1,2,3,4,4])
s.add(5)
print(s)
s.remove(1)
print(s)

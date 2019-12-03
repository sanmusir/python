#!/usr/local/bin/python3.7
#判断语句
age = 3
if age > 4 :
    print('you age > 4')
elif age < 1:
    print('you age < 1')
else:
    print('you age >= 1 and <= 4')

#循环语句
lists = ['aaa', 'bbb', 'ccc']
for i in lists:
    print(i)

sum = 0
num = 0
while num < 100:
    sum += num
    num += 1
print(sum)

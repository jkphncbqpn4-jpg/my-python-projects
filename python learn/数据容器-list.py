# #列表操作
# # 定义列表 - list
# s = [32,435,234,66,2,8,"d",False,"D"]
#
# print(type(s))
#
# #访问列表元素
# #获取
# print(s[0])#正向索引，从0开始
# print(s[-9])#反向索引，从-1开始
#
# #修改
# s[6] = "z"
# print(s)
#
# #删除
# del s[4]
# print(s)
#
# #注意：如果指定的索引，超出范围，将会报错list assignment index out of range
# # s[9] ="safd"
# #print(s)
#
# #遍历
# for i in s:
#     print(i)

#列表list切片

# s =["A","B","C","D","E","F"]
# #切片操作 s[开始索引：结束索引：步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
# print(s[:5])#如果是顺序索引，步长为1可以省略0与后面的:1但是前面的：不能省略，因为[:5]与[5]含义不一样

s = [21,324,12,54,76,22,55,75,77,21]
#在尾部追加元素
s.append(23)
print(s)

#在指定索引前插入元素
s.insert(0,15)
print(s)

#移除索引匹配到的第一个匹配到的元素
s.remove(21)
print(s)

#移除指定索引的元素并返回（如未指定，自动删除最后一个索引的元素）
i=s.pop(3)
print(s)
print(i)
s.pop()
print(s)

#反转列表的所有元素
s.reverse()
print(s)

#给列表的所有元素排序（只能排序相同元素的值，如果列表有不同的值则无法排序）
s.sort()
print(s)
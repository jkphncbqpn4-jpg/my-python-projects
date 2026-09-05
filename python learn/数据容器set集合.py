#set是无序的、不可重复、可修改的数据容器
#空集合的定义
# s2 = set()
#空集合的定义不能使用{}，{}表示的是空字典
# s1 = {100,200,300,400,500,600,700,800}
#
# #pop() 随机删除集合里的元素并返回
# e = s1.pop()
# print(e)
# #add() 添加一个元素到集合里面
# s1.add(1000)
# print(s1)
# #remove 删除集合里的指定元素
# s1.remove(100)
# print(s1)
# #clear 删除集合里的所有元素
# s1.clear()
# print(s1)

s2 = {100,200,300,400,500,600,700,800}
s3 = {700,800,1200,1500}
#difference() : 求两个集合的差集（存在与第一个，不存在第二个集合）
print(s2.difference(s3))
print(s3.difference(s2))
#union():求两个集合的并集
print(s2.union(s3))
print(s3.union(s2))
#intersection() : 求两个集合的交集
print(s2.intersection(s3))
print(s3.intersection(s2))
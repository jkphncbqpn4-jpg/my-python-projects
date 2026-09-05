# 变量是能存储计算结果或能表示值的抽象概念。
# 简单来说就是程序运行时，记录数据的。
# 格式为 变量名＝变量值 =是赋值的意思就是把右边的值赋予给左边
money = 100
print("你的钱包里面还有",money,"元")

money=money-10
print("现在还剩",money,"元")

# 变量的值是可以改变的

# 练习
qian = 50
print("当前钱包余额:",qian,"元")
bql=10
print("购买了冰淇淋，花费",bql,"元")
kele=5
print("购买了可乐，花费",kele,"元")
print("最终，钱包剩余:",qian-bql-kele,"元")

a = 100
b = 200
c = 300
# d = c
# c = a
# a = b
# b = d
a, b, c = c, a, b
print(c, a, b)  # 同样输出 100 200 300



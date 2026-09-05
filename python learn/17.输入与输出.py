# #获取键盘上输入的数据--input
# name=input("你是谁：")#无论键盘输入什么样的数据，获取到的数据都是字符串类型
# #获取输出的数据-print
# print(f"你的名字是：{name}")

#案例1
# Money = 10000
# pwd = input("输入密码:")
# Draw_Money = input("输入要取钱的金额")
# print(f"您的银行卡余额为{Money-int(Draw_Money)}")
#整数（int）不能直接和字符串（str）做减法,需要将Draw_Money转化为整数类型int

#案例2
num1 = input("输入第一个数:")
num2 = input("输入第二个数:")
print(f"两个数之和为{int(num1) + int(num2)}")
# print(f"两个数之和为{int(num1+num2)}")
#这种是错误写法，电脑会先执行num1+num2字符串的拼接也就是括号里面的内容而最后才会执行int整数类型
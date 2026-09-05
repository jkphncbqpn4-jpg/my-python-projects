# while True:
#     user1 = input("请输入账号：")
#     pwd1 = input("请输入密码：")
#     users = ["admin", "eve", "root"]
#     if user1 == "" or pwd1 == "":
#         print("账户或密码不能为空,请重新输入")
#         continue
#     if user1 in users and pwd1 == "123":
#         print("登陆成功")
#         break
#     else:
#         print("账户或密码错误，请重新输入")
from http.cookiejar import user_domain_match

# num = 5
# while True:
#         user1 = input("请输入账号:")
#         pwd = input("请输入密码:")
#         if pwd == "" or user1 == "":
#             num-=1
#             print(f"账号密码不允许为空,还有{num}次机会")
#             if num == 0:
#                 print("输入错误五次，不允许操作")
#                 break
#         continue
#         if user1 == "admin" and pwd=="123":
#             print("登陆成功")
#             break
#         elif user1 == "eve" and pwd=="234":
#             print("登陆成功")
#             break
#         elif user1 == "root" and pwd == "789":
#             print("登陆成功")
#             break
#         else:
#             num-=1
#             if num == 0:
#                 print("输入错误五次，不允许操作")
#                 break
#             print(f"账号或密码错误，请重新输入，还有{num}次机会")

# for i in range(5):
#     user1 = input("请输入账号:")
#     pwd = input("请输入密码:")
#     if pwd == "" or user1 == "":
#         print(f"账号密码不允许为空,还有{4-i}次机会")
#         continue
#     if (user1 == "admin" and pwd == "123") or \
#             (user1 == "eve" and pwd == "234") or \
#             (user1 == "root" and pwd == "789"):
#         print("登录成功")
#         break
#     else:
#         print(f"账号或密码错误，请重新输入，还有{4 - i}次机会")
# else:
#     print("输入错误五次，不允许操作")
# sorce =0
# import random
# random_number = random.randint(1, 100)
# while True:
#     try:
#         num = int(input("请输入1~100的数字"))
#     except ValueError:
#         print("请输入有效数字")
#         continue
#     if num >100 or num <1:
#         print("数字的大小是1~100，请重新输入")
#         continue
#     sorce +=1
#     if num > random_number:
#         print("猜大了,重新猜猜")
#     elif num < random_number:
#         print("猜小了,重新猜猜")
#     else:
#         print(f"猜对了,一共用了{sorce}次")
#         break
# print("随机生成的数字是：",random_number)

# num = 0
# for i in  range(1,1001):
#     if i % 5 ==0:
#         num+=i
# print(f"1-1000之间5的倍数数加起来为{num}")

# a=0
# k=0
# letter ="akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# for i in letter:
#     if i=="a":
#         a+=1
#     elif i=="k":
#         k+=1
# print(f"该字符串里面有{a}个a与{k}个k")




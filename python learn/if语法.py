# num = 681
# if num>680:
#     print("恭喜你")
# else:print("不好意思")
#案例：
# user=int(input("请输入账号:"))
# pwd=int(input("请输入密码:"))
# if user ==1234 and pwd ==666888:
#     print("密码账号正确")
# else:
#     print("账号或密码有误")
#案例2：
# years=int(input("请输入年份"))
# if (years % 100!=0 and years % 4 == 0 )or years % 400!=0:
#     print("该年为闰年")
# else:
#     print("该年为平年")
from platform import processor

#案例3
#1
# num =int(input("输入数字："))
# if num%2==0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")
#2
# year=int(input("输入你的年龄:"))
# if year>=18:
#     print(f"{year}岁已成年")
# else:
#     print(f"{year}岁未成年")
#3
# num = int(input("请输入数字:"))
# if num>0:
#     print(f"{num}该数字是正数")
# elif num<0:
#     print(f"{num}该数字是负数")
# else:
#     print(f"{num}该数字是0")

#案例4
# user =input("请输入用户名:")
# pwd =input("请输入密码:")
# if (
#         user == "admin" and pwd == "123"
# ):
#     print("登录成功")
# elif (
#         user == "root" and pwd == "456"
# ):
#     print("登录成功")
# elif (
#         user == "eve" and pwd == "789"
# ):
#     print("登录成功")
# else:
#     print("登录失败，账号或密码错误")

#综合案例


# side1=int(input("输入第一条边的长度"))
# side2=int(input("输入第二条边的长度"))
# side3=int(input("输入第三条边的长度"))
# if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
#     if side1==side2==side3:
#         print("该三角形为等边三角形")
#     elif side1==side2 or side1==side3 or side2==side3:
#         print("该三角形为等腰三角形")
#     else:print("该三角形为普通三角形")
# else:print("不能构成三角形")

#练习

# score=int(input("请输入您的分数"))
# if score>=85:
#     print("优秀")
# elif score>60 and score<85:
#     print("及格")
# else:print("不及格")
# try:
#     moneys = int(input("请输入金额:"))
# except ValueError:
#     print("输入无效，请输入整数")
#     exit()
# if moneys >= 500:
#     moneys *= 0.8
#     print(f"{moneys}该金额打八折")
# elif 300<=moneys<500:
#     moneys *= 0.9
#     print(f"{moneys}该金额打九折")
# elif 100<=moneys<=300:
#     moneys *= 0.95
#     print(f"{moneys}该金额打九五折")
# else:print(f"{moneys}该金额无折扣")

#练习案例
try:
    electrical = float(input("请输入用电量:"))
except ValueError:
    print("请输入数字")
    exit()
if electrical<2880:
    price = 0.4883
elif 2880<=electrical<=4800:
    price = 0.5383
else:
    price = 0.7883
print(f"{electrical}为用电度数，价格为{price}元/度")
total = electrical * price
print(f"这个月的电费为{total:.2f}元")


























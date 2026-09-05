#+加 -减 *乘 /除（结果是小数） //整除（结果是整数） %取余 **冥
#运算顺序**>* / // %>+ -
#案例
# x=float(input("请输入x的数:"))
# y=float(input("请输入y的数:"))
# print(f"x+y的和为{x + y}")
# print(f"x-y的结果为{x - y}")

#赋值运算符
#=把右边赋值给左边
#+= num+=1 相当于num=num+1
#-+ num-=1 相当于num=num-1
#*= num*=1 相当于num=num*1
#/= num/=1 相当于num=num/1
#%= num/=1 相当于num=num/1
#//= num//=1 相当于num=num//1
#**= num**=1 相当于num=num**1

#逻辑运算符
#案例
num = int(input("输入一个整数:"))
print(f"{num}在10-20之间:",num>=10 and num<=20)
print(f"{num}不在10-20之间",num<10 or num>20)
# # m=int(input("输入长方形的长度"))
# # n=int(input("输入长方形的宽带"))
# # for j in range(n):
# #     for i in range(m):
# #         print("*",end="")
# #     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={int(j)*int(i)}",end="\t")
#     print()
#
# # n=int(input("三角形的直角边长"))
# # for i in range(1,n):
# #     for j in range(1,i+1):
# #         print("*",end="\t")
# #     print("\t")
# #练习
# # n= int(input("输入数字"))
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print(i,end=" ")
# #     print()
#
# # n = int(input("输入数字"))
# # for i in range(1,n+1):
# #     for j in range(1,n+2-i):
# #         print(j,end="")
# #     print("")
#
# # n = int(input("请输入数字"))
# # for i in range(1,n+1):
# #     for j in range(1,n+1-i):
# #         print("    ",end="")
# #     for k in range(1,i+1):
# #         print(f"{k:3d}",end=" ")
# #     print()
#
# # n = int(input("请输入宽"))
# # for i in range(n):
# #     for j in range(n):
# #         if (i+j)%2==0:
# #             print("1",end=" ")
# #         else:
# #             print("2",end=" ")
# #     print()
#
# # n=5
# # for i in range(n):
# #     for j in range(n):#由于i==0这行是true所以j=0~4时都执行*与最后一行一样所以不会多*
# #         if i == 0 or i == n-1 or j == 0 or j == n-1:
# #             print("*",end="")
# #         else:
# #             print("",end=" ")
# #     print()
#
# # n =4
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #         print(f"{int(i)*int(j)}",end=" ")
# #     print()
#
# # n=5
# # for i in range(n):
# #     for j in range(n-i):
# #         print(" ",end="")
# #     for k in range(i+1):
# #         print(f"{k+1}",end="")
# #     print()
#
# # print("程序开始！")
# # for i in range(2):
# #     print(f"----> 外层 i 变成了 {i}，内层准备开始跑！")
# #     for j in range(3):
# #         print(f"     内层 j 变成了 {j}")
# #     print(f"----> 内层跑完了！外层 i 准备变成下一个数！")
# # print("程序结束！")
#
# n =4
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()
#
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()
#
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
#
# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print(i, end="")
#     print()
#
# n=4
# for i in range(n):
#     for j in range(n-i):
#        print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()
#


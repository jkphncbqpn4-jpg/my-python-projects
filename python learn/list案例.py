# amount = 10
# num_list = []
# for i in range(10):
#     while True:
#         try:
#             num = int(input(f"剩余{amount}个数字\n请输入:"))
#             break
#         except ValueError:
#             print("请输入有效数字,请重新输入")
#     amount -= 1
#     num_list.append(num)
# print(f"列表为{num_list}")
# num_list.sort()
# print(f"排序后的列表为{num_list}")
# print(f"列表的最小值为{num_list[0]}")
# print(f"列表的最大值为{num_list[-1]}")
# print(f"列表的平均值为{sum(num_list)/len(num_list)}")

#案例
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# for num1 in num_list1:
#     num_list2.append(num1)
# print(num_list2)
#
# num_list = []
# for num1 in num_list2:
#     if num1 not in num_list:
#         num_list.append(num1)
# print(num_list)

# #简化版1
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# #解包，将这一类容器解开成一个个独立的元素。
# #组包，将多个值合并到一个容器里
# num_list = [*num_list1, *num_list2]
# print(f"合并后的列表{num_list}")
#
# #去重，去除重复的元素
# new_list = []
# for num in num_list:
#     if num not in new_list:#如果num的数字在new_list列表没有时，添加元素进去
#         new_list.append(num)
# print(f"去重后的列表{new_list}")

# #简化版2
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
#
# num_list = num_list1+num_list2#合并列表
# print(f"合并后的列表{num_list}")
#
# #去重，去除重复的元素
# new_list = []
# for num in num_list:
#     if num not in new_list:#如果num的数字在new_list列表没有时，添加元素进去
#         new_list.append(num)
# print(f"去重后的列表{new_list}")

#方法一
# num = []
# for i in range(1,21):
#     num.append(i**2)
# print(num)
#方法二
#列表推导式 --->就是按照一定规则快速生成一个列表的方法 格式1：[要插入的值 for i in 序列/列表]

# num = [i**2 for i in range(1,21)]
# print(num)

#方法1
# new_list = []
# num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
# for num in num_list:
#     if num % 2 == 0:
#         new_list.append(num**2)
# print(new_list)

#方法二
#列表推导式 --->就是按照一定规则快速生成一个列表的方法 格式2：[要插入的值 for i in 序列/列表 if 条件]
# num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
# new_list = [num**2 for num in num_list if num % 2 == 0]
# print(new_list)

#案例：
# 1. 将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。

# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
#
# list4 = [*list1, *list2, *list3]
# print(list4)
#
# new_list = []
# for item in list4:
#     if item not in new_list:
#         new_list.append(item)
# new_list.sort()
# print(new_list)
#
# # 2. 将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# new_list = [num**2 for num in list1 if num %3 == 0 or num %5 == 0]
# print(new_list)
#
# # 3. 将如下列表中的正数提取出来，封装为一个新的列表。
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# new_list = [item for item in list1 if item>0]
# print(new_list)

#综合练习给定一个字符串 s = "a1b2c3d4e5"，提取出其中所有的数字，组成一个新字符串，并计算这些数字的和。
#原字符串：a1b2c3d4e5
# 提取的数字：12345
# 数字之和：15
# s = "a1b2c3d4e5"
# new_list1 = [int(i) for i in s if i.isdecimal()]
# new_list2 = [(i) for i in s if i.isalpha()]
# print(new_list1)
# print(new_list2)
# num = 0
# for i in new_list1:
#     num += i
# print(num)

# #给定一个数字列表，将其中的偶数和奇数分别提取出来，放入两个新列表并打印。
# numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
# new_list = [i for i in numbers if i%2==0]
# print(new_list)
# new_list2 = [i for i in numbers if i%2!=0]
# print(new_list2)
#
# # 合并下面两个列表，去除重复的元素，然后输出这个新列表的最大值和最小值。
# list_a = [5, 8, 12, 3, 7]
# list_b = [3, 7, 9, 15, 8]
#
# new_list =[*list_a,*list_b]
# print(new_list)
# list_c = []
# for i in new_list:
#     if i not in list_c:
#         list_c.append(i)
# list_c.sort()
# print(list_c)
# print(list_c[0])
# print(list_c[-1])

# 合并下面两个列表，去除重复的元素，然后输出这个新列表的最大值和最小值。(优化版)
list_a = [5, 8, 12, 3, 7]
list_b = [3, 7, 9, 15, 8]

new_list =[*list_a,*list_b]
print(new_list)
list_c = []
for i in new_list:
    if i not in list_c:
        list_c.append(i)
print(list_c)
print(max(list_c))
print(min(list_c))

# #题目：给定一个列表，反转它（不许用 .reverse() 方法，自己用循环或切片做），然后从反转后的列表中，只提取出大于 50 的数字，组成新列表。
# scores = [45, 88, 23, 99, 12, 76, 34, 91]
# new_list=scores[-1:-9:-1]
# print(new_list)
# new_list=[i for i in new_list if i>50]
# print(new_list)

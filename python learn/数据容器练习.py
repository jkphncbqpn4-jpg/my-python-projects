# #练习1
# data = [5, 2, 8, 2, 9, 1, 5, 8, 3]
# # 使用集合去除重复数字。
# new_set = set(data)
# print(new_set)
# # 将去重后的结果按降序（从大到小）排序。
# new_set2 = (sorted(new_set,reverse=True))
# print(new_set2)
# # 将最终结果转换为元组（tuple）并输出。
# new_tuple = tuple(new_set2)
# print(new_tuple)

# #练习2
# class_a = ["王林", "韩立", "厉飞雨", "紫灵", "天运子"]
# class_b = ["韩立", "天运子", "红蝶", "曾牛", "乌丑"]
# list_a = set(class_a)
# list_b = set(class_b)
# # 既选了A班又选了B班的学生（交集）。
# A_B = list_a & list_b
# print(f"两班都选的同学{list(A_B)}")
# # 至少选了一个班的学生（并集）。
# AoB=list_a | list_b
# print(f"至少选了一个班的学生{list(AoB)}")
# # 只在A班，不在B班的学生（差集）。
# A=list_a - list_b
# print(f"只在A班，不在B班的学生{list(A)}")

# #练习3
# students = [("王林", 85), ("韩立", 92), ("厉飞雨", 78), ("紫灵", 85), ("天运子", 92), ("红蝶", 88)]
# # 提取出所有不重复的分数，从高到低排序。
# source = []
# for i in students:
#     source.append(i[1])
# set_source = set(source)
# print(f"分数从高到低为{sorted(set_source,reverse=True)}")
# # 计算全班平均分。
# avg = sum(source)/len(source)
# print(f"全班平均分为{avg:.1f}")
# # 找出高于平均分的学生姓名，放入列表并输出。
# avg_list = [i[0] for i in students if i[1] > avg]
# print(f"高于平均分的学生有{avg_list}")

# #练习4
# user_a = ["苹果", "香蕉", "葡萄", "橙子", "西瓜"]
# user_b = ["香蕉", "葡萄", "猕猴桃", "哈密瓜", "苹果"]
# set_a = set(user_a)
# set_b = set(user_b)
# # 找出两个人共同购买的商品。
# a_b = set_a & set_b
# print(a_b)
# # 找出只被其中一个人购买的商品（即除去共同商品外的所有商品，对称差集）。
# aob = set_a ^ set_b
# print(aob)
# # 统计所有商品中，被购买次数 大于 1 的商品有哪些。
# user_c = [*user_a, *user_b]
# more = [i for i in set(user_c) if user_c.count(i) > 1]
# print(more)
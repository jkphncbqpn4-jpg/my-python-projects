# students =(
#     ("S001", "王林", 85, 92, 78),
#     ("S002", "李慧娟", 92, 88, 95),
#     ("S003", "十三", 78, 85, 82),
#     ("S004", "曾伟", 88, 79, 91),
#     ("S005", "周铁", 95, 96, 89),
#     ("S006", "王卓", 76, 82, 77),
#     ("S007", "红蝶", 89, 91, 94),
#     ("S008", "徐立国", 75, 69, 82),
#     ("S009", "许木", 86, 89, 98),
#     ("S010", "通天", 66, 59, 72),
# )
# print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# # 计算每个学生的总分、各科平均分，然后一并输出出来。
# for i in students:
#     total = i[2] + i[3] +i[4]
#     avg = total / 3
#     print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t {avg:.1f}")
#
# print()
# # 统计各科成绩的最低分、最高分、平均分，并输出。
# chinese_scores = [i[2] for i in students]
# math_scores = [i[3] for i in students]
# english_scores = [i[4] for i in students]
# print(f"语文最低分{min(chinese_scores)},语文最高分{max(chinese_scores)},语文平均分{sum(chinese_scores)/len(chinese_scores)}")
# print(f"数学最低分{min(math_scores)},数学最高分{max(math_scores)},数学平均分{sum(math_scores)/len(math_scores)}")
# print(f"英语最低分{min(english_scores)},英语最高分{max(english_scores)},英语平均分{sum(english_scores)/len(english_scores)}")
# print()
# # 查找成绩优秀（平均分大于90）的学生，并输出。
# excellent = [i[1] for i in students if (i[2] + i[3]+ i[4])/3 > 90]
# print(f"成绩优秀（平均分大于90）的学生{excellent}")

while True:
    email = input("请输入要注册的邮箱 ").strip()
    if email == "":
        print("邮箱不能为空")
        continue
    if email.count("@") != 1:
      print(f"{email}邮箱格式错误，请重新输入")
      continue
    em = email.split("@")
    user = em[0]
    num = em[1]

    if user == "" or num == "":
        print(f"{email}邮箱格式错误，请重新输入")
        continue
    elif "."not in num or num.startswith(".") or num.endswith("."):
        print(f"{email}邮箱格式错误，请重新输入")
        continue
    print(f"{email}邮箱注册成功")
    break
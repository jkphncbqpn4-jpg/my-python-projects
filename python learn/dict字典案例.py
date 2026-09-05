# shopping_cart = {}
# print("欢迎使用购物车管理系统")
# menu ="""
# ##########购物车管理系统##########
# #         1.添加购物车          #
# #         2.修改购物车          #
# #         3.删除购物车          #
# #         4.查询购物车          #
# #         5.退出购物车          #
# ###############################
# """
#
# while True:
#     print(menu)
#     operate = input("请选择要执行的操作(1-5)")
#     match operate:
#         # 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#         case "1":
#             trade_name = input("请输入商品的名称")
#             trade_price = float(input("请输入商品的价格"))
#             trade_num = int(input("请输入商品的数量"))
#             if trade_name in shopping_cart:
#                 print("该商品已存在")
#             else:
#                 shopping_cart[trade_name] = {"price": trade_price, "num": trade_num}
#                 print("添加成功")
#         # 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
#         case "2":
#             trade_name = input("请输入商品要修改的名称")
#             trade_price = float(input("请输入商品要修改的价格"))
#             trade_num = int(input("请输入商品要修改的数量"))
#             if trade_name not in shopping_cart:
#                 print("商品不存在，请重新选择")
#             else:
#                 shopping_cart[trade_name] = {"price": trade_price, "num": trade_num}
#                 print("修改成功")
#         # 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#         case "3":
#             trade_name = input("请输入商品要删除的名称")
#             if trade_name not in shopping_cart:
#                 print("该商品不存在，请重新选择")
#             else:
#                 del shopping_cart[trade_name]
#                 print("删除成功")
#         # 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：×××，商品价格：×××，商品数量：×××"。
#         case "4":
#             trade_name = input("请输入要查询的商品名称")
#             if trade_name not in shopping_cart:
#                 print("该商品不存在，请重新选择")
#             else:
#                 info = shopping_cart[trade_name]
#                 print(f"商品名称为{trade_name},商品价格为{info['price']},商品数量为{info['num']}")
#         # 5.退出购物车
#         case "5":
#             print("退出成功")
#             break
#         case _:
#             print("该操作不支持")

score = {}
print("欢迎来到教务管理系统")
menu = """
#######################################【菜单】#######################################
1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统
####################################################################################
"""
while True:
    print(menu)
    choice = int(input("输入要进行的操作(1-7)"))
    match choice:
        # 1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        case 1:
            student_name = input("输入学生姓名:")
            student_chinese = float(input("输入语文成绩:"))
            student_math = float(input("输入数学成绩:"))
            student_english = float(input("输入英语成绩:"))
            score[student_name] = {"chinese": student_chinese, "math": student_math, "english": student_english}
            print(f"添加【{student_name}】成功")
        # 2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        case 2:
            student_name = input("输入要修改的学生姓名")
            if student_name not in score:
                print("该学生不存在,请重新输入")
                continue
            student_chinese = float(input("输入要修改的语文成绩"))
            student_math = float(input("输入要修改的数学成绩"))
            student_english = float(input("输入要修改的英语成绩"))
            score[student_name] = {"chinese": student_chinese, "math": student_math, "english": student_english}
            print(f"修改【{student_name}】成功")
        # 3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        case 3:
            student_name = input("输入要删除的学生姓名")
            if student_name not in score:
                print("该学生不存在,请重新输入")
                continue
            else:
                del score[student_name]
        # 4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        case 4:
            student_name = input("输入要查询的学生姓名")
            if student_name not in score:
                print("该学生不存在,请重新输入")
                continue
            else:
                info = score[student_name]
                print(f"姓名:【{student_name}】,语文:{info['chinese']},数学:{info['math']},英语:{info['english']}")
        # 5.列出所有学生：遍历所有学生信息并输出。
        case 5:
            for student in score.keys():
                info = score[student]
                print(f"姓名:【{student}】,语文:{info['chinese']},数学:{info['math']},英语:{info['english']}")
        # 6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        case 6:
            if len(score) == 0:
                print("当前没有学生信息，无法统计")
                continue
            chinese_score = [score[name]['chinese'] for name in score]#取出名字对应的分数,score = name{'chinese':(分数),'math':(分数),'english':(分数)}
            math_score = [score[name]['math'] for name in score]
            english_score = [score[name]['english'] for name in score]
            print(f"语文最高分{max(chinese_score)},语文最低分{min(chinese_score)},语文平均分{sum(chinese_score)/len(chinese_score)}")
            print(f"数学最高分{max(math_score)},数学最低分{min(math_score)},数学平均分{sum(math_score) / len(math_score)}")
            print(f"英语最高分{max(english_score)},英语最低分{min(english_score)},英语平均分{sum(english_score) / len(english_score)}")
            #语文
            max_chinese_student = [name for name in score if score[name]['chinese'] == max(chinese_score)]
            min_chinese_student = [name for name in score if score[name]['chinese'] == min(chinese_score)]
            print(f"语文最高分的学生{max_chinese_student},语文最低分的学生{min_chinese_student}")
            #数学
            max_math_student = [name for name in score if score[name]['math'] == max(math_score)]
            min_math_student = [name for name in score if score[name]['math'] == min(math_score)]
            print(f"数学最高分的学生{max_math_student},数学最低分的学生{min_math_student}")
            #英语
            max_english_student = [name for name in score if score[name]['english'] == max(english_score)]
            min_english_student = [name for name in score if score[name]['english'] == min(english_score)]
            print(f"英语最高分的学生{max_english_student},英语最低分的学生{min_english_student}")

        # 7.退出系统。
        case 7:
            print("系统退出成功")
            break
        case _:
            print("操作不支持")















# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print(f"{j}x{i}={i*j}",end=" ")
#     print()
#
#
# # 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# shopping_cart = {}
# print("欢迎来到购物管理系统")
# menu = """
# #########购物车管理系统#########
# #        1.添加购物车         #
# #        2.修改购物车         #
# #        3.删除购物车         #
# #        4.查询购物车         #
# #        5.退出购物车         #
# #############################
# """
# while True:
#     print(menu)
#     choose = input("请输入要进行的操作(1-5)")
#     match choose:
#         # 1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#         case "1":
#             shopping_name = input("请输入要录入的商品名称")
#             if shopping_name in shopping_cart:
#                 print("商品已存在，请重新选择")
#                 continue
#             shopping_price = float(input("请输入要录入的价格"))
#             shopping_num = int(input("请输入要录入的数量"))
#             shopping_cart[shopping_name] = {"price": shopping_price, "num": shopping_num}
#             print("商品添加成功")
#         # 2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
#         case "2":
#             shopping_name = input("请输入要修改的商品名称")
#             if shopping_name not in shopping_cart:
#                 print("商品不存在，请重新选择")
#                 continue
#             shopping_price = float(input("请输入要修改的价格"))
#             shopping_num = int(input("请输入要修改的数量"))
#             shopping_cart[shopping_name] = {"price": shopping_price, "num": shopping_num}
#             print("商品修改成功")
#         # 3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#         case "3":
#             shopping_name = input("请输入要删除的商品名称")
#             if shopping_name not in shopping_cart:
#                 print("商品不存在，请重新选择")
#             else:
#                 del shopping_cart[shopping_name]
#                 print("商品删除成功")
#         # 4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：×××，商品价格：×××，商品数量：×××"。
#         case "4":
#                 for i in shopping_cart.keys():
#                     info = shopping_cart[i]
#                     print(f"商品名称:{i},商品价格:{info['price']},商品数量:{info['num']}")
#         case "5":
#             print("退出成功")
#             break
#         case _:
#             print("操作不支持")
#
# # 1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# # 2.修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# # 3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# # 4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# # 5.列出所有学生：遍历所有学生信息并输出。
# # 6.统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# # 7.退出系统。
# student_info = {}
# print("欢迎来到学生教务系统")
# menu = """
# ####################################################################################
# 1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出所有学生 6.统计班级成绩 7.退出系统
# ####################################################################################
# """
# while True:
#     print(menu)
#     operate = input("请输入要进行的操作1-7:")
#     match operate:
#         case "1":
#             student_name = input("请输入学生姓名")
#             chinese_score = float(input("请输入语文成绩"))
#             math_score = float(input("请输入数学成绩"))
#             english_score = float(input("请输入英语成绩"))
#             student_info[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
#             print("添加成功")
#         case "2":
#             student_name = input("请输入要修改学生的姓名")
#             chinese_score = float(input("请输入要修改的语文成绩"))
#             math_score = float(input("请输入要修改的数学成绩"))
#             english_score = float(input("请输入要修改的英语成绩"))
#             if student_name not in student_info:
#                 print("该学生不存在，请重新输入")
#             student_info[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
#             print("修改成功")
#         case "3":
#             student_name = input("请输入要删除的学生姓名")
#             if student_name not in student_info:
#                 print("该学生不存在，请重新输入")
#             del student_info[student_name]
#             print("删除成功")
#         case "4":
#             student_name = input("请输入要查询的学生姓名")
#             if student_name not in student_info:
#                 print("该学生不存在，请重新输入")
#             info = student_info[student_name]
#             print(f"姓名:{student_name},语文:{info['chinese']},数学:{info['math']},英语:{info['english']}")
#         case "5":
#             for i in student_info:
#                 info = student_info[i]
#                 print(f"姓名:{i},语文:{info['chinese']},数学:{info['math']},英语:{info['english']}")
#         case "6":
#             if len(student_info) == 0:
#                 print("当前没有学生信息")
#                 continue
#             student_chinese = [student_info[student]['chinese'] for student in student_info]
#             student_math = [student_info[student]['math'] for student in student_info]
#             student_english = [student_info[student]['english'] for student in student_info]
#             print(f"语文最高分为{max(student_chinese)},语文最低分为{min(student_chinese)},语文平均分为{(sum(student_chinese)/len(student_chinese)):.1f}")
#             print(f"数学最高分为{max(student_math)},数学最低分为{min(student_math)},数学平均分为{(sum(student_math) / len(student_math)):.1f}")
#             print(f"英语最高分为{max(student_english)},英语最低分为{min(student_english)},英语平均分为{(sum(student_english) / len(student_english)):.1f}")
#             #语文
#             max_chinese_student = [student for student in student_info if student_info[student]['chinese']==max(student_chinese)]
#             min_chinese_student = [student for student in student_info if student_info[student]['chinese']==min(student_chinese)]
#             print(f"语文最高分的学生:{max_chinese_student},语文最低分的学生:{min_chinese_student}")
#             #数学
#             max_math_student = [student for student in student_info if student_info[student]['math'] == max(student_math)]
#             min_math_student = [student for student in student_info if student_info[student]['math'] == min(student_math)]
#             print(f"数学最高分的学生:{max_math_student},数学最低分的学生:{min_math_student}")
#             #英语
#             max_english_student = [student for student in student_info if student_info[student]['english'] == max(student_english)]
#             min_english_student = [student for student in student_info if student_info[student]['english'] == min(student_english)]
#             print(f"英语最高分的学生:{max_english_student},英语最低分的学生:{min_english_student}")
#         case "7":
#             print("系统退出成功")
#             break
#
# while True:
#     email = input("请输入邮箱格式").strip()
#     if email == "":
#         print("邮箱不能为空请重新输入")
#         continue
#     if email.count("@") !=1:
#         print("邮箱格式错误，@多或少了")
#         continue
#     em = email.split("@")
#     em_start = em[0]
#     em_end = em[1]
#     if em_start == "" or em_end == "":
#         print("邮箱格式不能为空")
#         continue
#     if "." not in em_end or em_end.startswith(".") or em_end.endswith("."):
#         print("邮箱格式错误")
#         continue
#     print("邮箱格式正确")
#     break
#
# 商品库：{商品编号: [名称, 单价, 库存]}
products = {
    "A001": ["苹果", 5.5, 100],
    "A002": ["香蕉", 3.0, 50],
    "B001": ["纯牛奶", 25.0, 30],
    "B002": ["薯片", 8.5, 80],
    "C001": ["钢笔", 15.0, 20],
    "C002": ["笔记本", 22.0, 15]
}
cart = []

def Browse_Products():
    """
    遍历 products 字典，打印出所有商品信息
    打印出所有商品(编号、名称、单价、库存）。
    """
    for num,info in products.items():
        name,price,stock = info
        print(f"编号:{num} 名称:{name} 单价:{price} 库存:{stock}")

def Add_Cart():
    """
    提示用户输入商品编号，若不存在则重输。
    提示用户输入数量，若输入非数字或数量≤0则重输。
    检查库存是否充足，若不足则重输。
    合法则将商品信息以字典形式追加到 cart 列表中。
    更新 products 中的库存数量（扣减）。
    """
    while True:
        num = input("请输入商品编号")
        if num not in products:
            print("商品不存在,请重新输入")
            continue

        try:
            stock_num = int(input("请输入商品的数量"))
        except ValueError:
            print("请输入有效的整数")
            continue

        if stock_num <= 0:
            print("数量必须为正整数")
            continue

        name,price,stock = products[num]
        if stock_num > stock:
            print(f"库存不足,当前库存剩余{stock}")
            continue

        cart.append({
            "id": num,
            "name": name,
            "price": price,
            "num": stock_num
        })
        products[num][2] -= stock_num
        return

def View_Cart():
    """
    打印购物车中所有商品的详细信息，包括编号、名称、单价、数量及小计（单价×数量）。
    如果购物车为空，则打印提示信息。
    """
    if not cart:
        print("购物车为空")
        return
    for item in cart:
        subtotal = item["price"] * item["num"]
        print(f"编号:{item['id']},名称:{item['name']},单价:{item['price']},库存:{item['num']},小计:{subtotal}")

def checkout():
    """
    若购物车为空，提示并返回。计算所有商品的原价总和。
    根据总价确定折扣（满200打9折，满100打9.5折，否则无折扣）。
    计算折后价格，再根据折后价是否≥99判断是否免运费（否则运费8元）。
    打印购物小票（含明细、折扣、运费、实付金额）。
    清空购物车 cart。
    """
    if not cart:
        print("购物车为空")
        return
    total = 0
    for item in cart:
        subtotal = item["price"] * item["num"]
        total += subtotal
    print("""
    ========== 购物小票 ==========
    """)
    for item in cart:
        print(f"{item['name']} x {item['num']}    ￥{subtotal:.1f}")
    print("-"* 30)
    print(f"商品原价:{total}")
    if total >= 200:
        discount = 0.9
        discount_price = total * discount
        print("折扣:9折")
    elif total >= 100:
        discount = 0.95
        discount_price = total * discount
        print("折扣:9.5折")
    else :
        discount = 1
        discount_price = total * discount
        print("折扣:无")

    if discount_price >= 99:
        carriage = 0
        print("运费:无")
    else:
        carriage = 8
        print("运费:￥8.0")
    print("-"*30)
    Final_Price = discount_price + carriage
    print(f"实付金额:{Final_Price}")
    print(f"优惠的金额:{discount_price}")
    print("感谢光临!")
    print("================================")

    cart.clear()

menu="""
===== 超市收银系统 =====
1. 浏览商品
2. 购买商品（添加购物车）
3. 查看购物车
4. 结算并打印小票
5. 退出系统
=======================
请选择操作(1-5):
"""

while True:
    print(menu)
    choice = input()
    match choice:
        case "1":
            Browse_Products()
        case "2":
            Add_Cart()
        case "3":
            View_Cart()
        case "4":
            checkout()
        case "5":
            print("退出成功")
            break
        case _:
            print("不支持该操作")



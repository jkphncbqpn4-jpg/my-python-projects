# while True:
#     email = input("请输入你的邮箱: ")
#     if email == "":
#         print(f"{email}邮箱格式错误,邮箱不能为空")
#         continue
#     elif email.count("@") != 1 and email.count(".") < 1:
#         print(f"{email}邮箱格式错误")
#         continue
#
#     user = email.split("@")#用split拆分
#     user1 = user[0]#0为@左边部分
#     user2 = user[1]#1为@右边部分
#
#     if user1 == "" or user2 == "":
#         print(f"{email}邮箱格式错误")
#         continue
#     elif "." not in user2 or user2.startswith(".") or user2.endswith("."):
#         print(f"{email}邮箱格式错误")
#         continue
#     elif email.startswith("@") or email.endswith("@"):
#         print(f"{email}邮箱格式错误")
#         continue
#     print(f"{email}邮箱格式正确")
#     break

#改进版
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



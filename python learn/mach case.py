#案例、
# try:
#     num1 = int(input("请输入数字1:"))
#     num2 = int(input("请输入数字2:"))
# except ValueError:
#     print("请输入正确的数字")
#     exit()
# num3 = input("输入运算符:")
# match num3:
#     case "+":
#         print(f"{num1+num2}")
#     case "-":
#         print(f"{num1-num2}")
#     case "*":
#         print(f"{num1*num2}")
#     case "/" if num2 !=0:
#         print(f"{num1/num2}")
#     case _:
#         print("操作不支持")

#案例2
key =input("请输入指令:")
match key:
    case "w"|"W":
        print("角色向上移动")
    case "s"|"S":
        print("角色向下移动")
    case "a"|"A":
        print("角色向左移动")
    case "d"|"D":
        print("角色向右移动")
    case" ":
        print("角色跳跃")
    case"j"|"J":
        print("角色发动攻击")
    case"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("没有该操作")
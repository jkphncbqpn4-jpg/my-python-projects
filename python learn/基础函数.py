#函数定义时不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义，后调用；
#函数定义
# def out_line():
#     print("___________________")
#
# #函数调用
# out_line()

#函数的参数与返回值
#函数一
def circle_area(r):
    area = 3.14 * r * r
    return area
circle_r = circle_area(3)
print(circle_r)

#函数二
def rectangle_area(l,w):
    """
    根据长方形的长度和宽度来计算长方形的面积
    :param l:长
    :param w:宽
    :return:长方形面积
    """
    area = l * w
    return area
rectangle_a = rectangle_area(22,15)
print(rectangle_a)

#函数三 计算圆的面积，周长 -- 半径 --->返回值有多个，用逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len (r):
    area_len = round(3.14 * r ** 2,1) , round(3.14 * 2 * r,1)
    return area_len
circle_area_len1 = circle_area_len(4)
print(circle_area_len1)
print(type(circle_area_len1))

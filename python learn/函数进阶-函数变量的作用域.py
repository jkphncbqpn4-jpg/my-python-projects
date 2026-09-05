#全局变量,在函数内部和外部都能使用
num = 100
def circle_area(r):
    #局部变量：只能在函数内部使用
    area = 3.14 * r * r
    return area

circle_r = circle_area(3)
print(circle_r)
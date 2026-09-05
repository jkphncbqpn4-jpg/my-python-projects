# 定义一个函数，根据传入的底和高计算三角形面积。
def triangle_area(b,h):
    """
    计算三角形的面积底乘高除2
    :param b: 底
    :param h: 高
    :return: 面积
    """
    area = round((b * h)/2,1)
    return area
triangle_a = triangle_area(5,7)
print(f"三角形的面积为{triangle_a}")
# 定义一个函数，计算传入的字符串中元音字母的个数，元音字母为： a e i o u A E I O U
def count_vowel(s):
    """
    计算字符串中的元音个数
    :param s: 字符串
    :return: 字符串中的元音个数
    :return: 字符串中的元音个数
    """
    vowels = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count
count_a = count_vowel("heallo")
print(count_a)
# 定义一个函数，计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数），并返回。
def Gaokao_sorce(o):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）
    :param o:传入的列表
    :return: 最高分、最低分、平均分（保留1位小数）
    """
    source_list = max(o),min(o),round(sum(o)/len(o),1)
    return source_list
result = Gaokao_sorce([85, 92, 78, 88, 95])
print(result)  # 输出 (95, 78, 87.6)

# 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数 >= 90：A
# 分数 >= 75：B
# 分数 >= 60：C
# 分数 < 60：D
def good_score(s):
    """
    根据传入的分数，计算对应的分数等级并返回
    :param s: 分数
    :return: 等级
    """
    if s >= 90:
        return "A"
    elif s >= 75:
        return "B"
    elif s >= 60:
        return "C"
    else:
        return "D"

score = good_score(1)
print(score)  # 输出 "D"

# 定义一个函数，用于判断一个字符串是否是回文串，返回 bool 值。
# 回文串定义： 把字符串反转，如果和原字符串相同，就是回文串。
# 示例： "level"、"radar"、"黄山落叶松叶落山黄" 都是回文串。
def palindrome(s):
    """
    用于判断一个字符串是否是回文串，返回 bool 值
    把字符串反转，如果和原字符串相同，就是回文串
    :param s: 字符串
    :return:布尔值
    """
    if s[::-1] == s:
        return True
    else:
        return False
list1 = palindrome("heh")
print(list1)

#定义一个函数，完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def convert_time(t):
    """
    完成时间转换功能，将传入的秒转换为小时、分钟、秒。
    :param t: 时间
    :return: 时,分,秒
    """
    if t >= 3600:
        h = t // 3600
        m = t % 3600 // 60
        s = t % 60
    elif t < 3600:
        h = 0
        m = t // 60
        s = t % 60
    c_time = f"{h}小时{m}分{s}秒"
    return c_time
a = convert_time(360)
print(a)

# 定义一个函数，根据传入的三角形三个边的边长，判定三角形的类型。
# 如果不能构成三角形，返回 "不能构成三角形"
# 如果三边相等，返回 "等边三角形"
# 如果两边相等，返回 "等腰三角形"
# 否则返回 "普通三角形"
# 构成三角形的条件： 任意两边之和大于第三边
def triangle(a,b,c):
    """
    根据传入的三角形三个边的边长，判定三角形的类型
    :param a: 边
    :param b: 边
    :param c: 边
    :return: 三角形类型
    """
    if a+b>c and a+c>b and b+c>a:
        if a == b == c:
            return ("等边三角形")
        elif a == b or a == c or b == c:
            return ("等腰三角形")
        else:
            return ("普通三角形")
    else:
        return ("三角形不成立")

result = triangle(2,2,3)
print(result)
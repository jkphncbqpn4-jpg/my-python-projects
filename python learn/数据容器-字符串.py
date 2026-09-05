# #字符串 基本操作---->不可变的(无法修改)、有序性、可迭代性
#
# s = "Hello-World"
# print(s[3])
# print(s[-9])
#
# for i in s:
#     print(i)
#
# #切片
# print(s[6:12:1])

s = "   Hello-World-Hello-Python   "

#将字符串转为小写与大写
sl=s.lower()
print(sl)
su=s.upper()
print(su)
#查找字符串中子串首次出现的位置
print(s.find("o"))
#统计字符串中子串出现的次数
print(s.count("l"))
#将字符串按指定字符串切割，切割的字符串返回列表
sp = s.split("-")
print(sp)
#将字符串两端的空格去除
st = s.strip()
print(st)
#替换字符串里面指定的字符串
sr = s.replace("-","_")
print(sr)
#判断字符串是否以该指定的字符串开头
print(s.startswith("Hello"))
#判断字符串是否以该指定的字符串结尾
print(s.endswith("Python"))
#字符串所有的方法都不会修改原本的字符串
print(s)


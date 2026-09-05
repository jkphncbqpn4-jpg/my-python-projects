#字符串格式化的方法1-%s自动将变量转化为字符串
name = "某"
age =18
specialty = "云计算应用服务"
hobby = "Linux、Python"
# print("大家好,我是" + name + ",今年" + str(age) + "岁,专业是" + specialty + ",爱好 ")
print("大家好，我是%s,今年%s岁，我的专业是%s，我的爱好是%s" % (name, age, specialty, hobby))
#用%s来做字符串拼接时前后的数据要一致有多少个%s就要有但是个数据%s表示占位符s表示string也就是字符串类型

#字符串格式化的方法2-f"内容{变量/表达式}"推荐这种
print(f"大家好，我是{name},今年{age}岁，我的专业是{specialty}，我的爱好是{hobby}")
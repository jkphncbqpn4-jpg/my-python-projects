#默认参数跟在非默认参数之后
def reg_stu(name,age,gender="女",city="北京"):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

stu = reg_stu("李四",18)
print(stu)
stu1 = reg_stu("张三",19,"男","重庆")
print(stu1)
stu2 = reg_stu("王五",19,city="上海")
print(stu2)
def reg_stu(name,age,gender,city):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

#传参方式一：位置参数需要按顺序
stu = reg_stu("李四",18,"女","北京")
print(stu)

#传参方式二:关键字参数，不需要按顺序
stu2 = reg_stu(name="万五",gender="男",age="23",city="湖南")
print(stu2)

#传参方式三:位置参数+关键字参数 位置参数在前，关键字在后
stu3 = reg_stu("李柱",19,city="海南",gender="男")
print(stu3)
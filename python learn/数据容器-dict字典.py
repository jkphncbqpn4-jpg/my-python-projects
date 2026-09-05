#字典 使用键值对(key:value)来存储数据
#键值对(key:value)存储、键(key)不能重复、存储的值可修改
#字典中的value可以是任何类型的数据，但是key不能为可变类型
#key不能重复，如果重复后面的值会覆盖前面的值
# dict1 = {"张三":456,"李四":789,"王五":234,"张三":234}
# #定义空字典
# dic2 = {}
# dict3 = dict()
# #根据key获取value
# print(dict1)
# score = dict1["李四"]
# print(score)

#字典的使用方法
dict1 = {"张三":456,"李四":789,"王五":234,"二狗":234}
#添加
dict1["立柱"] = 567
print(dict1)
#修改
dict1["张三"] = 574
print(dict1)
#查询
print(dict1["张三"])
print(dict1.get("张三"))
print(dict1.keys())#查询字典里所有的key
print(dict1.values())#查询字典里所有的values
print(dict1.items())#查询字典里所有的键值对

#删除
source = dict1.pop("李四")#删除指定key并把key的value值返回
print(source)

del dict1["王五"]#删除指定的键值对
print(dict1)

#遍历
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")

for v in dict1.items():
    print(f"{v[0]}: {v[1]}")
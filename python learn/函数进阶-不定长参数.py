#不定长参数 位置参数---->*args(元组)
#args并不是绝对的可以起其他变量名，不过这个是约定俗成规范的写法
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = round(sum(args)/len(args),1)
    return min_data,max_data,avg_data
data1 = calc_data(145,123,45,12,564,12)
print(data1)

#不定长参数 关键字参数---->**kwargs(字典)
#kwargs并不是绝对的可以起其他变量名，不过这个是约定俗成规范的写法
def calc_data(*args,**kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最大值{max_data},最小值{min_data},平均值{avg_data}")
    return min_data,max_data,avg_data
data1 = calc_data(145,123,45,12,564,12,round=2,print=True)
print(data1)
#*args适用于处理数量不确定的数据
#**kwargs适用于处理数量不确定的选项(函数的配置参数，用来定制函数的行为)

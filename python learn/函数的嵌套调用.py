#函数的嵌套 函数的调用使用了栈结构 --->后进先出
def function_a():
    print("a before")#先输出a before
    function_b()#调用b
    print("a after")#回到a，输出a after

def function_b():
    print("b before")#输出b before
    function_c()#调用c
    print("b after")#回到b,输出b after

def function_c():
    print("c")#输出c，回到b

function_a()
#函数的阶乘
#递归调用（层层递进，再逐步回归）:指的是在函数中自己调用自己的情况下 --->一定得有终结点


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def commodity(*args,coupon=0,integral=0,shipping=0.0):
    """
        计算商品总价（满5000可用优惠券和积分）

        args: 每个元素为 (商品名, 单价, 数量)
        coupon: 优惠券金额（元）
        integral: 积分（100积分=1元）
        shipping: 运费（元）
        return:优惠后的总金额
        """
    total= [i[1] * i[2] for i in args]
    total_price = sum(total)#没优惠的总价
    if total_price >= 5000:
        total_price -= min(coupon,total_price)#使用优惠卷过后的金额
        deduction = (integral // 100) * 1
        total_price -= min(deduction,total_price)#确保积分金额如果过高但不会高于现在优惠过的金额
    total_price += shipping
    return total_price


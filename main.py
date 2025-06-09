def cal_profit(x:list, p:list):
    profit = sum(s * s1 for s, s1 in (x,p))
    return profit
def recursive_func(x:list, p:list, x_opt:list, p_opt, l):
    if l == len(x) + 1:
        p_cur = cal_profit(x, p)
        if p_cur > p_opt:
            p_opt =  p_cur
            x_opt = x
    else:
        x[l] = 1
        recursive_func(x, p, x_opt, p_opt, l + 1)
        x[l] = 0
        recursive_func(x, p, x_opt, p_opt, l + 1)
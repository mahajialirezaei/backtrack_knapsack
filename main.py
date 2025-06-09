def cal_product_ls(x:list, p:list):
    profit = sum(s * s1 for s, s1 in (x,p))
    return profit
def recursive_func(x:list, p:list, x_opt:list, w:list ,p_opt, l, b):
    if l == len(x) + 1:
        if cal_product_ls(x, w) <= b:
            p_cur = cal_product_ls(x, p)
            if p_cur > p_opt:
                p_opt =  p_cur
                x_opt = x
    else:
        x[l] = 1
        recursive_func(x, p, x_opt, w,p_opt, l + 1, b)
        x[l] = 0
        recursive_func(x, p, x_opt, w, p_opt, l + 1, b)

x = [0, 0, 0]
p = [1, 2, 3]
w = [1, 2, 999]
b = 1000
def cal_product_ls(x: list, p: list):
    profit = sum(s * s1 for (s, s1) in zip(x, p))
    return profit


def recursive_func(x: list, p: list, w: list, l, b):
    global x_opt, p_opt
    print(x_opt)
    print(p_opt)
    if l == len(x):
        if cal_product_ls(x, w) <= b:
            p_cur = cal_product_ls(x, p)
            if p_cur > p_opt:
                p_opt = p_cur
                x_opt = x.copy()
    else:
        x[l] = 1
        recursive_func(x, p,  w,  l + 1, b)
        x[l] = 0
        recursive_func(x, p,  w,  l + 1, b)


x = [0, 0, 0]
p = [1, 2, 3]
w = [1, 2, 999]
b = 1000
x_opt = [0, 0, 0]
p_opt = 0
recursive_func(x, p, w, 0, b)
print(x_opt)
print(p_opt)
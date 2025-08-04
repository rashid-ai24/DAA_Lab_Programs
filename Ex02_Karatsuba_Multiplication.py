# Ex No: 2 - IMPLEMENTATION OF MULTIPLICATION OF LARGE INTEGERS USING DIVIDE AND CONQUER APPROACH

def karatsuba(x, y):
    x_str, y_str = str(x), str(y)
    if len(x_str) == 1 or len(y_str) == 1:
        return x * y
    max_len = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)
    n = len(x_str)
    n_half = n // 2
    a, b = int(x_str[:n_half]), int(x_str[n_half:])
    c, d = int(y_str[:n_half]), int(y_str[n_half:])
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd
    result = (10 ** (2 * n_half)) * ac + (10 ** n_half) * ad_bc + bd
    return result

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
result = karatsuba(num1, num2)
print(result)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

p = 26513
q = 32321

gcd_value, u, v = extended_gcd(p, q)

print(u if u < v else v)

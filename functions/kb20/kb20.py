def kb(x, a):
    x_val = tmpld.mpmath.mpf(x)
    alpha = tmpld.mpmath.mpf(a)
    arg = 2 * x_val
    arg = 1 - arg * arg
    arg = alpha * tmpld.mpmath.pi * tmpld.mpmath.sqrt(arg)
    numer = tmpld.mpmath.besseli(0, arg) - 1
    denom = tmpld.mpmath.besseli(0, alpha * tmpld.mpmath.pi) - 1
    return numer / denom

def kb20(x):
    return kb(x, 2)

def f(x):
    if x == 0:
        return -4*tmpld.mpmath.pi**2 / (tmpld.mpmath.besseli(0, 2 * tmpld.mpmath.pi) - 1)
    x_val = tmpld.mpmath.mpf(x)
    c = x_val + 1 / 2
    return kb20(c) / x_val

(p_tail, q_tail, e) = tmpld.remez.rat_remez(f, 10, 8, -0.25, 0.25)
(p_tail, q_tail, e) = tmpld.remez.rat_remez(f, 8, 6, -0.25, -1.0E-15)

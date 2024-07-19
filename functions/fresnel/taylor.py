import tmpld
import tmpld.poly

def taylor(x, n):
    xval = tmpld.mpmath.mpf(x) * tmpld.mpmath.sqrt(tmpld.mpmath.pi() / 2)
    xpow = xval ** (4*n + 1)
    denom = tmpld.mpmath.mpf(4*n + 1) * tmpld.mpmath.factorial(2*n)
    return (-1)**n * xpow / denom

a = [taylor(1, n) for n in range(1, 10)]
tmpld.poly.print_coeffs(a)

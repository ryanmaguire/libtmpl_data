import tmpld
import tmpld.remez
tmpld.mpmath.mp.prec = 300
PI_FACTOR = tmpld.mpmath.sqrt(tmpld.mpmath.pi()) / 2
PLUS_SCALE = tmpld.mpmath.mpc(1 + 1j)
MINUS_SCALE = tmpld.mpmath.mpc(1 - 1j)
HALF = tmpld.mpmath.mpf(0.5)

def fresnel_cos(x):
    factor = tmpld.mpmath.mpf(x) * PI_FACTOR
    left = MINUS_SCALE * tmpld.mpmath.erf(PLUS_SCALE * factor)
    right = PLUS_SCALE * tmpld.mpmath.erf(MINUS_SCALE * factor)
    return (left + right).real / 4

def fresnel_sin(x):
    factor = tmpld.mpmath.mpf(x) * PI_FACTOR
    left = PLUS_SCALE * tmpld.mpmath.erf(PLUS_SCALE * factor)
    right = MINUS_SCALE * tmpld.mpmath.erf(MINUS_SCALE * factor)
    return (left + right).real / 4

def ff(x):
    factor = tmpld.mpmath.mpf(x)
    A = fresnel_cos(factor) - HALF
    B = fresnel_sin(factor) - HALF
    a = tmpld.mpmath.sin(tmpld.mpmath.pi() * factor * factor * HALF)
    b = tmpld.mpmath.cos(tmpld.mpmath.pi() * factor * factor * HALF)
    return a*A - b*B

def fg(x):
    factor = tmpld.mpmath.mpf(x)
    A = fresnel_cos(factor) - HALF
    B = fresnel_sin(factor) - HALF
    a = tmpld.mpmath.sin(tmpld.mpmath.pi() * factor * factor * HALF)
    b = tmpld.mpmath.cos(tmpld.mpmath.pi() * factor * factor * HALF)
    return -a*B - A*b

def t(x):
    y = tmpld.mpmath.mpf(x)
    return tmpld.mpmath.mpf(4) / y


def f(x):
    return fg(t(x))

START = 2**-15
END = 1.0

(P, Q, e) = tmpld.remez.rat_remez(f, 8, 6, START, END)
tmpld.remez.print_rat_coeffs(P, Q)

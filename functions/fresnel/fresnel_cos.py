def fresnel_cos(x):
    PI_FACTOR = tmpld.mpmath.sqrt(tmpld.mpmath.pi()) / 2
    PLUS_SCALE = tmpld.mpmath.mpc(1 + 1j)
    MINUS_SCALE = tmpld.mpmath.mpc(1 - 1j)
    HALF = tmpld.mpmath.mpf(0.5)
    factor = tmpld.mpmath.mpf(x) * PI_FACTOR
    left = MINUS_SCALE * tmpld.mpmath.erf(PLUS_SCALE * factor)
    right = PLUS_SCALE * tmpld.mpmath.erf(MINUS_SCALE * factor)
    return (left + right).real / 4

def ld2mpf(t):
    out = tmpld.mpmath.mpf(0)
    for n in range(10):
        float_t = float(t)
        out += float_t
    t = t - float_t
    if t == 0:
        break
    return out

"""
################################################################################
#                                   LICENSE                                    #
################################################################################
#   This file is part of libtmpl_data.                                         #
#                                                                              #
#   libtmpl_data is free software: you can redistribute it and/or modify it    #
#   under the terms of the GNU General Public License as published by          #
#   the Free Software Foundation, either version 3 of the License, or          #
#   (at your option) any later version.                                        #
#                                                                              #
#   libtmpl_data is distributed in the hope that it will be useful,            #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#   GNU General Public License for more details.                               #
#                                                                              #
#   You should have received a copy of the GNU General Public License          #
#   along with libtmpl_data.  If not, see <https://www.gnu.org/licenses/>.     #
################################################################################
#   Purpose:                                                                   #
#       Computes the Chebyshev coefficients for the error function Erf(x).     #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 19, 2023.                                                  #
################################################################################
"""

# Chebyshev evaluation and coefficients.
import tmpld.chebyshev

# Polynomial evaluation via Horner's method.
import tmpld.poly

def f(x):
    y = tmpld.mpmath.mpf(2)*(tmpld.mpmath.mpf(x) + tmpld.mpmath.mpf(2.0))
    return tmpld.mpmath.erf(y)

def coeffs(N):
    return tmpld.chebyshev.cheb_coeffs(f, N, 1000)

def cheb_eval(a, x):
    y = (tmpld.mpmath.mpf(x) - tmpld.mpmath.mpf(4)) / tmpld.mpmath.mpf(2)
    return tmpld.chebyshev.cheb_eval(a, y)

def poly_eval(a, x):
    y = (tmpld.mpmath.mpf(x) - tmpld.mpmath.mpf(4)) / tmpld.mpmath.mpf(2)
    return tmpld.poly.poly_eval(a, y)

def diff(a, x):
    y = cheb_eval(a, x)
    z = tmpld.mpmath.erf(x)
    return (y - z) / z

# Desired precision.
EPS = 2**-54

# Print which values of N achieved double precision.
x = 2
N = 40

for m in range(27, N):
    a = coeffs(m)
    y = diff(a, x)

    # If the expansion was very accurate, move along.
    if abs(y) < EPS:
        b = tmpld.chebyshev.cheb_to_poly(a)
        tmpld.poly.print_coeffs(b)
        break

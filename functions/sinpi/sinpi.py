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
#       Taylor coefficients for the normalized function.                       #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       November 6, 2025.                                              #
################################################################################
"""

# Arbitrary precision numbers found here.
import tmpld

# Compute the nth Taylor coefficient of sin(pi x).
def taylor(ind):
    """
        Function:
            taylor
        Purpose:
            Given a non-negative integer n, compute the coefficient of the
            nth term of the Taylor series for sin(pi x) at x = 0.
        Arguments:
            ind (int):
                The index of the coefficient to be computed.
        Output:
            coeff (fraction):
                The coefficient of the Taylor series of sin(pi x) at x = 0.
    """
    power = 2 * ind + 1
    num = tmpld.mpmath.pi ** power
    den = tmpld.mpmath.factorial(power)
    return (-1) ** ind * num / den

# Computes the Taylor series for sin(pi x) / x.
def sincpi_taylor(coeffs, x_val):
    """
        Function:
            sincpi_taylor
        Purpose:
            Computes the Taylor series of sin(pi x) / x.
    """
    x_mpf = tmpld.mpmath.mpf(x_val)
    x_sq = x_mpf * x_mpf
    out = tmpld.mpmath.mpf(0)
    deg = len(coeffs) - 1

    # Horner's method for polynomial evaluation.
    for ind in range(deg + 1):
        out = out * x_sq + coeffs[deg - ind]

    return out

def sincpi(x_val):
    """
        Function:
            sincpi
        Purpose:
            Computes sin(pi x) / x.
    """
    x_mpf = tmpld.mpmath.mpf(x_val)

    if x_mpf == 0:
        return tmpld.mpmath.pi

    return tmpld.mpmath.sin(tmpld.mpmath.pi * x_mpf) / x_mpf

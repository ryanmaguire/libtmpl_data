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
#       Computes the rational minimax coefficients for arc-sine.               #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 13, 2023.                                                      #
################################################################################
"""

# mpmath imported here.
import tmpld

# Algorithm for computing Remez coefficients given here.
import tmpld.remez

# Arcsin Taylor coefficients given here.
import arcsin

# Compute and print the coefficients for the Pade approximant of asin(x).
coeffs = [arcsin.taylor(n) for n in range(1, 60)]

# Computes the Taylor series for (asin(x) - x) / x^3.
def asin_taylor(x_val):
    """
        Function:
            asin_taylor
        Purpose:
            Computes the Taylor series of (asin(x) - x) / x^3.
    """
    x_mpf = tmpld.mpmath.mpf(x_val)
    x_sq = x_mpf * x_mpf
    out = tmpld.mpmath.mpf(0)
    deg = len(coeffs) - 1

    # Horner's method for polynomial evaluation.
    for ind in range(deg+1):
        num = coeffs[deg - ind].numerator
        den = coeffs[deg - ind].denominator
        coeff = tmpld.mpmath.mpf(num) / tmpld.mpmath.mpf(den)
        out = out*x_sq + coeff

    return out

# Print the coefficients for the rational minimax approximation.
(P, Q, err) = tmpld.remez.rat_remez(asin_taylor, 8, 8, -0.5, 0.5)

# Odd coefficients are negligible. In the absence of rounding error, the
# odd coefficients would be zero.
P_even = [P[2*k] for k in range(1 + (len(P) >> 1))]
Q_even = [Q[2*k] for k in range(1 + (len(Q) >> 1))]
tmpld.remez.print_rat_coeffs(P_even, Q_even)

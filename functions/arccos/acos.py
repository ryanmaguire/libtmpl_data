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
#       Taylor coefficients for the inverse cosine function.                   #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   October 29, 2024.                                                  #
################################################################################
"""

# Arbitrary precision rationals here.
import fractions

# Denominator given by factorial function.
import math

# Numerator given by rising factorial.
import tmpld.math

# Compute the nth Taylor coefficient of acos(x).
def taylor(ind):
    """
        Function:
            taylor
        Purpose:
            Given a non-negative integer n, compute the coefficient of the
            nth term of the Taylor series for arccos at x = 0.
        Arguments:
            ind (int):
                The index of the coefficient to be computed.
        Output:
            coeff (fraction):
                The coefficient of the Taylor series of arccos(x) at x = 0.
    """
    num = tmpld.math.half_rising_factorial(ind)
    den = (2*ind + 1)*math.factorial(ind)
    return fractions.Fraction(num, den)

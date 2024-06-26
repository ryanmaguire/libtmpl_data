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
#       Routines for evaluating polynomials and derivatives.                   #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 8, 2023.                                                   #
################################################################################
"""

# mpmath is imported here.
import tmpld

# mpmath constants found here.
import tmpld.constants

# Compute the derivative of a polynomial using Horner's method.
def dpoly_eval(coeffs, x_val):
    """
        Function:
            dpoly_eval
        Purpose:
            Evaluates the derivative of a polynomial using Horner's method.
        Arguments:
            coeffs (list):
                The coefficients of the polynomial.
            x_val (float or mpmath.mpf):
                The point where the polynomial is computed.
        Output:
            dpval (mpmath.mpf):
                The value dP(x)/dx at x = x_val, where P is the polynomial.
    """

    # The degree is given by the length of the coefficient list.
    deg = len(coeffs) - 1

    # Initialize the output to zero.
    dpval = tmpld.constants.zero

    # Convert the input to an mpmath object if necessary.
    x_mpf = tmpld.mpmath.mpf(x_val)

    # Compute using Horner's method.
    for ind in range(deg):
        dpval = x_mpf*dpval + tmpld.mpmath.mpf(deg - ind)*coeffs[deg - ind]

    return dpval

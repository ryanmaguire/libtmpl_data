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
#       Computes the minimax coefficients for sqrt.                            #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 19, 2025.                                                      #
################################################################################
"""

# mpmath imported here.
import tmpld

# Algorithm for computing Remez coefficients given here.
import tmpld.remez

def sqrt_shift(x_val):
    """
        Function:
            sqrt_shift
        Purpose:
            Computes sqrt(1 + x).
    """
    if x_val == 0:
        return tmpld.mpmath.mpf(0.5)

    x_mpf = tmpld.mpmath.mpf(x_val) + tmpld.mpmath.mpf(1)
    return (tmpld.mpmath.sqrt(x_mpf) - 1.0) / (x_mpf - 1)

# Print the coefficients for the minimax approximation.
coeffs = tmpld.remez.remez(sqrt_shift, 1, 0.0, 1.0 / 128.0)
tmpld.remez.print_coeffs(coeffs)

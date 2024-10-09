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
#       Remez coefficients for the auxiliary Fresnel functions f and g.        #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 23, 2024.                                                    #
################################################################################
"""
import tmpld

PI_FACTOR = tmpld.mpmath.sqrt(tmpld.mpmath.pi()) / 2
PLUS_SCALE = tmpld.mpmath.mpc(1 + 1j)
MINUS_SCALE = tmpld.mpmath.mpc(1 - 1j)
HALF = tmpld.mpmath.mpf(0.5)

def fresnel_cos(x_val):
    """
        Function:
            fresnel_cos
        Purpose:
            Computes the normalized Fresnel cosine function.
        Arguments:
            x_val:
                The independent variable. A real number.
        Output:
            C_x:
                The normalized Fresnel Cosine evaluated at x.
        Method:
            Use the complex error function
            formula for the Fresnel functions.
    """
    factor = tmpld.mpmath.mpf(x_val) * PI_FACTOR
    left = MINUS_SCALE * tmpld.mpmath.erf(PLUS_SCALE * factor)
    right = PLUS_SCALE * tmpld.mpmath.erf(MINUS_SCALE * factor)
    return (left + right).real / 4

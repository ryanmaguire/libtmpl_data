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
#       Computes the normalized Fresnel sine function.                         #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 23, 2024.                                                      #
################################################################################
"""
import tmpld

def fresnel_sin(x_val):
    """
        Function:
            fresnel_sin
        Purpose:
            Computes the normalized Fresnel sine function.
        Arguments:
            x_val:
                The independent variable. A real number.
        Output:
            S_x:
                The normalized Fresnel Sine evaluated at x.
        Method:
            Use the complex error function
            formula for the Fresnel functions.
    """
    pi_factor = tmpld.mpmath.sqrt(tmpld.mpmath.pi()) / 2
    plus_scale = tmpld.mpmath.mpc(1 + 1j)
    minus_scale = tmpld.mpmath.mpc(1 - 1j)
    factor = tmpld.mpmath.mpf(x_val) * pi_factor
    left = plus_scale * tmpld.mpmath.erf(plus_scale * factor)
    right = minus_scale * tmpld.mpmath.erf(minus_scale * factor)
    return (left + right).real / 4

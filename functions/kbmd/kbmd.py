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
#       Provides a function for computing the modified Kaiser-Bessel window.   #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   February 18, 2026.                                                 #
################################################################################
"""
import tmpld
import tmpld.remez

def kbmd(x_arg, alpha):
    """
        Function:
            kbmd
        Purpose:
            Computes the modified Kaiser-Bessel window.
        Arguments:
            x_arg (float):
                The point in the window, -1 <= x <= 1.
            alpha (float):
                The alpha value for the window.
        Output:
            kbmd_alpha_x (float):
                The modified Kaiser-Bessel window with parameter alpha * pi
                evaluated at x.
        Notes:
            There are no checks for |x| <= 1.
            Outside the window, the function should return zero.
            For the purposes of this function, the input must satisfy
            |x| <= 1 to obtain a meaningful result.
    """
    x_val = tmpld.mpmath.mpf(x_arg)
    alpha_val = tmpld.mpmath.mpf(alpha)
    arg = 2 * x_val
    arg = 1 - arg * arg
    arg = alpha_val * tmpld.mpmath.pi * tmpld.mpmath.sqrt(arg)
    numer = tmpld.mpmath.besseli(0, arg) - 1
    denom = tmpld.mpmath.besseli(0, alpha_val * tmpld.mpmath.pi) - 1
    return numer / denom

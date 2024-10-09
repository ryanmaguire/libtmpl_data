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
#       Taylor coefficients for the normalized Fresnel Cosine function.        #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 23, 2024.                                                      #
################################################################################
"""
import tmpld

def fresnel_cos_taylor(x_val, index):
    """
        Function:
            fresnel_cos_taylor
        Purpose:
            Computes the nth Term of the Taylor series for the
            normalized Fresnel cosine function evaluated at x.
        Arguments:
            x_val:
                A real number, the point where the series is evaluated.
            index:
                An integer, the index for the Taylor coefficient.
    """
    x_mpf = tmpld.mpmath.mpf(x_val)
    factor = x_mpf * tmpld.mpmath.sqrt(tmpld.mpmath.pi() / 2)
    xpow = factor ** (4 * index)
    denom = tmpld.mpmath.mpf(4*index + 1) * tmpld.mpmath.factorial(2 * index)
    return (-1)**index * xpow * x_mpf / denom

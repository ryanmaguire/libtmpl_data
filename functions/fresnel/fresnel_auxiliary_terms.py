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
#       Computes the terms common to the auxiliary "f" and "g" functions.      #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   OCtober 9, 2024.                                                   #
################################################################################
"""
import tmpld
from fresnel_cos import fresnel_cos
from fresnel_sin import fresnel_sin

def fresnel_auxiliary_terms(x_val):
    """
        Function:
            fresnel_auxiliary_terms
        Purpose:
            Computes the terms common to the "f" and
            "g" auxiliary functions.
        Arguments:
            x_val:
                A real number, the independent variable.
        Outputs:
            f_cos_factor:
                Normalized Fresnel cosine at x.
            f_sin_factor:
                Normalized Fresnel sine at x.
            sin_factor:
                sin(pi/2 x^2)
            cos_factor
                cos(pi/2 x^2)
    """
    factor = tmpld.mpmath.mpf(x_val)
    half = tmpld.mpmath.mpf(0.5)
    f_cos_factor = fresnel_cos(factor) - half
    f_sin_factor = fresnel_sin(factor) - half
    sin_factor = tmpld.mpmath.sin(tmpld.mpmath.pi() * factor * factor * half)
    cos_factor = tmpld.mpmath.cos(tmpld.mpmath.pi() * factor * factor * half)
    return f_cos_factor, f_sin_factor, sin_factor, cos_factor

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
#   Date:   May 23, 2024.                                                      #
################################################################################
"""
import tmpld
import tmpld.remez
from fresnel_auxiliary_f import auxiliary_f
from fresnel_auxiliary_g import auxiliary_g

def transform(x_val):
    """
        Function:
            transform
        Purpose:
            Transforms the interval [1, infinity) to (0, 1] using y = 1 / x.
    """
    x_mpf = tmpld.mpmath.mpf(x_val)
    return tmpld.mpmath.mpf(1) / x_mpf

def tranformed_f(x_val):
    """
        Function:
            transformed_f
        Purpose:
            Computes the auxiliary "f" functions for
            the transformed variable "x".
    """
    return auxiliary_f(transform(x_val))

def tranformed_g(x_val):
    """
        Function:
            transformed_g
        Purpose:
            Computes the auxiliary "g" functions for
            the transformed variable "x".
    """
    return auxiliary_g(transform(x_val))

START = 0.25
END = 0.5

(P, Q, e) = tmpld.remez.rat_remez(tranformed_f, 28, 3, START, END)
tmpld.remez.print_rat_coeffs(P, Q)

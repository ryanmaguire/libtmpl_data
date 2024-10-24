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
#       Computes the auxiliary "f" function for the normalized Fresnel cosine. #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 29, 2024.                                                      #
################################################################################
"""
from fresnel_auxiliary_terms import fresnel_auxiliary_terms

def auxiliary_g(x_val):
    """
        Function:
            auxiliary_g
        Purpose:
            Computes the auxiliary "g" function for the Fresnel functions.
        Method:
            The "f" and "g" functions are defined by:

                C(x) = 0.5 + f(x) sin(pi/2 x^2) - g(x) cos(pi/2 x^2)
                S(x) = 0.5 - f(x) cos(pi/2 x^2) - g(x) sin(pi/2 x^2)

            This system can be inverted, formulating f and g in terms of
            C(x) and S(x). This functions does exactly that.
    """
    f_cos_val, f_sin_val, cos_val, sin_val = fresnel_auxiliary_terms(x_val)
    return -sin_val*f_sin_val - cos_val*f_cos_val

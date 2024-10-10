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
#       Computes the Remez coefficients for Fresnel cosine.                    #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   October 10, 2024.                                                  #
################################################################################
"""
import tmpld.remez
import tmpld.string
from fresnel_cos import fresnel_cos

def get_coeffs(index, deg):
    """
        Function:
            get_coeffs
        Purpose:
            Computes coefficients for the Remez polynomial of
            the Fresnel cosine on the interval [1 + n/32, 1 + (n+1)/32].
        Arguments:
            index:
                The value n for the interval above.
            deg:
                The degree of the Remez polynomial.
        Output:
            coeffs:
                The Remez coefficients.
    """

    def shifted_f_cos(x_val):
        """
            Computes the Fresnel cosine function
            for a shifted, or translated, variable.
        """
        shift = tmpld.mpmath.mpf(1) + tmpld.mpmath.mpf(index) / 32
        x_mpf = tmpld.mpmath.mpf(x_val)
        y_val = x_mpf + shift
        return fresnel_cos(y_val)

    return tmpld.remez.remez(shifted_f_cos, deg, 0, 1/32, interactive = False)

# Precisions:
#   Single:         DEGREE =  3
#   Double:         DEGREE =  8
#   Extended:       DEGREE =  9
#   Double-Double:  DEGREE = 15
#   Quadruple:      DEGREE = 16
DEGREE = 8
REMEZ_COEFFS = []

# Get the coefficients for each interval [1 + n/32, 1 + (n+1)/32].
for ind in range(32):

    # The last element of the list is the epsilon term. It is
    # needed for the coefficients of the polynomial, discard it.
    REMEZ_COEFFS += get_coeffs(ind, DEGREE)[0:DEGREE+1]

tmpld.string.print_mpf_array(REMEZ_COEFFS, padding = " "*4, suffix = ",")

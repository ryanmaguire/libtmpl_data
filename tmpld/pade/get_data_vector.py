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
#       Routines for computing Pade approximants.                              #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 8, 2023.                                                   #
################################################################################
"""

# Matrix manipulations.
import sympy

# Computes the column vector for the Pade approximant.
def get_data_vector(coeffs, deg):
    """
        Function:
            get_data_vector
        Purpose:
            Computes the column vector in the Pade approximant algorithm.
        Arguments:
            coeffs (list):
                The coefficients of the Taylor series of the function.
            deg (int):
                The sum of the degrees of the numerator and denominator.
        Outputs:
            data (sympy.Matrix):
                The data column vector.
    """

    # Initialize the vector as an empty list.
    data = []

    # Loop over the coefficients and append their negative to the list.
    for ind in range(deg):
        data.append(-coeffs[ind + 1])

    # Convert to a sympy matrix and return.
    return sympy.Matrix(data)

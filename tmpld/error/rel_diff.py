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
#       Computes the relative difference of two functions.                     #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 8, 2023.                                                   #
################################################################################
"""

# Compute the relative error at the point x of functions f and g.
def rel_diff(func0, func1, val):
    """
        Function:
            abs_diff
        Purpose:
            Compute the relative difference of two functions at the point "val".
        Arguments:
            func0 (function):
                The first function.
            func1 (function):
                The second function.
            val (float / mpmath.mpf):
                The value where the relative difference is computed.
    """

    # Evaluate the two functions at the given point.
    y_val = func0(val)
    z_val = func1(val)

    # Return the relative difference.
    return (y_val - z_val)/z_val

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
#       Provides a function for computing the squared cosine window.           #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   April 7, 2026.                                                     #
################################################################################
"""
import tmpld
import tmpld.remez

def coss(x_val):
    """
        Function:
            coss
        Purpose:
            Computes the squared cosine window.
        Arguments:
            x_val (float):
                The point in the window, -1 <= x <= 1.
        Output:
            coss_x (float):
                The squared cosine window evaluated at x.
        Notes:
            There are no checks for |x| <= 1.
            Outside the window, the function should return zero.
            For the purposes of this function, the input must satisfy
            |x| <= 1 to obtain a meaningful result.
    """
    arg = tmpld.mpmath.pi * tmpld.mpmath.mpf(x_val)
    cos_arg = tmpld.mpmath.cos(arg)
    return cos_arg * cos_arg

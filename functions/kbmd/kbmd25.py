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
#       Computes the modified Kaiser-Bessel window with alpha = 2.5 pi.        #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 19, 2026.                                                      #
################################################################################
"""
from kbmd import kbmd

def kbmd25(x_val):
    """
        Function:
            kbmd25
        Arguments:
            x_val (float):
                The input for the window.
        Output:
            kbmd25_x (float):
                The Kaiser-Bessel window with alpha = 2.5 * pi at x.
    """
    return kbmd(x_val, 2.5)

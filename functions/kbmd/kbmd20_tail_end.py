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
#       Provides a rational Remez expansion for kbmd20 with x close to 1.      #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   February 20, 2026.                                                 #
################################################################################
"""
import tmpld.remez
from kbmd20 import kbmd20

def shifted_kbmd20(x_val):
    """
        Function:
            shifted_kbmd20
        Purpose:
            Computes a shifted version of kbmd20 to allow for an expansion
            of kbmd20(x) at x = 1.
        Arguments:
            x_val (float):
                The input for the window.
        Output:
            shifted_kbmd20_x (float):
                The shifted kbmd20 function at x.
    """

    if x_val == 0:
        numer = -4 * tmpld.mpmath.pi**2
        denom = tmpld.mpmath.besseli(0, 2 * tmpld.mpmath.pi) - 1
        return numer / denom

    x_mpf = tmpld.mpmath.mpf(x_val)
    x_shift = x_mpf + 1 / 2
    return kbmd20(x_shift) / x_mpf

# Degree:
#   single        -> ( 4,  3)
#   double        -> ( 8,  6)
#   extended      -> ( 8,  8)
#   double-double -> (12, 12)
#   quadruple     -> (14, 12)
if __name__ == "__main__":
    (p, q, e) = tmpld.remez.rat_remez(shifted_kbmd20, 8, 6, -0.25, -1.0E-15)
    tmpld.remez.print_rat_coeffs(p, q)

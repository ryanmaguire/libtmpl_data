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
#       Provides the Remez coefficients for kbmd25 on [-1/32, 1/32].           #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 19, 2026.                                                      #
################################################################################
"""
import tmpld.remez
from kbmd25 import kbmd25

def scaled_kbmd25(x_val):
    """
        Function:
            scaled_kbmd25
        Purpose:
            Computes (kbmd25(x) - 1) / x^2 with correct limit at zero.
        Arguments:
            x_val (float):
                The point in the window.
        Output:
            scaled_kbmd25_x (float):
                (kbmd25(x) - 1) / x^2, with correct limit at x = 0.
    """

    if x_val == 0:
        factor = tmpld.mpmath.besseli(1, 2.5 * tmpld.mpmath.pi)
        numer = -5 * tmpld.mpmath.pi * factor
        denom = tmpld.mpmath.besseli(0, 2.5 * tmpld.mpmath.pi) - 1
        return numer / denom

    x_mpf = tmpld.mpmath.mpf(x_val)
    numer = kbmd25(x_mpf) - 1
    denom = x_mpf ** 2
    return numer / denom

# Degree:
#   single        ->  4
#   double        ->  8
#   extended      -> 10
#   double-double -> 16
#   quadruple     -> 16
if __name__ == "__main__":
    (p, _, e) = tmpld.remez.rat_remez(scaled_kbmd25, 8, 0, -1/32, 1/32)
    p0 = [p[2*k] for k in range((len(p) >> 1) + 1)]
    tmpld.remez.print_coeffs(p0)

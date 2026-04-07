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
#       Provides a rational Remez expansion for coss with x close to 1 / 2.    #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   April 7, 2026.                                                     #
################################################################################
"""
import tmpld.remez
from coss import coss

def shifted_coss(x_val):
    """
        Function:
            shifted_coss
        Purpose:
            Computes a shifted version of coss to allow for an expansion
            of coss(x) at x = 1 / 2.
        Arguments:
            x_val (float):
                The input for the window.
        Output:
            shifted_coss_x (float):
                The shifted coss function at x.
    """

    if x_val == 0:
        return tmpld.mpmath.pi**2

    x_mpf = tmpld.mpmath.mpf(x_val)
    x_shift = x_mpf + 1 / 2
    return coss(x_shift) / x_mpf**2

# Degree:
#   single        -> ( 4,  3)
#   double        -> ( 6,  6)
#   extended      -> ( 8,  6)
#   double-double -> (12, 10)
#   quadruple     -> (12, 11)
if __name__ == "__main__":
    (p, q, e) = tmpld.remez.rat_remez(shifted_coss, 6, 6, -0.25, -1.0E-15)
    tmpld.remez.print_rat_coeffs(p, q)

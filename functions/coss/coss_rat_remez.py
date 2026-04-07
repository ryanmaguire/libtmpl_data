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
#       Provides the rational Remez coefficients for coss on [-1/4, 1/4].      #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   April 7, 2026.                                                     #
################################################################################
"""
import tmpld.remez
from coss import coss

# Degree:
#   single        -> ( 6,  4)
#   double        -> ( 8,  8)
#   extended      -> (12, 10)
#   double-double -> (16, 14)
#   quadruple     -> (16, 16)
if __name__ == "__main__":
    (p, q, e) = tmpld.remez.rat_remez(coss, 8, 8, -0.25, 0.25)
    p0 = [p[2*k] for k in range((len(p) >> 1) + 1)]
    q0 = [q[2*k] for k in range((len(q) >> 1) + 1)]
    tmpld.remez.print_rat_coeffs(p0, q0)

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
#       Compute the Remez coefficient for exp(x) on [-1/128, 1/128].           #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 8, 2023.                                                   #
################################################################################
"""

# Remez routines found here.
import tmpld.remez

# We're computing the minimax polynomial on the interval [-1/128, 1/128].
start = -tmpld.mpmath.mpf(1) / tmpld.mpmath.mpf(128)
end = tmpld.mpmath.mpf(1) / tmpld.mpmath.mpf(128)

# Float = 2, Double = 5, Quadruple = 10, double-double = 10, extended = 6
deg = 5
c = tmpld.remez.remez(tmpld.mpmath.exp, deg, start, end)
tmpld.remez.print_coeffs(c)

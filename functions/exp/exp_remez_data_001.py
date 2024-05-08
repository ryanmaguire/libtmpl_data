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
#       Compute the Remez coefficient for exp(x) on [-1/4, 1/4].               #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 26, 2023.                                                  #
################################################################################
"""

# Remez routines found here.
import tmpld.remez

# We're computing the minimax polynomial on the interval [-1/4, 1/4].
start = -tmpld.mpmath.mpf(1) / tmpld.mpmath.mpf(4)
end = tmpld.mpmath.mpf(1) / tmpld.mpmath.mpf(4)

# Float = 5, double = 10, extended = 11, quadruple = 18, double-double = 17
deg = 18
c = tmpld.remez.remez(tmpld.mpmath.exp, deg, start, end)
tmpld.remez.print_coeffs(c)

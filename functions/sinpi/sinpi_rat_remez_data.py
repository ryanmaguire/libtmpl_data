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
#       Computes the rational minimax coefficients for sin(pi x).              #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       November 6, 2025.                                              #
################################################################################
"""

# mpmath imported here.
import tmpld

# Algorithm for computing Remez coefficients given here.
import tmpld.remez

# Normalized sinc function given here.
import sinpi

# Print the coefficients for the rational minimax approximation.
(numer, denom, err) = tmpld.remez.rat_remez(sinpi.sincpi, 8, 6, -0.5, 0.5)

# Odd coefficients are negligible. In the absence of rounding error, the
# odd coefficients would be zero.
num_even = [numer[2*k] for k in range(1 + (len(numer) >> 1))]
den_even = [denom[2*k] for k in range(1 + (len(denom) >> 1))]
tmpld.remez.print_rat_coeffs(num_even, den_even)

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
#       Computes the Pade coefficients for the normalized sine function.       #
################################################################################
#   Author:     Ryan Maguire                                                   #
#   Date:       November 6, 2025.                                              #
################################################################################
"""

# Algorithm for computing Pade coefficients given here.
import tmpld.pade

# Normalized sine Taylor coefficients given here.
import sinpi

# Compute and print the coefficients for the Pade approximant of sin(pi x).
coefficients = [sinpi.taylor(n) for n in range(11)]
(numerator, denominator) = tmpld.pade.mp_pade(COEFFICIENTS, 4, 4)
tmpld.pade.mp_print_coeffs(numerator, denominator)

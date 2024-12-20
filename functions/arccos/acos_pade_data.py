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
#       Computes the Pade coefficients for the inverse cosine function, acos.  #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   October 29, 2024.                                                  #
################################################################################
"""

# Algorithm for computing Pade coefficients given here.
import tmpld.pade

# Arccos Taylor coefficients given here.
import acos

# Compute and print the coefficients for the Pade approximant of acos(x).
A = [acos.taylor(n) for n in range(11)]
(P, Q) = tmpld.pade.pade(A, 4, 5)
tmpld.pade.print_coeffs(P, Q)

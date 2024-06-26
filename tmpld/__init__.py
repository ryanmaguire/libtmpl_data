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
#       Python routines for obtaining the numerical constants used in          #
#       libtmpl. This package is not used directly in libtmpl, and the Python  #
#       language is not needed at all. This code is kept here to remove the    #
#       mystery as to where various computations come from. A function is      #
#       usually computed via one of the following means:                       #
#           1.) Taylor / MacLaurin Series.                                     #
#           2.) Pade Approximant.                                              #
#           3.) Remez Exchange (Minimax Polynomial or Minimax Rational)        #
#           4.) Asymptotic Expansion.                                          #
#           5.) Chebyshev Polynomials.                                         #
#       The coefficients for these approximations magically appear in the C    #
#       code as fixed literal constants. In reality there are algorithms for   #
#       computing these values, and then one just copy / pastes them into      #
#       their code. These algorithms are provided with this package.           #
#                                                                              #
#           tmpld = tmpl data                                                  #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   March 13, 2023.                                                    #
################################################################################
"""

# Muli-precision math routines found here.
import mpmath

# The highest precision of long double is 112-bit mantissa. 224 bits is safe
# enough for all precisions used by libtmpl long double functions.
mpmath.mp.prec = 224

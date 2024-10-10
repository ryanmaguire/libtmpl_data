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
#       Prints log(2) in the form a0 + a1, correctly rounded.                  #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 18, 2023.                                                  #
################################################################################
"""

# Functions for working in binary.
import tmpld.binary

# Multi-precision math functions.
import mpmath

# Set precision to 1500 bits. Overkill for most things.
mpmath.mp.prec = 1500

LOG_2_VAL = mpmath.log(mpmath.mpf(2))
LOG_2_BINARY_VAL = tmpld.binary.float_to_binary(LOG_2_VAL)

NUMBER = 2

SKIP = 52
START = SKIP

for n in range(NUMBER):
    ynew = tmpld.binary.round_up_binary(LOG_2_BINARY_VAL, START + SKIP*n)
    xnew = tmpld.binary.binary_to_float(ynew)

    float_string = mpmath.nstr(
        xnew, 50, strip_zeros = True, min_fixed = 0, max_fixed = 0
    )

    if float_string[0] != "-":
        float_string = "+" + float_string

    float_string = float_string.replace("e", "E")
    print(f"    {float_string}")
    LOG_2_VAL = LOG_2_VAL - xnew
    LOG_2_BINARY_VAL = tmpld.binary.float_to_binary(LOG_2_VAL)

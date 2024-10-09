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
#       Converts a float or long double to a mpmath.mpf object.                #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   May 23, 2024.                                                      #
################################################################################
"""
import tmpld

def ld2mpf(long_double):
    """
        Function:
            ld2mpf
        Purpose:
            Converts a long double, or floating point
            object, into an mpmath.mpf object. That is,
            long-double-2-mpf.
    """
    out = tmpld.mpmath.mpf(0)

    # We get 52 bits after each iteration.
    # 10 iterations allows for a maximum of a whopping
    # 520 bits, which is way more than any actual implementation
    # of long double supports. Quadruple, for example, is 112 bits.
    # Octuple, which no current hardware supports, is 224 bits or 236 bits.
    for _ in range(32):
        float_val = float(long_double)
        out += float_val
        long_double = long_double - float_val
        if long_double == 0:
            break

    return out

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
#       Provides various constants in mpf form that are often used.            #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   March 13, 2023.                                                    #
################################################################################
"""

# mpmath is imported here.
import tmpld

# Integer constants.
zero = tmpld.mpmath.mpf(0)
one = tmpld.mpmath.mpf(1)
two = tmpld.mpmath.mpf(2)
three = tmpld.mpmath.mpf(3)
four = tmpld.mpmath.mpf(4)
five = tmpld.mpmath.mpf(5)
eight = tmpld.mpmath.mpf(8)
twelve = tmpld.mpmath.mpf(12)
sixteen = tmpld.mpmath.mpf(16)
thirty = tmpld.mpmath.mpf(30)

minus_one = tmpld.mpmath.mpf(-1)

# Fractional constants.
half = tmpld.mpmath.mpf(0.5)
one_tenth = tmpld.mpmath.mpf(0.1)
remez_increment = tmpld.mpmath.mpf(1.0E-3)

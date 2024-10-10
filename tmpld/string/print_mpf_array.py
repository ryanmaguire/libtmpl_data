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
#       Converts an array of mpmath.mpf objects as decimals in scientific form.#
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   October 10, 2024.                                                  #
################################################################################
"""

# Tool for converting an mpf object to a decimal.
from tmpld.string.float_to_c_string import float_to_c_string

# Print out an array or list of mpf objects as ordinary decimals.
def print_mpf_array(array, padding = "", suffix = ""):
    """
        Function:
            print_mpf_array
        Purpose:
            Print an array of mpmath.mpf objects as decimals.
        Arguments:
            array:
                An array or list of mpf objects.
        Output:
            None.
    """

    # Loop through the numbers in the array.
    for number in array:
        number_string = float_to_c_string(number)

        # Negative numbers automatically get a minus sign. Give a
        # Plus sign to positive numbers to be consistent in style.
        if number >= 0:
            number_string = "+" + number_string

        print(padding + number_string + suffix)

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
#       Routines for computing Remez polynomials.                              #
################################################################################
#   Author: Ryan Maguire                                                       #
#   Date:   January 8, 2023.                                                   #
################################################################################
"""

# Arrays.
import numpy

import matplotlib.pyplot as plt

# mpmath imported here.
import tmpld

# Polynomial evaluation.
from tmpld.poly.poly_eval import poly_eval

# Initial setup function.
from tmpld.remez.start_exchange import start_exchange

# Updates the samples in the Remez exchange.
from tmpld.remez.reset_samples import reset_samples

# Remez exchange function.
from tmpld.remez.perform_remez_exchange import perform_remez_exchange

# Function for updating points.
from tmpld.remez.select_points import select_points

# Computes the degree "deg" Remez MiniMax polynomial of "f" on [start, end]
def remez(func, deg, start, end, interactive = True):
    """
        Function:
            remez
        Purpose:
            Computes the Minimax polynomial of a function f on a given interval
            of a specified degree using the Remez exchange algorithm.
        Arguments:
            f (function):
                The function to be approximated.
            deg (int):
                The degree of the output Minimax polynomial.
            start (float):
                The left-most point of the interval f is approximated on.
            end (float):
                The right-most point of the interval f is approximated on.
        Output:
            coeffs (list):
                The coefficients of the Minimax polynomial in ascending order
                in terms of the degrees.
    """

    # Convert the inputs to mpmath objects if necessary.
    xarr, farr, x_vals, y_vals = start_exchange(func, deg, start, end)

    # Iteratively perform the Remez exchange algorithm until the error is good.
    while True:

        # Invert the coefficient matrix and solve for the polynomial.
        data = perform_remez_exchange(x_vals, y_vals)

        # Compute the error. If the bumps are the same magnitude, stop.
        yarr = numpy.abs(
            numpy.array(
                [
                    float(farr[k] - poly_eval(data, xarr[k]))
                    for k in range(len(xarr))
                ]
            )
        )

        # Plot the error. If the local extrema alternate and are of similar
        # magnitude, the algorithm is complete.
        if interactive:
            plt.plot(xarr, yarr)
            plt.show()

        # Stop the computation if this is good enough.
        if input(f"Max Err = {numpy.max(yarr)} | Stop? (y/n): ") == "y":
            return data

        # Reset the samples to the peaks and compute the function there.
        x_vals, y_vals = reset_samples(func, xarr, yarr)

        # If there were not enough samples in x_vals, add some.
        if len(x_vals) != deg + 2:
            for value in x_vals:
                tmpld.mpmath.nprint(value)

            print(
                f"Please Add {((deg + 2) - len(x_vals))} Missing Points."
                "Captured Points Printed Above."
            )

            select_points(func, x_vals, y_vals, xarr, yarr, deg)

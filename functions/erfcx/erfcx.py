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
"""

import tmpld
import tmpld.chebyshev
import tmpld.poly
import tmpld.pade
import tmpld.rat
import tmpld.remez

FOUR = tmpld.mpmath.mpf(4)
END = tmpld.mpmath.mpf(64)
NUMBER = tmpld.mpmath.mpf(128)
STEP = END / NUMBER

def forward(t_val):
    mpf_t = tmpld.mpmath.mpf(t_val)
    return FOUR / (FOUR + mpf_t)

def backward(t_val):
    mpf_t = tmpld.mpmath.mpf(t_val)
    return (FOUR - FOUR*mpf_t) / mpf_t

def erfcx(t_val):
    mpf_t = tmpld.mpmath.mpf(t_val)
    return tmpld.mpmath.exp(mpf_t*mpf_t) * tmpld.mpmath.erfc(mpf_t)

def cheb(t_val):
    return erfcx(backward(t_val))

def poly(coeffs, t_val):
    return tmpld.poly.poly_eval(coeffs, forward(t_val))

START = tmpld.mpmath.mpf(1)
LAST = forward(END)
INCREMENT = (START - LAST) / NUMBER
NEXT = START - INCREMENT

(P, Q, e) = tmpld.remez.rat_remez(cheb, 6, 0, NEXT, START)

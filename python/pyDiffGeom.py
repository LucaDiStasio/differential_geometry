# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2018 Université de Lorraine & Luleå tekniska universitet
Author: Luca Di Stasio <luca.distasio@gmail.com>
                       <luca.distasio@ingpec.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

=====================================================================================

DESCRIPTION

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution in Windows 7.

'''

import sys

def convertIndecesTensorToHelical(indeces,lengths):
    # indeces = [innermost ... outermost]
    # lengths = [innermost ... outermost]
    hindex = 0
    for i in range(len(indeces)-1,-1,-1):
        coeff = 1
        for j in range(i-1,-1,-1):
            coeff *= lengths[j]
        index += indeces[i]*coeff
    return hindex

def covariantBaseAtPoint(indeces,lengths,rmap,qmap):
    index = convertIndecesTensorToHelical(indeces,lengths)
    rs = rmap[index]
    qs = qmap[index]
    gs = []
    for q in qs:
        g = []
        for r in rs:
        gs.append(g)

    return gs

def main(argv):



if __name__ == "__main__":
    main(sys.argv[1:])

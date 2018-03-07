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
from ..finite_differences/python import computeWeights, computeDerivativeAtPoint

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

def buildStencilsIndeces(indeces,lengths,stencilSize):
    # finite differences are assumed to be centered, thus stencilSize must an odd number
    # if the central finite difference cannot be performed, an alternative is computed
    stencilIndeces = []
    deltaIndex = np.floor(0.5*stencilSize)
    for i,cartesianIndex in enumerate(indeces):
        if (cartesianIndex-deltaIndex)>-1 && (cartesianIndex+deltaIndex)<lengths[i]: #centered finite difference can be performed
            startIndex = cartesianIndex-deltaIndex
            endIndex = cartesianIndex+deltaIndex
        elif (cartesianIndex-deltaIndex)>-1 # got to be ajusted on the right side
            startIndex = (cartesianIndex-deltaIndex) - ((cartesianIndex+deltaIndex)-(lengths[i]-1))
            endIndex = lengths[i]-1
            if startIndex<0:
                raise ValueError('The specified stencil size is not compatible with the mesh along dimension ' + str(i+1) + '. Check your input.')
        elif (cartesianIndex+deltaIndex)<lengths[i] # got to be ajusted on the left side
            startIndex = 0
            endIndex = (cartesianIndex+deltaIndex) - (cartesianIndex-deltaIndex) #(cartesianIndex-deltaIndex)<0 in this case
            if endIndex>=lengths[i]:
                raise ValueError('The specified stencil size is not compatible with the mesh along dimension ' + str(i+1) + '. Check your input.')
        else:
            raise ValueError('The specified stencil size is not compatible with the mesh along dimension ' + str(i+1) + '. Check your input.')
        currentStencil = []
        tempCartesianIndeces = indeces
        for j in range(startIndex,endIndex+1):
            tempCartesianIndeces[i] = j
            currentStencil.append(convertIndecesTensorToHelical(tempCartesianIndeces,lengths))
        stencilIndeces.append(currentStencil)
    return stencilIndeces

def covariantBaseAtPoint(indeces,lengths,rmap,qmap,stencilSize):
    index = convertIndecesTensorToHelical(indeces,lengths)
    rs = rmap[index]
    qs = qmap[index]
    hStencils = buildStencilsIndeces(indeces,lengths,stencilSize)
    gs = []
    for q,q0 in enumerate(qs):
        stencilIndexSet = hStencils[q]
        xs = []
        for sIndex in stencilIndexSet:
            xs.append(qmap[sIndex][q])
        g = []
        for r in rs:
            fs = []
            for sIndex in stencilIndexSet:
                fs.append(rmap[sIndex][r])
            g.append(computeDerivativeAtPoint(1,q0,xs,fs))
        gs.append(g)
    return gs

def main(argv):



if __name__ == "__main__":
    main(sys.argv[1:])

# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def computecovariantbase3D(N=None,deltaq=None,lattice=None,firstdevneighbours=None,*args,**kwargs):
    varargin = computecovariantbase3D.varargin
    nargin = computecovariantbase3D.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: May 28th, 2014
#    Last update: July 8th, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    ##
    
    covariantbase=zeros(N,9)
    for i in arange(1,N).reshape(-1):
        for j in arange(1,3).reshape(-1):
            if 1 == firstdevneighbours[i,dot(4,(j - 1)) + 1]:
                covariantbase[i,dot(3,(j - 1)) + 1:dot(3,(j - 1)) + 3]=multiply(0.5,cat((lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],7] - lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],7]),(lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],8] - lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],8]),(lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],9] - lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],9]))) / deltaq[j]
            else:
                if 2 == firstdevneighbours[i,dot(4,(j - 1)) + 1]:
                    covariantbase[i,dot(3,(j - 1)) + 1:dot(3,(j - 1)) + 3]=cat((dot(- 1.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],7]) + dot(2,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],7]) - dot(0.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 4],7])),(dot(- 1.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],8]) + dot(2,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],8]) - dot(0.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 4],8])),(dot(- 1.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],9]) + dot(2,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],9]) - dot(0.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 4],9]))) / deltaq[j]
                else:
                    if 3 == firstdevneighbours[i,dot(4,(j - 1)) + 1]:
                        covariantbase[i,dot(3,(j - 1)) + 1:dot(3,(j - 1)) + 3]=cat((dot(1.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],7]) - dot(2,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],7]) + dot(0.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 4],7])),(dot(- 1.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],8]) + dot(2,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],8]) - dot(0.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 4],8])),(dot(- 1.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 2],9]) + dot(2,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 3],9]) - dot(0.5,lattice[firstdevneighbours[i,dot(4,(j - 1)) + 4],9]))) / deltaq[j]
    
    # covariantbase = [(geometricdata(:,8).*geometricdata(geometricdata(:,5),1)+geometricdata(:,9).*geometricdata(geometricdata(:,6),1)+geometricdata(:,10).*geometricdata(geometricdata(:,7),1))./geometricdata(:,4)...
#                  (geometricdata(:,8).*geometricdata(geometricdata(:,5),2)+geometricdata(:,9).*geometricdata(geometricdata(:,6),2)+geometricdata(:,10).*geometricdata(geometricdata(:,7),2))./geometricdata(:,4)...
#                  (geometricdata(:,8).*geometricdata(geometricdata(:,5),3)+geometricdata(:,9).*geometricdata(geometricdata(:,6),3)+geometricdata(:,10).*geometricdata(geometricdata(:,7),3))./geometricdata(:,4)...
#                  (geometricdata(:,15).*geometricdata(geometricdata(:,12),1)+geometricdata(:,16).*geometricdata(geometricdata(:,13),1)+geometricdata(:,17).*geometricdata(geometricdata(:,14),1))./geometricdata(:,11)...
#                  (geometricdata(:,15).*geometricdata(geometricdata(:,12),2)+geometricdata(:,16).*geometricdata(geometricdata(:,13),2)+geometricdata(:,17).*geometricdata(geometricdata(:,14),2))./geometricdata(:,11)...
#                  (geometricdata(:,15).*geometricdata(geometricdata(:,12),3)+geometricdata(:,16).*geometricdata(geometricdata(:,13),3)+geometricdata(:,17).*geometricdata(geometricdata(:,14),3))./geometricdata(:,11)...
#                  (geometricdata(:,22).*geometricdata(geometricdata(:,19),1)+geometricdata(:,23).*geometricdata(geometricdata(:,20),1)+geometricdata(:,24).*geometricdata(geometricdata(:,21),1))./geometricdata(:,18)...
#                  (geometricdata(:,22).*geometricdata(geometricdata(:,19),2)+geometricdata(:,23).*geometricdata(geometricdata(:,20),2)+geometricdata(:,24).*geometricdata(geometricdata(:,21),2))./geometricdata(:,18)...
#                  (geometricdata(:,22).*geometricdata(geometricdata(:,19),3)+geometricdata(:,23).*geometricdata(geometricdata(:,20),3)+geometricdata(:,24).*geometricdata(geometricdata(:,21),3))./geometricdata(:,18)];
    
    return covariantbase
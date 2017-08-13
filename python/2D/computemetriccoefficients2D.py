# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def computemetriccoefficients2D(covariantbase=None,*args,**kwargs):
    varargin = computemetriccoefficients2D.varargin
    nargin = computemetriccoefficients2D.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: July 11th, 2014
#    Last update: July 11th, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    ##
    
    g11=sum(multiply(covariantbase[:,1:2],covariantbase[:,1:2]),2)
    g22=sum(multiply(covariantbase[:,3:4],covariantbase[:,3:4]),2)
    g12=sum(multiply(covariantbase[:,1:2],covariantbase[:,3:4]),2)
    g=multiply(g11,g22) - multiply(g12,g12)
    sqrtg=sqrt(g)
    metriccoefficients=matlabarray(cat(g11,g22,g12))
    return metriccoefficients,g,sqrtg
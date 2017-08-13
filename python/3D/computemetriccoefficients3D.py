# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def computemetriccoefficients3D(covariantbase=None,*args,**kwargs):
    varargin = computemetriccoefficients3D.varargin
    nargin = computemetriccoefficients3D.nargin

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
    
    g11=sum(multiply(covariantbase[:,1:3],covariantbase[:,1:3]),2)
    g22=sum(multiply(covariantbase[:,4:6],covariantbase[:,4:6]),2)
    g33=sum(multiply(covariantbase[:,7:9],covariantbase[:,7:9]),2)
    g12=sum(multiply(covariantbase[:,1:3],covariantbase[:,4:6]),2)
    g13=sum(multiply(covariantbase[:,1:3],covariantbase[:,7:9]),2)
    g23=sum(multiply(covariantbase[:,4:6],covariantbase[:,7:9]),2)
    g=multiply(g11,(multiply(g22,g33) - g23 ** 2)) + multiply(g12,(multiply(g13,g23) - multiply(g12,g33))) + multiply(g13,(multiply(g12,g23) - multiply(g13,g22)))
    sqrtg=sqrt(g)
    metriccoefficients=matlabarray(cat(g11,g22,g33,g12,g13,g23))
    return metriccoefficients,g,sqrtg
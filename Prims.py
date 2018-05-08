#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 01:34:06 2001

@author: santavasquez
"""
from Weighted_Graph import *

def Prims(T):
    VG = G.vertex_set() 
    i=0    
    while T[0]!= VG: 
        i+=1    
        T = update_tree(G, T)
    total_cost = 0
    for e in T[1]:
        total_cost += cost(G, e)
    return(T, '  Total Cost = ', total_cost)
    
print(Prims(T))

#def tot_c(T):
#    VG = G.vertex_set() 
#    i=0    
#    while T[0]!= VG: 
#        i+=1    
#        T = update_tree(G, T)
#    ttotal_cost = 0
#    for e in T[1]:
#        ttotal_cost += cost(G, e)
#    return(ttotal_cost)
#print(tot_c(T))

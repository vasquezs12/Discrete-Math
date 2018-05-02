#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 12:27:48 2018

@author: santavasquez
"""

from Weighted_Graph import *

G = Weighted_Graph('example.txt')
G.draw_graph()

def cost(G,e):
    return G.edge_dict()[e]
        
print('The cost of is : ', cost(G, (0,1)))

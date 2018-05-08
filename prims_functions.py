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
        
#print('The cost of (3,4)is : ', cost(G, (3, 4)))

def tree_one(v):
    return ({v},[])

VT = {0}
ET = []
T = (VT, ET)

def incident_edges(G, T):
    temp_edges = []
    E = G.edge_set()
    for e in E:
        for v in T[0]:
            if v in e and e not in T[1]:
                temp_edges.append(e)
    return temp_edges


def valid_incident_edges(G, T):
        temp_edges = []
        possible_edges = incident_edges(G, T)
        for e in possible_edges: 
            if e[0] not in T[0] or e[1] not in T[0]:
             temp_edges.append(e)
        return temp_edges

#print('Valid_incident_edges T: ', valid_incident_edges(G, T))
    
    
def min_incident_edge(G, T):
    edges = incident_edges(G, T)
    min_edge = edges[0]
    for e in edges:
        if cost(G, e) < cost(G, min_edge):
            min_edge = e
    return min_edge
#print('Min_incident_edges T: ', min_incident_edge(G, T))

def update_tree(G, T):
   edges = incident_edges(G, T)
   min_edge = edges[0]
   for e in edges:
      if cost(G, e) < cost(G, min_edge):
           min_edge = e       
   new_edges = []
   new_edges.append(min_edge)

   for e in T[1]:
         new_edges.append(e)
   new_vertices = {min_edge[0], min_edge[1]}     
   return (new_vertices.union(T[0]), new_edges)
   

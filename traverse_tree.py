#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:24:14 2022

@author: parisbg
"""

binary_tree = {'A':['B','C'],
              'B':['D','E'],
              'C':['F','G'],
              'D':[],
              'E':[],
              'F':[],
              'G':[],
              
              }

visited = []
queue = []

def traverse_tree(visited,binary_tree,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        x = queue.pop(0)
        print (x, end = " ") 
        
        for i in binary_tree[x]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                
# Driver Code
traverse_tree(visited, binary_tree, 'A')
                
            
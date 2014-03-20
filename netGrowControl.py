#!/usr/bin/python
# -*- coding: UTF-8 -*-
import digraph
import matchings
import random
from scipy.stats import bernoulli

__author__ = 'Luis Úbeda (http://www.github.com/lubeme)'


def net_grow_control(n):

    #init
    G = digraph.DiGraph()
    G.add_nodes(range(1, n + 1))
    posibleEdges = {}
    keyAux = 0
    
    for node1 in xrange(1, n+1):
        for node2 in xrange(node1 + 1, n+1):
            posibleEdges[keyAux]=(node1, node2)
            keyAux += 1
            posibleEdges[keyAux]=(node2, node1)
            keyAux += 1
    totalEdges=keyAux       
    controlersPerNumEdges={} 
    
    for numEdges in xrange(1, totalEdges+1):
        edge = posibleEdges.pop(random.choice(posibleEdges.keys()))
        G.add_edge(edge[0],edge[1])
        match=matchings.matching(G)
        mSize=len(match)
        if mSize==n-1:
			for i in xrange(numEdges,totalEdges+1):
				controlersPerNumEdges[i]=1
			break
        controlersPerNumEdges[numEdges]=n-mSize
    return controlersPerNumEdges

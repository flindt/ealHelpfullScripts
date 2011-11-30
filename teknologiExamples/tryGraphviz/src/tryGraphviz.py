'''
Created on Nov 29, 2011

@author: flindt
'''

import pygraphviz 


graph = pygraphviz.AGraph(directed = True)
graph.add_edge("ISP1", "the internet", headport="s")
graph.add_edge("localPC1", "localRouter", taillabel="192.168.1.19",headlabel="192.168.1.1")
graph.add_edge("localRouter", "ISP1", headlabel="80.17.33.33",taillabel="80.17.33.1")


graph.draw("./try.svg", "svg", prog="dot")
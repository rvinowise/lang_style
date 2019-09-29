import pygraphml as gm
from pygraphml import GraphMLParser
from pygraphml import Graph

def open_file(file):
    parser = GraphMLParser()
    graph = parser.parse(file)
    #graph.show()
    return graph
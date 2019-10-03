from pygraphml import GraphMLParser

from lxml import etree

if (__name__ == "__main__"):
    gp = GraphMLParser()
    g = gp.parse("weather.graphml")
    node0 = g.get_node("in the middle","NodeLabel")
    group = node0.container_node[0]
    g.set_root(node0)

    nodes = g.BFS(direction="contained_nodes")
    for node in nodes:
        print(node.attr.get("NodeLabel"))

    node1 = g.get_node("n0","id")

    test = etree.tostring(g.xml, encoding=str)

    gp.write(g)


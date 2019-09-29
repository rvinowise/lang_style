import graph_helper as gh

if (__name__ == "__main__"):
    g = gh.open_file("weather.graphml")
    node0 = g.get_node("in the middle","NodeLabel")
    group = node0.container_node()
    g.set_root(node0)

    nodes = g.BFS(direction="contained_nodes")
    for node in nodes:
        print(node.attr.get("NodeLabel"))

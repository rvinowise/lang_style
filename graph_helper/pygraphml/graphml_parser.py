# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from lxml import etree

from . import Graph


class GraphMLParser:
    """
    """

    ns = {"_":"http://graphml.graphdrawing.org/xmlns",
        "java":"http://www.yworks.com/xml/yfiles-common/1.0/java",
        'sys':"http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0",
        'x':"http://www.yworks.com/xml/yfiles-common/markup/2.0",
        'xsi':"http://www.w3.org/2001/XMLSchema-instance",
        'y':"http://www.yworks.com/xml/graphml",
        'yed':"http://www.yworks.com/xml/yed/3" }

    def __init__(self):
        """
        """

    def write(self, graph, fname=None):

        doc = minidom.Document()

        root = doc.createElement('graphml')
        doc.appendChild(root)

        # Add attributs
        for a in graph.get_attributs():
            attr_node = doc.createElement('key')
            attr_node.setAttribute('id', a.name)
            attr_node.setAttribute('attr.name', a.name)
            attr_node.setAttribute('attr.type', a.type)
            root.appendChild(attr_node)

        graph_node = doc.createElement('graph')
        graph_node.setAttribute('id', graph.name)
        if graph.directed:
            graph_node.setAttribute('edgedefault', 'directed')
        else:
            graph_node.setAttribute('edgedefault', 'undirected')
        root.appendChild(graph_node)

        # Add nodes
        for n in graph.nodes():

            node = doc.createElement('node')
            node.setAttribute('id', n['label'])
            for a in n.attributes():
                if a != 'label':
                    data = doc.createElement('data')
                    data.setAttribute('key', a)
                    data.appendChild(doc.createTextNode(str(n[a])))
                    node.appendChild(data)
            graph_node.appendChild(node)

        # Add edges
        for e in graph.edges():

            edge = doc.createElement('edge')
            edge.setAttribute('source', e.node1['label'])
            edge.setAttribute('target', e.node2['label'])
            if e.directed() != graph.directed:
                edge.setAttribute('directed', 'true' if e.directed() else 'false')
            for a in e.attributes():
                if e != 'label':
                    data = doc.createElement('data')
                    data.setAttribute('key', a)
                    data.appendChild(doc.createTextNode(e[a]))
                    edge.appendChild(data)
            graph_node.appendChild(edge)

        if fname is not None:
            f = open(fname, 'w')
            f.write(doc.toprettyxml(indent='    '))
        else:
            return doc.toprettyxml(indent='', newl='')


    def parse(self, fname):

        with open( fname, 'r') as file:

            parser = etree.XMLParser(remove_blank_text=True)
            dom = etree.parse(fname, parser=parser)
            #xml_str = etree.tostring(elem,encoding=str)

            root = dom.getroot()
            src_graph = root.findall("_:graph",self.ns)[0]
            name = src_graph.attrib['id']

            dst_graph = Graph(name)

            # Get nodes
            dst_graph_node = dst_graph.add_node(id="graph")
            self.recursively_read_node(dst_graph, dst_graph_node, src_graph)

            # Get edges
            for edge in src_graph.findall("edge"):
                source = edge.attrib['source']
                dest = edge.attrib['target']

                # source/target attributes refer to IDs: http://graphml.graphdrawing.org/xmlns/1.1/graphml-structure.xsd
                e = dst_graph.add_edge_by_id(source, dest)


        return dst_graph

    ignored_nodes = ["ViewState"]

    def recursively_read_node(self, dst_graph, dst_node, src_node):
        try:
            if src_node.attrib["id"] == "n0::n13":
                test =True
            if src_node.attrib["id"] == "n1":
                test =True
        except:
            pass

        for child in src_node.getchildren():
            #if child.tag == "_:graph":
            if etree.QName(child).localname == "graph":
                self.recursively_read_node(dst_graph, dst_node, child)
            elif etree.QName(child).localname == "node":
                new_node = dst_graph.add_node(id=child.attrib['id'])
                new_node._container_node.append(dst_node)
                dst_node._contained_nodes.append(new_node)
                self.recursively_read_node(dst_graph, new_node, child)
            else:
                if etree.QName(child).localname not in self.ignored_nodes:
                    if (etree.QName(child).localname == "Realizers"):
                        which_to_use = int(child.attrib["active"])
                        self.recursively_read_attribs(dst_node, child.getchildren()[which_to_use])
                    else:
                        self.recursively_read_attribs(dst_node, child)
        if src_node.attrib:
            for attrName, attrValue in src_node.attrib.items():
                dst_node[attrName] = attrValue
        if hasattr(src_node, "text"):
            if str(src_node.text).strip():
                key = etree.QName(src_node).localname
                val = src_node.text
                dst_node[key] = src_node.text

        self.save_xml_to_node(dst_node, src_node)


    def recursively_read_attribs(self, dst_node, src_node):
        try:
            if src_node.getAttribute("id") == "n0::n13":
                test =True
        except:
            pass

        for child in src_node.getchildren():
            if etree.QName(child).localname == "node":
                raise NameError("child node outside of Graph node")

            if etree.QName(child).localname not in self.ignored_nodes:
                if (etree.QName(child).localname == "Realizers"):
                    which_to_use = int(child.attrib["active"])
                    self.recursively_read_attribs(dst_node, child.getchildren()[which_to_use])
                else:
                    self.recursively_read_attribs(dst_node, child)
        if src_node.attrib:
            for attrName, attrValue in src_node.attrib.items():
                dst_node[attrName] = attrValue
        if hasattr(src_node, "text"):
            if str(src_node.text).strip():
                key = etree.QName(src_node).localname
                val = src_node.text
                dst_node[key] = src_node.text


    def save_xml_to_node(self, dst_node, src_node):
        dst_node._xml_node = etree.tostring(src_node)


if __name__ == '__main__':

    parser = GraphMLParser()
    g = parser.parse('test.graphml')

    g.show(True)

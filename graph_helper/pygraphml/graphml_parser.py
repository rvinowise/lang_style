# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from lxml import etree

from . import Graph
from . import Node

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

    def write(self, graph, file_name='out.graphml'):

        dst_graph = graph.xml

        #for src_node in graph.nodes():
        self.recursive_write_node(dst_graph, graph)
        gst_graph_section = dst_graph.find("_:graph",self.ns)
        self.write_edges(gst_graph_section, graph)

        #child = etree.SubElement(root, "test_child")

        doc = etree.ElementTree(dst_graph)

        with open(file_name, 'wb') as file:
            file.write(etree.tostring(doc, pretty_print=True))


    def recursive_write_node(self, dst_node, src_node):
        grapn_section = dst_node.find("_:graph",self.ns)
        assert (grapn_section!=None) == (len(src_node.contained_nodes())>0), '"graph" section is needed if the node has children'

        for child in src_node.contained_nodes():
            grapn_section.append(child.xml)
            self.recursive_write_node(child.xml, child)

    def write_edges(self, gst_graph_section, graph):
        for edge in graph.edges():
            gst_graph_section.append(edge.xml)


    def parse(self, fname):

        with open( fname, 'r') as file:

            parser = etree.XMLParser(remove_blank_text=True)
            dom = etree.parse(fname, parser=parser)
            #xml_str = etree.tostring(elem,encoding=str)

            root = dom.getroot()
            #src_envelope = root.find("_:graphml",self.ns)
            #src_envelope.remove(src_envelope.find())
            src_graph = root.find("_:graph",self.ns)
            name = src_graph.attrib['id']

            dst_graph = Graph(name)

            # Get nodes
            #dst_graph_node = dst_graph.add_node(id="doc")
            #for high_level_node in src_graph.findall("_:node",self.ns):
            self.recursively_import_node(dst_graph, dst_graph, src_graph)

            # Get edges
            for src_edge in src_graph.findall("_:edge",self.ns):
                self.import_edge(dst_graph, src_edge)

            dst_graph.xml = root

        return dst_graph

    ignored_nodes = ["ViewState"]

    def recursively_import_node(self, graph, dst_node, src_node):
        try:
            if src_node.attrib["id"] == "n0::n12":
                test =True
        except:
            pass

        for child in src_node.getchildren():
            #if child.tag == "_:graph":
            if etree.QName(child).localname == "graph":
                self.recursively_import_node(graph, dst_node, child)
            elif etree.QName(child).localname == "node":
                new_node = graph.add_node(child.attrib['id'])
                new_node.container_node.append(dst_node)
                dst_node._contained_nodes.append(new_node)
                self.recursively_import_node(graph, new_node, child)
                self.save_xml_to_node(new_node, child)
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
        dst_node.xml = src_node
        parent = src_node.getparent()
        test0 = etree.tostring(parent, pretty_print=True, encoding=str)
        src_node.getparent().remove(src_node)
        test1 = etree.tostring(parent, pretty_print=True, encoding=str)
        pass

    def import_edge(self, dst_graph, src_edge):
        source = src_edge.attrib['source']
        dest = src_edge.attrib['target']
        edge = dst_graph.add_edge_by_id(source, dest)
        edge.xml = src_edge

        #test0 = etree.tostring(src_edge.getparent(), pretty_print=True, encoding=str)
        src_edge.getparent().remove(src_edge)
        #test1 = etree.tostring(src_edge.getparent(), pretty_print=True, encoding=str)


if __name__ == '__main__':

    parser = GraphMLParser()
    g = parser.parse('test.graphml')

    g.show(True)

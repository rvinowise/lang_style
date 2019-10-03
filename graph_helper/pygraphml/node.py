# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from __future__ import print_function


from . import Item

class Node(Item):
    """
    """

    def __init__(self, id=None):
        """
        """

        super(Node, self).__init__(id)

        self._edges = []
        self._contained_nodes = []
        self.container_node = []

        xml = None

    def edges(self, ):
        """
        """

        return self._edges


    def next_nodes(self):
        """
        """

        next_nodes = []
        for e in self._edges:
            if e.parent() == self:
                next_nodes.append(e.child())

        return next_nodes

    def prev_nodes(self):
        """
        """

        prev_nodes = []
        for e in self._edges:
            if e.child() == self:
                prev_nodes.append(e.parent())

        return prev_nodes


    def contained_nodes(self):
        return self._contained_nodes

    #def container_node(self):
        #return self.container_node
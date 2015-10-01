#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, name=""):
        self.name = name
        self.contains = []
        self.indent = None

    def append(self, content):
        self.contains.append(content)

    def render(self, file_out, indent=""):
        file_out.write("<html>\n")
        for values in self.contains:
            file_out.write(values)
        file_out.write("\n</html>")

#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.

# 4 Spaces used to make all indents easier
INDENT = "    "


class Element(object):

    def __init__(self, name="", indent=""):
        self.name = name
        self.contains = []
        self.indent = indent

    def append(self, content):
        self.contains.append(content)

    def render(self, file_out):
        file_out.write("{}<{}>\n".format(self.indent, self.name))
        for values in self.contains:
            # If the content is another element render it
            if(isinstance(values, Element)):
                values.render(file_out)
            else:  # Render out its contents
                file_out.write(self.indent + INDENT + values + "\n")
        file_out.write("{}</{}>\n".format(self.indent, self.name))


class Html(Element):

    def __init__(self):
        Element.__init__(self, "html")


class Head(Element):

    def __init__(self):
        Element.__init__(self, "head", INDENT)


class Body(Element):

    def __init__(self):
        Element.__init__(self, "body", INDENT)


class OneLineTag(Element):

    def render(self, file_out):
        file_out.write("{s}<{n}>{c}</{n}>\n".format(s=self.indent, n=self.name,
                                                    c=self.contains[0]))


class Title(OneLineTag):

    def __init__(self, content):
        OneLineTag.__init__(self, "title", INDENT * 2)
        self.contains.append(content)


class P(Element):

    def __init__(self, content):
        Element.__init__(self, "p", INDENT * 2)
        self.append(content)

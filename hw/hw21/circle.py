#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):

    def __init__(self, radius):
        """
        Initialize a circle with a given radius
        """
        self.radius = radius
        self._D = radius * 2
        self._area = math.pi * radius ** 2

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __add__(self, c):
        """Returns a new circle with a radius the sum of the radii of self and c
        """
        rad1 = self.radius
        rad2 = c.radius
        return Circle(rad1 + rad2)

    def _getd(self):
        return self._D

    def _setd(self, val):
        self._D = val
        self.radius = val / 2
        self._area = math.pi * self.radius ** 2
    diameter = property(_getd, _setd, doc="The diameter of a circle")

    def _geta(self):
        return self._area
    area = property(_geta, doc="The area of a circle")

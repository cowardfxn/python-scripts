#!/usr/bin/python3
# encoding: utf-8

"""
a laundary list of special methods
collection of operation overloading

"""

from array import array
import math, traceback

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __iter__(self):
        return (e for e in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self): 
        return bool(abs(self))  # 应用上面实装的__abs__方法

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec=""):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            out_fmt = "<{}, {}>"
        else:
            coords = self
            out_fmt = "({}, {})"
        components = (format(c, format_spec) for c in coords)
        return out_fmt.format(*components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

"""
A 2-dimensional vector class
    >>> v1 = Vector2d(3, 4)
    >>> print(v1.x, v1.y)
    3.0 4.0
    >>> x, y = v1
    >>> x, y
    (3.0, 4.0)
    >>> v1
    Vector2d(3.0, 4.0)
    >>> v1_clone = eval(repr(v1))
    >>> v1 == v1_clone
    True
    >>> print(v1)
    (3.0, 4.0)
    >>> octets = bytes(v1)
    >>> octets
    b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x08@\\x00\\x00\\x00\\x00\\x00\\x00\\x10@'
    >>> abs(v1)
    5.0
    >>> bool(v1), bool(Vector2d(0, 0))
    (True, False)
Test of ``.frombytes()`` class method:
    >>> v1_clone = Vector2d.frombytes(bytes(v1))
    >>> v1_clone
    Vector2d(3.0, 4.0)
    >>> v1 == v1_clone
True
Tests of ``format()`` with Cartesian coordinates:
    >>> format(v1)
    '(3.0, 4.0)'
    >>> format(v1, '.2f')
    '(3.00, 4.00)'
    >>> format(v1, '.3e')
    '(3.000e+00, 4.000e+00)'
Tests of the ``angle`` method::
    >>> Vector2d(0, 0).angle()
    0.0
    >>> Vector2d(1, 0).angle()
    0.0
    >>> epsilon = 10**-8
    >>> abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
    True
    >>> abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon
    True
Tests of ``format()`` with polar coordinates:
    >>> format(Vector2d(1, 1), 'p')  # doctest:+ELLIPSIS
    '<1.414213..., 0.785398...>'
    >>> format(Vector2d(1, 1), '.3ep')
    '<1.414e+00, 7.854e-01>'
    >>> format(Vector2d(1, 1), '0.5fp')
    '<1.41421, 0.78540>'
Tests of `x` and `y` read-only properties:
    >>> v1.x, v1.y
    (3.0, 4.0)
    >>> v1.x = 123
    Traceback (most recent call last):
      ...
    AttributeError: can't set attribute
Tests of hashing:
    >>> v1 = Vector2d(3, 4)
    >>> v2 = Vector2d(3.1, 4.2)
    >>> hash(v1), hash(v2)
    (7, 384307168202284039)
    >>> len(set([v1, v2]))
    2
"""

if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v1_clone = Vector2d.frombytes(bytes(v1))
    print(v1_clone)
    assert v1 == v1_clone

    assert format(v1) == '(3.0, 4.0)'
    assert format(v1, '.2f') == '(3.00, 4.00)'
    assert format(v1, '.3e') == '(3.000e+00, 4.000e+00)'

    assert Vector2d(0, 0).angle() == 0.0
    assert Vector2d(1, 0).angle() == 0.0
    epsilon = 10**-8
    assert abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon
    assert abs(Vector2d(1, 1).angle() - math.pi/4) < epsilon

    print(format(Vector2d(1, 1), 'p'))  # doctest:+ELLIPSIS
    print(format(Vector2d(1, 1), '.3ep'))
    print(format(Vector2d(1, 1), '0.5fp'))

    print(v1.x, v1.y)
    try:
        v1.x = 123
    except Exception as e:
        print(traceback.format_exc())

    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    assert hash(v1), hash(v2) == (7, 384307168202284039)
    print(set([v1, v2]))

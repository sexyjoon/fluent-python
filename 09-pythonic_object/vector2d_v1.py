import math


import vector2d_v0


class Vector2dV1(vector2d_v0.Vector2d):
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_format = '<{}, {}>'
        else:
            coords = self
            outer_format = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_format.format(*components)


if __name__ == '__main__':
    v1 = Vector2dV1(3, 4)
    print(format(v1))
    print(format(v1, '.2f'))
    print(format(v1, '.3e'))

    print(format(Vector2dV1(1, 1), 'p'))
    print(format(Vector2dV1(1, 1), '.3ep'))
    print(format(Vector2dV1(1, 1), '.5fp'))
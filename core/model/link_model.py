import numpy as np

from .transformations import (
    rotation_around_x,
    rotation_around_y,
    rotation_around_z,
    translation_along_z,
)


class Link:

    __rotation_functions = {
        "x": rotation_around_x,
        "y": rotation_around_y,
        "z": rotation_around_z,
    }

    def __init__(self, length, default_axis, rotation=0):
        self.parent = None
        self.child = None
        self._length = length
        self._rotation = rotation

        if default_axis not in self.__rotation_functions:
            raise ValueError("axis must be equal to 'x', 'y', or 'z'")
        self._axis = default_axis

        self._base = np.identity(4)
        self._T = translation_along_z(self._length)
        self._R = self.__rotation_functions[self._axis](self._rotation)
        self.set_pose(rotation)

    @property
    def length(self):
        return self._length

    @property
    def rotation(self):
        return self._rotation

    @property
    def origin(self):
        if not self.parent:
            return np.array([0, 0, 0])
        return self.parent.end

    @property
    def end(self):
        return self._base[:-1, 3]

    @property
    def base(self):
        b = self._base
        return b[:-1, 0], b[:-1, 1], b[:-1, 2]

    def set_parent(self, parent):
        self.parent = parent
        parent.child = self
        self.set_pose()

    def set_pose(self, rotation=None, propagate=True):
        self._base = np.identity(4)

        if rotation:
            self._rotation = rotation
            self._R = self.__rotation_functions[self._axis](self._rotation)

        self._base = np.matmul(self._T, self._base)
        self._base = np.matmul(self._R, self._base)
        if self.parent:
            self._base = np.matmul(self.parent._base, self._base)

        if propagate:
            child = self.child
            while child:
                child.set_pose(propagate=False)
                child = child.child

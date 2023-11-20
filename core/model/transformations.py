import numpy as np


def rotation_around_x(angle):
    R = np.array(
        [
            [1, 0, 0, 0],
            [0, np.cos(angle), -np.sin(angle), 0],
            [0, np.sin(angle), np.cos(angle), 0],
            [0, 0, 0, 1],
        ]
    )
    return R


def rotation_around_z(angle):
    R = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0, 0],
            [np.sin(angle), np.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
    return R


def rotation_around_y(angle):
    R = np.array(
        [
            [np.cos(angle), 0, np.sin(angle), 0],
            [0, 1, 0, 0],
            [-np.sin(angle), 0, np.cos(angle), 0],
            [0, 0, 0, 1],
        ]
    )
    return R


def translation_along_x(distance):
    T = np.array([[1, 0, 0, distance], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    return T


def translation_along_y(distance):
    T = np.array([[1, 0, 0, 0], [0, 1, 0, distance], [0, 0, 1, 0], [0, 0, 0, 1]])
    return T


def translation_along_z(distance):
    T = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, distance], [0, 0, 0, 1]])
    return T

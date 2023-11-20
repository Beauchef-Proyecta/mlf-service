import numpy as np

from .robot_model import GenericRobot


class MK2Model:

    _build_instructions = {
        "link_0": {"length": 55, "axis": "z", "rotation": 0, "parent": None},
        "link_1": {"length": 39, "axis": "z", "rotation": 0, "parent": "link_0"},
        "link_2": {"length": 135, "axis": "y", "rotation": 0, "parent": "link_1"},
        "link_3": {
            "length": 147,
            "axis": "y",
            "rotation": 0 * np.pi / 180,
            "parent": "link_2",
        },
        "link_4": {"length": 66, "axis": "y", "rotation": 0, "parent": "link_3"},
    }

    HOME_Q0 = 0
    HOME_Q1 = 0
    HOME_Q2 = 90
    HOME_Q3 = 120

    def __init__(self):
        self.model = GenericRobot(self._build_instructions).assemble()

    def home(self):
        self.set_pose(self.HOME_Q0, self.HOME_Q1, self.HOME_Q2)  # set to home positions

    def set_pose(self, q0, q1, q2):
        q0 = q0 * np.pi / 180
        q1 = q1 * np.pi / 180
        q2 = q2 * np.pi / 180

        Q = dict()
        Q["link_0"] = 0
        Q["link_1"] = q0
        Q["link_2"] = q1
        Q["link_3"] = q2
        Q["link_4"] = np.pi / 2 - q1 - q2

        self.model.set_pose(Q)

    def get_pose(self):
        return self.model.get_pose

    def inverse_kinematics(self, xyz: tuple):
        # Aux variables for code readibility
        x, y, z = xyz
        q = [0, 0, 0]
        l = []
        for link in self._build_instructions.values():
            l.append(link["length"])

        # Calculations
        q[0] = np.arctan(y / x)
        
        q[2] = np.arccos(
            (
                (np.sqrt(x ** 2 + y ** 2) - l[4]) ** 2
                + (z - l[1] - l[0]) ** 2
                + -l[2] ** 2
                + -l[3] ** 2
            )
            / (2 * l[2] * l[3])
        )
        
        q[1] = (
            np.pi / 2
            + -np.arctan((z - l[1] - l[0]) / (np.sqrt(x ** 2 + y ** 2) - l[4]))
            + -np.arctan((l[3] * np.sin(q[2])) / (l[2] + l[3] * np.cos(q[2])))
        )

        # Formatting
        q0 = np.round(q[0] * 180 / np.pi, 0)
        q1 = np.round(q[1] * 180 / np.pi, 0)
        q2 = np.round(q[2] * 180 / np.pi, 0)
        return [q0, q1, q2]

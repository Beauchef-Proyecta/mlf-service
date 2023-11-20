from .link_model import Link


class GenericRobot:
    """A robot is a tree"""

    def __init__(self, build_instructions: dict):
        self.links = dict()
        self.roots = []
        self.build_instructions = build_instructions

    def assemble(self):
        # This implementation will throw an Error when trying to build a closed-loop :)
        for name, param in self.build_instructions.items():
            link = Link(param["length"], param["axis"], param["rotation"])
            self.links[name] = link
            if param["parent"]:
                link.set_parent(self.links[param["parent"]])
            else:
                self.roots.append(link)

        return self

    @property
    def get_pose(self):
        return {name: (l.origin, l.end) for name, l in self.links.items()}

    def set_pose(self, angles: dict):
        for name, angle in angles.items():
            self.links[name].set_pose(angle, propagate=False)

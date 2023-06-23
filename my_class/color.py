class Color:
    def __init__(self, rgb, name):
        self._rgb = rgb
        self._name = name

    @property
    def name(self):
        """new doc"""
        return self._name

    @name.setter
    def name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f"Invalid name {name!r}")

    @property
    def rgb(self):
        return self._rgb

    @rgb.setter
    def rgb(self, rgb):
        self._rgb = rgb

    @name.deleter
    def name(self):
        print("Deleting...")
        del self._name


c = Color(0x45548, "blue")
c.name = "red"
print(c.name)
print(c.rgb)
del c.name

class Color:
    def __init__(self, rgb, name):
        self._rgb = rgb
        self._name = name

    def set_name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f"Invalid name {name!r}")
    def get_name(self):
        return self._name

    def set_rgb(self, rgb):
        self._rgb = rgb

    def get_rgb(self):
        return self._rgb


c1 = Color(0x6783F5, "light blue")
print(c1.get_name())
c1.set_rgb(0x6783F6)
c1.set_name("blue")
print(c1.get_rgb())

print("*"*40)

c2 = Color(0x6784F5, "light red")
print(c2.get_name())
c2.set_rgb(0x6763F6)
c2.set_name("red")
print(c2.get_rgb())
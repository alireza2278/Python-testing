class Color:
    def __init__(self, rgb, name):
        pass
        self.rgb = rgb
        self.name = name

    def _set_name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f"Invalid name {name!r}")

    def _get_name(self):
        return self._name

    def _set_rgb(self, rgb):
        self._rgb = rgb

    def _get_rgb(self):
        return self._rgb

    def _del_name(self):
        print("Deleting...")
        del self._name
    name = property()
    #name = property(_get_name, _set_name, _del_name, "new doc")


c = Color(0x45548, "blou")
c.name = "red"
print(c.name)
help(c)


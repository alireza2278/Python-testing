class Shape:
    def __init__(self, **kwargs):
        self.area = None
        self.environment = None
        for key, value in kwargs.items():
            setattr(self, key, value)
    def Calculate_area(self):
        pass

    def Calculate_environment(self):
        pass
    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value>0:
                info += f"{key}:{value:.2f}\n"
            print(info)
    def __str__(self):
        return self.__class__.__name__

class
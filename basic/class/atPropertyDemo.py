class Swan:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height

    @area.setter
    def widthSetter(self, width):
        self._width = width

    @area.setter
    def heightSetter(self, height):
        self._height = height

    @area.getter
    def heightGetter(self):
        return self._height

    @area.deleter
    def heightDeleter(self):
        del self._height

swan = Swan(4, 6)
print(swan.area)

swan.widthSetter = 6
swan.heightSetter = 102

print(swan.area)
swan.heightDeleter
print(swan.heightGetter)
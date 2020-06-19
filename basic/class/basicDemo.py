class Geese:
    '''大鳄'''
    
    # class property
    classProperty = "classProperty"

    # protected property
    _classProperty = "protected _classProperty"

    # private property
    __classProperty = "private __classProperty"

    def __init__(self, arg01):
        # instance property
        self.instanceProperty = arg01
        print(arg01)

    def fly(self, state = "default 0"):
        return "state: %s " %state
    

geese = Geese("init")
#print(geese.fly(), geese.fly("1"),Geese.fly("2"))

#print(Geese.classProperty, geese.classProperty)
#print(geese.instanceProperty)
#geese.classProperty = "change"
#print(Geese.classProperty, geese.classProperty)

#print(Geese._classProperty, geese._classProperty)

# AttributeError: type object 'Geese' has no attribute '__classProperty'
#print(Geese.__classProperty, geese.__classProperty)

print(Geese._Geese__classProperty, geese._Geese__classProperty)


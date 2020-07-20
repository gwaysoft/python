import sys
# abstract path
# sys.path.append("D:/project/python/basic/module/custom/createModule")
sys.path.append("./createModule")

import createModuleDemo as mo, os
from createModuleDemo01 import add as a
from createModuleDemo02 import *

# import default path
print(sys.path)
print(mo.add(3, 4.555))

# print(a(30, 4))
# print(add(34, 4))
# # show method
# print(dir())
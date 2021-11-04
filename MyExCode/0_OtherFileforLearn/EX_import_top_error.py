import os
import sys


# dir_name =os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

dir_name = __file__
for i in range(5):
    dir_name = os.path.dirname(dir_name)
print(dir_name)

sys.path.append(os.path.join(dir_name))

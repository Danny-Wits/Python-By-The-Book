# Importing Modules with `from`
# the from keyword is used to import specific components
# (functions, classes, or variables) directly from a module.
# ! Syntax: from module_name import function_name, class_name, variable_name,...

from math import pi as MY_PI
from math import pi

short_pi = round(pi, 2)
print(short_pi)

# using alias name


print(MY_PI)

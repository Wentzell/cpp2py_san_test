# Generated automatically using the command :
# c++2py mytest.hpp -p --members_read_only -m mytest -o mytest
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "mytest", doc = "", app_name = "mytest")

# Imports

# Add here all includes
module.add_include("mytest.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
""")
module.add_function ("int add (int i, int j)", doc = """""")

module.add_function ("int segfault (int idx)", doc = """""")

module.generate_code()
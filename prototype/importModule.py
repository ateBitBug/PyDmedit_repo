# importing a program in dir1/dir2/.../dir#/<filename>.py
# must include "__init__.py"
#   dir1/dir2/.../dir$/__init__.py

# from dir1.dir2...dir# import <filename>
# from modules1.modules2.modules3 import h
#               or
# import dir1.dir2...dir#.<filename> as <handle>
# import modules1.modules2.modules3.h as mh

# dynamically importing "h.py"
# dynamically importing "w.py"
# h = importlib.import_module("modules1.h")
# w = importlib.import_module("modules1.w")
# h.hello()
# w.world()

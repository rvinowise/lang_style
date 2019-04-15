import ctypes
import os
#os.chdir(r"D:\prj\lang_style\envelope")
#liblang = ctypes.WinDLL("liblang_style.dll")
#liblang = ctypes.WinDLL("D:/prj/lang_style/envelope/tests/liblang_style.dll")
#liblang = ctypes.WinDLL(r"D:\prj\lang_style\envelope\tests\liblang_style.dll")
#liblang = ctypes.WinDLL("D\\prj\\lang_style\\envelope\\tests\\liblang_style.dll")

from pathlib import Path
import sys

# /whole_project/ENVELOPE/test/this_module
envelope_dir = str(Path(__file__).absolute().parent.parent)
sys.path.append(envelope_dir)

from lang_style.collocation_checker import Collocation_checker


if (__name__ == "__main__"):
    checker = Collocation_checker()
    print(repr(checker._instance))
    checker.set_text("bla bla")
    res = checker.get_result()
    print(res)
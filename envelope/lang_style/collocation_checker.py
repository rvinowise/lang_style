import ctypes

liblang = ctypes.CDLL("/home/rvi/prj/nlp/envelope/lang_style/liblang_style.so")


class Collocation_checker:
    def __init__(self):
        self._instance = liblang.new_checker()

    def set_text(self, text):
        c_text = ctypes.c_wchar_p(text)
        liblang.set_text(self._instance, c_text)

    def get_result(self):
        res = liblang.get_result(self._instance)
        return res

    def __del__(self):
        liblang.delete_checker(self._instance)

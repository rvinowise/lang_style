import ctypes
#liblang = ctypes.CDLL("/home/rvi/prj/nlp/envelope/lang_style/liblang_style.so")


def init_external_library():
    liblang: ctypes.CDLL = ctypes.CDLL("liblang_style.dll")
    # Collocations_checker* new_checker();
    liblang.new_checker.restype = ctypes.POINTER(ctypes.c_void_p)
    return liblang

#liblang = init_external_library()
liblang = None

class Collocation_checker:
    @staticmethod
    def init_external_library():
        init_external_library()

    def __init__(self):
        if (liblang == None):
            try:
                self.init_external_library()
                cat
        self._instance = liblang.new_checker()
        print("python: instance of checker = "+repr(self._instance))

    def set_text(self, text):
        print("encoded: "+repr(text.encode('utf-8')))
        #c_text = ctypes.c_char_p(text.encode('utf-8'))
        c_text = ctypes.create_string_buffer(text.encode('utf-8'))
        liblang.set_text(self._instance, c_text)

    def get_result(self):
        res = liblang.get_result(self._instance)
        return res

    def __del__(self):
        #liblang.delete_checker(self._instance)
        pass

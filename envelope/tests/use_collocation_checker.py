from lang_style.collocation_checker import Collocation_checker


if (__name__ == "__main__"):
    print("testing")
    checker = Collocation_checker()
    checker.set_text("bla bla")
    res = checker.get_result()
    print("res="+res)
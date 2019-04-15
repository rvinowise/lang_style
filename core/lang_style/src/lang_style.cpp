#include "lang_style.h"

#include "Collocations_checker/Collocations_checker.h"


using namespace lang_style_check;



Collocations_checker* new_checker() {
    Collocations_checker* checker = new Collocations_checker();
    return checker;
}

void set_text(Collocations_checker* checker, const char* text) {
    std::string string{text};
    checker->set_text(string);
}

int get_result(Collocations_checker* checker) {
    checker->process();
    return 10;//checker->get_result();
}

void delete_checker(Collocations_checker* checker) {
    delete checker;
}

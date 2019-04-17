/* entry-level file of the library, provides its interface
 */

#include <boost/config/user.hpp>

#include "lang_style.h"
#include <iostream>

#include "Collocations_checker/Collocations_checker.h"
#include "logging/init_logging.hpp"

using namespace boost::log;


void init_library() {
    LOG(trace) << "init_library";
}
void deinit_library() {

}

#ifdef __GNUG__
// automaticly invoked
void __attribute__((constructor)) init() {
    init_library();
}
void __attribute__((destructor)) deinit() {
    deinit_library();
}
#elif
// user has to invoke those on his own
void init() {
    init_library();
}
void deinit() {
    init_library();
}
#endif


namespace lang_style_check {

Collocations_checker* new_checker() {
    Collocations_checker* checker = new Collocations_checker();
    std::cout<<"new_checker from C++ address =" << checker<<"\n";
    return checker;
}

void set_text(Collocations_checker* checker, const char* text) {
    std::cout<<"set_text from C++, checker address = "<<checker<<"\n";
    std::flush(std::cout);

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

}

#include <iostream>

#include <boost/log/trivial.hpp>

// test framework
//#include "gtest/gtest.h"
//#include "gmock/gmock.h"

//#define CATCH_CONFIG_MAIN
#include "catch2/catch.hpp"

// tested modules
#include "lang_style.h"
#include "Collocations_checker/Collocations_checker.h"

using namespace lang_style_check;
using namespace boost::log;
int main(int, char**) {
    BOOST_LOG_TRIVIAL(trace) << "A trace severity message";
    Collocations_checker collocations_checker{};

    //collocations_checker.set_text("bla bla bla");
    set_text(&collocations_checker, "lol lol lol");
    collocations_checker.process();
    auto corrections = collocations_checker.get_result();
    return 0;
}

/*TEST_CASE("Collocation_checker worked" ) {
    Collocations_checker collocations_checker{};
    //collocations_checker.set_text("bla bla bla");
    set_text(&collocations_checker, "lol lol lol");
    collocations_checker.process();
    auto corrections = collocations_checker.get_result();
    std::cout << "test\n";
}*/

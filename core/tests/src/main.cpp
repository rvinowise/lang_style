#include <iostream>

// test framework
//#include "gtest/gtest.h"
//#include "gmock/gmock.h"

#define CATCH_CONFIG_MAIN
#include "catch2/catch.hpp"

// tested modules
#include "lang_style.h"
#include "Collocations_checker/Collocations_checker.h"

using namespace lang_style_check;


TEST_CASE("Collocation_checker worked" ) {
    Collocations_checker collocations_checker{};
    collocations_checker.set_text("bla bla bla");
    collocations_checker.process();
    auto corrections = collocations_checker.get_result();
}
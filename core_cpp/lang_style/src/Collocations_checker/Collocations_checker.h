#pragma once

#include <string>

#include "Corrections/Corrections.h"

namespace lang_style_check {

class Corrections;

class Collocations_checker
{
public:
    Collocations_checker();
    void set_text(std::string in_text) {
        this->text = in_text;
    }
    int process();
    Corrections get_result();
private:
    std::string text;
};


}

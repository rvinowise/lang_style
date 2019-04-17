#pragma once
#include <vector>

#include "Word_choice/Word_choice.h"

namespace lang_style_check {

struct Corrections
{
    Corrections();

    std::vector<Word_choice> word_choices;
};


}

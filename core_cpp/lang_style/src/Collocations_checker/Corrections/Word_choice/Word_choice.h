#pragma once

#include <vector>

#include "Word/Word.h"

namespace lang_style_check {

struct Word_choice
{
public:
    Word_choice(const Word given_word):
        given_word{given_word}
    {};

    std::vector<Word> better_choices;
private:
    Word given_word;

};


}

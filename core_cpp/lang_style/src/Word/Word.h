#pragma once

#include <string>

namespace lang_style_check {

class Word: public std::string
{
public:
    Word();
    Word(const char* data):
        std::string(data)
    {};
    Word(const Word& other):// = default;
        std::string{other}
    {}
};

}

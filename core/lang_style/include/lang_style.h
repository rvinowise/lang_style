#pragma once

namespace lang_style_check {
    class Collocations_checker;
}

extern "C" lang_style_check::Collocations_checker* new_checker();

extern "C" void set_text(const char* text);

extern "C" int get_result();

extern "C" void delete_checker(lang_style_check::Collocations_checker*);

#pragma once

namespace lang_style_check {
    class Collocations_checker;
}

extern "C" lang_style_check::Collocations_checker* new_checker();

extern "C" void set_text(lang_style_check::Collocations_checker*, const char* text);

extern "C" int get_result(lang_style_check::Collocations_checker*);

extern "C" void delete_checker(lang_style_check::Collocations_checker*);

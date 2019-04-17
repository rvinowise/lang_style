#pragma once


namespace lang_style_check {

class Collocations_checker;

extern "C" {

void init();
void deinit();


Collocations_checker* new_checker();

void set_text(Collocations_checker*, const char* text);

int get_result(Collocations_checker*);

void delete_checker(Collocations_checker*);


}
}

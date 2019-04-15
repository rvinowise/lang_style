cmake_minimum_required(VERSION 3.6)

project(lang_style)
add_library(${PROJECT_NAME} SHARED src/lang_style.cpp
    src/Collocations_checker/Collocations_checker.cpp
    src/Collocations_checker/Corrections/Corrections.cpp
    src/Collocations_checker/Corrections/Word_choice/Word_choice.cpp
    src/Word/Word.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE ${PROJECT_SOURCE_DIR}/src)
target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR}/include)





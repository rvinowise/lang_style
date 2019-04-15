cmake_minimum_required(VERSION 3.6)

project(testing)

add_executable(testing src/main.cpp)

target_link_libraries(${PROJECT_NAME} LINK_PUBLIC lang_style)
target_include_directories(${PROJECT_NAME} PRIVATE ${PROJECT_SOURCE_DIR}/src)

#the tested internals (not exposed to a real user)
set(TESTED_INTERNALS_DIR ${PROJECT_SOURCE_DIR}/../lang_style/src)
target_include_directories(${PROJECT_NAME} PRIVATE ${TESTED_INTERNALS_DIR})

#param
set(CATCH_INCLUDE_DIR D:/proger/test/catch2/single_include)
target_include_directories(${PROJECT_NAME} PRIVATE ${CATCH_INCLUDE_DIR})

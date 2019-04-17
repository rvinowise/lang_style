cmake_minimum_required(VERSION 3.6)

project(lang_style)
add_library(${PROJECT_NAME} STATIC src/lang_style.cpp
    src/Collocations_checker/Collocations_checker.cpp
    src/Collocations_checker/Corrections/Corrections.cpp
    src/Collocations_checker/Corrections/Word_choice/Word_choice.cpp
    src/Word/Word.cpp
    src/logging/init_logging.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE ${PROJECT_SOURCE_DIR}/src)
target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR}/include)




set(Boost_USE_STATIC_LIBS ON)
find_package(Boost 1.70 COMPONENTS log REQUIRED)
if (Boost_FOUND)
    target_include_directories(${PROJECT_NAME} PRIVATE ${Boost_INCLUDE_DIR})
    target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES})
endif()



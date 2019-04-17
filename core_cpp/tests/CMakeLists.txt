cmake_minimum_required(VERSION 3.6)

project(tests)

add_executable(${PROJECT_NAME} src/main.cpp)

target_link_libraries(${PROJECT_NAME} LINK_PUBLIC lang_style)
target_include_directories(${PROJECT_NAME} PRIVATE ${PROJECT_SOURCE_DIR}/src)

#the tested internals (not exposed to a real user)
set(TESTED_INTERNALS_DIR ${PROJECT_SOURCE_DIR}/../lang_style/src)
target_include_directories(${PROJECT_NAME} PRIVATE ${TESTED_INTERNALS_DIR})

#param
#set(CATCH_INCLUDE_DIR D:/proger/test/catch2/single_include) #windows
set(CATCH_INCLUDE_DIR /home/rvi/prg/test/catch2/single_include) #linux
target_include_directories(${PROJECT_NAME} PRIVATE ${CATCH_INCLUDE_DIR})




set(Boost_USE_STATIC_LIBS ON)
find_package(Boost 1.70 COMPONENTS log REQUIRED)
if (Boost_FOUND)
    target_include_directories(${PROJECT_NAME} PRIVATE ${Boost_INCLUDE_DIR})
    target_link_libraries(${PROJECT_NAME} PRIVATE ${Boost_LIBRARIES})
endif()

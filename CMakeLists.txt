cmake_minimum_required(VERSION 2.8.7 FATAL_ERROR)
project(test CXX)
find_package(Cpp2Py REQUIRED)

add_compile_options(-std=c++14 -fsanitize=address)

include_directories(${CMAKE_SOURCE_DIR})

add_cpp2py_module(mytest)

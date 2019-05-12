cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test_himalaya test_himalaya.cpp)
target_link_libraries(test_himalaya ${CONAN_LIBS})

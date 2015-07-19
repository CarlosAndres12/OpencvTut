cmake_minimum_required(VERSION 3.2)
project(cpp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")


INCLUDE_DIRECTORIES("/opt/local/include")

Find_package (OpenCV  REQUIRED)
set(SOURCE_FILES main.cpp)
add_executable(cpp ${SOURCE_FILES})
target_link_libraries(cpp  ${OpenCV_LIBS})
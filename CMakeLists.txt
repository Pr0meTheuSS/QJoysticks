cmake_minimum_required(VERSION 3.0)
project(QJoysticks)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt6 COMPONENTS Core Gui Widgets REQUIRED)


file(GLOB HEADERS_LIST ${CMAKE_CURRENT_SOURCE_DIR}/src/*.h
                        ${CMAKE_CURRENT_SOURCE_DIR}/src/*/*.h)
file(GLOB SOURCES_LIST ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp
                        ${CMAKE_CURRENT_SOURCE_DIR}/src/*/*.cpp)

set(RESOURCES
    etc/resources/qjoysticks-res.qrc
)

qt6_add_resources(RESOURCES_RCC ${RESOURCES})

add_library(${PROJECT_NAME} SHARED ${HEADERS_LIST} ${SOURCES_LIST} ${RESOURCES_RCC})
target_link_libraries(${PROJECT_NAME}
    Qt6::Core
    Qt6::Gui
    Qt6::Widgets
)

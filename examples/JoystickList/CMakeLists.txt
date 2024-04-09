cmake_minimum_required(VERSION 3.22)

project(MyQtProject LANGUAGES CXX)

# Добавляем путь к папке с установленными пакетами Conan
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# include(${CMAKE_BINARY_DIR}/conan_paths.cmake)
# conan_basic_setup()
conan_set_find_library_paths()

# Добавляем пути до заголовочных файлов пакетов Conan
include_directories(${CONAN_INCLUDE_DIRS})
link_directories(${CONAN_LIB_DIRS})

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt6 COMPONENTS Core Gui Widgets Qml REQUIRED)
find_package(qjoystick REQUIRED)

 set(RESOURCES
     qml.qrc
 )

qt_add_executable(MyQtApp main.cpp ${RESOURCES})

# Линкуем Qt библиотеки
target_link_libraries(MyQtApp PUBLIC QJoysticks Qt6::Core Qt6::Qml Qt6::Gui)


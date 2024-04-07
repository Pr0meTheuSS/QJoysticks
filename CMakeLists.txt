cmake_minimum_required(VERSION 3.22)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(QJoysticks)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

find_package(Qt6 COMPONENTS Core Gui Widgets REQUIRED)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/lib/SDL/include)

# Явно перечислим исходные файлы
set(HEADERS_LIST
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/Android_Joystick.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/JoysticksCommon.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/SDL_Joysticks.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/VirtualJoystick.h"
)

set(SOURCES_LIST
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/Android_Joystick.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/SDL_Joysticks.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/SDL_Joysticks.cpp"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/VirtualJoystick.cpp"
)

set(RESOURCES
    etc/resources/qjoysticks-res.qrc
)

qt6_add_resources(RESOURCES_RCC ${RESOURCES})

qt_add_library(${PROJECT_NAME} STATIC ${HEADERS_LIST} ${SOURCES_LIST} ${RESOURCES_RCC})
target_link_libraries(${PROJECT_NAME}
    Qt6::Core
    Qt6::Gui
    Qt6::Widgets
)

message('try to copy files')
# Копируем файлы перед установкой библиотеки
install(FILES
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/Android_Joystick.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/JoysticksCommon.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/SDL_Joysticks.h"
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks/VirtualJoystick.h"
    DESTINATION include/QJoysticks
)
install(FILES
    "${CMAKE_CURRENT_SOURCE_DIR}/src/QJoysticks.h"
    DESTINATION include
)

# Копируем DLL-файлы в зависимости от операционной системы и компилятора
if(WIN32)
    # Копирование DLL для сборки с помощью MSVC
    if(MSVC)
        # Копирование DLL в зависимости от разрядности архитектуры (86 или 64)
        if(CMAKE_SIZEOF_VOID_P EQUAL 8)
            install(FILES
                "${CMAKE_CURRENT_SOURCE_DIR}/lib/SDL/bin/windows/msvc/x64/*.dll"
                DESTINATION bin
            )
            install(FILES
                "${CMAKE_CURRENT_SOURCE_DIR}/lib/SDL/bin/windows/msvc/x64/*.lib"
                DESTINATION lib
            )
        else()
            install(FILES
                "${CMAKE_CURRENT_SOURCE_DIR}/lib/SDL/bin/windows/msvc/x86/*.dll"
                DESTINATION bin
            )
            install(FILES
                "${CMAKE_CURRENT_SOURCE_DIR}/lib/SDL/bin/windows/msvc/x86/*.lib"
                DESTINATION lib
            )
        endif()
    elseif(MINGW)
        # Копирование DLL для сборки с помощью MinGW
        install(FILES
            "${CMAKE_CURRENT_SOURCE_DIR}/lib/SDL/bin/windows/mingw/SDL2.dll"
            DESTINATION bin
        )
    endif()
elseif(APPLE)
    # Добавляем инструкции для сборки на macOS
    install(TARGETS ${PROJECT_NAME}
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
    )
endif()

# Установка библиотеки
install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

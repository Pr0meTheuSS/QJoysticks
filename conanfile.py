from conans import ConanFile, CMake, tools

class QJoystickConan(ConanFile):
    name = "qjoystick"
    version = "1.0.0"
    url = "https://github.com/alex-spataru/QJoysticks"
    description = "Library for handling joystick input in Qt applications"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    source_folder = "."

    options = {"shared": [True, False]}
    default_options = {"shared": True}

    def source(self):
        print("source")
        git = tools.Git(folder=self.source_folder)
        git.clone(self.url)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder)
        cmake.build()

    def package(self):
        print("package")
        self.copy("*.hpp", dst="include", src=self.source_folder)
        self.copy("*.h", dst="include", src=self.source_folder)
        if self.options.shared:
            self.copy("*.so*", dst="lib", keep_path=False)
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.dylib", dst="lib", keep_path=False)
        else:
            self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        print("package_info")
        self.cpp_info.libs = ["qjoystick"]


from conans import ConanFile

class QJoystickConan(ConanFile):
    name = "test_qjoystick"
    version = "1.0.0"
    generators = ["cmake", "cmake_find_package"] 


    requires = ["qjoystick/1.0.0"]
    default_options = { "qt:shared": True, "qt:qtshadertools": True, "qt:qtdeclarative": True}

    def overrides(self):
        self.requires("libffi/3.4.3")

    # options = {"shared": [True, False]}
    # default_options = {"shared": False }


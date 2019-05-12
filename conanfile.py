import os
from conans import ConanFile, CMake, tools


class HimalayaConan(ConanFile):
    name = "Himalaya"
    version = "2.0.1"
    license = "GPL-3.0-only"
    author = "Alexander Voigt"
    url = "https://github.com/Himalaya-Library/Himalaya"
    description = "C++ library to calculate three-loop corrections to the Higgs boson mass in the MSSM"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = ("shared=False", "fPIC=True")
    exports = ["LICENSE", "FindHimalaya.cmake"]
    generators = "cmake"
    requires = ("eigen/[>=3.0]@conan/stable")
    _source_subfolder = "Himalaya"

    def source(self):
        self.run("git clone https://github.com/Himalaya-Library/Himalaya")
        self.run("cd Himalaya && git checkout {}".format(self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        for header in ["HierarchyCalculator.hpp", "HierarchyObject.hpp",
                       "Himalaya_interface.hpp", "version.hpp"]:
            self.copy(header, dst="include",
                      src="Himalaya{}source{}include".format(os.sep, os.sep),
                      keep_path=False)

        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("LICENSE", src=self._source_subfolder, dst="licenses", keep_path=False)
        self.copy('FindHimalaya.cmake', '.', '.')

    def package_info(self):
        self.cpp_info.libs = ["Himalaya"]


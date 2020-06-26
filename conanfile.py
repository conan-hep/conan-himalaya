import os
from conans import ConanFile, CMake, tools
from conans.model.version import Version
from conans.tools import SystemPackageTool


class HimalayaConan(ConanFile):
    name = "Himalaya"
    version = "4.0.0"
    license = "GPL-3.0-only"
    author = "Alexander Voigt"
    url = "https://github.com/Himalaya-Library/Himalaya"
    description = "C++ library to calculate three-loop corrections to the Higgs boson mass in the MSSM"
    topics = ("HEP")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = ("shared=False", "fPIC=True")
    exports = ["LICENSE"]
    generators = "cmake_paths"
    requires = ("eigen/[>=3.0]@conan/stable")
    _source_subfolder = "Himalaya-{}".format(version)
    _tarball = "{}.tar.gz".format(version)

    def _have_fortran_compiler(self):
        return tools.which("gfortran") != None or tools.which("ifort") != None

    def source(self):
        tools.get("https://github.com/Himalaya-Library/Himalaya/archive/{}".format(self._tarball))

    def system_requirements(self):
        installer = SystemPackageTool()

        if not self._have_fortran_compiler():
            if tools.os_info.is_linux:
                if tools.os_info.with_pacman or tools.os_info.with_yum or tools.os_info.with_zypper:
                    installer.install("gcc-fortran")
                else:
                    installer.install("gfortran")
                    versionfloat = Version(self.settings.compiler.version.value)
                    if self.settings.compiler == "gcc":
                        if versionfloat < "5.0":
                            installer.install("libgfortran-{}-dev".format(versionfloat))
                        else:
                            installer.install("libgfortran-{}-dev".format(int(versionfloat)))

        if tools.os_info.is_macos and Version(self.settings.compiler.version.value) > "7.3":
            try:
                installer.install("gcc", update=True, force=True)
            except Exception:
                self.output.warn("brew install gcc failed. Tying to fix it with 'brew link'")
                self.run("brew link --overwrite gcc")

    def build(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_TOOLCHAIN_FILE'] = 'conan_paths.cmake'
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy("*.hpp", src="{}{}include".format(self._source_subfolder, os.sep),
                  dst="include", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("LICENSE", src=self._source_subfolder, dst="licenses", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Himalaya", "DSZ"]


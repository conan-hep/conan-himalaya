[![Build Status Travis](https://travis-ci.org/conan-hep/conan-himalaya.svg)](https://travis-ci.org/conan-hep/conan-himalaya)

## Conan package recipe for [*Himalaya*](https://github.com/Himalaya-Library)

References:

* Robert V. Harlander, Jonas Klappert, Alexander Voigt, *Higgs mass
  prediction in the MSSM at three-loop level in a pure DR context*,
  [*Eur.Phys.J.* **C77** (2017) no.12, 814](https://inspirehep.net/record/1617767)
  [arXiv:1708.05720](https://arxiv.org/abs/1708.05720)

* R.V. Harlander, J. Klappert, A.D. Ochoa Franco, A. Voigt, *The light
  CP-even MSSM Higgs mass resummed to fourth logarithmic order*,
  [*Eur.Phys.J.* **C78** (2018) no.10, 874](https://inspirehep.net/record/1681658)
  [arXiv:1807.03509](https://arxiv.org/abs/1807.03509)

* R. V. Harlander, J. Klappert, and A. Voigt,
  *The light CP-even MSSM Higgs mass including N3LO+N3LL QCD corrections*,
  [arXiv:1910.03595](https://arxiv.org/abs/1910.03595)

## For users

### Installation of dependencies

Himalaya can be installed with conan by running:

    conan install Himalaya/4.0.0@conan/stable

Alternatively a `conanfile.txt` file can be created in your project
directory with the following content:

    [requires]
    Himalaya/4.0.0@conan/stable

    [generators]
    cmake
    make
    pkg_config

The dependencies of your project are then installed by running:

    mkdir build
    cd build
    conan install ..

### Building your project

Afterwards the project can be configured via CMake and build with
`make` by running:

    cmake ..
    make

Alternatively the project can be configured with Meson and build with
`ninja` by running:

    export PKG_CONFIG_PATH=.
    meson ..
    ninja

Alternatively the project can be build with `make` by running:

    make -f ../Makefile

A complete example can be found in the `examples/` directory.


## Build and package

The following command both runs all the steps of the conan file, and
publishes the package to the local system cache.  This includes
downloading dependencies from "build_requires" and "requires" , and
then running the build() method.

    $ conan create . conan/stable


### Available Options

| Option        | Default          | Possible Values                          |
| ------------- |------------------|------------------------------------------|
| shared        | False            |  [True, False]                           |
| fPIC          | True             |  [True, False]                           |


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this
recipe, which can be used to build and package Himalaya.  It does *not* in
any way apply or is related to the actual software being packaged.

[MIT](LICENSE)

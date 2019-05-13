find_library(Himalaya_LIBRARY NAMES ${CONAN_LIBS_HIMALAYA} PATHS ${CONAN_LIB_DIRS_HIMALAYA})
find_path(Himalaya_INCLUDE_DIRS NAMES himalaya/version.hpp PATHS ${CONAN_INCLUDE_DIRS_HIMALAYA})

set(Himalaya_FOUND TRUE)
set(Himalaya_INCLUDE_DIRS ${HIMALAYA_INCLUDE_DIR})
set(Himalaya_LIBRARIES ${Himalaya_LIBRARY})
mark_as_advanced(Himalaya_LIBRARY HIMALAYA_INCLUDE_DIR)

if(Himalaya_FOUND AND NOT TARGET Himalaya::Himalaya)
  add_library(Himalaya::Himalaya UNKNOWN IMPORTED)
  set_target_properties(Himalaya::Himalaya PROPERTIES
    IMPORTED_LOCATION "${Himalaya_LIBRARIES}"
    INTERFACE_INCLUDE_DIRECTORIES "${Himalaya_INCLUDE_DIRS}"
  )
endif()

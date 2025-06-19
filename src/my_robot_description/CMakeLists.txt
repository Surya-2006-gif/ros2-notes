cmake_minimum_required(VERSION 3.8)
project(my_robot_description)

# Set default C++ standard
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

# Find ROS 2 build system
find_package(ament_cmake REQUIRED)
# find_package(lidar_based_controller REQUIRED)

# Install robot description files
install(
  DIRECTORY urdf meshes launch
  DESTINATION share/${PROJECT_NAME}
)


# Optional: Enable tests
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

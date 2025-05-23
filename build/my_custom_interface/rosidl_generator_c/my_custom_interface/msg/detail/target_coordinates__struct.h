// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_custom_interface:msg/TargetCoordinates.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_INTERFACE__MSG__DETAIL__TARGET_COORDINATES__STRUCT_H_
#define MY_CUSTOM_INTERFACE__MSG__DETAIL__TARGET_COORDINATES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"
// Member 'coordinates'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in msg/TargetCoordinates in the package my_custom_interface.
/**
  * this is target coordinates msg
 */
typedef struct my_custom_interface__msg__TargetCoordinates
{
  rosidl_runtime_c__String name;
  geometry_msgs__msg__Point coordinates;
} my_custom_interface__msg__TargetCoordinates;

// Struct for a sequence of my_custom_interface__msg__TargetCoordinates.
typedef struct my_custom_interface__msg__TargetCoordinates__Sequence
{
  my_custom_interface__msg__TargetCoordinates * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_custom_interface__msg__TargetCoordinates__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_CUSTOM_INTERFACE__MSG__DETAIL__TARGET_COORDINATES__STRUCT_H_

// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from yolov8_msgs:msg/Yolo.idl
// generated code does not contain a copyright notice

#ifndef YOLOV8_MSGS__MSG__DETAIL__YOLO__STRUCT_H_
#define YOLOV8_MSGS__MSG__DETAIL__YOLO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'class_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/Yolo in the package yolov8_msgs.
typedef struct yolov8_msgs__msg__Yolo
{
  rosidl_runtime_c__String class_name;
  int32_t class_id;
  float confidence;
  float x1;
  float y1;
  float x2;
  float y2;
} yolov8_msgs__msg__Yolo;

// Struct for a sequence of yolov8_msgs__msg__Yolo.
typedef struct yolov8_msgs__msg__Yolo__Sequence
{
  yolov8_msgs__msg__Yolo * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} yolov8_msgs__msg__Yolo__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // YOLOV8_MSGS__MSG__DETAIL__YOLO__STRUCT_H_

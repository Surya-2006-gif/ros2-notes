// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from yolov8_msgs:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef YOLOV8_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_H_
#define YOLOV8_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'detections'
#include "yolov8_msgs/msg/detail/yolo__struct.h"

/// Struct defined in msg/Detections in the package yolov8_msgs.
typedef struct yolov8_msgs__msg__Detections
{
  yolov8_msgs__msg__Yolo__Sequence detections;
} yolov8_msgs__msg__Detections;

// Struct for a sequence of yolov8_msgs__msg__Detections.
typedef struct yolov8_msgs__msg__Detections__Sequence
{
  yolov8_msgs__msg__Detections * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} yolov8_msgs__msg__Detections__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // YOLOV8_MSGS__MSG__DETAIL__DETECTIONS__STRUCT_H_

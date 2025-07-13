// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from yolov8_msgs:msg/Yolo.idl
// generated code does not contain a copyright notice
#include "yolov8_msgs/msg/detail/yolo__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `class_name`
#include "rosidl_runtime_c/string_functions.h"

bool
yolov8_msgs__msg__Yolo__init(yolov8_msgs__msg__Yolo * msg)
{
  if (!msg) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__init(&msg->class_name)) {
    yolov8_msgs__msg__Yolo__fini(msg);
    return false;
  }
  // class_id
  // confidence
  // x1
  // y1
  // x2
  // y2
  return true;
}

void
yolov8_msgs__msg__Yolo__fini(yolov8_msgs__msg__Yolo * msg)
{
  if (!msg) {
    return;
  }
  // class_name
  rosidl_runtime_c__String__fini(&msg->class_name);
  // class_id
  // confidence
  // x1
  // y1
  // x2
  // y2
}

bool
yolov8_msgs__msg__Yolo__are_equal(const yolov8_msgs__msg__Yolo * lhs, const yolov8_msgs__msg__Yolo * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->class_name), &(rhs->class_name)))
  {
    return false;
  }
  // class_id
  if (lhs->class_id != rhs->class_id) {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // x1
  if (lhs->x1 != rhs->x1) {
    return false;
  }
  // y1
  if (lhs->y1 != rhs->y1) {
    return false;
  }
  // x2
  if (lhs->x2 != rhs->x2) {
    return false;
  }
  // y2
  if (lhs->y2 != rhs->y2) {
    return false;
  }
  return true;
}

bool
yolov8_msgs__msg__Yolo__copy(
  const yolov8_msgs__msg__Yolo * input,
  yolov8_msgs__msg__Yolo * output)
{
  if (!input || !output) {
    return false;
  }
  // class_name
  if (!rosidl_runtime_c__String__copy(
      &(input->class_name), &(output->class_name)))
  {
    return false;
  }
  // class_id
  output->class_id = input->class_id;
  // confidence
  output->confidence = input->confidence;
  // x1
  output->x1 = input->x1;
  // y1
  output->y1 = input->y1;
  // x2
  output->x2 = input->x2;
  // y2
  output->y2 = input->y2;
  return true;
}

yolov8_msgs__msg__Yolo *
yolov8_msgs__msg__Yolo__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  yolov8_msgs__msg__Yolo * msg = (yolov8_msgs__msg__Yolo *)allocator.allocate(sizeof(yolov8_msgs__msg__Yolo), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(yolov8_msgs__msg__Yolo));
  bool success = yolov8_msgs__msg__Yolo__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
yolov8_msgs__msg__Yolo__destroy(yolov8_msgs__msg__Yolo * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    yolov8_msgs__msg__Yolo__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
yolov8_msgs__msg__Yolo__Sequence__init(yolov8_msgs__msg__Yolo__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  yolov8_msgs__msg__Yolo * data = NULL;

  if (size) {
    data = (yolov8_msgs__msg__Yolo *)allocator.zero_allocate(size, sizeof(yolov8_msgs__msg__Yolo), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = yolov8_msgs__msg__Yolo__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        yolov8_msgs__msg__Yolo__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
yolov8_msgs__msg__Yolo__Sequence__fini(yolov8_msgs__msg__Yolo__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      yolov8_msgs__msg__Yolo__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

yolov8_msgs__msg__Yolo__Sequence *
yolov8_msgs__msg__Yolo__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  yolov8_msgs__msg__Yolo__Sequence * array = (yolov8_msgs__msg__Yolo__Sequence *)allocator.allocate(sizeof(yolov8_msgs__msg__Yolo__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = yolov8_msgs__msg__Yolo__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
yolov8_msgs__msg__Yolo__Sequence__destroy(yolov8_msgs__msg__Yolo__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    yolov8_msgs__msg__Yolo__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
yolov8_msgs__msg__Yolo__Sequence__are_equal(const yolov8_msgs__msg__Yolo__Sequence * lhs, const yolov8_msgs__msg__Yolo__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!yolov8_msgs__msg__Yolo__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
yolov8_msgs__msg__Yolo__Sequence__copy(
  const yolov8_msgs__msg__Yolo__Sequence * input,
  yolov8_msgs__msg__Yolo__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(yolov8_msgs__msg__Yolo);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    yolov8_msgs__msg__Yolo * data =
      (yolov8_msgs__msg__Yolo *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!yolov8_msgs__msg__Yolo__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          yolov8_msgs__msg__Yolo__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!yolov8_msgs__msg__Yolo__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

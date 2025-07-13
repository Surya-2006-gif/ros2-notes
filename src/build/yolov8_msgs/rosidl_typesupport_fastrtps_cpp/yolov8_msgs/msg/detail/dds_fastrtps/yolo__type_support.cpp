// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from yolov8_msgs:msg/Yolo.idl
// generated code does not contain a copyright notice
#include "yolov8_msgs/msg/detail/yolo__rosidl_typesupport_fastrtps_cpp.hpp"
#include "yolov8_msgs/msg/detail/yolo__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace yolov8_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolov8_msgs
cdr_serialize(
  const yolov8_msgs::msg::Yolo & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: class_name
  cdr << ros_message.class_name;
  // Member: class_id
  cdr << ros_message.class_id;
  // Member: confidence
  cdr << ros_message.confidence;
  // Member: x1
  cdr << ros_message.x1;
  // Member: y1
  cdr << ros_message.y1;
  // Member: x2
  cdr << ros_message.x2;
  // Member: y2
  cdr << ros_message.y2;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolov8_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  yolov8_msgs::msg::Yolo & ros_message)
{
  // Member: class_name
  cdr >> ros_message.class_name;

  // Member: class_id
  cdr >> ros_message.class_id;

  // Member: confidence
  cdr >> ros_message.confidence;

  // Member: x1
  cdr >> ros_message.x1;

  // Member: y1
  cdr >> ros_message.y1;

  // Member: x2
  cdr >> ros_message.x2;

  // Member: y2
  cdr >> ros_message.y2;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolov8_msgs
get_serialized_size(
  const yolov8_msgs::msg::Yolo & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: class_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.class_name.size() + 1);
  // Member: class_id
  {
    size_t item_size = sizeof(ros_message.class_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: confidence
  {
    size_t item_size = sizeof(ros_message.confidence);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: x1
  {
    size_t item_size = sizeof(ros_message.x1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y1
  {
    size_t item_size = sizeof(ros_message.y1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: x2
  {
    size_t item_size = sizeof(ros_message.x2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: y2
  {
    size_t item_size = sizeof(ros_message.y2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_yolov8_msgs
max_serialized_size_Yolo(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: class_name
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: class_id
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: confidence
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: x1
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: y1
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: x2
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: y2
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = yolov8_msgs::msg::Yolo;
    is_plain =
      (
      offsetof(DataType, y2) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _Yolo__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const yolov8_msgs::msg::Yolo *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Yolo__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<yolov8_msgs::msg::Yolo *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Yolo__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const yolov8_msgs::msg::Yolo *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Yolo__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Yolo(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Yolo__callbacks = {
  "yolov8_msgs::msg",
  "Yolo",
  _Yolo__cdr_serialize,
  _Yolo__cdr_deserialize,
  _Yolo__get_serialized_size,
  _Yolo__max_serialized_size
};

static rosidl_message_type_support_t _Yolo__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Yolo__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace yolov8_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_yolov8_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<yolov8_msgs::msg::Yolo>()
{
  return &yolov8_msgs::msg::typesupport_fastrtps_cpp::_Yolo__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, yolov8_msgs, msg, Yolo)() {
  return &yolov8_msgs::msg::typesupport_fastrtps_cpp::_Yolo__handle;
}

#ifdef __cplusplus
}
#endif

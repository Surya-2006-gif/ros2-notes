// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from yolov8_msgs:msg/Yolo.idl
// generated code does not contain a copyright notice

#ifndef YOLOV8_MSGS__MSG__DETAIL__YOLO__BUILDER_HPP_
#define YOLOV8_MSGS__MSG__DETAIL__YOLO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "yolov8_msgs/msg/detail/yolo__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace yolov8_msgs
{

namespace msg
{

namespace builder
{

class Init_Yolo_y2
{
public:
  explicit Init_Yolo_y2(::yolov8_msgs::msg::Yolo & msg)
  : msg_(msg)
  {}
  ::yolov8_msgs::msg::Yolo y2(::yolov8_msgs::msg::Yolo::_y2_type arg)
  {
    msg_.y2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::yolov8_msgs::msg::Yolo msg_;
};

class Init_Yolo_x2
{
public:
  explicit Init_Yolo_x2(::yolov8_msgs::msg::Yolo & msg)
  : msg_(msg)
  {}
  Init_Yolo_y2 x2(::yolov8_msgs::msg::Yolo::_x2_type arg)
  {
    msg_.x2 = std::move(arg);
    return Init_Yolo_y2(msg_);
  }

private:
  ::yolov8_msgs::msg::Yolo msg_;
};

class Init_Yolo_y1
{
public:
  explicit Init_Yolo_y1(::yolov8_msgs::msg::Yolo & msg)
  : msg_(msg)
  {}
  Init_Yolo_x2 y1(::yolov8_msgs::msg::Yolo::_y1_type arg)
  {
    msg_.y1 = std::move(arg);
    return Init_Yolo_x2(msg_);
  }

private:
  ::yolov8_msgs::msg::Yolo msg_;
};

class Init_Yolo_x1
{
public:
  explicit Init_Yolo_x1(::yolov8_msgs::msg::Yolo & msg)
  : msg_(msg)
  {}
  Init_Yolo_y1 x1(::yolov8_msgs::msg::Yolo::_x1_type arg)
  {
    msg_.x1 = std::move(arg);
    return Init_Yolo_y1(msg_);
  }

private:
  ::yolov8_msgs::msg::Yolo msg_;
};

class Init_Yolo_confidence
{
public:
  explicit Init_Yolo_confidence(::yolov8_msgs::msg::Yolo & msg)
  : msg_(msg)
  {}
  Init_Yolo_x1 confidence(::yolov8_msgs::msg::Yolo::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_Yolo_x1(msg_);
  }

private:
  ::yolov8_msgs::msg::Yolo msg_;
};

class Init_Yolo_class_id
{
public:
  explicit Init_Yolo_class_id(::yolov8_msgs::msg::Yolo & msg)
  : msg_(msg)
  {}
  Init_Yolo_confidence class_id(::yolov8_msgs::msg::Yolo::_class_id_type arg)
  {
    msg_.class_id = std::move(arg);
    return Init_Yolo_confidence(msg_);
  }

private:
  ::yolov8_msgs::msg::Yolo msg_;
};

class Init_Yolo_class_name
{
public:
  Init_Yolo_class_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Yolo_class_id class_name(::yolov8_msgs::msg::Yolo::_class_name_type arg)
  {
    msg_.class_name = std::move(arg);
    return Init_Yolo_class_id(msg_);
  }

private:
  ::yolov8_msgs::msg::Yolo msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::yolov8_msgs::msg::Yolo>()
{
  return yolov8_msgs::msg::builder::Init_Yolo_class_name();
}

}  // namespace yolov8_msgs

#endif  // YOLOV8_MSGS__MSG__DETAIL__YOLO__BUILDER_HPP_

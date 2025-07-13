// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from yolov8_msgs:msg/Detections.idl
// generated code does not contain a copyright notice

#ifndef YOLOV8_MSGS__MSG__DETAIL__DETECTIONS__BUILDER_HPP_
#define YOLOV8_MSGS__MSG__DETAIL__DETECTIONS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "yolov8_msgs/msg/detail/detections__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace yolov8_msgs
{

namespace msg
{

namespace builder
{

class Init_Detections_detections
{
public:
  Init_Detections_detections()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::yolov8_msgs::msg::Detections detections(::yolov8_msgs::msg::Detections::_detections_type arg)
  {
    msg_.detections = std::move(arg);
    return std::move(msg_);
  }

private:
  ::yolov8_msgs::msg::Detections msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::yolov8_msgs::msg::Detections>()
{
  return yolov8_msgs::msg::builder::Init_Detections_detections();
}

}  // namespace yolov8_msgs

#endif  // YOLOV8_MSGS__MSG__DETAIL__DETECTIONS__BUILDER_HPP_

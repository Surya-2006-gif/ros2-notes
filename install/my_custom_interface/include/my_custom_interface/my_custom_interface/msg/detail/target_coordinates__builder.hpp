// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_custom_interface:msg/TargetCoordinates.idl
// generated code does not contain a copyright notice

#ifndef MY_CUSTOM_INTERFACE__MSG__DETAIL__TARGET_COORDINATES__BUILDER_HPP_
#define MY_CUSTOM_INTERFACE__MSG__DETAIL__TARGET_COORDINATES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_custom_interface/msg/detail/target_coordinates__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_custom_interface
{

namespace msg
{

namespace builder
{

class Init_TargetCoordinates_coordinates
{
public:
  explicit Init_TargetCoordinates_coordinates(::my_custom_interface::msg::TargetCoordinates & msg)
  : msg_(msg)
  {}
  ::my_custom_interface::msg::TargetCoordinates coordinates(::my_custom_interface::msg::TargetCoordinates::_coordinates_type arg)
  {
    msg_.coordinates = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_custom_interface::msg::TargetCoordinates msg_;
};

class Init_TargetCoordinates_name
{
public:
  Init_TargetCoordinates_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TargetCoordinates_coordinates name(::my_custom_interface::msg::TargetCoordinates::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_TargetCoordinates_coordinates(msg_);
  }

private:
  ::my_custom_interface::msg::TargetCoordinates msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_custom_interface::msg::TargetCoordinates>()
{
  return my_custom_interface::msg::builder::Init_TargetCoordinates_name();
}

}  // namespace my_custom_interface

#endif  // MY_CUSTOM_INTERFACE__MSG__DETAIL__TARGET_COORDINATES__BUILDER_HPP_

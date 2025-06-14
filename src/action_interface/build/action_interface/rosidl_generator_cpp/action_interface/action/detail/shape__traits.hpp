// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from action_interface:action/Shape.idl
// generated code does not contain a copyright notice

#ifndef ACTION_INTERFACE__ACTION__DETAIL__SHAPE__TRAITS_HPP_
#define ACTION_INTERFACE__ACTION__DETAIL__SHAPE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "action_interface/action/detail/shape__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: shape
  {
    out << "shape: ";
    rosidl_generator_traits::value_to_yaml(msg.shape, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: shape
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "shape: ";
    rosidl_generator_traits::value_to_yaml(msg.shape, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_Goal & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_Goal>()
{
  return "action_interface::action::Shape_Goal";
}

template<>
inline const char * name<action_interface::action::Shape_Goal>()
{
  return "action_interface/action/Shape_Goal";
}

template<>
struct has_fixed_size<action_interface::action::Shape_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<action_interface::action::Shape_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<action_interface::action::Shape_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_Result & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_Result>()
{
  return "action_interface::action::Shape_Result";
}

template<>
inline const char * name<action_interface::action::Shape_Result>()
{
  return "action_interface/action/Shape_Result";
}

template<>
struct has_fixed_size<action_interface::action::Shape_Result>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<action_interface::action::Shape_Result>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<action_interface::action::Shape_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'current_pos'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: current_pos
  {
    out << "current_pos: ";
    to_flow_style_yaml(msg.current_pos, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: current_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_pos:\n";
    to_block_style_yaml(msg.current_pos, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_Feedback & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_Feedback>()
{
  return "action_interface::action::Shape_Feedback";
}

template<>
inline const char * name<action_interface::action::Shape_Feedback>()
{
  return "action_interface/action/Shape_Feedback";
}

template<>
struct has_fixed_size<action_interface::action::Shape_Feedback>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<action_interface::action::Shape_Feedback>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<action_interface::action::Shape_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "action_interface/action/detail/shape__traits.hpp"

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_SendGoal_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_SendGoal_Request & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_SendGoal_Request>()
{
  return "action_interface::action::Shape_SendGoal_Request";
}

template<>
inline const char * name<action_interface::action::Shape_SendGoal_Request>()
{
  return "action_interface/action/Shape_SendGoal_Request";
}

template<>
struct has_fixed_size<action_interface::action::Shape_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<action_interface::action::Shape_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<action_interface::action::Shape_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<action_interface::action::Shape_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<action_interface::action::Shape_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_SendGoal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_SendGoal_Response & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_SendGoal_Response>()
{
  return "action_interface::action::Shape_SendGoal_Response";
}

template<>
inline const char * name<action_interface::action::Shape_SendGoal_Response>()
{
  return "action_interface/action/Shape_SendGoal_Response";
}

template<>
struct has_fixed_size<action_interface::action::Shape_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<action_interface::action::Shape_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<action_interface::action::Shape_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<action_interface::action::Shape_SendGoal>()
{
  return "action_interface::action::Shape_SendGoal";
}

template<>
inline const char * name<action_interface::action::Shape_SendGoal>()
{
  return "action_interface/action/Shape_SendGoal";
}

template<>
struct has_fixed_size<action_interface::action::Shape_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<action_interface::action::Shape_SendGoal_Request>::value &&
    has_fixed_size<action_interface::action::Shape_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<action_interface::action::Shape_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<action_interface::action::Shape_SendGoal_Request>::value &&
    has_bounded_size<action_interface::action::Shape_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<action_interface::action::Shape_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<action_interface::action::Shape_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<action_interface::action::Shape_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_GetResult_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_GetResult_Request & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_GetResult_Request>()
{
  return "action_interface::action::Shape_GetResult_Request";
}

template<>
inline const char * name<action_interface::action::Shape_GetResult_Request>()
{
  return "action_interface/action/Shape_GetResult_Request";
}

template<>
struct has_fixed_size<action_interface::action::Shape_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<action_interface::action::Shape_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<action_interface::action::Shape_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "action_interface/action/detail/shape__traits.hpp"

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_GetResult_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: result
  {
    out << "result: ";
    to_flow_style_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_block_style_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_GetResult_Response & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_GetResult_Response>()
{
  return "action_interface::action::Shape_GetResult_Response";
}

template<>
inline const char * name<action_interface::action::Shape_GetResult_Response>()
{
  return "action_interface/action/Shape_GetResult_Response";
}

template<>
struct has_fixed_size<action_interface::action::Shape_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<action_interface::action::Shape_Result>::value> {};

template<>
struct has_bounded_size<action_interface::action::Shape_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<action_interface::action::Shape_Result>::value> {};

template<>
struct is_message<action_interface::action::Shape_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<action_interface::action::Shape_GetResult>()
{
  return "action_interface::action::Shape_GetResult";
}

template<>
inline const char * name<action_interface::action::Shape_GetResult>()
{
  return "action_interface/action/Shape_GetResult";
}

template<>
struct has_fixed_size<action_interface::action::Shape_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<action_interface::action::Shape_GetResult_Request>::value &&
    has_fixed_size<action_interface::action::Shape_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<action_interface::action::Shape_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<action_interface::action::Shape_GetResult_Request>::value &&
    has_bounded_size<action_interface::action::Shape_GetResult_Response>::value
  >
{
};

template<>
struct is_service<action_interface::action::Shape_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<action_interface::action::Shape_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<action_interface::action::Shape_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "action_interface/action/detail/shape__traits.hpp"

namespace action_interface
{

namespace action
{

inline void to_flow_style_yaml(
  const Shape_FeedbackMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: feedback
  {
    out << "feedback: ";
    to_flow_style_yaml(msg.feedback, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Shape_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_block_style_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Shape_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace action_interface

namespace rosidl_generator_traits
{

[[deprecated("use action_interface::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const action_interface::action::Shape_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  action_interface::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use action_interface::action::to_yaml() instead")]]
inline std::string to_yaml(const action_interface::action::Shape_FeedbackMessage & msg)
{
  return action_interface::action::to_yaml(msg);
}

template<>
inline const char * data_type<action_interface::action::Shape_FeedbackMessage>()
{
  return "action_interface::action::Shape_FeedbackMessage";
}

template<>
inline const char * name<action_interface::action::Shape_FeedbackMessage>()
{
  return "action_interface/action/Shape_FeedbackMessage";
}

template<>
struct has_fixed_size<action_interface::action::Shape_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<action_interface::action::Shape_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<action_interface::action::Shape_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<action_interface::action::Shape_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<action_interface::action::Shape_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<action_interface::action::Shape>
  : std::true_type
{
};

template<>
struct is_action_goal<action_interface::action::Shape_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<action_interface::action::Shape_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<action_interface::action::Shape_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // ACTION_INTERFACE__ACTION__DETAIL__SHAPE__TRAITS_HPP_

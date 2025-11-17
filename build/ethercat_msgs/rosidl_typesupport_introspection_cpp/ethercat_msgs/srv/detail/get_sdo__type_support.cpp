// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from ethercat_msgs:srv/GetSdo.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "ethercat_msgs/srv/detail/get_sdo__functions.h"
#include "ethercat_msgs/srv/detail/get_sdo__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void GetSdo_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ethercat_msgs::srv::GetSdo_Request(_init);
}

void GetSdo_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ethercat_msgs::srv::GetSdo_Request *>(message_memory);
  typed_message->~GetSdo_Request();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember GetSdo_Request_message_member_array[5] = {
  {
    "master_id",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Request, master_id),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "slave_position",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Request, slave_position),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sdo_index",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Request, sdo_index),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sdo_subindex",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Request, sdo_subindex),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sdo_data_type",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Request, sdo_data_type),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers GetSdo_Request_message_members = {
  "ethercat_msgs::srv",  // message namespace
  "GetSdo_Request",  // message name
  5,  // number of fields
  sizeof(ethercat_msgs::srv::GetSdo_Request),
  false,  // has_any_key_member_
  GetSdo_Request_message_member_array,  // message members
  GetSdo_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  GetSdo_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t GetSdo_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GetSdo_Request_message_members,
  get_message_typesupport_handle_function,
  &ethercat_msgs__srv__GetSdo_Request__get_type_hash,
  &ethercat_msgs__srv__GetSdo_Request__get_type_description,
  &ethercat_msgs__srv__GetSdo_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ethercat_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Request>()
{
  return &::ethercat_msgs::srv::rosidl_typesupport_introspection_cpp::GetSdo_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ethercat_msgs, srv, GetSdo_Request)() {
  return &::ethercat_msgs::srv::rosidl_typesupport_introspection_cpp::GetSdo_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__functions.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void GetSdo_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ethercat_msgs::srv::GetSdo_Response(_init);
}

void GetSdo_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ethercat_msgs::srv::GetSdo_Response *>(message_memory);
  typed_message->~GetSdo_Response();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember GetSdo_Response_message_member_array[4] = {
  {
    "success",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Response, success),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sdo_return_message",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Response, sdo_return_message),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sdo_return_value_string",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Response, sdo_return_value_string),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "sdo_return_value",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Response, sdo_return_value),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers GetSdo_Response_message_members = {
  "ethercat_msgs::srv",  // message namespace
  "GetSdo_Response",  // message name
  4,  // number of fields
  sizeof(ethercat_msgs::srv::GetSdo_Response),
  false,  // has_any_key_member_
  GetSdo_Response_message_member_array,  // message members
  GetSdo_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  GetSdo_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t GetSdo_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GetSdo_Response_message_members,
  get_message_typesupport_handle_function,
  &ethercat_msgs__srv__GetSdo_Response__get_type_hash,
  &ethercat_msgs__srv__GetSdo_Response__get_type_description,
  &ethercat_msgs__srv__GetSdo_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ethercat_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Response>()
{
  return &::ethercat_msgs::srv::rosidl_typesupport_introspection_cpp::GetSdo_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ethercat_msgs, srv, GetSdo_Response)() {
  return &::ethercat_msgs::srv::rosidl_typesupport_introspection_cpp::GetSdo_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__functions.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void GetSdo_Event_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) ethercat_msgs::srv::GetSdo_Event(_init);
}

void GetSdo_Event_fini_function(void * message_memory)
{
  auto typed_message = static_cast<ethercat_msgs::srv::GetSdo_Event *>(message_memory);
  typed_message->~GetSdo_Event();
}

size_t size_function__GetSdo_Event__request(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<ethercat_msgs::srv::GetSdo_Request> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GetSdo_Event__request(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<ethercat_msgs::srv::GetSdo_Request> *>(untyped_member);
  return &member[index];
}

void * get_function__GetSdo_Event__request(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<ethercat_msgs::srv::GetSdo_Request> *>(untyped_member);
  return &member[index];
}

void fetch_function__GetSdo_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const ethercat_msgs::srv::GetSdo_Request *>(
    get_const_function__GetSdo_Event__request(untyped_member, index));
  auto & value = *reinterpret_cast<ethercat_msgs::srv::GetSdo_Request *>(untyped_value);
  value = item;
}

void assign_function__GetSdo_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<ethercat_msgs::srv::GetSdo_Request *>(
    get_function__GetSdo_Event__request(untyped_member, index));
  const auto & value = *reinterpret_cast<const ethercat_msgs::srv::GetSdo_Request *>(untyped_value);
  item = value;
}

void resize_function__GetSdo_Event__request(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<ethercat_msgs::srv::GetSdo_Request> *>(untyped_member);
  member->resize(size);
}

size_t size_function__GetSdo_Event__response(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<ethercat_msgs::srv::GetSdo_Response> *>(untyped_member);
  return member->size();
}

const void * get_const_function__GetSdo_Event__response(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<ethercat_msgs::srv::GetSdo_Response> *>(untyped_member);
  return &member[index];
}

void * get_function__GetSdo_Event__response(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<ethercat_msgs::srv::GetSdo_Response> *>(untyped_member);
  return &member[index];
}

void fetch_function__GetSdo_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const ethercat_msgs::srv::GetSdo_Response *>(
    get_const_function__GetSdo_Event__response(untyped_member, index));
  auto & value = *reinterpret_cast<ethercat_msgs::srv::GetSdo_Response *>(untyped_value);
  value = item;
}

void assign_function__GetSdo_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<ethercat_msgs::srv::GetSdo_Response *>(
    get_function__GetSdo_Event__response(untyped_member, index));
  const auto & value = *reinterpret_cast<const ethercat_msgs::srv::GetSdo_Response *>(untyped_value);
  item = value;
}

void resize_function__GetSdo_Event__response(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<ethercat_msgs::srv::GetSdo_Response> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember GetSdo_Event_message_member_array[3] = {
  {
    "info",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<service_msgs::msg::ServiceEventInfo>(),  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Event, info),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "request",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Request>(),  // members of sub message
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Event, request),  // bytes offset in struct
    nullptr,  // default value
    size_function__GetSdo_Event__request,  // size() function pointer
    get_const_function__GetSdo_Event__request,  // get_const(index) function pointer
    get_function__GetSdo_Event__request,  // get(index) function pointer
    fetch_function__GetSdo_Event__request,  // fetch(index, &value) function pointer
    assign_function__GetSdo_Event__request,  // assign(index, value) function pointer
    resize_function__GetSdo_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Response>(),  // members of sub message
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(ethercat_msgs::srv::GetSdo_Event, response),  // bytes offset in struct
    nullptr,  // default value
    size_function__GetSdo_Event__response,  // size() function pointer
    get_const_function__GetSdo_Event__response,  // get_const(index) function pointer
    get_function__GetSdo_Event__response,  // get(index) function pointer
    fetch_function__GetSdo_Event__response,  // fetch(index, &value) function pointer
    assign_function__GetSdo_Event__response,  // assign(index, value) function pointer
    resize_function__GetSdo_Event__response  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers GetSdo_Event_message_members = {
  "ethercat_msgs::srv",  // message namespace
  "GetSdo_Event",  // message name
  3,  // number of fields
  sizeof(ethercat_msgs::srv::GetSdo_Event),
  false,  // has_any_key_member_
  GetSdo_Event_message_member_array,  // message members
  GetSdo_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  GetSdo_Event_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t GetSdo_Event_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GetSdo_Event_message_members,
  get_message_typesupport_handle_function,
  &ethercat_msgs__srv__GetSdo_Event__get_type_hash,
  &ethercat_msgs__srv__GetSdo_Event__get_type_description,
  &ethercat_msgs__srv__GetSdo_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ethercat_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Event>()
{
  return &::ethercat_msgs::srv::rosidl_typesupport_introspection_cpp::GetSdo_Event_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ethercat_msgs, srv, GetSdo_Event)() {
  return &::ethercat_msgs::srv::rosidl_typesupport_introspection_cpp::GetSdo_Event_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__functions.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers GetSdo_service_members = {
  "ethercat_msgs::srv",  // service namespace
  "GetSdo",  // service name
  // the following fields are initialized below on first access
  // see get_service_type_support_handle<ethercat_msgs::srv::GetSdo>()
  nullptr,  // request message
  nullptr,  // response message
  nullptr,  // event message
};

static const rosidl_service_type_support_t GetSdo_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &GetSdo_service_members,
  get_service_typesupport_handle_function,
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Request>(),
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Response>(),
  ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<ethercat_msgs::srv::GetSdo_Event>(),
  &::rosidl_typesupport_cpp::service_create_event_message<ethercat_msgs::srv::GetSdo>,
  &::rosidl_typesupport_cpp::service_destroy_event_message<ethercat_msgs::srv::GetSdo>,
  &ethercat_msgs__srv__GetSdo__get_type_hash,
  &ethercat_msgs__srv__GetSdo__get_type_description,
  &ethercat_msgs__srv__GetSdo__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace ethercat_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<ethercat_msgs::srv::GetSdo>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::ethercat_msgs::srv::rosidl_typesupport_introspection_cpp::GetSdo_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure all of the service_members are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr ||
    service_members->event_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::ethercat_msgs::srv::GetSdo_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::ethercat_msgs::srv::GetSdo_Response
      >()->data
      );
    // initialize the event_members_ with the static function from the external library
    service_members->event_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::ethercat_msgs::srv::GetSdo_Event
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, ethercat_msgs, srv, GetSdo)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<ethercat_msgs::srv::GetSdo>();
}

#ifdef __cplusplus
}
#endif

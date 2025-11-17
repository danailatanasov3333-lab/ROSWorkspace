// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ethercat_msgs:srv/SetSdo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ethercat_msgs/srv/detail/set_sdo__rosidl_typesupport_introspection_c.h"
#include "ethercat_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ethercat_msgs/srv/detail/set_sdo__functions.h"
#include "ethercat_msgs/srv/detail/set_sdo__struct.h"


// Include directives for member types
// Member `sdo_data_type`
// Member `sdo_value`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ethercat_msgs__srv__SetSdo_Request__init(message_memory);
}

void ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_fini_function(void * message_memory)
{
  ethercat_msgs__srv__SetSdo_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_member_array[6] = {
  {
    "master_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Request, master_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "slave_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Request, slave_position),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sdo_index",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Request, sdo_index),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sdo_subindex",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Request, sdo_subindex),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sdo_data_type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Request, sdo_data_type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sdo_value",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Request, sdo_value),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_members = {
  "ethercat_msgs__srv",  // message namespace
  "SetSdo_Request",  // message name
  6,  // number of fields
  sizeof(ethercat_msgs__srv__SetSdo_Request),
  false,  // has_any_key_member_
  ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_member_array,  // message members
  ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_type_support_handle = {
  0,
  &ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_members,
  get_message_typesupport_handle_function,
  &ethercat_msgs__srv__SetSdo_Request__get_type_hash,
  &ethercat_msgs__srv__SetSdo_Request__get_type_description,
  &ethercat_msgs__srv__SetSdo_Request__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ethercat_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Request)() {
  if (!ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_type_support_handle.typesupport_identifier) {
    ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__rosidl_typesupport_introspection_c.h"
// already included above
// #include "ethercat_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__functions.h"
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__struct.h"


// Include directives for member types
// Member `sdo_return_message`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ethercat_msgs__srv__SetSdo_Response__init(message_memory);
}

void ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_fini_function(void * message_memory)
{
  ethercat_msgs__srv__SetSdo_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_member_array[2] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "sdo_return_message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Response, sdo_return_message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_members = {
  "ethercat_msgs__srv",  // message namespace
  "SetSdo_Response",  // message name
  2,  // number of fields
  sizeof(ethercat_msgs__srv__SetSdo_Response),
  false,  // has_any_key_member_
  ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_member_array,  // message members
  ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_type_support_handle = {
  0,
  &ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_members,
  get_message_typesupport_handle_function,
  &ethercat_msgs__srv__SetSdo_Response__get_type_hash,
  &ethercat_msgs__srv__SetSdo_Response__get_type_description,
  &ethercat_msgs__srv__SetSdo_Response__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ethercat_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Response)() {
  if (!ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_type_support_handle.typesupport_identifier) {
    ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__rosidl_typesupport_introspection_c.h"
// already included above
// #include "ethercat_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__functions.h"
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__struct.h"


// Include directives for member types
// Member `info`
#include "service_msgs/msg/service_event_info.h"
// Member `info`
#include "service_msgs/msg/detail/service_event_info__rosidl_typesupport_introspection_c.h"
// Member `request`
// Member `response`
#include "ethercat_msgs/srv/set_sdo.h"
// Member `request`
// Member `response`
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ethercat_msgs__srv__SetSdo_Event__init(message_memory);
}

void ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_fini_function(void * message_memory)
{
  ethercat_msgs__srv__SetSdo_Event__fini(message_memory);
}

size_t ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__size_function__SetSdo_Event__request(
  const void * untyped_member)
{
  const ethercat_msgs__srv__SetSdo_Request__Sequence * member =
    (const ethercat_msgs__srv__SetSdo_Request__Sequence *)(untyped_member);
  return member->size;
}

const void * ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_const_function__SetSdo_Event__request(
  const void * untyped_member, size_t index)
{
  const ethercat_msgs__srv__SetSdo_Request__Sequence * member =
    (const ethercat_msgs__srv__SetSdo_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_function__SetSdo_Event__request(
  void * untyped_member, size_t index)
{
  ethercat_msgs__srv__SetSdo_Request__Sequence * member =
    (ethercat_msgs__srv__SetSdo_Request__Sequence *)(untyped_member);
  return &member->data[index];
}

void ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__fetch_function__SetSdo_Event__request(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const ethercat_msgs__srv__SetSdo_Request * item =
    ((const ethercat_msgs__srv__SetSdo_Request *)
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_const_function__SetSdo_Event__request(untyped_member, index));
  ethercat_msgs__srv__SetSdo_Request * value =
    (ethercat_msgs__srv__SetSdo_Request *)(untyped_value);
  *value = *item;
}

void ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__assign_function__SetSdo_Event__request(
  void * untyped_member, size_t index, const void * untyped_value)
{
  ethercat_msgs__srv__SetSdo_Request * item =
    ((ethercat_msgs__srv__SetSdo_Request *)
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_function__SetSdo_Event__request(untyped_member, index));
  const ethercat_msgs__srv__SetSdo_Request * value =
    (const ethercat_msgs__srv__SetSdo_Request *)(untyped_value);
  *item = *value;
}

bool ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__resize_function__SetSdo_Event__request(
  void * untyped_member, size_t size)
{
  ethercat_msgs__srv__SetSdo_Request__Sequence * member =
    (ethercat_msgs__srv__SetSdo_Request__Sequence *)(untyped_member);
  ethercat_msgs__srv__SetSdo_Request__Sequence__fini(member);
  return ethercat_msgs__srv__SetSdo_Request__Sequence__init(member, size);
}

size_t ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__size_function__SetSdo_Event__response(
  const void * untyped_member)
{
  const ethercat_msgs__srv__SetSdo_Response__Sequence * member =
    (const ethercat_msgs__srv__SetSdo_Response__Sequence *)(untyped_member);
  return member->size;
}

const void * ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_const_function__SetSdo_Event__response(
  const void * untyped_member, size_t index)
{
  const ethercat_msgs__srv__SetSdo_Response__Sequence * member =
    (const ethercat_msgs__srv__SetSdo_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void * ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_function__SetSdo_Event__response(
  void * untyped_member, size_t index)
{
  ethercat_msgs__srv__SetSdo_Response__Sequence * member =
    (ethercat_msgs__srv__SetSdo_Response__Sequence *)(untyped_member);
  return &member->data[index];
}

void ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__fetch_function__SetSdo_Event__response(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const ethercat_msgs__srv__SetSdo_Response * item =
    ((const ethercat_msgs__srv__SetSdo_Response *)
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_const_function__SetSdo_Event__response(untyped_member, index));
  ethercat_msgs__srv__SetSdo_Response * value =
    (ethercat_msgs__srv__SetSdo_Response *)(untyped_value);
  *value = *item;
}

void ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__assign_function__SetSdo_Event__response(
  void * untyped_member, size_t index, const void * untyped_value)
{
  ethercat_msgs__srv__SetSdo_Response * item =
    ((ethercat_msgs__srv__SetSdo_Response *)
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_function__SetSdo_Event__response(untyped_member, index));
  const ethercat_msgs__srv__SetSdo_Response * value =
    (const ethercat_msgs__srv__SetSdo_Response *)(untyped_value);
  *item = *value;
}

bool ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__resize_function__SetSdo_Event__response(
  void * untyped_member, size_t size)
{
  ethercat_msgs__srv__SetSdo_Response__Sequence * member =
    (ethercat_msgs__srv__SetSdo_Response__Sequence *)(untyped_member);
  ethercat_msgs__srv__SetSdo_Response__Sequence__fini(member);
  return ethercat_msgs__srv__SetSdo_Response__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_member_array[3] = {
  {
    "info",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Event, info),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "request",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Event, request),  // bytes offset in struct
    NULL,  // default value
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__size_function__SetSdo_Event__request,  // size() function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_const_function__SetSdo_Event__request,  // get_const(index) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_function__SetSdo_Event__request,  // get(index) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__fetch_function__SetSdo_Event__request,  // fetch(index, &value) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__assign_function__SetSdo_Event__request,  // assign(index, value) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__resize_function__SetSdo_Event__request  // resize(index) function pointer
  },
  {
    "response",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    1,  // array size
    true,  // is upper bound
    offsetof(ethercat_msgs__srv__SetSdo_Event, response),  // bytes offset in struct
    NULL,  // default value
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__size_function__SetSdo_Event__response,  // size() function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_const_function__SetSdo_Event__response,  // get_const(index) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__get_function__SetSdo_Event__response,  // get(index) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__fetch_function__SetSdo_Event__response,  // fetch(index, &value) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__assign_function__SetSdo_Event__response,  // assign(index, value) function pointer
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__resize_function__SetSdo_Event__response  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_members = {
  "ethercat_msgs__srv",  // message namespace
  "SetSdo_Event",  // message name
  3,  // number of fields
  sizeof(ethercat_msgs__srv__SetSdo_Event),
  false,  // has_any_key_member_
  ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_member_array,  // message members
  ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_init_function,  // function to initialize message memory (memory has to be allocated)
  ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_type_support_handle = {
  0,
  &ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_members,
  get_message_typesupport_handle_function,
  &ethercat_msgs__srv__SetSdo_Event__get_type_hash,
  &ethercat_msgs__srv__SetSdo_Event__get_type_description,
  &ethercat_msgs__srv__SetSdo_Event__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ethercat_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Event)() {
  ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, service_msgs, msg, ServiceEventInfo)();
  ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Request)();
  ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Response)();
  if (!ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_type_support_handle.typesupport_identifier) {
    ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ethercat_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "ethercat_msgs/srv/detail/set_sdo__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_service_members = {
  "ethercat_msgs__srv",  // service namespace
  "SetSdo",  // service name
  // the following fields are initialized below on first access
  NULL,  // request message
  // ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_Request_message_type_support_handle,
  NULL,  // response message
  // ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_Response_message_type_support_handle
  NULL  // event_message
  // ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_Response_message_type_support_handle
};


static rosidl_service_type_support_t ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_service_type_support_handle = {
  0,
  &ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_service_members,
  get_service_typesupport_handle_function,
  &ethercat_msgs__srv__SetSdo_Request__rosidl_typesupport_introspection_c__SetSdo_Request_message_type_support_handle,
  &ethercat_msgs__srv__SetSdo_Response__rosidl_typesupport_introspection_c__SetSdo_Response_message_type_support_handle,
  &ethercat_msgs__srv__SetSdo_Event__rosidl_typesupport_introspection_c__SetSdo_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    ethercat_msgs,
    srv,
    SetSdo
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    ethercat_msgs,
    srv,
    SetSdo
  ),
  &ethercat_msgs__srv__SetSdo__get_type_hash,
  &ethercat_msgs__srv__SetSdo__get_type_description,
  &ethercat_msgs__srv__SetSdo__get_type_description_sources,
};

// Forward declaration of message type support functions for service members
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Request)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Response)(void);

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Event)(void);

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ethercat_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo)(void) {
  if (!ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_service_type_support_handle.typesupport_identifier) {
    ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Response)()->data;
  }
  if (!service_members->event_members_) {
    service_members->event_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, SetSdo_Event)()->data;
  }

  return &ethercat_msgs__srv__detail__set_sdo__rosidl_typesupport_introspection_c__SetSdo_service_type_support_handle;
}

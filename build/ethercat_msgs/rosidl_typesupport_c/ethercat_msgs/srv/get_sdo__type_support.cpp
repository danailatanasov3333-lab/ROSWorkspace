// generated from rosidl_typesupport_c/resource/idl__type_support.cpp.em
// with input from ethercat_msgs:srv/GetSdo.idl
// generated code does not contain a copyright notice

#include "cstddef"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "ethercat_msgs/srv/detail/get_sdo__struct.h"
#include "ethercat_msgs/srv/detail/get_sdo__type_support.h"
#include "ethercat_msgs/srv/detail/get_sdo__functions.h"
#include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/message_type_support_dispatch.h"
#include "rosidl_typesupport_c/type_support_map.h"
#include "rosidl_typesupport_c/visibility_control.h"
#include "rosidl_typesupport_interface/macros.h"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _GetSdo_Request_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSdo_Request_type_support_ids_t;

static const _GetSdo_Request_type_support_ids_t _GetSdo_Request_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _GetSdo_Request_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSdo_Request_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSdo_Request_type_support_symbol_names_t _GetSdo_Request_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ethercat_msgs, srv, GetSdo_Request)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, GetSdo_Request)),
  }
};

typedef struct _GetSdo_Request_type_support_data_t
{
  void * data[2];
} _GetSdo_Request_type_support_data_t;

static _GetSdo_Request_type_support_data_t _GetSdo_Request_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSdo_Request_message_typesupport_map = {
  2,
  "ethercat_msgs",
  &_GetSdo_Request_message_typesupport_ids.typesupport_identifier[0],
  &_GetSdo_Request_message_typesupport_symbol_names.symbol_name[0],
  &_GetSdo_Request_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSdo_Request_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSdo_Request_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &ethercat_msgs__srv__GetSdo_Request__get_type_hash,
  &ethercat_msgs__srv__GetSdo_Request__get_type_description,
  &ethercat_msgs__srv__GetSdo_Request__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace ethercat_msgs

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, ethercat_msgs, srv, GetSdo_Request)() {
  return &::ethercat_msgs::srv::rosidl_typesupport_c::GetSdo_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__struct.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__type_support.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__functions.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _GetSdo_Response_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSdo_Response_type_support_ids_t;

static const _GetSdo_Response_type_support_ids_t _GetSdo_Response_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _GetSdo_Response_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSdo_Response_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSdo_Response_type_support_symbol_names_t _GetSdo_Response_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ethercat_msgs, srv, GetSdo_Response)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, GetSdo_Response)),
  }
};

typedef struct _GetSdo_Response_type_support_data_t
{
  void * data[2];
} _GetSdo_Response_type_support_data_t;

static _GetSdo_Response_type_support_data_t _GetSdo_Response_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSdo_Response_message_typesupport_map = {
  2,
  "ethercat_msgs",
  &_GetSdo_Response_message_typesupport_ids.typesupport_identifier[0],
  &_GetSdo_Response_message_typesupport_symbol_names.symbol_name[0],
  &_GetSdo_Response_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSdo_Response_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSdo_Response_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &ethercat_msgs__srv__GetSdo_Response__get_type_hash,
  &ethercat_msgs__srv__GetSdo_Response__get_type_description,
  &ethercat_msgs__srv__GetSdo_Response__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace ethercat_msgs

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, ethercat_msgs, srv, GetSdo_Response)() {
  return &::ethercat_msgs::srv::rosidl_typesupport_c::GetSdo_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__struct.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__type_support.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__functions.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
// already included above
// #include "rosidl_typesupport_c/message_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_c/visibility_control.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_c
{

typedef struct _GetSdo_Event_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSdo_Event_type_support_ids_t;

static const _GetSdo_Event_type_support_ids_t _GetSdo_Event_message_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _GetSdo_Event_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSdo_Event_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSdo_Event_type_support_symbol_names_t _GetSdo_Event_message_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ethercat_msgs, srv, GetSdo_Event)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, GetSdo_Event)),
  }
};

typedef struct _GetSdo_Event_type_support_data_t
{
  void * data[2];
} _GetSdo_Event_type_support_data_t;

static _GetSdo_Event_type_support_data_t _GetSdo_Event_message_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSdo_Event_message_typesupport_map = {
  2,
  "ethercat_msgs",
  &_GetSdo_Event_message_typesupport_ids.typesupport_identifier[0],
  &_GetSdo_Event_message_typesupport_symbol_names.symbol_name[0],
  &_GetSdo_Event_message_typesupport_data.data[0],
};

static const rosidl_message_type_support_t GetSdo_Event_message_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSdo_Event_message_typesupport_map),
  rosidl_typesupport_c__get_message_typesupport_handle_function,
  &ethercat_msgs__srv__GetSdo_Event__get_type_hash,
  &ethercat_msgs__srv__GetSdo_Event__get_type_description,
  &ethercat_msgs__srv__GetSdo_Event__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace ethercat_msgs

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_c, ethercat_msgs, srv, GetSdo_Event)() {
  return &::ethercat_msgs::srv::rosidl_typesupport_c::GetSdo_Event_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "cstddef"
#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "ethercat_msgs/srv/detail/get_sdo__type_support.h"
// already included above
// #include "rosidl_typesupport_c/identifier.h"
#include "rosidl_typesupport_c/service_type_support_dispatch.h"
// already included above
// #include "rosidl_typesupport_c/type_support_map.h"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
#include "service_msgs/msg/service_event_info.h"
#include "builtin_interfaces/msg/time.h"

namespace ethercat_msgs
{

namespace srv
{

namespace rosidl_typesupport_c
{
typedef struct _GetSdo_type_support_ids_t
{
  const char * typesupport_identifier[2];
} _GetSdo_type_support_ids_t;

static const _GetSdo_type_support_ids_t _GetSdo_service_typesupport_ids = {
  {
    "rosidl_typesupport_fastrtps_c",  // ::rosidl_typesupport_fastrtps_c::typesupport_identifier,
    "rosidl_typesupport_introspection_c",  // ::rosidl_typesupport_introspection_c::typesupport_identifier,
  }
};

typedef struct _GetSdo_type_support_symbol_names_t
{
  const char * symbol_name[2];
} _GetSdo_type_support_symbol_names_t;

#define STRINGIFY_(s) #s
#define STRINGIFY(s) STRINGIFY_(s)

static const _GetSdo_type_support_symbol_names_t _GetSdo_service_typesupport_symbol_names = {
  {
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, ethercat_msgs, srv, GetSdo)),
    STRINGIFY(ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ethercat_msgs, srv, GetSdo)),
  }
};

typedef struct _GetSdo_type_support_data_t
{
  void * data[2];
} _GetSdo_type_support_data_t;

static _GetSdo_type_support_data_t _GetSdo_service_typesupport_data = {
  {
    0,  // will store the shared library later
    0,  // will store the shared library later
  }
};

static const type_support_map_t _GetSdo_service_typesupport_map = {
  2,
  "ethercat_msgs",
  &_GetSdo_service_typesupport_ids.typesupport_identifier[0],
  &_GetSdo_service_typesupport_symbol_names.symbol_name[0],
  &_GetSdo_service_typesupport_data.data[0],
};

static const rosidl_service_type_support_t GetSdo_service_type_support_handle = {
  rosidl_typesupport_c__typesupport_identifier,
  reinterpret_cast<const type_support_map_t *>(&_GetSdo_service_typesupport_map),
  rosidl_typesupport_c__get_service_typesupport_handle_function,
  &GetSdo_Request_message_type_support_handle,
  &GetSdo_Response_message_type_support_handle,
  &GetSdo_Event_message_type_support_handle,
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_CREATE_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    ethercat_msgs,
    srv,
    GetSdo
  ),
  ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_DESTROY_EVENT_MESSAGE_SYMBOL_NAME(
    rosidl_typesupport_c,
    ethercat_msgs,
    srv,
    GetSdo
  ),
  &ethercat_msgs__srv__GetSdo__get_type_hash,
  &ethercat_msgs__srv__GetSdo__get_type_description,
  &ethercat_msgs__srv__GetSdo__get_type_description_sources,
};

}  // namespace rosidl_typesupport_c

}  // namespace srv

}  // namespace ethercat_msgs

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_c, ethercat_msgs, srv, GetSdo)() {
  return &::ethercat_msgs::srv::rosidl_typesupport_c::GetSdo_service_type_support_handle;
}

#ifdef __cplusplus
}
#endif

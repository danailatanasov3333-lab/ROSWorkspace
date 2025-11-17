

#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetSdo_Request {
    pub master_id: i16,
    pub slave_position: i16,
    pub sdo_index: i16,
    pub sdo_subindex: i16,
    pub sdo_data_type: std::string::String,
    pub sdo_value: std::string::String,
}



impl Default for SetSdo_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::srv::rmw::SetSdo_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SetSdo_Request {
  type RmwMsg = crate::srv::rmw::SetSdo_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        master_id: msg.master_id,
        slave_position: msg.slave_position,
        sdo_index: msg.sdo_index,
        sdo_subindex: msg.sdo_subindex,
        sdo_data_type: msg.sdo_data_type.as_str().into(),
        sdo_value: msg.sdo_value.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      master_id: msg.master_id,
      slave_position: msg.slave_position,
      sdo_index: msg.sdo_index,
      sdo_subindex: msg.sdo_subindex,
        sdo_data_type: msg.sdo_data_type.as_str().into(),
        sdo_value: msg.sdo_value.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      master_id: msg.master_id,
      slave_position: msg.slave_position,
      sdo_index: msg.sdo_index,
      sdo_subindex: msg.sdo_subindex,
      sdo_data_type: msg.sdo_data_type.to_string(),
      sdo_value: msg.sdo_value.to_string(),
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetSdo_Response {
    pub success: bool,
    pub sdo_return_message: std::string::String,
}



impl Default for SetSdo_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::srv::rmw::SetSdo_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SetSdo_Response {
  type RmwMsg = crate::srv::rmw::SetSdo_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
        sdo_return_message: msg.sdo_return_message.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
        sdo_return_message: msg.sdo_return_message.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
      sdo_return_message: msg.sdo_return_message.to_string(),
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetSdo_Request {
    pub master_id: i16,
    pub slave_position: u16,
    pub sdo_index: u16,
    pub sdo_subindex: u8,
    pub sdo_data_type: std::string::String,
}



impl Default for GetSdo_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::srv::rmw::GetSdo_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetSdo_Request {
  type RmwMsg = crate::srv::rmw::GetSdo_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        master_id: msg.master_id,
        slave_position: msg.slave_position,
        sdo_index: msg.sdo_index,
        sdo_subindex: msg.sdo_subindex,
        sdo_data_type: msg.sdo_data_type.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      master_id: msg.master_id,
      slave_position: msg.slave_position,
      sdo_index: msg.sdo_index,
      sdo_subindex: msg.sdo_subindex,
        sdo_data_type: msg.sdo_data_type.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      master_id: msg.master_id,
      slave_position: msg.slave_position,
      sdo_index: msg.sdo_index,
      sdo_subindex: msg.sdo_subindex,
      sdo_data_type: msg.sdo_data_type.to_string(),
    }
  }
}


#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetSdo_Response {
    pub success: bool,
    pub sdo_return_message: std::string::String,
    pub sdo_return_value_string: std::string::String,
    pub sdo_return_value: f64,
}



impl Default for GetSdo_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(crate::srv::rmw::GetSdo_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetSdo_Response {
  type RmwMsg = crate::srv::rmw::GetSdo_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
        sdo_return_message: msg.sdo_return_message.as_str().into(),
        sdo_return_value_string: msg.sdo_return_value_string.as_str().into(),
        sdo_return_value: msg.sdo_return_value,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
        sdo_return_message: msg.sdo_return_message.as_str().into(),
        sdo_return_value_string: msg.sdo_return_value_string.as_str().into(),
      sdo_return_value: msg.sdo_return_value,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
      sdo_return_message: msg.sdo_return_message.to_string(),
      sdo_return_value_string: msg.sdo_return_value_string.to_string(),
      sdo_return_value: msg.sdo_return_value,
    }
  }
}






#[link(name = "ethercat_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__SetSdo() -> *const std::ffi::c_void;
}

// Corresponds to ethercat_msgs__srv__SetSdo
pub struct SetSdo;

impl rosidl_runtime_rs::Service for SetSdo {
  type Request = crate::srv::SetSdo_Request;
  type Response = crate::srv::SetSdo_Response;

  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__SetSdo() }
  }
}




#[link(name = "ethercat_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__GetSdo() -> *const std::ffi::c_void;
}

// Corresponds to ethercat_msgs__srv__GetSdo
pub struct GetSdo;

impl rosidl_runtime_rs::Service for GetSdo {
  type Request = crate::srv::GetSdo_Request;
  type Response = crate::srv::GetSdo_Response;

  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__GetSdo() }
  }
}




pub mod rmw {

#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};

#[link(name = "ethercat_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__SetSdo_Request() -> *const std::ffi::c_void;
}

#[link(name = "ethercat_msgs__rosidl_generator_c")]
extern "C" {
    fn ethercat_msgs__srv__SetSdo_Request__init(msg: *mut SetSdo_Request) -> bool;
    fn ethercat_msgs__srv__SetSdo_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetSdo_Request>, size: usize) -> bool;
    fn ethercat_msgs__srv__SetSdo_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetSdo_Request>);
    fn ethercat_msgs__srv__SetSdo_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetSdo_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<SetSdo_Request>) -> bool;
}

// Corresponds to ethercat_msgs__srv__SetSdo_Request
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetSdo_Request {
    pub master_id: i16,
    pub slave_position: i16,
    pub sdo_index: i16,
    pub sdo_subindex: i16,
    pub sdo_data_type: rosidl_runtime_rs::String,
    pub sdo_value: rosidl_runtime_rs::String,
}



impl Default for SetSdo_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ethercat_msgs__srv__SetSdo_Request__init(&mut msg as *mut _) {
        panic!("Call to ethercat_msgs__srv__SetSdo_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetSdo_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__SetSdo_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__SetSdo_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__SetSdo_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetSdo_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetSdo_Request where Self: Sized {
  const TYPE_NAME: &'static str = "ethercat_msgs/srv/SetSdo_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__SetSdo_Request() }
  }
}


#[link(name = "ethercat_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__SetSdo_Response() -> *const std::ffi::c_void;
}

#[link(name = "ethercat_msgs__rosidl_generator_c")]
extern "C" {
    fn ethercat_msgs__srv__SetSdo_Response__init(msg: *mut SetSdo_Response) -> bool;
    fn ethercat_msgs__srv__SetSdo_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetSdo_Response>, size: usize) -> bool;
    fn ethercat_msgs__srv__SetSdo_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetSdo_Response>);
    fn ethercat_msgs__srv__SetSdo_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetSdo_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<SetSdo_Response>) -> bool;
}

// Corresponds to ethercat_msgs__srv__SetSdo_Response
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetSdo_Response {
    pub success: bool,
    pub sdo_return_message: rosidl_runtime_rs::String,
}



impl Default for SetSdo_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ethercat_msgs__srv__SetSdo_Response__init(&mut msg as *mut _) {
        panic!("Call to ethercat_msgs__srv__SetSdo_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetSdo_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__SetSdo_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__SetSdo_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__SetSdo_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetSdo_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetSdo_Response where Self: Sized {
  const TYPE_NAME: &'static str = "ethercat_msgs/srv/SetSdo_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__SetSdo_Response() }
  }
}


#[link(name = "ethercat_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__GetSdo_Request() -> *const std::ffi::c_void;
}

#[link(name = "ethercat_msgs__rosidl_generator_c")]
extern "C" {
    fn ethercat_msgs__srv__GetSdo_Request__init(msg: *mut GetSdo_Request) -> bool;
    fn ethercat_msgs__srv__GetSdo_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetSdo_Request>, size: usize) -> bool;
    fn ethercat_msgs__srv__GetSdo_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetSdo_Request>);
    fn ethercat_msgs__srv__GetSdo_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetSdo_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetSdo_Request>) -> bool;
}

// Corresponds to ethercat_msgs__srv__GetSdo_Request
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetSdo_Request {
    pub master_id: i16,
    pub slave_position: u16,
    pub sdo_index: u16,
    pub sdo_subindex: u8,
    pub sdo_data_type: rosidl_runtime_rs::String,
}



impl Default for GetSdo_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ethercat_msgs__srv__GetSdo_Request__init(&mut msg as *mut _) {
        panic!("Call to ethercat_msgs__srv__GetSdo_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetSdo_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__GetSdo_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__GetSdo_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__GetSdo_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetSdo_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetSdo_Request where Self: Sized {
  const TYPE_NAME: &'static str = "ethercat_msgs/srv/GetSdo_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__GetSdo_Request() }
  }
}


#[link(name = "ethercat_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__GetSdo_Response() -> *const std::ffi::c_void;
}

#[link(name = "ethercat_msgs__rosidl_generator_c")]
extern "C" {
    fn ethercat_msgs__srv__GetSdo_Response__init(msg: *mut GetSdo_Response) -> bool;
    fn ethercat_msgs__srv__GetSdo_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetSdo_Response>, size: usize) -> bool;
    fn ethercat_msgs__srv__GetSdo_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetSdo_Response>);
    fn ethercat_msgs__srv__GetSdo_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetSdo_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetSdo_Response>) -> bool;
}

// Corresponds to ethercat_msgs__srv__GetSdo_Response
#[repr(C)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetSdo_Response {
    pub success: bool,
    pub sdo_return_message: rosidl_runtime_rs::String,
    pub sdo_return_value_string: rosidl_runtime_rs::String,
    pub sdo_return_value: f64,
}



impl Default for GetSdo_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !ethercat_msgs__srv__GetSdo_Response__init(&mut msg as *mut _) {
        panic!("Call to ethercat_msgs__srv__GetSdo_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetSdo_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__GetSdo_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__GetSdo_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { ethercat_msgs__srv__GetSdo_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetSdo_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetSdo_Response where Self: Sized {
  const TYPE_NAME: &'static str = "ethercat_msgs/srv/GetSdo_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__ethercat_msgs__srv__GetSdo_Response() }
  }
}






  #[link(name = "ethercat_msgs__rosidl_typesupport_c")]
  extern "C" {
      fn rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__SetSdo() -> *const std::ffi::c_void;
  }

  // Corresponds to ethercat_msgs__srv__SetSdo
  pub struct SetSdo;

  impl rosidl_runtime_rs::Service for SetSdo {
    type Request = crate::srv::rmw::SetSdo_Request;
    type Response = crate::srv::rmw::SetSdo_Response;

    fn get_type_support() -> *const std::ffi::c_void {
      // SAFETY: No preconditions for this function.
      unsafe { rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__SetSdo() }
    }
  }




  #[link(name = "ethercat_msgs__rosidl_typesupport_c")]
  extern "C" {
      fn rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__GetSdo() -> *const std::ffi::c_void;
  }

  // Corresponds to ethercat_msgs__srv__GetSdo
  pub struct GetSdo;

  impl rosidl_runtime_rs::Service for GetSdo {
    type Request = crate::srv::rmw::GetSdo_Request;
    type Response = crate::srv::rmw::GetSdo_Response;

    fn get_type_support() -> *const std::ffi::c_void {
      // SAFETY: No preconditions for this function.
      unsafe { rosidl_typesupport_c__get_service_type_support_handle__ethercat_msgs__srv__GetSdo() }
    }
  }


}  // mod rmw

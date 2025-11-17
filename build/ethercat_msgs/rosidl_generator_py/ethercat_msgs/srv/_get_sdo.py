# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ethercat_msgs:srv/GetSdo.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
from os import getenv
import typing

import rosidl_pycommon.interface_base_classes

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_GetSdo_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'GetSdo_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class GetSdo_RequestConstants(typing.TypedDict):
        pass

    __constants: GetSdo_RequestConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('ethercat_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ethercat_msgs.srv.GetSdo_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_sdo__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_sdo__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_sdo__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_sdo__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_sdo__request

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetSdo_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_GetSdo_Request):
    """Message class 'GetSdo_Request'."""

    __slots__ = [
        '_master_id',
        '_slave_position',
        '_sdo_index',
        '_sdo_subindex',
        '_sdo_data_type',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'master_id': 'int16',
        'slave_position': 'uint16',
        'sdo_index': 'uint16',
        'sdo_subindex': 'uint8',
        'sdo_data_type': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 master_id: typing.Optional[int] = None,  # noqa: E501
                 slave_position: typing.Optional[int] = None,  # noqa: E501
                 sdo_index: typing.Optional[int] = None,  # noqa: E501
                 sdo_subindex: typing.Optional[int] = None,  # noqa: E501
                 sdo_data_type: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.master_id = master_id if master_id is not None else int()
        self.slave_position = slave_position if slave_position is not None else int()
        self.sdo_index = sdo_index if sdo_index is not None else int()
        self.sdo_subindex = sdo_subindex if sdo_subindex is not None else int()
        self.sdo_data_type = sdo_data_type if sdo_data_type is not None else str()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GetSdo_Request):
            return False
        if self.master_id != other.master_id:
            return False
        if self.slave_position != other.slave_position:
            return False
        if self.sdo_index != other.sdo_index:
            return False
        if self.sdo_subindex != other.sdo_subindex:
            return False
        if self.sdo_data_type != other.sdo_data_type:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def master_id(self) -> int:
        """Message field 'master_id'."""
        return self._master_id

    @master_id.setter
    def master_id(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'master_id' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'master_id' field must be an integer in [-32768, 32767]"
        self._master_id = value

    @builtins.property
    def slave_position(self) -> int:
        """Message field 'slave_position'."""
        return self._slave_position

    @slave_position.setter
    def slave_position(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'slave_position' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'slave_position' field must be an unsigned integer in [0, 65535]"
        self._slave_position = value

    @builtins.property
    def sdo_index(self) -> int:
        """Message field 'sdo_index'."""
        return self._sdo_index

    @sdo_index.setter
    def sdo_index(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'sdo_index' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'sdo_index' field must be an unsigned integer in [0, 65535]"
        self._sdo_index = value

    @builtins.property
    def sdo_subindex(self) -> int:
        """Message field 'sdo_subindex'."""
        return self._sdo_subindex

    @sdo_subindex.setter
    def sdo_subindex(self, value: int) -> None:
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'sdo_subindex' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'sdo_subindex' field must be an unsigned integer in [0, 255]"
        self._sdo_subindex = value

    @builtins.property
    def sdo_data_type(self) -> str:
        """Message field 'sdo_data_type'."""
        return self._sdo_data_type

    @sdo_data_type.setter
    def sdo_data_type(self, value: str) -> None:
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'sdo_data_type' field must be of type 'str'"
        self._sdo_data_type = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_GetSdo_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'GetSdo_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class GetSdo_ResponseConstants(typing.TypedDict):
        pass

    __constants: GetSdo_ResponseConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('ethercat_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ethercat_msgs.srv.GetSdo_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_sdo__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_sdo__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_sdo__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_sdo__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_sdo__response

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetSdo_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_GetSdo_Response):
    """Message class 'GetSdo_Response'."""

    __slots__ = [
        '_success',
        '_sdo_return_message',
        '_sdo_return_value_string',
        '_sdo_return_value',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'success': 'boolean',
        'sdo_return_message': 'string',
        'sdo_return_value_string': 'string',
        'sdo_return_value': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, *,
                 success: typing.Optional[bool] = None,  # noqa: E501
                 sdo_return_message: typing.Optional[str] = None,  # noqa: E501
                 sdo_return_value_string: typing.Optional[str] = None,  # noqa: E501
                 sdo_return_value: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.success = success if success is not None else bool()
        self.sdo_return_message = sdo_return_message if sdo_return_message is not None else str()
        self.sdo_return_value_string = sdo_return_value_string if sdo_return_value_string is not None else str()
        self.sdo_return_value = sdo_return_value if sdo_return_value is not None else float()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GetSdo_Response):
            return False
        if self.success != other.success:
            return False
        if self.sdo_return_message != other.sdo_return_message:
            return False
        if self.sdo_return_value_string != other.sdo_return_value_string:
            return False
        if self.sdo_return_value != other.sdo_return_value:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self) -> bool:
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value: bool) -> None:
        if self._check_fields:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def sdo_return_message(self) -> str:
        """Message field 'sdo_return_message'."""
        return self._sdo_return_message

    @sdo_return_message.setter
    def sdo_return_message(self, value: str) -> None:
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'sdo_return_message' field must be of type 'str'"
        self._sdo_return_message = value

    @builtins.property
    def sdo_return_value_string(self) -> str:
        """Message field 'sdo_return_value_string'."""
        return self._sdo_return_value_string

    @sdo_return_value_string.setter
    def sdo_return_value_string(self, value: str) -> None:
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'sdo_return_value_string' field must be of type 'str'"
        self._sdo_return_value_string = value

    @builtins.property
    def sdo_return_value(self) -> float:
        """Message field 'sdo_return_value'."""
        return self._sdo_return_value

    @sdo_return_value.setter
    def sdo_return_value(self, value: float) -> None:
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'sdo_return_value' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'sdo_return_value' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._sdo_return_value = value


if typing.TYPE_CHECKING:
    import collections
    from service_msgs.msg import ServiceEventInfo


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_GetSdo_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'GetSdo_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class GetSdo_EventConstants(typing.TypedDict):
        pass

    __constants: GetSdo_EventConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('ethercat_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ethercat_msgs.srv.GetSdo_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__get_sdo__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__get_sdo__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__get_sdo__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__get_sdo__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__get_sdo__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo._TYPE_SUPPORT is None:
                ServiceEventInfo.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class GetSdo_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_GetSdo_Event):
    """Message class 'GetSdo_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<ethercat_msgs/GetSdo_Request, 1>',
        'response': 'sequence<ethercat_msgs/GetSdo_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['ethercat_msgs', 'srv'], 'GetSdo_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['ethercat_msgs', 'srv'], 'GetSdo_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[typing.Union[collections.abc.Sequence[GetSdo_Request], collections.abc.Set[GetSdo_Request], collections.UserList[GetSdo_Request]]] = None,  # noqa: E501
                 response: typing.Optional[typing.Union[collections.abc.Sequence[GetSdo_Response], collections.abc.Set[GetSdo_Response], collections.UserList[GetSdo_Response]]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from service_msgs.msg import ServiceEventInfo
        self.info = info if info is not None else ServiceEventInfo()
        self.request = request if request is not None else []
        self.response = response if response is not None else []

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GetSdo_Event):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self) -> ServiceEventInfo:
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value: ServiceEventInfo) -> None:
        if self._check_fields:
            from service_msgs.msg import ServiceEventInfo
            assert \
                isinstance(value, ServiceEventInfo), \
                "The 'info' field must be a sub message of type 'ServiceEventInfo'"
        self._info = value

    @builtins.property
    def request(self) -> typing.Union[collections.abc.Sequence[GetSdo_Request], collections.abc.Set[GetSdo_Request], collections.UserList[GetSdo_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: typing.Union[collections.abc.Sequence[GetSdo_Request], collections.abc.Set[GetSdo_Request], collections.UserList[GetSdo_Request]]) -> None:
        if self._check_fields:
            from ethercat_msgs.srv import GetSdo_Request
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, GetSdo_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'GetSdo_Request'"
        self._request = value

    @builtins.property
    def response(self) -> typing.Union[collections.abc.Sequence[GetSdo_Response], collections.abc.Set[GetSdo_Response], collections.UserList[GetSdo_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: typing.Union[collections.abc.Sequence[GetSdo_Response], collections.abc.Set[GetSdo_Response], collections.UserList[GetSdo_Response]]) -> None:
        if self._check_fields:
            from ethercat_msgs.srv import GetSdo_Response
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) <= 1 and
                 all(isinstance(v, GetSdo_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'GetSdo_Response'"
        self._response = value


class Metaclass_GetSdo(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'GetSdo'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('ethercat_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'ethercat_msgs.srv.GetSdo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__get_sdo

            from ethercat_msgs.srv import _get_sdo
            if _get_sdo.Metaclass_GetSdo_Request._TYPE_SUPPORT is None:
                _get_sdo.Metaclass_GetSdo_Request.__import_type_support__()
            if _get_sdo.Metaclass_GetSdo_Response._TYPE_SUPPORT is None:
                _get_sdo.Metaclass_GetSdo_Response.__import_type_support__()
            if _get_sdo.Metaclass_GetSdo_Event._TYPE_SUPPORT is None:
                _get_sdo.Metaclass_GetSdo_Event.__import_type_support__()


class GetSdo(rosidl_pycommon.interface_base_classes.BaseService[
    GetSdo_Request,
    GetSdo_Response
], metaclass=Metaclass_GetSdo):
    Request: type[GetSdo_Request] = GetSdo_Request
    Response: type[GetSdo_Response] = GetSdo_Response
    from ethercat_msgs.srv._get_sdo import GetSdo_Event as Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')

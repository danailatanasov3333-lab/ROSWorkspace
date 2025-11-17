# generated from rosidl_generator_py/resource/_idl.py.em
# with input from ethercat_msgs:srv/SetSdo.idl
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


class Metaclass_SetSdo_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'SetSdo_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SetSdo_RequestConstants(typing.TypedDict):
        pass

    __constants: SetSdo_RequestConstants = {
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
                'ethercat_msgs.srv.SetSdo_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_sdo__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_sdo__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_sdo__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_sdo__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_sdo__request

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetSdo_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_SetSdo_Request):
    """Message class 'SetSdo_Request'."""

    __slots__ = [
        '_master_id',
        '_slave_position',
        '_sdo_index',
        '_sdo_subindex',
        '_sdo_data_type',
        '_sdo_value',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'master_id': 'int16',
        'slave_position': 'int16',
        'sdo_index': 'int16',
        'sdo_subindex': 'int16',
        'sdo_data_type': 'string',
        'sdo_value': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 master_id: typing.Optional[int] = None,  # noqa: E501
                 slave_position: typing.Optional[int] = None,  # noqa: E501
                 sdo_index: typing.Optional[int] = None,  # noqa: E501
                 sdo_subindex: typing.Optional[int] = None,  # noqa: E501
                 sdo_data_type: typing.Optional[str] = None,  # noqa: E501
                 sdo_value: typing.Optional[str] = None,  # noqa: E501
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
        self.sdo_value = sdo_value if sdo_value is not None else str()

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
        if not isinstance(other, SetSdo_Request):
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
        if self.sdo_value != other.sdo_value:
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
            assert value >= -32768 and value < 32768, \
                "The 'slave_position' field must be an integer in [-32768, 32767]"
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
            assert value >= -32768 and value < 32768, \
                "The 'sdo_index' field must be an integer in [-32768, 32767]"
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
            assert value >= -32768 and value < 32768, \
                "The 'sdo_subindex' field must be an integer in [-32768, 32767]"
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

    @builtins.property
    def sdo_value(self) -> str:
        """Message field 'sdo_value'."""
        return self._sdo_value

    @sdo_value.setter
    def sdo_value(self, value: str) -> None:
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'sdo_value' field must be of type 'str'"
        self._sdo_value = value


if typing.TYPE_CHECKING:
    pass


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetSdo_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'SetSdo_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SetSdo_ResponseConstants(typing.TypedDict):
        pass

    __constants: SetSdo_ResponseConstants = {
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
                'ethercat_msgs.srv.SetSdo_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_sdo__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_sdo__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_sdo__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_sdo__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_sdo__response

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetSdo_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_SetSdo_Response):
    """Message class 'SetSdo_Response'."""

    __slots__ = [
        '_success',
        '_sdo_return_message',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'success': 'boolean',
        'sdo_return_message': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 success: typing.Optional[bool] = None,  # noqa: E501
                 sdo_return_message: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.success = success if success is not None else bool()
        self.sdo_return_message = sdo_return_message if sdo_return_message is not None else str()

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
        if not isinstance(other, SetSdo_Response):
            return False
        if self.success != other.success:
            return False
        if self.sdo_return_message != other.sdo_return_message:
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


if typing.TYPE_CHECKING:
    import collections
    from service_msgs.msg import ServiceEventInfo


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetSdo_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'SetSdo_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class SetSdo_EventConstants(typing.TypedDict):
        pass

    __constants: SetSdo_EventConstants = {
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
                'ethercat_msgs.srv.SetSdo_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_sdo__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_sdo__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_sdo__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_sdo__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_sdo__event

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


class SetSdo_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_SetSdo_Event):
    """Message class 'SetSdo_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<ethercat_msgs/SetSdo_Request, 1>',
        'response': 'sequence<ethercat_msgs/SetSdo_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['ethercat_msgs', 'srv'], 'SetSdo_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['ethercat_msgs', 'srv'], 'SetSdo_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[typing.Union[collections.abc.Sequence[SetSdo_Request], collections.abc.Set[SetSdo_Request], collections.UserList[SetSdo_Request]]] = None,  # noqa: E501
                 response: typing.Optional[typing.Union[collections.abc.Sequence[SetSdo_Response], collections.abc.Set[SetSdo_Response], collections.UserList[SetSdo_Response]]] = None,  # noqa: E501
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
        if not isinstance(other, SetSdo_Event):
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
    def request(self) -> typing.Union[collections.abc.Sequence[SetSdo_Request], collections.abc.Set[SetSdo_Request], collections.UserList[SetSdo_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: typing.Union[collections.abc.Sequence[SetSdo_Request], collections.abc.Set[SetSdo_Request], collections.UserList[SetSdo_Request]]) -> None:
        if self._check_fields:
            from ethercat_msgs.srv import SetSdo_Request
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
                 all(isinstance(v, SetSdo_Request) for v in value) and
                 True), \
                "The 'request' field must be a set or sequence with length <= 1 and each value of type 'SetSdo_Request'"
        self._request = value

    @builtins.property
    def response(self) -> typing.Union[collections.abc.Sequence[SetSdo_Response], collections.abc.Set[SetSdo_Response], collections.UserList[SetSdo_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: typing.Union[collections.abc.Sequence[SetSdo_Response], collections.abc.Set[SetSdo_Response], collections.UserList[SetSdo_Response]]) -> None:
        if self._check_fields:
            from ethercat_msgs.srv import SetSdo_Response
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
                 all(isinstance(v, SetSdo_Response) for v in value) and
                 True), \
                "The 'response' field must be a set or sequence with length <= 1 and each value of type 'SetSdo_Response'"
        self._response = value


class Metaclass_SetSdo(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'SetSdo'."""

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
                'ethercat_msgs.srv.SetSdo')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_sdo

            from ethercat_msgs.srv import _set_sdo
            if _set_sdo.Metaclass_SetSdo_Request._TYPE_SUPPORT is None:
                _set_sdo.Metaclass_SetSdo_Request.__import_type_support__()
            if _set_sdo.Metaclass_SetSdo_Response._TYPE_SUPPORT is None:
                _set_sdo.Metaclass_SetSdo_Response.__import_type_support__()
            if _set_sdo.Metaclass_SetSdo_Event._TYPE_SUPPORT is None:
                _set_sdo.Metaclass_SetSdo_Event.__import_type_support__()


class SetSdo(rosidl_pycommon.interface_base_classes.BaseService[
    SetSdo_Request,
    SetSdo_Response
], metaclass=Metaclass_SetSdo):
    Request: type[SetSdo_Request] = SetSdo_Request
    Response: type[SetSdo_Response] = SetSdo_Response
    from ethercat_msgs.srv._set_sdo import SetSdo_Event as Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')

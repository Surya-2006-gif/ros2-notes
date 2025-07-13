// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from yolov8_msgs:msg/Detections.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "yolov8_msgs/msg/detail/detections__struct.h"
#include "yolov8_msgs/msg/detail/detections__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "yolov8_msgs/msg/detail/yolo__functions.h"
// end nested array functions include
bool yolov8_msgs__msg__yolo__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * yolov8_msgs__msg__yolo__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool yolov8_msgs__msg__detections__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[39];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("yolov8_msgs.msg._detections.Detections", full_classname_dest, 38) == 0);
  }
  yolov8_msgs__msg__Detections * ros_message = _ros_message;
  {  // detections
    PyObject * field = PyObject_GetAttrString(_pymsg, "detections");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'detections'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!yolov8_msgs__msg__Yolo__Sequence__init(&(ros_message->detections), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create yolov8_msgs__msg__Yolo__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    yolov8_msgs__msg__Yolo * dest = ros_message->detections.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!yolov8_msgs__msg__yolo__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * yolov8_msgs__msg__detections__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Detections */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("yolov8_msgs.msg._detections");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Detections");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  yolov8_msgs__msg__Detections * ros_message = (yolov8_msgs__msg__Detections *)raw_ros_message;
  {  // detections
    PyObject * field = NULL;
    size_t size = ros_message->detections.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    yolov8_msgs__msg__Yolo * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->detections.data[i]);
      PyObject * pyitem = yolov8_msgs__msg__yolo__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "detections", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

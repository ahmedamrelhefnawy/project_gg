'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_IMG_context_priority'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_IMG_context_priority',error_checker=_errors._error_checker)
EGL_CONTEXT_PRIORITY_HIGH_IMG=_C('EGL_CONTEXT_PRIORITY_HIGH_IMG',0x3101)
EGL_CONTEXT_PRIORITY_LEVEL_IMG=_C('EGL_CONTEXT_PRIORITY_LEVEL_IMG',0x3100)
EGL_CONTEXT_PRIORITY_LOW_IMG=_C('EGL_CONTEXT_PRIORITY_LOW_IMG',0x3103)
EGL_CONTEXT_PRIORITY_MEDIUM_IMG=_C('EGL_CONTEXT_PRIORITY_MEDIUM_IMG',0x3102)


'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_packed_depth_stencil'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_packed_depth_stencil',error_checker=_errors._error_checker)
GL_DEPTH_STENCIL_NV=_C('GL_DEPTH_STENCIL_NV',0x84F9)
GL_UNSIGNED_INT_24_8_NV=_C('GL_UNSIGNED_INT_24_8_NV',0x84FA)


'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_texture_buffer_object_rgb32'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_texture_buffer_object_rgb32',error_checker=_errors._error_checker)
GL_RGB32F=_C('GL_RGB32F',0x8815)
GL_RGB32I=_C('GL_RGB32I',0x8D83)
GL_RGB32UI=_C('GL_RGB32UI',0x8D71)


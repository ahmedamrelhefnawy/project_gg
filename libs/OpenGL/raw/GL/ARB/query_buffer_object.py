'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_query_buffer_object'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_query_buffer_object',error_checker=_errors._error_checker)
GL_QUERY_BUFFER=_C('GL_QUERY_BUFFER',0x9192)
GL_QUERY_BUFFER_BARRIER_BIT=_C('GL_QUERY_BUFFER_BARRIER_BIT',0x00008000)
GL_QUERY_BUFFER_BINDING=_C('GL_QUERY_BUFFER_BINDING',0x9193)
GL_QUERY_RESULT_NO_WAIT=_C('GL_QUERY_RESULT_NO_WAIT',0x9194)


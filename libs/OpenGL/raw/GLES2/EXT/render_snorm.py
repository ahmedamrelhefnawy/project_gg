'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_EXT_render_snorm'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_EXT_render_snorm',error_checker=_errors._error_checker)
GL_BYTE=_C('GL_BYTE',0x1400)
GL_R16_SNORM_EXT=_C('GL_R16_SNORM_EXT',0x8F98)
GL_R8_SNORM=_C('GL_R8_SNORM',0x8F94)
GL_RG16_SNORM_EXT=_C('GL_RG16_SNORM_EXT',0x8F99)
GL_RG8_SNORM=_C('GL_RG8_SNORM',0x8F95)
GL_RGBA16_SNORM_EXT=_C('GL_RGBA16_SNORM_EXT',0x8F9B)
GL_RGBA8_SNORM=_C('GL_RGBA8_SNORM',0x8F97)
GL_SHORT=_C('GL_SHORT',0x1402)


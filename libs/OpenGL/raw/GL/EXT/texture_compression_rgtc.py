'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_texture_compression_rgtc'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_texture_compression_rgtc',error_checker=_errors._error_checker)
GL_COMPRESSED_RED_GREEN_RGTC2_EXT=_C('GL_COMPRESSED_RED_GREEN_RGTC2_EXT',0x8DBD)
GL_COMPRESSED_RED_RGTC1_EXT=_C('GL_COMPRESSED_RED_RGTC1_EXT',0x8DBB)
GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT=_C('GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT',0x8DBE)
GL_COMPRESSED_SIGNED_RED_RGTC1_EXT=_C('GL_COMPRESSED_SIGNED_RED_RGTC1_EXT',0x8DBC)


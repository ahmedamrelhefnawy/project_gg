'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLSC2 import _types as _cs
# End users want this...
from OpenGL.raw.GLSC2._types import *
from OpenGL.raw.GLSC2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLSC2_EXT_texture_compression_s3tc'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLSC2,'GLSC2_EXT_texture_compression_s3tc',error_checker=_errors._error_checker)
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT=_C('GL_COMPRESSED_RGBA_S3TC_DXT1_EXT',0x83F1)
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT=_C('GL_COMPRESSED_RGBA_S3TC_DXT3_EXT',0x83F2)
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT=_C('GL_COMPRESSED_RGBA_S3TC_DXT5_EXT',0x83F3)
GL_COMPRESSED_RGB_S3TC_DXT1_EXT=_C('GL_COMPRESSED_RGB_S3TC_DXT1_EXT',0x83F0)


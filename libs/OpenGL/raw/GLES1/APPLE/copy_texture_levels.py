'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES1_APPLE_copy_texture_levels'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES1,'GLES1_APPLE_copy_texture_levels',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLint,_cs.GLsizei)
def glCopyTextureLevelsAPPLE(destinationTexture,sourceTexture,sourceBaseLevel,sourceLevelCount):pass

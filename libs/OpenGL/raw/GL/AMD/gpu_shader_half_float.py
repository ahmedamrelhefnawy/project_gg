'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_AMD_gpu_shader_half_float'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_AMD_gpu_shader_half_float',error_checker=_errors._error_checker)
GL_FLOAT16_MAT2_AMD=_C('GL_FLOAT16_MAT2_AMD',0x91C5)
GL_FLOAT16_MAT2x3_AMD=_C('GL_FLOAT16_MAT2x3_AMD',0x91C8)
GL_FLOAT16_MAT2x4_AMD=_C('GL_FLOAT16_MAT2x4_AMD',0x91C9)
GL_FLOAT16_MAT3_AMD=_C('GL_FLOAT16_MAT3_AMD',0x91C6)
GL_FLOAT16_MAT3x2_AMD=_C('GL_FLOAT16_MAT3x2_AMD',0x91CA)
GL_FLOAT16_MAT3x4_AMD=_C('GL_FLOAT16_MAT3x4_AMD',0x91CB)
GL_FLOAT16_MAT4_AMD=_C('GL_FLOAT16_MAT4_AMD',0x91C7)
GL_FLOAT16_MAT4x2_AMD=_C('GL_FLOAT16_MAT4x2_AMD',0x91CC)
GL_FLOAT16_MAT4x3_AMD=_C('GL_FLOAT16_MAT4x3_AMD',0x91CD)
GL_FLOAT16_NV=_C('GL_FLOAT16_NV',0x8FF8)
GL_FLOAT16_VEC2_NV=_C('GL_FLOAT16_VEC2_NV',0x8FF9)
GL_FLOAT16_VEC3_NV=_C('GL_FLOAT16_VEC3_NV',0x8FFA)
GL_FLOAT16_VEC4_NV=_C('GL_FLOAT16_VEC4_NV',0x8FFB)


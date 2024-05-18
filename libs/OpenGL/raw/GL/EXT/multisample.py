'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_multisample'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_multisample',error_checker=_errors._error_checker)
GL_1PASS_EXT=_C('GL_1PASS_EXT',0x80A1)
GL_2PASS_0_EXT=_C('GL_2PASS_0_EXT',0x80A2)
GL_2PASS_1_EXT=_C('GL_2PASS_1_EXT',0x80A3)
GL_4PASS_0_EXT=_C('GL_4PASS_0_EXT',0x80A4)
GL_4PASS_1_EXT=_C('GL_4PASS_1_EXT',0x80A5)
GL_4PASS_2_EXT=_C('GL_4PASS_2_EXT',0x80A6)
GL_4PASS_3_EXT=_C('GL_4PASS_3_EXT',0x80A7)
GL_MULTISAMPLE_BIT_EXT=_C('GL_MULTISAMPLE_BIT_EXT',0x20000000)
GL_MULTISAMPLE_EXT=_C('GL_MULTISAMPLE_EXT',0x809D)
GL_SAMPLES_EXT=_C('GL_SAMPLES_EXT',0x80A9)
GL_SAMPLE_ALPHA_TO_MASK_EXT=_C('GL_SAMPLE_ALPHA_TO_MASK_EXT',0x809E)
GL_SAMPLE_ALPHA_TO_ONE_EXT=_C('GL_SAMPLE_ALPHA_TO_ONE_EXT',0x809F)
GL_SAMPLE_BUFFERS_EXT=_C('GL_SAMPLE_BUFFERS_EXT',0x80A8)
GL_SAMPLE_MASK_EXT=_C('GL_SAMPLE_MASK_EXT',0x80A0)
GL_SAMPLE_MASK_INVERT_EXT=_C('GL_SAMPLE_MASK_INVERT_EXT',0x80AB)
GL_SAMPLE_MASK_VALUE_EXT=_C('GL_SAMPLE_MASK_VALUE_EXT',0x80AA)
GL_SAMPLE_PATTERN_EXT=_C('GL_SAMPLE_PATTERN_EXT',0x80AC)
@_f
@_p.types(None,_cs.GLclampf,_cs.GLboolean)
def glSampleMaskEXT(value,invert):pass
@_f
@_p.types(None,_cs.GLenum)
def glSamplePatternEXT(pattern):pass

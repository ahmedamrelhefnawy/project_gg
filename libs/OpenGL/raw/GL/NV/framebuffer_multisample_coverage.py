'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_framebuffer_multisample_coverage'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_framebuffer_multisample_coverage',error_checker=_errors._error_checker)
GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV=_C('GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV',0x8E11)
GL_MULTISAMPLE_COVERAGE_MODES_NV=_C('GL_MULTISAMPLE_COVERAGE_MODES_NV',0x8E12)
GL_RENDERBUFFER_COLOR_SAMPLES_NV=_C('GL_RENDERBUFFER_COLOR_SAMPLES_NV',0x8E10)
GL_RENDERBUFFER_COVERAGE_SAMPLES_NV=_C('GL_RENDERBUFFER_COVERAGE_SAMPLES_NV',0x8CAB)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageMultisampleCoverageNV(target,coverageSamples,colorSamples,internalformat,width,height):pass

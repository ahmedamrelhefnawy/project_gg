'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_NV_fence'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_NV_fence',error_checker=_errors._error_checker)
GL_ALL_COMPLETED_NV=_C('GL_ALL_COMPLETED_NV',0x84F2)
GL_FENCE_CONDITION_NV=_C('GL_FENCE_CONDITION_NV',0x84F4)
GL_FENCE_STATUS_NV=_C('GL_FENCE_STATUS_NV',0x84F3)
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteFencesNV(n,fences):pass
@_f
@_p.types(None,_cs.GLuint)
def glFinishFenceNV(fence):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenFencesNV(n,fences):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetFenceivNV(fence,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsFenceNV(fence):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glSetFenceNV(fence,condition):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glTestFenceNV(fence):pass

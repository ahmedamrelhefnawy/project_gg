'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_query_resource_tag'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_query_resource_tag',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLsizei,arrays.GLintArray)
def glDeleteQueryResourceTagNV(n,tagIds):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLintArray)
def glGenQueryResourceTagNV(n,tagIds):pass
@_f
@_p.types(None,_cs.GLint,arrays.GLcharArray)
def glQueryResourceTagNV(tagId,tagString):pass

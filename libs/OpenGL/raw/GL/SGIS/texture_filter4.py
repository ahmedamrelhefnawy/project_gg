'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIS_texture_filter4'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_SGIS_texture_filter4',error_checker=_errors._error_checker)
GL_FILTER4_SGIS=_C('GL_FILTER4_SGIS',0x8146)
GL_TEXTURE_FILTER4_SIZE_SGIS=_C('GL_TEXTURE_FILTER4_SIZE_SGIS',0x8147)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexFilterFuncSGIS(target,filter,weights):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,arrays.GLfloatArray)
def glTexFilterFuncSGIS(target,filter,n,weights):pass

'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_vertex_attrib_64bit'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_vertex_attrib_64bit',error_checker=_errors._error_checker)
GL_DOUBLE_MAT2=_C('GL_DOUBLE_MAT2',0x8F46)
GL_DOUBLE_MAT2x3=_C('GL_DOUBLE_MAT2x3',0x8F49)
GL_DOUBLE_MAT2x4=_C('GL_DOUBLE_MAT2x4',0x8F4A)
GL_DOUBLE_MAT3=_C('GL_DOUBLE_MAT3',0x8F47)
GL_DOUBLE_MAT3x2=_C('GL_DOUBLE_MAT3x2',0x8F4B)
GL_DOUBLE_MAT3x4=_C('GL_DOUBLE_MAT3x4',0x8F4C)
GL_DOUBLE_MAT4=_C('GL_DOUBLE_MAT4',0x8F48)
GL_DOUBLE_MAT4x2=_C('GL_DOUBLE_MAT4x2',0x8F4D)
GL_DOUBLE_MAT4x3=_C('GL_DOUBLE_MAT4x3',0x8F4E)
GL_DOUBLE_VEC2=_C('GL_DOUBLE_VEC2',0x8FFC)
GL_DOUBLE_VEC3=_C('GL_DOUBLE_VEC3',0x8FFD)
GL_DOUBLE_VEC4=_C('GL_DOUBLE_VEC4',0x8FFE)
GL_RGB32I=_C('GL_RGB32I',0x8D83)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLdoubleArray)
def glGetVertexAttribLdv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble)
def glVertexAttribL1d(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL1dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble)
def glVertexAttribL2d(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL2dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexAttribL3d(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL3dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexAttribL4d(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL4dv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribLPointer(index,size,type,stride,pointer):pass

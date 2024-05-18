'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_IMG_bindless_texture'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_IMG_bindless_texture',error_checker=_errors._error_checker)

@_f
@_p.types(_cs.GLuint64,_cs.GLuint)
def glGetTextureHandleIMG(texture):pass
@_f
@_p.types(_cs.GLuint64,_cs.GLuint,_cs.GLuint)
def glGetTextureSamplerHandleIMG(texture,sampler):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint64)
def glProgramUniformHandleui64IMG(program,location,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glProgramUniformHandleui64vIMG(program,location,count,values):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint64)
def glUniformHandleui64IMG(location,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glUniformHandleui64vIMG(location,count,value):pass

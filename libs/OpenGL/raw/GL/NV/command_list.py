'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_command_list'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_command_list',error_checker=_errors._error_checker)
GL_ALPHA_REF_COMMAND_NV=_C('GL_ALPHA_REF_COMMAND_NV',0x000F)
GL_ATTRIBUTE_ADDRESS_COMMAND_NV=_C('GL_ATTRIBUTE_ADDRESS_COMMAND_NV',0x0009)
GL_BLEND_COLOR_COMMAND_NV=_C('GL_BLEND_COLOR_COMMAND_NV',0x000B)
GL_DRAW_ARRAYS_COMMAND_NV=_C('GL_DRAW_ARRAYS_COMMAND_NV',0x0003)
GL_DRAW_ARRAYS_INSTANCED_COMMAND_NV=_C('GL_DRAW_ARRAYS_INSTANCED_COMMAND_NV',0x0007)
GL_DRAW_ARRAYS_STRIP_COMMAND_NV=_C('GL_DRAW_ARRAYS_STRIP_COMMAND_NV',0x0005)
GL_DRAW_ELEMENTS_COMMAND_NV=_C('GL_DRAW_ELEMENTS_COMMAND_NV',0x0002)
GL_DRAW_ELEMENTS_INSTANCED_COMMAND_NV=_C('GL_DRAW_ELEMENTS_INSTANCED_COMMAND_NV',0x0006)
GL_DRAW_ELEMENTS_STRIP_COMMAND_NV=_C('GL_DRAW_ELEMENTS_STRIP_COMMAND_NV',0x0004)
GL_ELEMENT_ADDRESS_COMMAND_NV=_C('GL_ELEMENT_ADDRESS_COMMAND_NV',0x0008)
GL_FRONT_FACE_COMMAND_NV=_C('GL_FRONT_FACE_COMMAND_NV',0x0012)
GL_LINE_WIDTH_COMMAND_NV=_C('GL_LINE_WIDTH_COMMAND_NV',0x000D)
GL_NOP_COMMAND_NV=_C('GL_NOP_COMMAND_NV',0x0001)
GL_POLYGON_OFFSET_COMMAND_NV=_C('GL_POLYGON_OFFSET_COMMAND_NV',0x000E)
GL_SCISSOR_COMMAND_NV=_C('GL_SCISSOR_COMMAND_NV',0x0011)
GL_STENCIL_REF_COMMAND_NV=_C('GL_STENCIL_REF_COMMAND_NV',0x000C)
GL_TERMINATE_SEQUENCE_COMMAND_NV=_C('GL_TERMINATE_SEQUENCE_COMMAND_NV',0x0000)
GL_UNIFORM_ADDRESS_COMMAND_NV=_C('GL_UNIFORM_ADDRESS_COMMAND_NV',0x000A)
GL_VIEWPORT_COMMAND_NV=_C('GL_VIEWPORT_COMMAND_NV',0x0010)
@_f
@_p.types(None,_cs.GLuint)
def glCallCommandListNV(list):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glCommandListSegmentsNV(list,segments):pass
@_f
@_p.types(None,_cs.GLuint)
def glCompileCommandListNV(list):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateCommandListsNV(n,lists):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glCreateStatesNV(n,states):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteCommandListsNV(n,lists):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteStatesNV(n,states):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuint64Array,arrays.GLsizeiArray,_cs.GLuint)
def glDrawCommandsAddressNV(primitiveMode,indirects,sizes,count):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,ctypes.POINTER(_cs.GLintptr),arrays.GLsizeiArray,_cs.GLuint)
def glDrawCommandsNV(primitiveMode,buffer,indirects,sizes,count):pass
@_f
@_p.types(None,arrays.GLuint64Array,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLuintArray,_cs.GLuint)
def glDrawCommandsStatesAddressNV(indirects,sizes,states,fbos,count):pass
@_f
@_p.types(None,_cs.GLuint,ctypes.POINTER(_cs.GLintptr),arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLuintArray,_cs.GLuint)
def glDrawCommandsStatesNV(buffer,indirects,sizes,states,fbos,count):pass
@_f
@_p.types(_cs.GLuint,_cs.GLenum,_cs.GLuint)
def glGetCommandHeaderNV(tokenID,size):pass
@_f
@_p.types(_cs.GLushort,_cs.GLenum)
def glGetStageIndexNV(shadertype):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsCommandListNV(list):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsStateNV(state):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,arrays.GLvoidpArray,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLuintArray,_cs.GLuint)
def glListDrawCommandsStatesClientNV(list,segment,indirects,sizes,states,fbos,count):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glStateCaptureNV(state,mode):pass

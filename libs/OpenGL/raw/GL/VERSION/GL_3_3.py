'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_VERSION_GL_3_3'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_VERSION_GL_3_3',error_checker=_errors._error_checker)
GL_ANY_SAMPLES_PASSED=_C('GL_ANY_SAMPLES_PASSED',0x8C2F)
GL_INT_2_10_10_10_REV=_C('GL_INT_2_10_10_10_REV',0x8D9F)
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS=_C('GL_MAX_DUAL_SOURCE_DRAW_BUFFERS',0x88FC)
GL_ONE_MINUS_SRC1_ALPHA=_C('GL_ONE_MINUS_SRC1_ALPHA',0x88FB)
GL_ONE_MINUS_SRC1_COLOR=_C('GL_ONE_MINUS_SRC1_COLOR',0x88FA)
GL_RGB10_A2UI=_C('GL_RGB10_A2UI',0x906F)
GL_SAMPLER_BINDING=_C('GL_SAMPLER_BINDING',0x8919)
GL_SRC1_COLOR=_C('GL_SRC1_COLOR',0x88F9)
GL_TEXTURE_SWIZZLE_A=_C('GL_TEXTURE_SWIZZLE_A',0x8E45)
GL_TEXTURE_SWIZZLE_B=_C('GL_TEXTURE_SWIZZLE_B',0x8E44)
GL_TEXTURE_SWIZZLE_G=_C('GL_TEXTURE_SWIZZLE_G',0x8E43)
GL_TEXTURE_SWIZZLE_R=_C('GL_TEXTURE_SWIZZLE_R',0x8E42)
GL_TEXTURE_SWIZZLE_RGBA=_C('GL_TEXTURE_SWIZZLE_RGBA',0x8E46)
GL_TIMESTAMP=_C('GL_TIMESTAMP',0x8E28)
GL_TIME_ELAPSED=_C('GL_TIME_ELAPSED',0x88BF)
GL_VERTEX_ATTRIB_ARRAY_DIVISOR=_C('GL_VERTEX_ATTRIB_ARRAY_DIVISOR',0x88FE)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLuint,arrays.GLcharArray)
def glBindFragDataLocationIndexed(program,colorNumber,index,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glBindSampler(unit,sampler):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glColorP3ui(type,color):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glColorP3uiv(type,color):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glColorP4ui(type,color):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glColorP4uiv(type,color):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteSamplers(count,samplers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenSamplers(count,samplers):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetFragDataIndex(program,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetQueryObjecti64v(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuint64Array)
def glGetQueryObjectui64v(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetSamplerParameterIiv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetSamplerParameterIuiv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetSamplerParameterfv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetSamplerParameteriv(sampler,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsSampler(sampler):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glMultiTexCoordP1ui(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glMultiTexCoordP1uiv(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glMultiTexCoordP2ui(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glMultiTexCoordP2uiv(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glMultiTexCoordP3ui(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glMultiTexCoordP3uiv(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glMultiTexCoordP4ui(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glMultiTexCoordP4uiv(texture,type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glNormalP3ui(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glNormalP3uiv(type,coords):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glQueryCounter(id,target):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glSamplerParameterIiv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glSamplerParameterIuiv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLfloat)
def glSamplerParameterf(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glSamplerParameterfv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glSamplerParameteri(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glSamplerParameteriv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glSecondaryColorP3ui(type,color):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glSecondaryColorP3uiv(type,color):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glTexCoordP1ui(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glTexCoordP1uiv(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glTexCoordP2ui(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glTexCoordP2uiv(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glTexCoordP3ui(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glTexCoordP3uiv(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glTexCoordP4ui(type,coords):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glTexCoordP4uiv(type,coords):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glVertexAttribDivisor(index,divisor):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,_cs.GLuint)
def glVertexAttribP1ui(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,arrays.GLuintArray)
def glVertexAttribP1uiv(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,_cs.GLuint)
def glVertexAttribP2ui(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,arrays.GLuintArray)
def glVertexAttribP2uiv(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,_cs.GLuint)
def glVertexAttribP3ui(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,arrays.GLuintArray)
def glVertexAttribP3uiv(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,_cs.GLuint)
def glVertexAttribP4ui(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLboolean,arrays.GLuintArray)
def glVertexAttribP4uiv(index,type,normalized,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glVertexP2ui(type,value):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glVertexP2uiv(type,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glVertexP3ui(type,value):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glVertexP3uiv(type,value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glVertexP4ui(type,value):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLuintArray)
def glVertexP4uiv(type,value):pass

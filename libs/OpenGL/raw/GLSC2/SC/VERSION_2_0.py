'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLSC2 import _types as _cs
# End users want this...
from OpenGL.raw.GLSC2._types import *
from OpenGL.raw.GLSC2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLSC2_SC_VERSION_2_0'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLSC2,'GLSC2_SC_VERSION_2_0',error_checker=_errors._error_checker)
GL_ACTIVE_TEXTURE=_C('GL_ACTIVE_TEXTURE',0x84E0)
GL_ALIASED_LINE_WIDTH_RANGE=_C('GL_ALIASED_LINE_WIDTH_RANGE',0x846E)
GL_ALIASED_POINT_SIZE_RANGE=_C('GL_ALIASED_POINT_SIZE_RANGE',0x846D)
GL_ALPHA_BITS=_C('GL_ALPHA_BITS',0x0D55)
GL_ALWAYS=_C('GL_ALWAYS',0x0207)
GL_ARRAY_BUFFER=_C('GL_ARRAY_BUFFER',0x8892)
GL_ARRAY_BUFFER_BINDING=_C('GL_ARRAY_BUFFER_BINDING',0x8894)
GL_BACK=_C('GL_BACK',0x0405)
GL_BLEND=_C('GL_BLEND',0x0BE2)
GL_BLEND_COLOR=_C('GL_BLEND_COLOR',0x8005)
GL_BLEND_DST_ALPHA=_C('GL_BLEND_DST_ALPHA',0x80CA)
GL_BLEND_DST_RGB=_C('GL_BLEND_DST_RGB',0x80C8)
GL_BLEND_EQUATION=_C('GL_BLEND_EQUATION',0x8009)
GL_BLEND_EQUATION_ALPHA=_C('GL_BLEND_EQUATION_ALPHA',0x883D)
GL_BLEND_EQUATION_RGB=_C('GL_BLEND_EQUATION_RGB',0x8009)
GL_BLEND_SRC_ALPHA=_C('GL_BLEND_SRC_ALPHA',0x80CB)
GL_BLEND_SRC_RGB=_C('GL_BLEND_SRC_RGB',0x80C9)
GL_BLUE_BITS=_C('GL_BLUE_BITS',0x0D54)
GL_BUFFER_SIZE=_C('GL_BUFFER_SIZE',0x8764)
GL_BUFFER_USAGE=_C('GL_BUFFER_USAGE',0x8765)
GL_BYTE=_C('GL_BYTE',0x1400)
GL_CCW=_C('GL_CCW',0x0901)
GL_CLAMP_TO_EDGE=_C('GL_CLAMP_TO_EDGE',0x812F)
GL_COLOR_ATTACHMENT0=_C('GL_COLOR_ATTACHMENT0',0x8CE0)
GL_COLOR_BUFFER_BIT=_C('GL_COLOR_BUFFER_BIT',0x00004000)
GL_COLOR_CLEAR_VALUE=_C('GL_COLOR_CLEAR_VALUE',0x0C22)
GL_COLOR_WRITEMASK=_C('GL_COLOR_WRITEMASK',0x0C23)
GL_COMPRESSED_TEXTURE_FORMATS=_C('GL_COMPRESSED_TEXTURE_FORMATS',0x86A3)
GL_CONSTANT_ALPHA=_C('GL_CONSTANT_ALPHA',0x8003)
GL_CONSTANT_COLOR=_C('GL_CONSTANT_COLOR',0x8001)
GL_CONTEXT_LOST=_C('GL_CONTEXT_LOST',0x0507)
GL_CONTEXT_ROBUST_ACCESS=_C('GL_CONTEXT_ROBUST_ACCESS',0x90F3)
GL_CULL_FACE=_C('GL_CULL_FACE',0x0B44)
GL_CULL_FACE_MODE=_C('GL_CULL_FACE_MODE',0x0B45)
GL_CURRENT_PROGRAM=_C('GL_CURRENT_PROGRAM',0x8B8D)
GL_CURRENT_VERTEX_ATTRIB=_C('GL_CURRENT_VERTEX_ATTRIB',0x8626)
GL_CW=_C('GL_CW',0x0900)
GL_DECR=_C('GL_DECR',0x1E03)
GL_DECR_WRAP=_C('GL_DECR_WRAP',0x8508)
GL_DEPTH_ATTACHMENT=_C('GL_DEPTH_ATTACHMENT',0x8D00)
GL_DEPTH_BITS=_C('GL_DEPTH_BITS',0x0D56)
GL_DEPTH_BUFFER_BIT=_C('GL_DEPTH_BUFFER_BIT',0x00000100)
GL_DEPTH_CLEAR_VALUE=_C('GL_DEPTH_CLEAR_VALUE',0x0B73)
GL_DEPTH_COMPONENT16=_C('GL_DEPTH_COMPONENT16',0x81A5)
GL_DEPTH_FUNC=_C('GL_DEPTH_FUNC',0x0B74)
GL_DEPTH_RANGE=_C('GL_DEPTH_RANGE',0x0B70)
GL_DEPTH_TEST=_C('GL_DEPTH_TEST',0x0B71)
GL_DEPTH_WRITEMASK=_C('GL_DEPTH_WRITEMASK',0x0B72)
GL_DITHER=_C('GL_DITHER',0x0BD0)
GL_DONT_CARE=_C('GL_DONT_CARE',0x1100)
GL_DST_ALPHA=_C('GL_DST_ALPHA',0x0304)
GL_DST_COLOR=_C('GL_DST_COLOR',0x0306)
GL_DYNAMIC_DRAW=_C('GL_DYNAMIC_DRAW',0x88E8)
GL_ELEMENT_ARRAY_BUFFER=_C('GL_ELEMENT_ARRAY_BUFFER',0x8893)
GL_ELEMENT_ARRAY_BUFFER_BINDING=_C('GL_ELEMENT_ARRAY_BUFFER_BINDING',0x8895)
GL_EQUAL=_C('GL_EQUAL',0x0202)
GL_EXTENSIONS=_C('GL_EXTENSIONS',0x1F03)
GL_FALSE=_C('GL_FALSE',0)
GL_FASTEST=_C('GL_FASTEST',0x1101)
GL_FLOAT=_C('GL_FLOAT',0x1406)
GL_FRAMEBUFFER=_C('GL_FRAMEBUFFER',0x8D40)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME',0x8CD1)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE',0x8CD0)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL',0x8CD2)
GL_FRAMEBUFFER_BINDING=_C('GL_FRAMEBUFFER_BINDING',0x8CA6)
GL_FRAMEBUFFER_COMPLETE=_C('GL_FRAMEBUFFER_COMPLETE',0x8CD5)
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT=_C('GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT',0x8CD6)
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS=_C('GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS',0x8CD9)
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT=_C('GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT',0x8CD7)
GL_FRAMEBUFFER_UNDEFINED=_C('GL_FRAMEBUFFER_UNDEFINED',0x8219)
GL_FRAMEBUFFER_UNSUPPORTED=_C('GL_FRAMEBUFFER_UNSUPPORTED',0x8CDD)
GL_FRONT=_C('GL_FRONT',0x0404)
GL_FRONT_AND_BACK=_C('GL_FRONT_AND_BACK',0x0408)
GL_FRONT_FACE=_C('GL_FRONT_FACE',0x0B46)
GL_FUNC_ADD=_C('GL_FUNC_ADD',0x8006)
GL_FUNC_REVERSE_SUBTRACT=_C('GL_FUNC_REVERSE_SUBTRACT',0x800B)
GL_FUNC_SUBTRACT=_C('GL_FUNC_SUBTRACT',0x800A)
GL_GENERATE_MIPMAP_HINT=_C('GL_GENERATE_MIPMAP_HINT',0x8192)
GL_GEQUAL=_C('GL_GEQUAL',0x0206)
GL_GREATER=_C('GL_GREATER',0x0204)
GL_GREEN_BITS=_C('GL_GREEN_BITS',0x0D53)
GL_GUILTY_CONTEXT_RESET=_C('GL_GUILTY_CONTEXT_RESET',0x8253)
GL_HIGH_FLOAT=_C('GL_HIGH_FLOAT',0x8DF2)
GL_HIGH_INT=_C('GL_HIGH_INT',0x8DF5)
GL_IMPLEMENTATION_COLOR_READ_FORMAT=_C('GL_IMPLEMENTATION_COLOR_READ_FORMAT',0x8B9B)
GL_IMPLEMENTATION_COLOR_READ_TYPE=_C('GL_IMPLEMENTATION_COLOR_READ_TYPE',0x8B9A)
GL_INCR=_C('GL_INCR',0x1E02)
GL_INCR_WRAP=_C('GL_INCR_WRAP',0x8507)
GL_INNOCENT_CONTEXT_RESET=_C('GL_INNOCENT_CONTEXT_RESET',0x8254)
GL_INT=_C('GL_INT',0x1404)
GL_INVALID_ENUM=_C('GL_INVALID_ENUM',0x0500)
GL_INVALID_FRAMEBUFFER_OPERATION=_C('GL_INVALID_FRAMEBUFFER_OPERATION',0x0506)
GL_INVALID_OPERATION=_C('GL_INVALID_OPERATION',0x0502)
GL_INVALID_VALUE=_C('GL_INVALID_VALUE',0x0501)
GL_INVERT=_C('GL_INVERT',0x150A)
GL_KEEP=_C('GL_KEEP',0x1E00)
GL_LEQUAL=_C('GL_LEQUAL',0x0203)
GL_LESS=_C('GL_LESS',0x0201)
GL_LINEAR=_C('GL_LINEAR',0x2601)
GL_LINEAR_MIPMAP_LINEAR=_C('GL_LINEAR_MIPMAP_LINEAR',0x2703)
GL_LINEAR_MIPMAP_NEAREST=_C('GL_LINEAR_MIPMAP_NEAREST',0x2701)
GL_LINES=_C('GL_LINES',0x0001)
GL_LINE_LOOP=_C('GL_LINE_LOOP',0x0002)
GL_LINE_STRIP=_C('GL_LINE_STRIP',0x0003)
GL_LINE_WIDTH=_C('GL_LINE_WIDTH',0x0B21)
GL_LINK_STATUS=_C('GL_LINK_STATUS',0x8B82)
GL_LOSE_CONTEXT_ON_RESET=_C('GL_LOSE_CONTEXT_ON_RESET',0x8252)
GL_LOW_FLOAT=_C('GL_LOW_FLOAT',0x8DF0)
GL_LOW_INT=_C('GL_LOW_INT',0x8DF3)
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS=_C('GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS',0x8B4D)
GL_MAX_FRAGMENT_UNIFORM_VECTORS=_C('GL_MAX_FRAGMENT_UNIFORM_VECTORS',0x8DFD)
GL_MAX_RENDERBUFFER_SIZE=_C('GL_MAX_RENDERBUFFER_SIZE',0x84E8)
GL_MAX_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TEXTURE_IMAGE_UNITS',0x8872)
GL_MAX_TEXTURE_SIZE=_C('GL_MAX_TEXTURE_SIZE',0x0D33)
GL_MAX_VARYING_VECTORS=_C('GL_MAX_VARYING_VECTORS',0x8DFC)
GL_MAX_VERTEX_ATTRIBS=_C('GL_MAX_VERTEX_ATTRIBS',0x8869)
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS=_C('GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS',0x8B4C)
GL_MAX_VERTEX_UNIFORM_VECTORS=_C('GL_MAX_VERTEX_UNIFORM_VECTORS',0x8DFB)
GL_MAX_VIEWPORT_DIMS=_C('GL_MAX_VIEWPORT_DIMS',0x0D3A)
GL_MEDIUM_FLOAT=_C('GL_MEDIUM_FLOAT',0x8DF1)
GL_MEDIUM_INT=_C('GL_MEDIUM_INT',0x8DF4)
GL_MIRRORED_REPEAT=_C('GL_MIRRORED_REPEAT',0x8370)
GL_NEAREST=_C('GL_NEAREST',0x2600)
GL_NEAREST_MIPMAP_LINEAR=_C('GL_NEAREST_MIPMAP_LINEAR',0x2702)
GL_NEAREST_MIPMAP_NEAREST=_C('GL_NEAREST_MIPMAP_NEAREST',0x2700)
GL_NEVER=_C('GL_NEVER',0x0200)
GL_NICEST=_C('GL_NICEST',0x1102)
GL_NONE=_C('GL_NONE',0)
GL_NOTEQUAL=_C('GL_NOTEQUAL',0x0205)
GL_NO_ERROR=_C('GL_NO_ERROR',0)
GL_NO_ERROR=_C('GL_NO_ERROR',0)
GL_NUM_COMPRESSED_TEXTURE_FORMATS=_C('GL_NUM_COMPRESSED_TEXTURE_FORMATS',0x86A2)
GL_NUM_PROGRAM_BINARY_FORMATS=_C('GL_NUM_PROGRAM_BINARY_FORMATS',0x87FE)
GL_ONE=_C('GL_ONE',1)
GL_ONE_MINUS_CONSTANT_ALPHA=_C('GL_ONE_MINUS_CONSTANT_ALPHA',0x8004)
GL_ONE_MINUS_CONSTANT_COLOR=_C('GL_ONE_MINUS_CONSTANT_COLOR',0x8002)
GL_ONE_MINUS_DST_ALPHA=_C('GL_ONE_MINUS_DST_ALPHA',0x0305)
GL_ONE_MINUS_DST_COLOR=_C('GL_ONE_MINUS_DST_COLOR',0x0307)
GL_ONE_MINUS_SRC_ALPHA=_C('GL_ONE_MINUS_SRC_ALPHA',0x0303)
GL_ONE_MINUS_SRC_COLOR=_C('GL_ONE_MINUS_SRC_COLOR',0x0301)
GL_OUT_OF_MEMORY=_C('GL_OUT_OF_MEMORY',0x0505)
GL_PACK_ALIGNMENT=_C('GL_PACK_ALIGNMENT',0x0D05)
GL_POINTS=_C('GL_POINTS',0x0000)
GL_POLYGON_OFFSET_FACTOR=_C('GL_POLYGON_OFFSET_FACTOR',0x8038)
GL_POLYGON_OFFSET_FILL=_C('GL_POLYGON_OFFSET_FILL',0x8037)
GL_POLYGON_OFFSET_UNITS=_C('GL_POLYGON_OFFSET_UNITS',0x2A00)
GL_PROGRAM_BINARY_FORMATS=_C('GL_PROGRAM_BINARY_FORMATS',0x87FF)
GL_R8=_C('GL_R8',0x8229)
GL_RED=_C('GL_RED',0x1903)
GL_RED_BITS=_C('GL_RED_BITS',0x0D52)
GL_RENDERBUFFER=_C('GL_RENDERBUFFER',0x8D41)
GL_RENDERBUFFER_ALPHA_SIZE=_C('GL_RENDERBUFFER_ALPHA_SIZE',0x8D53)
GL_RENDERBUFFER_BINDING=_C('GL_RENDERBUFFER_BINDING',0x8CA7)
GL_RENDERBUFFER_BLUE_SIZE=_C('GL_RENDERBUFFER_BLUE_SIZE',0x8D52)
GL_RENDERBUFFER_DEPTH_SIZE=_C('GL_RENDERBUFFER_DEPTH_SIZE',0x8D54)
GL_RENDERBUFFER_GREEN_SIZE=_C('GL_RENDERBUFFER_GREEN_SIZE',0x8D51)
GL_RENDERBUFFER_HEIGHT=_C('GL_RENDERBUFFER_HEIGHT',0x8D43)
GL_RENDERBUFFER_INTERNAL_FORMAT=_C('GL_RENDERBUFFER_INTERNAL_FORMAT',0x8D44)
GL_RENDERBUFFER_RED_SIZE=_C('GL_RENDERBUFFER_RED_SIZE',0x8D50)
GL_RENDERBUFFER_STENCIL_SIZE=_C('GL_RENDERBUFFER_STENCIL_SIZE',0x8D55)
GL_RENDERBUFFER_WIDTH=_C('GL_RENDERBUFFER_WIDTH',0x8D42)
GL_RENDERER=_C('GL_RENDERER',0x1F01)
GL_REPEAT=_C('GL_REPEAT',0x2901)
GL_REPLACE=_C('GL_REPLACE',0x1E01)
GL_RESET_NOTIFICATION_STRATEGY=_C('GL_RESET_NOTIFICATION_STRATEGY',0x8256)
GL_RG=_C('GL_RG',0x8227)
GL_RG8=_C('GL_RG8',0x822B)
GL_RGB=_C('GL_RGB',0x1907)
GL_RGB565=_C('GL_RGB565',0x8D62)
GL_RGB5_A1=_C('GL_RGB5_A1',0x8057)
GL_RGB8=_C('GL_RGB8',0x8051)
GL_RGBA=_C('GL_RGBA',0x1908)
GL_RGBA4=_C('GL_RGBA4',0x8056)
GL_RGBA8=_C('GL_RGBA8',0x8058)
GL_SAMPLER_2D=_C('GL_SAMPLER_2D',0x8B5E)
GL_SAMPLES=_C('GL_SAMPLES',0x80A9)
GL_SAMPLE_ALPHA_TO_COVERAGE=_C('GL_SAMPLE_ALPHA_TO_COVERAGE',0x809E)
GL_SAMPLE_BUFFERS=_C('GL_SAMPLE_BUFFERS',0x80A8)
GL_SAMPLE_COVERAGE=_C('GL_SAMPLE_COVERAGE',0x80A0)
GL_SAMPLE_COVERAGE_INVERT=_C('GL_SAMPLE_COVERAGE_INVERT',0x80AB)
GL_SAMPLE_COVERAGE_VALUE=_C('GL_SAMPLE_COVERAGE_VALUE',0x80AA)
GL_SCISSOR_BOX=_C('GL_SCISSOR_BOX',0x0C10)
GL_SCISSOR_TEST=_C('GL_SCISSOR_TEST',0x0C11)
GL_SHADING_LANGUAGE_VERSION=_C('GL_SHADING_LANGUAGE_VERSION',0x8B8C)
GL_SHORT=_C('GL_SHORT',0x1402)
GL_SRC_ALPHA=_C('GL_SRC_ALPHA',0x0302)
GL_SRC_ALPHA_SATURATE=_C('GL_SRC_ALPHA_SATURATE',0x0308)
GL_SRC_COLOR=_C('GL_SRC_COLOR',0x0300)
GL_STATIC_DRAW=_C('GL_STATIC_DRAW',0x88E4)
GL_STENCIL_ATTACHMENT=_C('GL_STENCIL_ATTACHMENT',0x8D20)
GL_STENCIL_BACK_FAIL=_C('GL_STENCIL_BACK_FAIL',0x8801)
GL_STENCIL_BACK_FUNC=_C('GL_STENCIL_BACK_FUNC',0x8800)
GL_STENCIL_BACK_PASS_DEPTH_FAIL=_C('GL_STENCIL_BACK_PASS_DEPTH_FAIL',0x8802)
GL_STENCIL_BACK_PASS_DEPTH_PASS=_C('GL_STENCIL_BACK_PASS_DEPTH_PASS',0x8803)
GL_STENCIL_BACK_REF=_C('GL_STENCIL_BACK_REF',0x8CA3)
GL_STENCIL_BACK_VALUE_MASK=_C('GL_STENCIL_BACK_VALUE_MASK',0x8CA4)
GL_STENCIL_BACK_WRITEMASK=_C('GL_STENCIL_BACK_WRITEMASK',0x8CA5)
GL_STENCIL_BITS=_C('GL_STENCIL_BITS',0x0D57)
GL_STENCIL_BUFFER_BIT=_C('GL_STENCIL_BUFFER_BIT',0x00000400)
GL_STENCIL_CLEAR_VALUE=_C('GL_STENCIL_CLEAR_VALUE',0x0B91)
GL_STENCIL_FAIL=_C('GL_STENCIL_FAIL',0x0B94)
GL_STENCIL_FUNC=_C('GL_STENCIL_FUNC',0x0B92)
GL_STENCIL_INDEX8=_C('GL_STENCIL_INDEX8',0x8D48)
GL_STENCIL_PASS_DEPTH_FAIL=_C('GL_STENCIL_PASS_DEPTH_FAIL',0x0B95)
GL_STENCIL_PASS_DEPTH_PASS=_C('GL_STENCIL_PASS_DEPTH_PASS',0x0B96)
GL_STENCIL_REF=_C('GL_STENCIL_REF',0x0B97)
GL_STENCIL_TEST=_C('GL_STENCIL_TEST',0x0B90)
GL_STENCIL_VALUE_MASK=_C('GL_STENCIL_VALUE_MASK',0x0B93)
GL_STENCIL_WRITEMASK=_C('GL_STENCIL_WRITEMASK',0x0B98)
GL_STREAM_DRAW=_C('GL_STREAM_DRAW',0x88E0)
GL_SUBPIXEL_BITS=_C('GL_SUBPIXEL_BITS',0x0D50)
GL_TEXTURE=_C('GL_TEXTURE',0x1702)
GL_TEXTURE0=_C('GL_TEXTURE0',0x84C0)
GL_TEXTURE1=_C('GL_TEXTURE1',0x84C1)
GL_TEXTURE10=_C('GL_TEXTURE10',0x84CA)
GL_TEXTURE11=_C('GL_TEXTURE11',0x84CB)
GL_TEXTURE12=_C('GL_TEXTURE12',0x84CC)
GL_TEXTURE13=_C('GL_TEXTURE13',0x84CD)
GL_TEXTURE14=_C('GL_TEXTURE14',0x84CE)
GL_TEXTURE15=_C('GL_TEXTURE15',0x84CF)
GL_TEXTURE16=_C('GL_TEXTURE16',0x84D0)
GL_TEXTURE17=_C('GL_TEXTURE17',0x84D1)
GL_TEXTURE18=_C('GL_TEXTURE18',0x84D2)
GL_TEXTURE19=_C('GL_TEXTURE19',0x84D3)
GL_TEXTURE2=_C('GL_TEXTURE2',0x84C2)
GL_TEXTURE20=_C('GL_TEXTURE20',0x84D4)
GL_TEXTURE21=_C('GL_TEXTURE21',0x84D5)
GL_TEXTURE22=_C('GL_TEXTURE22',0x84D6)
GL_TEXTURE23=_C('GL_TEXTURE23',0x84D7)
GL_TEXTURE24=_C('GL_TEXTURE24',0x84D8)
GL_TEXTURE25=_C('GL_TEXTURE25',0x84D9)
GL_TEXTURE26=_C('GL_TEXTURE26',0x84DA)
GL_TEXTURE27=_C('GL_TEXTURE27',0x84DB)
GL_TEXTURE28=_C('GL_TEXTURE28',0x84DC)
GL_TEXTURE29=_C('GL_TEXTURE29',0x84DD)
GL_TEXTURE3=_C('GL_TEXTURE3',0x84C3)
GL_TEXTURE30=_C('GL_TEXTURE30',0x84DE)
GL_TEXTURE31=_C('GL_TEXTURE31',0x84DF)
GL_TEXTURE4=_C('GL_TEXTURE4',0x84C4)
GL_TEXTURE5=_C('GL_TEXTURE5',0x84C5)
GL_TEXTURE6=_C('GL_TEXTURE6',0x84C6)
GL_TEXTURE7=_C('GL_TEXTURE7',0x84C7)
GL_TEXTURE8=_C('GL_TEXTURE8',0x84C8)
GL_TEXTURE9=_C('GL_TEXTURE9',0x84C9)
GL_TEXTURE_2D=_C('GL_TEXTURE_2D',0x0DE1)
GL_TEXTURE_BINDING_2D=_C('GL_TEXTURE_BINDING_2D',0x8069)
GL_TEXTURE_IMMUTABLE_FORMAT=_C('GL_TEXTURE_IMMUTABLE_FORMAT',0x912F)
GL_TEXTURE_MAG_FILTER=_C('GL_TEXTURE_MAG_FILTER',0x2800)
GL_TEXTURE_MIN_FILTER=_C('GL_TEXTURE_MIN_FILTER',0x2801)
GL_TEXTURE_WRAP_S=_C('GL_TEXTURE_WRAP_S',0x2802)
GL_TEXTURE_WRAP_T=_C('GL_TEXTURE_WRAP_T',0x2803)
GL_TRIANGLES=_C('GL_TRIANGLES',0x0004)
GL_TRIANGLE_FAN=_C('GL_TRIANGLE_FAN',0x0006)
GL_TRIANGLE_STRIP=_C('GL_TRIANGLE_STRIP',0x0005)
GL_TRUE=_C('GL_TRUE',1)
GL_UNKNOWN_CONTEXT_RESET=_C('GL_UNKNOWN_CONTEXT_RESET',0x8255)
GL_UNPACK_ALIGNMENT=_C('GL_UNPACK_ALIGNMENT',0x0CF5)
GL_UNSIGNED_BYTE=_C('GL_UNSIGNED_BYTE',0x1401)
GL_UNSIGNED_INT=_C('GL_UNSIGNED_INT',0x1405)
GL_UNSIGNED_SHORT=_C('GL_UNSIGNED_SHORT',0x1403)
GL_UNSIGNED_SHORT_4_4_4_4=_C('GL_UNSIGNED_SHORT_4_4_4_4',0x8033)
GL_UNSIGNED_SHORT_5_5_5_1=_C('GL_UNSIGNED_SHORT_5_5_5_1',0x8034)
GL_UNSIGNED_SHORT_5_6_5=_C('GL_UNSIGNED_SHORT_5_6_5',0x8363)
GL_VENDOR=_C('GL_VENDOR',0x1F00)
GL_VERSION=_C('GL_VERSION',0x1F02)
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING=_C('GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING',0x889F)
GL_VERTEX_ATTRIB_ARRAY_ENABLED=_C('GL_VERTEX_ATTRIB_ARRAY_ENABLED',0x8622)
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED=_C('GL_VERTEX_ATTRIB_ARRAY_NORMALIZED',0x886A)
GL_VERTEX_ATTRIB_ARRAY_POINTER=_C('GL_VERTEX_ATTRIB_ARRAY_POINTER',0x8645)
GL_VERTEX_ATTRIB_ARRAY_SIZE=_C('GL_VERTEX_ATTRIB_ARRAY_SIZE',0x8623)
GL_VERTEX_ATTRIB_ARRAY_STRIDE=_C('GL_VERTEX_ATTRIB_ARRAY_STRIDE',0x8624)
GL_VERTEX_ATTRIB_ARRAY_TYPE=_C('GL_VERTEX_ATTRIB_ARRAY_TYPE',0x8625)
GL_VIEWPORT=_C('GL_VIEWPORT',0x0BA2)
GL_ZERO=_C('GL_ZERO',0)
@_f
@_p.types(None,_cs.GLenum)
def glActiveTexture(texture):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindBuffer(target,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindFramebuffer(target,framebuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindRenderbuffer(target,renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindTexture(target,texture):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glBlendColor(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLenum)
def glBlendEquation(mode):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glBlendEquationSeparate(modeRGB,modeAlpha):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glBlendFunc(sfactor,dfactor):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glBlendFuncSeparate(sfactorRGB,dfactorRGB,sfactorAlpha,dfactorAlpha):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizeiptr,ctypes.c_void_p,_cs.GLenum)
def glBufferData(target,size,data,usage):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLintptr,_cs.GLsizeiptr,ctypes.c_void_p)
def glBufferSubData(target,offset,size,data):pass
@_f
@_p.types(_cs.GLenum,_cs.GLenum)
def glCheckFramebufferStatus(target):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glClear(mask):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glClearColor(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLfloat)
def glClearDepthf(d):pass
@_f
@_p.types(None,_cs.GLint)
def glClearStencil(s):pass
@_f
@_p.types(None,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMask(red,green,blue,alpha):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTexSubImage2D(target,level,xoffset,yoffset,width,height,format,imageSize,data):pass
@_f
@_p.types(_cs.GLuint,)
def glCreateProgram():pass
@_f
@_p.types(None,_cs.GLenum)
def glCullFace(mode):pass
@_f
@_p.types(None,_cs.GLenum)
def glDepthFunc(func):pass
@_f
@_p.types(None,_cs.GLboolean)
def glDepthMask(flag):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glDepthRangef(n,f):pass
@_f
@_p.types(None,_cs.GLenum)
def glDisable(cap):pass
@_f
@_p.types(None,_cs.GLuint)
def glDisableVertexAttribArray(index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei)
def glDrawArrays(mode,first,count):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glDrawRangeElements(mode,start,end,count,type,indices):pass
@_f
@_p.types(None,_cs.GLenum)
def glEnable(cap):pass
@_f
@_p.types(None,_cs.GLuint)
def glEnableVertexAttribArray(index):pass
@_f
@_p.types(None,)
def glFinish():pass
@_f
@_p.types(None,)
def glFlush():pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glFramebufferRenderbuffer(target,attachment,renderbuffertarget,renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTexture2D(target,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLenum)
def glFrontFace(mode):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenBuffers(n,buffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenFramebuffers(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenRenderbuffers(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenTextures(n,textures):pass
@_f
@_p.types(None,_cs.GLenum)
def glGenerateMipmap(target):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetAttribLocation(program,name):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbooleanArray)
def glGetBooleanv(pname,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetBufferParameteriv(target,pname,params):pass
@_f
@_p.types(_cs.GLenum,)
def glGetError():pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glGetFloatv(pname,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFramebufferAttachmentParameteriv(target,attachment,pname,params):pass
@_f
@_p.types(_cs.GLenum,)
def glGetGraphicsResetStatus():pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glGetIntegerv(pname,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetProgramiv(program,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetRenderbufferParameteriv(target,pname,params):pass
@_f
@_p.types(arrays.GLubyteArray,_cs.GLenum)
def glGetString(name):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetTexParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameteriv(target,pname,params):pass
@_f
@_p.types(_cs.GLint,_cs.GLuint,arrays.GLcharArray)
def glGetUniformLocation(program,name):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLvoidpArray)
def glGetVertexAttribPointerv(index,pname,pointer):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetVertexAttribfv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetVertexAttribiv(index,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glGetnUniformfv(program,location,bufSize,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glGetnUniformiv(program,location,bufSize,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glHint(target,mode):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum)
def glIsEnabled(cap):pass
@_f
@_p.types(None,_cs.GLfloat)
def glLineWidth(width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPixelStorei(pname,param):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glPolygonOffset(factor,units):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei)
def glProgramBinary(program,binaryFormat,binary,length):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glReadnPixels(x,y,width,height,format,type,bufSize,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorage(target,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLboolean)
def glSampleCoverage(value,invert):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glScissor(x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLuint)
def glStencilFunc(func,ref,mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLuint)
def glStencilFuncSeparate(face,func,ref,mask):pass
@_f
@_p.types(None,_cs.GLuint)
def glStencilMask(mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glStencilMaskSeparate(face,mask):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glStencilOp(fail,zfail,zpass):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glStencilOpSeparate(face,sfail,dpfail,dppass):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glTexParameterf(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glTexParameterfv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glTexParameteri(target,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameteriv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glTexStorage2D(target,levels,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage2D(target,level,xoffset,yoffset,width,height,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat)
def glUniform1f(location,v0):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform1fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glUniform1i(location,v0):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform1iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat)
def glUniform2f(location,v0,v1):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform2fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glUniform2i(location,v0,v1):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform2iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glUniform3f(location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform3fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glUniform3i(location,v0,v1,v2):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform3iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glUniform4f(location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glUniform4fv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glUniform4i(location,v0,v1,v2,v3):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glUniform4iv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix2fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix3fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLfloatArray)
def glUniformMatrix4fv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLuint)
def glUseProgram(program):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat)
def glVertexAttrib1f(index,x):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib1fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat,_cs.GLfloat)
def glVertexAttrib2f(index,x,y):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib2fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertexAttrib3f(index,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib3fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertexAttrib4f(index,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLfloatArray)
def glVertexAttrib4fv(index,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLboolean,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribPointer(index,size,type,normalized,stride,pointer):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glViewport(x,y,width,height):pass

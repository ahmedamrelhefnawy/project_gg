'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES1_OES_framebuffer_object'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES1,'GLES1_OES_framebuffer_object',error_checker=_errors._error_checker)
GL_COLOR_ATTACHMENT0_OES=_C('GL_COLOR_ATTACHMENT0_OES',0x8CE0)
GL_DEPTH_ATTACHMENT_OES=_C('GL_DEPTH_ATTACHMENT_OES',0x8D00)
GL_DEPTH_COMPONENT16_OES=_C('GL_DEPTH_COMPONENT16_OES',0x81A5)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_OES',0x8CD1)
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES=_C('GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_OES',0x8CD0)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_OES',0x8CD3)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_OES',0x8CD2)
GL_FRAMEBUFFER_BINDING_OES=_C('GL_FRAMEBUFFER_BINDING_OES',0x8CA6)
GL_FRAMEBUFFER_COMPLETE_OES=_C('GL_FRAMEBUFFER_COMPLETE_OES',0x8CD5)
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES=_C('GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_OES',0x8CD6)
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES=_C('GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_OES',0x8CD9)
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES=_C('GL_FRAMEBUFFER_INCOMPLETE_FORMATS_OES',0x8CDA)
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES=_C('GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_OES',0x8CD7)
GL_FRAMEBUFFER_OES=_C('GL_FRAMEBUFFER_OES',0x8D40)
GL_FRAMEBUFFER_UNSUPPORTED_OES=_C('GL_FRAMEBUFFER_UNSUPPORTED_OES',0x8CDD)
GL_INVALID_FRAMEBUFFER_OPERATION_OES=_C('GL_INVALID_FRAMEBUFFER_OPERATION_OES',0x0506)
GL_MAX_RENDERBUFFER_SIZE_OES=_C('GL_MAX_RENDERBUFFER_SIZE_OES',0x84E8)
GL_NONE_OES=_C('GL_NONE_OES',0)
GL_RENDERBUFFER_ALPHA_SIZE_OES=_C('GL_RENDERBUFFER_ALPHA_SIZE_OES',0x8D53)
GL_RENDERBUFFER_BINDING_OES=_C('GL_RENDERBUFFER_BINDING_OES',0x8CA7)
GL_RENDERBUFFER_BLUE_SIZE_OES=_C('GL_RENDERBUFFER_BLUE_SIZE_OES',0x8D52)
GL_RENDERBUFFER_DEPTH_SIZE_OES=_C('GL_RENDERBUFFER_DEPTH_SIZE_OES',0x8D54)
GL_RENDERBUFFER_GREEN_SIZE_OES=_C('GL_RENDERBUFFER_GREEN_SIZE_OES',0x8D51)
GL_RENDERBUFFER_HEIGHT_OES=_C('GL_RENDERBUFFER_HEIGHT_OES',0x8D43)
GL_RENDERBUFFER_INTERNAL_FORMAT_OES=_C('GL_RENDERBUFFER_INTERNAL_FORMAT_OES',0x8D44)
GL_RENDERBUFFER_OES=_C('GL_RENDERBUFFER_OES',0x8D41)
GL_RENDERBUFFER_RED_SIZE_OES=_C('GL_RENDERBUFFER_RED_SIZE_OES',0x8D50)
GL_RENDERBUFFER_STENCIL_SIZE_OES=_C('GL_RENDERBUFFER_STENCIL_SIZE_OES',0x8D55)
GL_RENDERBUFFER_WIDTH_OES=_C('GL_RENDERBUFFER_WIDTH_OES',0x8D42)
GL_RGB565_OES=_C('GL_RGB565_OES',0x8D62)
GL_RGB5_A1_OES=_C('GL_RGB5_A1_OES',0x8057)
GL_RGBA4_OES=_C('GL_RGBA4_OES',0x8056)
GL_STENCIL_ATTACHMENT_OES=_C('GL_STENCIL_ATTACHMENT_OES',0x8D20)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindFramebufferOES(target,framebuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindRenderbufferOES(target,renderbuffer):pass
@_f
@_p.types(_cs.GLenum,_cs.GLenum)
def glCheckFramebufferStatusOES(target):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteFramebuffersOES(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteRenderbuffersOES(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glFramebufferRenderbufferOES(target,attachment,renderbuffertarget,renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTexture2DOES(target,attachment,textarget,texture,level):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenFramebuffersOES(n,framebuffers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenRenderbuffersOES(n,renderbuffers):pass
@_f
@_p.types(None,_cs.GLenum)
def glGenerateMipmapOES(target):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFramebufferAttachmentParameterivOES(target,attachment,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetRenderbufferParameterivOES(target,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsFramebufferOES(framebuffer):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsRenderbufferOES(renderbuffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageOES(target,internalformat,width,height):pass

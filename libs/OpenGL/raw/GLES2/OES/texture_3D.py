'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_OES_texture_3D'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_OES_texture_3D',error_checker=_errors._error_checker)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_OES=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_OES',0x8CD4)
GL_MAX_3D_TEXTURE_SIZE_OES=_C('GL_MAX_3D_TEXTURE_SIZE_OES',0x8073)
GL_SAMPLER_3D_OES=_C('GL_SAMPLER_3D_OES',0x8B5F)
GL_TEXTURE_3D_OES=_C('GL_TEXTURE_3D_OES',0x806F)
GL_TEXTURE_BINDING_3D_OES=_C('GL_TEXTURE_BINDING_3D_OES',0x806A)
GL_TEXTURE_WRAP_R_OES=_C('GL_TEXTURE_WRAP_R_OES',0x8072)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTexImage3DOES(target,level,internalformat,width,height,depth,border,imageSize,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glCompressedTexSubImage3DOES(target,level,xoffset,yoffset,zoffset,width,height,depth,format,imageSize,data):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glCopyTexSubImage3DOES(target,level,xoffset,yoffset,zoffset,x,y,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLint)
def glFramebufferTexture3DOES(target,attachment,textarget,texture,level,zoffset):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLint,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexImage3DOES(target,level,internalformat,width,height,depth,border,format,type,pixels):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,ctypes.c_void_p)
def glTexSubImage3DOES(target,level,xoffset,yoffset,zoffset,width,height,depth,format,type,pixels):pass

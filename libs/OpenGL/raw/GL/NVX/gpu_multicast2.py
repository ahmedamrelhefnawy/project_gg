'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NVX_gpu_multicast2'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NVX_gpu_multicast2',error_checker=_errors._error_checker)
GL_UPLOAD_GPU_MASK_NVX=_C('GL_UPLOAD_GPU_MASK_NVX',0x954A)
@_f
@_p.types(_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,arrays.GLuint64Array,_cs.GLuint,_cs.GLbitfield,_cs.GLuint,_cs.GLuint,_cs.GLintptr,_cs.GLintptr,_cs.GLsizeiptr,_cs.GLsizei,arrays.GLuintArray,arrays.GLuint64Array)
def glAsyncCopyBufferSubDataNVX(waitSemaphoreCount,waitSemaphoreArray,fenceValueArray,readGpu,writeGpuMask,readBuffer,writeBuffer,readOffset,writeOffset,size,signalSemaphoreCount,signalSemaphoreArray,signalValueArray):pass
@_f
@_p.types(_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,arrays.GLuint64Array,_cs.GLuint,_cs.GLbitfield,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,arrays.GLuintArray,arrays.GLuint64Array)
def glAsyncCopyImageSubDataNVX(waitSemaphoreCount,waitSemaphoreArray,waitValueArray,srcGpu,dstGpuMask,srcName,srcTarget,srcLevel,srcX,srcY,srcZ,dstName,dstTarget,dstLevel,dstX,dstY,dstZ,srcWidth,srcHeight,srcDepth,signalSemaphoreCount,signalSemaphoreArray,signalValueArray):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLintArray)
def glMulticastScissorArrayvNVX(gpu,first,count,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glMulticastViewportArrayvNVX(gpu,first,count,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLfloat,_cs.GLfloat)
def glMulticastViewportPositionWScaleNVX(gpu,index,xcoeff,ycoeff):pass
@_f
@_p.types(None,_cs.GLbitfield)
def glUploadGpuMaskNVX(mask):pass

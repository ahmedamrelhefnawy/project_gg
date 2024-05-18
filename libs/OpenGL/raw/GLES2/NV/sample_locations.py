'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_NV_sample_locations'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_NV_sample_locations',error_checker=_errors._error_checker)
GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_NV=_C('GL_FRAMEBUFFER_PROGRAMMABLE_SAMPLE_LOCATIONS_NV',0x9342)
GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_NV=_C('GL_FRAMEBUFFER_SAMPLE_LOCATION_PIXEL_GRID_NV',0x9343)
GL_PROGRAMMABLE_SAMPLE_LOCATION_NV=_C('GL_PROGRAMMABLE_SAMPLE_LOCATION_NV',0x9341)
GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_NV=_C('GL_PROGRAMMABLE_SAMPLE_LOCATION_TABLE_SIZE_NV',0x9340)
GL_SAMPLE_LOCATION_NV=_C('GL_SAMPLE_LOCATION_NV',0x8E50)
GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_NV=_C('GL_SAMPLE_LOCATION_PIXEL_GRID_HEIGHT_NV',0x933F)
GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_NV=_C('GL_SAMPLE_LOCATION_PIXEL_GRID_WIDTH_NV',0x933E)
GL_SAMPLE_LOCATION_SUBPIXEL_BITS_NV=_C('GL_SAMPLE_LOCATION_SUBPIXEL_BITS_NV',0x933D)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glFramebufferSampleLocationsfvNV(target,start,count,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLfloatArray)
def glNamedFramebufferSampleLocationsfvNV(framebuffer,start,count,v):pass
@_f
@_p.types(None,)
def glResolveDepthValuesNV():pass

'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_raster_multisample'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_raster_multisample',error_checker=_errors._error_checker)
GL_EFFECTIVE_RASTER_SAMPLES_EXT=_C('GL_EFFECTIVE_RASTER_SAMPLES_EXT',0x932C)
GL_MAX_RASTER_SAMPLES_EXT=_C('GL_MAX_RASTER_SAMPLES_EXT',0x9329)
GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT=_C('GL_MULTISAMPLE_RASTERIZATION_ALLOWED_EXT',0x932B)
GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT=_C('GL_RASTER_FIXED_SAMPLE_LOCATIONS_EXT',0x932A)
GL_RASTER_MULTISAMPLE_EXT=_C('GL_RASTER_MULTISAMPLE_EXT',0x9327)
GL_RASTER_SAMPLES_EXT=_C('GL_RASTER_SAMPLES_EXT',0x9328)
@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean)
def glRasterSamplesEXT(samples,fixedsamplelocations):pass

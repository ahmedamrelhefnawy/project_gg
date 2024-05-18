'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_KHR_partial_update'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_KHR_partial_update',error_checker=_errors._error_checker)
EGL_BUFFER_AGE_KHR=_C('EGL_BUFFER_AGE_KHR',0x313D)
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLSurface,arrays.GLintArray,_cs.EGLint)
def eglSetDamageRegionKHR(dpy,surface,rects,n_rects):pass

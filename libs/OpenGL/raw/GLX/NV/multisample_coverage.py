'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_NV_multisample_coverage'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_NV_multisample_coverage',error_checker=_errors._error_checker)
GLX_COLOR_SAMPLES_NV=_C('GLX_COLOR_SAMPLES_NV',0x20B3)
GLX_COVERAGE_SAMPLES_NV=_C('GLX_COVERAGE_SAMPLES_NV',100001)

